---
name: youtube-transcript
description: "Extract a YouTube video's transcript and ingest it into this wiki. Use when the user asks to add a YouTube link/video/talk/stream to the wiki, or asks for a transcript of a YouTube URL. Handles cloud-IP blocks by falling back through multiple methods and giving clear browser-based instructions when everything else fails."
---

# YouTube Transcript Ingestion

This skill captures the pipeline for adding a YouTube video to the wiki: link → metadata → transcript → wiki pages. It exists because YouTube aggressively blocks requests from cloud-provider IPs (AWS, GCP, Azure, etc.), so the naive approach ("just call `youtube-transcript-api`") fails in this sandbox.

## When to use

Invoke this skill when the user:
- pastes a YouTube URL (`youtube.com/watch`, `youtube.com/live`, `youtu.be/`, `youtube.com/shorts/`) and asks to add it / get the transcript
- says "ingest this video" / "add this talk to the wiki"
- references an existing pending-transcript stub in `raw/youtube-transcripts/` that needs the body filled in

## The constraint: cloud-IP blocking

**Every in-sandbox method will probably fail.** Expect this. Don't burn 20 minutes cycling through services before admitting it.

Fail-fast budget: **try one Python library + one Invidious instance**. If both fail with 403/429/empty-body, stop and fall back to instructing the user to paste the transcript from their browser.

## Pipeline (do these in order)

### 1. Get metadata (cheap, usually works)

Metadata retrieval is separate from caption retrieval and often succeeds even when captions fail. Use YouTube's oEmbed endpoint via WebFetch:

```
https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<VIDEO_ID>&format=json
```

Returns `title`, `author_name`, `author_url`, `thumbnail_url`. **Always capture this first** — even if transcript retrieval fails, you have enough to register the source.

`pytubefix` also gives `length`, `publish_date`, `description` before the IP ban kicks in on captions.

### 2. Try to fetch captions (will probably fail)

Run the bundled script:

```bash
python3 .claude/skills/youtube-transcript/scripts/fetch_transcript.py <VIDEO_URL_OR_ID>
```

It tries, in order: `youtube-transcript-api` → `pytubefix` → `yt-dlp` → 3 Invidious instances. Writes `transcript.vtt` + `transcript.md` to the current directory on success. Exits 1 with a clear error and the browser-fallback instructions if everything fails.

### 3. If automatic retrieval fails: create a pending-transcript stub

Don't pretend you got the transcript. Don't fabricate it. Create:

1. **`raw/youtube-transcripts/<slug>.md`** — metadata block + explicit paste marker. Template at `templates/raw-transcript-stub.md`.
2. **`wiki/sources/<slug>.md`** — pending-transcript source page. Template at `templates/wiki-source-stub.md`.
3. **Append link** to `raw/links/links.md`
4. **Update** `wiki/index.md` (add source row with ⚠️ transcript-pending flag) and `wiki/log.md` (append `[YYYY-MM-DD] ingest-stub | …` entry).

Explicitly tell the user the transcript needs to be pasted manually, with exact steps:
1. Open the video in a browser (residential IP)
2. Click ⋯ under the player → **"Show transcript"**
3. Copy the text
4. Paste below the `<!-- PASTE TRANSCRIPT BELOW THIS LINE -->` marker

### 4. If automatic retrieval succeeds: full ingestion

Follow the wiki's ingestion workflow from `CLAUDE.md`:
1. Save raw transcript to `raw/youtube-transcripts/<slug>.md` with frontmatter-style metadata header
2. Create `wiki/sources/<slug>.md` with full Summary / Key Claims / Connections / Questions Raised
3. Update or create relevant `wiki/concepts/` and `wiki/entities/` pages
4. Update `wiki/index.md` and append to `wiki/log.md`
5. Update `wiki/overview.md` if the source changes the big picture

## Slug convention

`<author-lastname>-<topic-kebab>.md` — e.g. `cole-medin-ai-dark-factory.md`, `dex-rpi-to-crispy.md`, `matt-pocock-dex-horthy-chat.md`. Keep it short enough to stay readable in `[[wikilinks]]`.

## See also

- `references/why-youtube-blocks.md` — concrete log of every method tried during the Cole Medin ingestion, with exact error messages. Consult before retrying an "obvious" solution.
- `templates/raw-transcript-stub.md`, `templates/wiki-source-stub.md` — copy-paste starting points.
- `scripts/fetch_transcript.py` — the consolidated multi-method fetcher.
