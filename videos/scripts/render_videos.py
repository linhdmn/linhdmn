#!/usr/bin/env python3
"""Render the FreePeak profile video series with local tools only."""
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "videos"
BUILD = OUT / "build"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FPS = 30
WIDTH, HEIGHT = 1080, 1920
DURATION = 45.0
VOICE_RATE = 190

# ponytail: one local renderer keeps the series reproducible without a new media
# dependency. Upgrade only if richer templates or multi-host rendering appear.
VIDEOS = [
    {
        "slug": "01-linh-doan",
        "name": "LINH DOAN",
        "kicker": "FREEPEAK OPEN SOURCE",
        "subtitle": "AI infrastructure for real production systems",
        "url": "https://github.com/linhdmn",
        "icon": "LH",
        "accent": "#22C55E",
        "tag": "ENGINEER • SRE • DEVOPS",
        "voice": (
            "Meet Linh Doan, a senior software engineer building open infrastructure where AI agents meet real production systems. "
            "Through FreePeak, he is building the database, context, gateway, coding agent, and delivery foundations that make autonomous engineering safer, cheaper, and easier to trust."
        ),
    },
    {
        "slug": "02-db-mcp-server",
        "name": "DB MCP SERVER",
        "kicker": "SAFE DATABASE ACCESS",
        "subtitle": "One MCP interface. Multiple databases. Real guardrails.",
        "url": "https://github.com/FreePeak/db-mcp-server",
        "icon": "DB",
        "accent": "#38BDF8",
        "tag": "GO • MCP • MYSQL • POSTGRES • ORACLE",
        "voice": (
            "DB MCP Server gives AI assistants one structured interface to query, inspect, and change multiple databases at the same time. "
            "It works across MySQL, PostgreSQL, SQLite, and Oracle, with read-only controls, row limits, query timeouts, masking, transactions, and audit logs. "
            "Give agents useful database access without giving them unlimited trust."
        ),
    },
    {
        "slug": "03-leankg",
        "name": "LEANKG",
        "kicker": "CODE WITH LESS CONTEXT",
        "subtitle": "A knowledge graph that makes every token count",
        "url": "https://github.com/FreePeak/LeanKG",
        "icon": "KG",
        "accent": "#A78BFA",
        "tag": "GO • MCP • 40 LANGUAGES",
        "voice": (
            "Coding agents waste tokens when every question triggers broad, repetitive searches. LeanKG indexes repositories into a local-first knowledge graph and retrieves only the relevant code, paths, callers, and impact. "
            "Its published A B results report sixty-five percent fewer tokens and eighty-five percent fewer tool calls. Less noise, faster answers, and measurable savings."
        ),
    },
    {
        "slug": "04-cortex",
        "name": "CORTEX",
        "kicker": "DECLARATIVE MCP",
        "subtitle": "Build reliable MCP servers in Go",
        "url": "https://github.com/FreePeak/cortex",
        "icon": "CX",
        "accent": "#F59E0B",
        "tag": "GO • TOOLS • RESOURCES • PROMPTS",
        "voice": (
            "Building an MCP server should not mean writing protocol plumbing by hand. Cortex is a declarative Go platform for exposing tools, resources, and prompts through a clean, structured API. "
            "Describe the surface your server needs, keep the core logic focused, and ship a standard, testable MCP experience with less boilerplate."
        ),
    },
    {
        "slug": "05-devagent",
        "name": "DEVAGENT",
        "kicker": "TICKET TO TESTED PR",
        "subtitle": "Autonomous backend delivery with evidence gates",
        "url": "https://github.com/FreePeak/devagent",
        "icon": "DV",
        "accent": "#F472B6",
        "tag": "GO • WORKTREES • SANDBOX • AUDIT",
        "voice": (
            "DevAgent turns a backend ticket into a tested pull request. It reads issues, plans implementation, runs coding workers in isolated worktrees, applies changes through sandboxed validation, and requires an independent audit before completion. "
            "The result is not code that merely looks right. It is evidence-backed delivery your team can review and merge."
        ),
    },
    {
        "slug": "06-onegw",
        "name": "ONEGW",
        "kicker": "ONE GATEWAY. THREE API FORMATS.",
        "subtitle": "Route, translate, and measure every LLM call",
        "url": "https://github.com/FreePeak/onegw",
        "icon": "OG",
        "accent": "#FB7185",
        "tag": "GO • OPENAI • ANTHROPIC • GEMINI",
        "voice": (
            "OneGW puts OpenAI, Anthropic, and Gemini compatible providers behind one lightweight Go gateway. It translates between API formats, creates fallback routes, manages provider keys, saves tokens, tracks usage, and includes its own dashboard. "
            "One process, one endpoint, and control over the whole LLM path."
        ),
    },
    {
        "slug": "07-xdev",
        "name": "XDEV",
        "kicker": "A SMALLER CODING AGENT",
        "subtitle": "One binary. Four core tools. Bounded memory.",
        "url": "https://github.com/FreePeak/xdev",
        "icon": "XD",
        "accent": "#2DD4BF",
        "tag": "GO • TUI • SESSION TREES • <100 MB RSS",
        "voice": (
            "Xdev is a lightweight coding agent rebuilt in Go as one static binary. It streams provider responses, runs the agent loop, executes four core tools, remembers sessions as inspectable JSONL trees, and renders everything in a terminal interface. "
            "Its hard memory budget keeps long runs bounded. Less runtime, less bloat, and a coding agent you can actually understand."
        ),
    },
]


