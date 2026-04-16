#!/usr/bin/env python3
"""
Fetch a YouTube transcript. Tries multiple methods in fail-fast order.

Usage:
    python3 fetch_transcript.py <VIDEO_URL_OR_ID> [output_dir]

On success: writes transcript.vtt (raw captions) and transcript.md
            (timestamped markdown) into output_dir (default: cwd).
On failure: prints a clear diagnosis + browser-fallback instructions
            and exits 1.

Design: fail fast. Each method gets ONE shot with a short timeout.
YouTube blocks cloud IPs aggressively; if the first method fails,
the second usually will too. Total budget is ~60 seconds.
"""

import json
import re
import ssl
import sys
import urllib.request
import urllib.parse
from pathlib import Path
from typing import Optional

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0"


def extract_video_id(url_or_id: str) -> str:
    """Accept a YouTube URL or a bare video ID."""
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", url_or_id):
        return url_or_id
    patterns = [
        r"(?:v=|/live/|/embed/|/shorts/|youtu\.be/)([A-Za-z0-9_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url_or_id)
        if m:
            return m.group(1)
    raise ValueError(f"Cannot extract video ID from: {url_or_id}")


def fetch_oembed_metadata(video_id: str) -> dict:
    """Cheap metadata fetch. Usually works even when captions are blocked."""
    url = (
        "https://www.youtube.com/oembed?url="
        + urllib.parse.quote(f"https://www.youtube.com/watch?v={video_id}")
        + "&format=json"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, context=SSL_CTX, timeout=10) as resp:
        return json.loads(resp.read().decode())


def try_youtube_transcript_api(video_id: str) -> Optional[list]:
    """Method 1: youtube-transcript-api (pip)."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("  [yta] not installed (pip install youtube-transcript-api)")
        return None
    try:
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id)
        return [
            {"start": s.start, "duration": s.duration, "text": s.text}
            for s in transcript.snippets
        ]
    except Exception as e:
        print(f"  [yta] {type(e).__name__}: {str(e).splitlines()[0][:120]}")
        return None


def try_pytubefix(video_id: str) -> Optional[list]:
    """Method 2: pytubefix. Often gets metadata before caption call fails."""
    try:
        from pytubefix import YouTube
    except ImportError:
        print("  [pytubefix] not installed (pip install pytubefix)")
        return None
    try:
        yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
        for code in ("en", "a.en", "en-US"):
            cap = yt.captions.get(code)
            if cap:
                srt = cap.generate_srt_captions()
                return parse_srt(srt)
        print("  [pytubefix] no English caption track")
        return None
    except Exception as e:
        print(f"  [pytubefix] {type(e).__name__}: {str(e)[:120]}")
        return None


def try_invidious(video_id: str) -> Optional[str]:
    """Method 3: Invidious mirrors. Most are down or rate-limited."""
    instances = [
        "https://inv.nadeko.net",
        "https://invidious.privacyredirect.com",
        "https://yewtu.be",
    ]
    for inst in instances:
        try:
            list_url = f"{inst}/api/v1/captions/{video_id}"
            req = urllib.request.Request(list_url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, context=SSL_CTX, timeout=10) as r:
                body = r.read().decode()
            try:
                caps = json.loads(body).get("captions", [])
            except json.JSONDecodeError:
                continue
            for cap in caps:
                lc = cap.get("languageCode") or cap.get("language_code", "")
                if lc.startswith("en"):
                    cap_url = inst + cap["url"]
                    req2 = urllib.request.Request(cap_url, headers={"User-Agent": UA})
                    with urllib.request.urlopen(req2, context=SSL_CTX, timeout=30) as r2:
                        vtt = r2.read().decode()
                    if len(vtt) > 500:
                        return vtt
        except Exception as e:
            print(f"  [invidious {inst}] {type(e).__name__}: {str(e)[:80]}")
    return None


def parse_srt(srt: str) -> list:
    """Convert SRT text into [{start, duration, text}]."""
    snippets = []
    blocks = re.split(r"\n\n+", srt.strip())
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 3:
            continue
        m = re.match(
            r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)",
            lines[1],
        )
        if not m:
            continue
        h1, m1, s1, ms1, h2, m2, s2, ms2 = map(int, m.groups())
        start = h1 * 3600 + m1 * 60 + s1 + ms1 / 1000.0
        end = h2 * 3600 + m2 * 60 + s2 + ms2 / 1000.0
        snippets.append({
            "start": start,
            "duration": end - start,
            "text": " ".join(lines[2:]).strip(),
        })
    return snippets


def parse_vtt(vtt: str) -> list:
    """Convert VTT text into [{start, duration, text}]."""
    snippets = []
    blocks = re.split(r"\n\n+", vtt.strip())
    for block in blocks:
        lines = [l for l in block.strip().split("\n") if not l.startswith("WEBVTT")]
        if len(lines) < 2:
            continue
        ts_line_idx = next(
            (i for i, l in enumerate(lines) if "-->" in l), None
        )
        if ts_line_idx is None:
            continue
        m = re.match(
            r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)",
            lines[ts_line_idx],
        )
        if not m:
            continue
        h1, m1, s1, ms1, h2, m2, s2, ms2 = map(int, m.groups())
        start = h1 * 3600 + m1 * 60 + s1 + ms1 / 1000.0
        end = h2 * 3600 + m2 * 60 + s2 + ms2 / 1000.0
        text = " ".join(lines[ts_line_idx + 1:]).strip()
        if text:
            snippets.append({"start": start, "duration": end - start, "text": text})
    return snippets


def format_timestamp(seconds: float) -> str:
    h = int(seconds) // 3600
    m = (int(seconds) % 3600) // 60
    s = int(seconds) % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def snippets_to_markdown(snippets: list, meta: dict) -> str:
    out = [f"# {meta.get('title', 'YouTube Transcript')}\n"]
    out.append(f"- **URL:** https://www.youtube.com/watch?v={meta['video_id']}")
    if meta.get("author_name"):
        out.append(f"- **Channel:** {meta['author_name']}")
    out.append("")
    out.append("## Transcript\n")
    for s in snippets:
        out.append(f"**[{format_timestamp(s['start'])}]** {s['text']}")
        out.append("")
    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        print("Usage: fetch_transcript.py <VIDEO_URL_OR_ID> [output_dir]", file=sys.stderr)
        sys.exit(2)
    video_id = extract_video_id(sys.argv[1])
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path.cwd()
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Video ID: {video_id}")
    try:
        meta = fetch_oembed_metadata(video_id)
        meta["video_id"] = video_id
        print(f"Title: {meta.get('title')}")
        print(f"Channel: {meta.get('author_name')}")
    except Exception as e:
        print(f"[warn] oEmbed failed: {e} — continuing without metadata")
        meta = {"video_id": video_id, "title": "YouTube Transcript"}

    print("\nAttempting transcript retrieval (fail-fast):")

    snippets = None

    print("→ Method 1: youtube-transcript-api")
    snippets = try_youtube_transcript_api(video_id)

    if not snippets:
        print("→ Method 2: pytubefix")
        snippets = try_pytubefix(video_id)

    if not snippets:
        print("→ Method 3: Invidious mirrors")
        vtt = try_invidious(video_id)
        if vtt:
            snippets = parse_vtt(vtt)
            (out_dir / "transcript.vtt").write_text(vtt)

    if not snippets:
        print_failure_help(video_id, meta, out_dir)
        sys.exit(1)

    md = snippets_to_markdown(snippets, meta)
    (out_dir / "transcript.md").write_text(md)
    print(f"\n✓ Wrote {out_dir}/transcript.md ({len(snippets)} segments)")


def print_failure_help(video_id: str, meta: dict, out_dir: Path):
    print("\n" + "=" * 70)
    print("✗ All automatic methods failed.")
    print("=" * 70)
    print(
        "YouTube blocks requests from cloud-provider IPs and most public\n"
        "transcript mirrors are down or rate-limited. This is expected.\n"
    )
    print("Browser fallback (works from any residential IP):")
    print(f"  1. Open https://www.youtube.com/watch?v={video_id}")
    print("  2. Click ⋯ below the video → 'Show transcript'")
    print("  3. Copy the text")
    print(f"  4. Paste into {out_dir}/transcript.md\n")
    meta_path = out_dir / "metadata.json"
    meta_path.write_text(json.dumps(meta, indent=2))
    print(f"Metadata saved to {meta_path} for the source stub.")


if __name__ == "__main__":
    main()
