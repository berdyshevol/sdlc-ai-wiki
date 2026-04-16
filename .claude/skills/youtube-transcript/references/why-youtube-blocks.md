# Why automatic YouTube transcript retrieval fails in this sandbox

Concrete log from the Cole Medin "Dark Factory" ingestion attempt (2026-04-16).
**Consult this before trying any "obvious" method** — they've all been tried.

## Root cause

YouTube rate-limits and bans IP ranges belonging to cloud providers (AWS, GCP,
Azure, DigitalOcean, Linode, etc.) to prevent scraping. This sandbox runs on a
cloud IP. Any direct YouTube call is likely to receive HTTP 429 / "Sign in to
confirm you're not a bot" / IpBlocked responses within seconds.

Public proxy services (Invidious, Piped, various "youtube transcript" websites)
either (a) also run on cloud IPs and are banned, (b) are overloaded by bots, or
(c) require authentication / paid API keys.

## Full list of methods tried

### Python libraries

| Tool | Result |
|------|--------|
| `youtube-transcript-api` | `IpBlocked` exception on first call |
| `pytubefix` | Metadata OK (title, author, length). Caption call → `HTTP 429 Too Many Requests` |
| `yt-dlp` | SSL cert errors, then `Sign in to confirm you're not a bot` |
| `youtube-dl` | Not installed; maintainer-abandoned |

### YouTube API endpoints (direct)

| Endpoint | Result |
|----------|--------|
| `/api/timedtext?v=X&lang=en` | HTTP 429 |
| `/api/timedtext?type=list&v=X` | HTTP 429 |
| `/youtubei/v1/get_transcript` | HTTP 429 |
| `/oembed?url=...&format=json` | ✓ **Works** — returns title/author/thumbnail only |

### Invidious mirrors (15+ instances tested)

Representative sample:

| Instance | Result |
|----------|--------|
| `inv.nadeko.net` | Lists captions in JSON but caption fetch returns 0 bytes |
| `yewtu.be` | HTTP 403 |
| `invidious.no-logs.com` | HTTP 503 |
| `inv.vern.cc` | HTTP 500 |
| `invidious.nerdvpn.de` | HTTP 403 |
| `invidious.privacyredirect.com` | HTTP 503 |
| `invidious.flokinet.to` | Timeout |
| `invidious.perennialte.ch` | HTTP 403 |
| `invidious.materialio.us` | "Please stop abusing my Invidious instance" |
| `iv.melmac.space` | HTTP 500 |
| `invidious.projectsegfau.lt` | HTTP 503 / not-JSON |
| `invidious.einfachzocken.eu` | Serves instance-list HTML instead of API |
| `tube.cadence.moe` | HTTP 404 (API disabled) |

### Piped mirrors (10+ instances tested)

| Instance | Result |
|----------|--------|
| `pipedapi.kavin.rocks` | HTTP 521 |
| `pipedapi.adminforge.de` | DNS fail |
| `api.piped.yt` | DNS fail |
| `watchapi.whatever.social` | Read timeout |
| `piped-api.lunar.icu` | HTTP 503 |
| `pipedapi.drgns.space` | HTTP 503 |
| `pipedapi.ducks.party` | Timeout |
| `pipedapi.leptons.xyz` | HTTP 502 |
| `api.piped.private.coffee` | HTTP 500 |
| `pipedapi.projectsegfau.lt` | HTTP 503 |

### Transcript websites (tried via WebFetch)

| Service | Result |
|---------|--------|
| `youtubetranscript.com` | HTTP 403 |
| `youtubetotranscript.com` | HTTP 403 |
| `youtube-transcript.io` | HTTP 401 / requires API key |
| `tactiq.io` (public page) | Marketing page only |
| `tactiq.io` (internal API) | HTTP 401 |
| `downsub.com` | HTTP 403 |
| `notegpt.io` | Marketing page only, requires JS form submission |
| `ytscribe.com` | Returns "Checking authentication..." page |
| `supadata.ai` API | HTTP 401, requires API key |
| `kome.ai` API | HTTP 522 / HTTP 405 |
| `searchapi.io` | HTTP 401, requires paid key |

## What actually works

1. **oEmbed metadata** — title, author, thumbnail. Always accessible.
2. **`pytubefix` metadata** — adds length, publish_date, description. Usually works before the IP ban kicks in.
3. **Browser on residential IP** — the ⋯ menu → "Show transcript" on youtube.com works for any logged-out user with a residential IP.
4. **Paid transcript services with API keys** — Supadata, SearchAPI.io, Tactiq enterprise, etc. Not configured in this sandbox.

## Fail-fast rule

When captions fail via the first two Python methods, **stop**. Don't cycle
through Invidious instances. Create a pending-transcript stub and give the
user browser instructions. Time spent beyond ~60 seconds on automatic
retrieval is wasted.
