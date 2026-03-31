# Workshop Plan — Build, Shape, and Extend an OpenClaw Agent on AMD

## Format
- Jupyter notebook, run together with participants
- Duration: ~1 hour
- Audience: beginner to intermediate developers
- Architecture overview: slides or a single markdown cell with diagram (not runnable code)
- Everything else: notebook cells, pre-written, run in order

## Core promise
By the end, attendees understand:
- How OpenClaw is structured
- How to customize agent behavior
- How skills fit in
- How tools and channels fit together
- How to turn those concepts into a visible, working experience

## The story arc
"Let's take an OpenClaw agent from default → customized → extended with a skill → used to improve a live app."

## Phases

### Phase 1 — Hook (0–4 min)
Show the finished adaptive typing experience:
- Local OpenClaw agent running
- Typing app in the browser
- One round played → results analyzed → smarter follow-up round generated
Message: "This is not just a chatbot. This is a shaped agent using tools, workspace context, and reusable skills."

### Phase 2 — Architecture overview (4–10 min)
SLIDES or single markdown cell (not live code). One visual covering:
- Gateway → Agent → Workspace → Markdown control files → Tools → Skills → Channels → ClawHub
Keep short. This makes everything else make sense.

### Phase 3 — Customize the agent (10–16 min)
Live notebook cells. Modify:
- SOUL — overall behavior/personality (more coach-like, concise, developer-focused)
- USER — user-specific preferences (direct feedback, code-flavored drills, short summaries)
- Briefly touch workspace structure / multi-agent hint
Message: "This agent is shaped by durable files, not only one-off prompts."

### Phase 4 — Use the agent to inspect/build the typing app (16–24 min)
Notebook cells that:
- Read history.json, show results inline (dataframe or formatted output)
- Call stats/history modules directly
- Generate next practice word set
- Add a stats/result view or improve the UI slightly
- Generate a README or notes
Point: the agent uses your custom setup to build something.

### Phase 5 — Show tools in context (24–30 min)
- Browser to test the app
- Dev server if relevant
- Hint at multi-agent use
Message: "Tools are how the agent interacts with the world."

### Phase 6 — Build the Typing Coach skill live (30–37 min)
Pre-written cells. The skill:
- Reads typing results
- Identifies weak patterns
- Proposes the next drill
- Optionally generates code-flavored practice text
- Optionally summarizes what to improve
Key teaching: a skill is reusable, lives in a skill folder, not a one-off prompt.

### Phase 7 — Re-run the app with the skill (37–41 min)
- Run one round → show stats → invoke skill → generate better next round
Line to say: "The app did not get smarter by accident. We added a capability."

### Phase 8 — ClawHub moment (41–43 min)
One slide or cell:
- Local skills = how you build
- ClawHub = how skills become shareable
Keep brief.

### Phase 9 — Challenge (43–45 min)
**Toolsmith Challenge** — one track with variants (NOT three separate domains):
Build a small skill or capability that makes an OpenClaw agent better at a visible job.
Variants all within the typing/coach theme:
- Typing Coach+: smarter drill generation
- Code mode: code-flavored practice text
- Weak-bigram mode: target specific letter pairs

## The typing app's role
- Demonstration vehicle, not the whole curriculum
- CLI version is the "before" — agent builds the web UI as the "after"
- Participants never need to touch the terminal; everything goes through the notebook
- practice mode = data source the notebook talks to (history.json → dataframe)
- The practice mode logic is the concrete before/after: hardcoded algo → agent skill

## Key decisions
- Drop "same agent, different surfaces" as live section — mention in architecture slide only
- Architecture overview must be slides/markdown, not runnable cells
- Skill-building section: read the cell together, then run it — not typed from scratch live
- Take-home: the notebook itself is the documentation

## Status
- [x] CLI typing app built (main.py, engine.py, stats.py, history.py, display.py, words.py, config.py)
- [x] 104 tests passing
- [x] Pushed to GitHub: github.com/Mahdi-CV/open_type_faster
- [x] Blog post: https://www.amd.com/en/developer/resources/technical-articles/2026/openclaw-on-amd-developer-cloud-qwen-3-5-and-sglang.html
  - AMD Developer Cloud, MI300X GPU, $100 free credits (~50 hrs)
  - Model: Qwen3.5-122B served via SGLang Docker on port 8090
  - OpenAI-compatible endpoint: http://<droplet-ip>:8090/v1
  - OpenClaw install via CLI onboarding: enter base URL, API key, model name
  - Key docker run flags: --tp-size 1, --reasoning-parser qwen3, --tool-call-parser qwen3_coder
- [ ] Jupyter notebook to be built
- [ ] OpenClaw install + first-run cells
- [ ] Customization cells (SOUL, USER)
- [ ] Typing Coach skill cells
- [ ] Web UI scaffold cells