def run(*args):
    subprocess.run(args, check=True)


def duration(path):
    output = subprocess.check_output(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(path),
        ],
        text=True,
    )
    return float(output.strip())


def sentences(text):
    return [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", text) if sentence.strip()]


def caption_lines(sentence):
    lines, current = [], ""
    for word in sentence.split():
        candidate = f"{current} {word}".strip()
        if len(candidate) > 29 and current:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def timings(item, speech_duration):
    sents = sentences(item["voice"])
    words = [max(len(sentence.split()), 1) for sentence in sents]
    available = max(0.1, speech_duration - 0.25)
    total = sum(words)
    start, result = 0.25, []
    for sentence, weight in zip(sents, words):
        end = min(speech_duration, start + available * weight / total)
        result.append((sentence, (start, end)))
        start = end
    return result


def art(item, index):
    names = {
        "01-linh-doan": ["GO", "TS", "RUST", "K8S"],
        "02-db-mcp-server": ["MySQL", "Postgres", "Oracle", "SQLite"],
        "03-leankg": ["tokens −65%", "tool calls −85%", "40 languages", "local-first"],
        "04-cortex": ["TOOL", "RESOURCE", "PROMPT", "MCP"],
        "05-devagent": ["TICKET", "PLAN", "BUILD", "AUDIT → PR"],
        "06-onegw": ["OpenAI", "Anthropic", "Gemini", "FALLBACK"],
        "07-xdev": ["read", "write", "edit", "bash"],
    }[item["slug"]]
    accent = item["accent"]
    cards = []
    for position, name in enumerate(names):
        x = 64 + (position % 2) * 474
        y = 480 + (position // 2) * 142
        cards.append(
            f'<div class="card" style="left:{x}px;top:{y}px;border-color:{accent}55">'
            f'<span class="dot" style="background:{accent}"></span>{html.escape(name)}</div>'
        )
    project = "PROFILE" if index == 0 else item["name"]
    return f"""
      <div class="orb orb-a" style="--accent:{accent}"></div>
      <div class="orb orb-b" style="--accent:{accent}"></div>
      <div class="grid"></div>
      <div class="chrome">
        <div class="lights"><i></i><i></i><i></i></div>
        <div class="address"><span class="lock">◆</span> github.com/{'FreePeak' if index else 'linhdmn'}</div>
        <div class="status"><b></b> PUBLIC REPOSITORY</div>
      </div>
      <div class="repo">
        <div class="repo-icon" style="background:linear-gradient(135deg,{accent},#0F172A)">{item['icon']}</div>
        <div><div class="repo-label">REPOSITORY</div><div class="repo-name">{html.escape(project)}</div></div>
      </div>
      {''.join(cards)}
      <div class="metric" style="border-color:{accent}88"><span style="color:{accent}">↗</span> OPEN SOURCE • SHIPPED IN PUBLIC</div>
      <div class="tag">{item['tag']}</div>
    """


def page(item, index, caption=None):
    accent = item["accent"]
    caption_html = ""
    if caption is not None:
        caption_html = (
            '<div class="caption"><span>'
            + "<br>".join(html.escape(line) for line in caption_lines(caption))
            + "</span></div>"
        )
    bars = "".join(
        f'<i style="height:{10 + ((j * 17 + index * 9) % 32)}px;animation-delay:{-j * 0.035}s"></i>'
        for j in range(54)
    )
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
* {{ box-sizing:border-box; }} html,body {{ margin:0; width:1080px; height:1920px; overflow:hidden; background:#07111F; }}
body {{ color:#F8FAFC; font-family:-apple-system,BlinkMacSystemFont,'SF Pro Display',Arial,sans-serif; }}
.bg {{ position:absolute; inset:0; background:radial-gradient(circle at 50% 22%, {accent}28 0, transparent 36%), linear-gradient(160deg,#07111F,#020617 65%,#07111F); }}
.grid {{ position:absolute; inset:330px 0 auto; height:870px; opacity:.11; background-image:linear-gradient({accent}88 1px,transparent 1px),linear-gradient(90deg,{accent}88 1px,transparent 1px); background-size:54px 54px; transform:perspective(700px) rotateX(58deg) translateY(-50px); transform-origin:center; mask-image:linear-gradient(transparent,black 18%,black 75%,transparent); }}
.orb {{ position:absolute; width:420px; height:420px; border-radius:50%; filter:blur(90px); opacity:.18; background:var(--accent); }} .orb-a{{left:-210px;top:630px}} .orb-b{{right:-220px;top:270px}}
.top {{ position:absolute; top:0; left:0; right:0; height:430px; padding:142px 66px 0; z-index:5; }}
.kicker {{ color:{accent}; font:700 27px/1.2 'SFMono-Regular',Consolas,monospace; letter-spacing:4px; text-align:center; }}
.name {{ margin:24px 0 0; text-align:center; font-size:98px; line-height:.96; font-weight:850; letter-spacing:-7px; max-width:1000px; margin-left:auto; margin-right:auto; }}
.name.long {{ font-size:76px; letter-spacing:-4px; }} .subtitle {{ margin:28px auto 0; max-width:880px; text-align:center; color:#CBD5E1; font-size:34px; line-height:1.25; font-weight:600; }}
.chrome {{ position:absolute; left:62px; right:62px; top:478px; height:820px; border:1px solid #47556977; border-radius:28px; background:linear-gradient(180deg,#172033F2,#0A1221F2); box-shadow:0 45px 100px #0009, 0 0 50px {accent}12; overflow:hidden; }}
.chrome:before {{ content:""; position:absolute; inset:0; background:linear-gradient(120deg,transparent 25%,{accent}0B 50%,transparent 70%); }}
.lights {{ position:absolute; top:25px; left:28px; display:flex; gap:13px; }} .lights i{{display:block;width:14px;height:14px;border-radius:50%;background:#475569}} .lights i:first-child{{background:#FB7185}}.lights i:nth-child(2){{background:#F59E0B}}.lights i:nth-child(3){{background:#22C55E}}
.address {{ position:absolute; top:19px; left:165px; right:28px; height:42px; border-radius:13px; background:#060D18; color:#64748B; text-align:center; font:19px/42px 'SFMono-Regular',Consolas,monospace; overflow:hidden; white-space:nowrap; }} .lock{{color:{accent};margin-right:9px}}
.status {{ position:absolute; top:92px; right:30px; color:#64748B; font:16px/1 monospace; letter-spacing:1px; }} .status b{{display:inline-block;width:9px;height:9px;border-radius:50%;background:#22C55E;margin-right:8px;box-shadow:0 0 14px #22C55E}}
.repo {{ position:absolute; left:42px; top:113px; display:flex; gap:23px; align-items:center; }} .repo-icon{{width:88px;height:88px;border-radius:22px;display:grid;place-items:center;font:800 30px 'SFMono-Regular',monospace;color:white;box-shadow:0 0 35px {accent}33}} .repo-label{{color:#64748B;font:15px monospace;letter-spacing:2px}} .repo-name{{font-size:34px;font-weight:760;margin-top:4px}}
.card {{ position:absolute; width:440px; height:110px; border:1px solid; border-radius:19px; background:#0B1526; display:flex; align-items:center; gap:18px; padding-left:31px; font:600 29px 'SFMono-Regular',monospace; color:#CBD5E1; box-shadow:0 18px 45px #0004; }} .dot{{width:13px;height:13px;border-radius:50%;box-shadow:0 0 18px currentColor}}
.metric {{ position:absolute; left:42px; right:42px; top:790px; height:62px; border:1px solid; border-radius:17px; display:flex;align-items:center;justify-content:center;gap:11px;color:#CBD5E1;font:600 20px monospace;letter-spacing:1.5px;background:#081321; }} .metric span{{font-size:27px}}
.tag {{ position:absolute; top:874px; left:42px; right:42px; color:{accent}; text-align:center; font:600 18px monospace; letter-spacing:1.3px; white-space:nowrap; }}
.caption {{ position:absolute; z-index:8; left:62px; right:62px; bottom:270px; color:white; text-align:center; font-size:42px; line-height:1.16; font-weight:780; letter-spacing:-1.1px; text-shadow:0 3px 16px #000,0 2px 4px #000; }}
.caption span {{ display:inline-block; background:#020617D9; padding:5px 11px; border-radius:8px; box-decoration-break:clone; -webkit-box-decoration-break:clone; }}
.wave {{ position:absolute; z-index:7; bottom:180px; left:0; right:0; height:55px; display:flex; align-items:center; justify-content:center; gap:5px; opacity:.35; }} .wave i{{display:block;width:4px;background:{accent};border-radius:4px;animation:pulse 1s ease-in-out infinite alternate}}
.cta {{ position:absolute; z-index:9; left:70px; right:70px; bottom:76px; min-height:82px; border-radius:24px; border:1px solid {accent}88; background:#081321EE; display:flex;align-items:center;justify-content:center;gap:17px; font:700 24px monospace; color:white; box-shadow:0 18px 60px #0008; }} .cta b{{color:{accent};font-size:34px}}
@keyframes pulse {{ from{{transform:scaleY(.45);opacity:.35}} to{{transform:scaleY(1);opacity:1}} }}
</style></head><body>
<div class="bg"></div><div class="top"><div class="kicker">{html.escape(item['kicker'])}</div><div class="name{' long' if len(item['name'])>9 else ''}">{html.escape(item['name'])}</div><div class="subtitle">{html.escape(item['subtitle'])}</div></div>
{art(item,index)}
<div class="wave">{bars}</div>
{caption_html}
<div class="cta"><b>↗</b> {item['url'].replace('https://github.com/','github.com/')}</div>
</body></html>"""


def screenshot(html_path, png_path):
    run(
        CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
        f"--screenshot={png_path}", f"--window-size={WIDTH},{HEIGHT}", f"file://{html_path}",
    )


def concat_quote(path):
    return str(path).replace("'", "'\\''")


def write_frame_list(frames, timeline, base_png):
    lines, previous_end = [], 0.0
    for frame, (_, (start, end)) in zip(frames, timeline):
        if start > previous_end:
            lines.extend([f"file '{concat_quote(base_png)}'", f"duration {start - previous_end:.3f}"])
        lines.extend([f"file '{concat_quote(frame)}'", f"duration {end - start:.3f}"])
        previous_end = end
    if previous_end < DURATION:
        lines.extend([f"file '{concat_quote(base_png)}'", f"duration {DURATION - previous_end:.3f}"])
    # The concat demuxer ignores the final duration unless the last file is repeated.
    lines.append(f"file '{concat_quote(base_png)}'")
    return "\n".join(lines) + "\n"


def render(item, index):
    slug = item["slug"]
    folder = BUILD / slug
    folder.mkdir(parents=True, exist_ok=True)
    audio = folder / "voice.aiff"
    run("say", "-v", "Eddy (English (US))", "-r", str(VOICE_RATE), "-o", str(audio), item["voice"])
    speech = duration(audio)
    timeline = timings(item, speech)
    base_html = folder / "base.html"
    base_png = folder / "base.png"
    base_html.write_text(page(item, index), encoding="utf-8")
    screenshot(base_html, base_png)
    frames = []
    for sentence, _ in timeline:
        frame_html = folder / f"caption-{len(frames)}.html"
        frame_png = folder / f"caption-{len(frames)}.png"
        frame_html.write_text(page(item, index, sentence), encoding="utf-8")
        screenshot(frame_html, frame_png)
        frames.append(frame_png)
    frame_list = folder / "frames.txt"
    frame_list.write_text(write_frame_list(frames, timeline, base_png), encoding="utf-8")
    silent = folder / "silent.mp4"
    run(
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(frame_list), "-i", str(audio),
        "-t", str(DURATION), "-vf", "fps=30,format=yuv420p", "-r", str(FPS),
        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "160k",
        "-movflags", "+faststart", str(silent),
    )
    output = OUT / f"{slug}.mp4"
    run(
        "ffmpeg", "-y", "-i", str(silent), "-f", "lavfi", "-i", "sine=frequency=196:sample_rate=48000:duration=45",
        "-f", "lavfi", "-i", "sine=frequency=294:sample_rate=48000:duration=45",
        "-filter_complex", "[0:a]aresample=48000,apad=pad_dur=45,atrim=duration=45,volume=1[voice];[1:a]volume=.012[a];[2:a]volume=.008[b];[voice][a][b]amix=inputs=3:duration=longest,afade=t=out:st=43:d=2[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
        "-t", str(DURATION), "-movflags", "+faststart", str(output),
    )
    print(f"rendered {output.name}: {DURATION:.0f}s (voice {speech:.1f}s)", flush=True)


def main():
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe") or not Path(CHROME).exists() or shutil.which("say") is None:
        sys.exit("Requires ffmpeg, ffprobe, macOS say, and Google Chrome")
    OUT.mkdir(exist_ok=True)
    BUILD.mkdir(exist_ok=True)
    for index, item in enumerate(VIDEOS):
        render(item, index)


if __name__ == "__main__":
    main()
