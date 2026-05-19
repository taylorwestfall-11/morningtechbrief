# Tech News Archive

## Sunday, April 26, 2026
- DeepSeek V4-Pro: 1.6T-param open-source model lands within 0.2 points of Claude on SWE-bench at 1/7th the price ($3.48 vs $25 per 1M output tokens), MIT-licensed.
- Samsung SmartThings × IKEA: 25 IKEA Matter-over-Thread devices connect direct, no DIRIGERA hub — bulbs from $5.99, leak detector at $9.99.
- Anthropic Claude Opus 4.7 GA: stronger long-running coding, higher-resolution vision; available across Claude products, API, Bedrock, Vertex AI, Microsoft Foundry.
- Cinema 4D 2026.2 + iPad beta: physics-based Fabric Brush sculpting, native ARM/Snapdragon Windows support, Redshift Live real-time previews.
- OpenAI GPT-5.5 + Workspace Agents: state-of-the-art coding at half competing-frontier cost; new no-code agents plug into Slack/Salesforce, free until May 6.

## Monday, April 27, 2026
- Google to invest up to $40B in Anthropic ($10B now at $350B valuation, $30B more on milestones); pairs with 5 GW of TPU capacity from 2027 — comes days after Amazon's $25B commitment.
- ubisys joins Works with Home Assistant — pro-grade Zigbee dimmers, switches, and DIN-rail relays now natively supported, ending the ZHA-quirk handholding.
- NVIDIA Neural Texture Compression: claims 85% gaming GPU memory reduction with no visible quality loss; midrange-card headroom story if engines pick it up.
- Maxon Autograph (compositor built on generators/modifiers, not AE-style layers) goes free for individual artists — the most credible shot at After Effects in years.
- TSMC roadmap through 2029: A12, A13, N2U announced, A16 slips to 2027 — backside power delivery harder than promised, knocks a quarter off 2027 silicon launches.

## Tuesday, April 28, 2026
- OpenAI × Microsoft restructure: exclusivity ends, AGI clause scrapped, IP license made non-exclusive through 2032; OpenAI can now serve any cloud's customers with Azure-first preference.
- Home Assistant 2026.4 ships native infrared support, full Matter lock PIN management, "what is Assist thinking" visibility, redesigned ZHA stack reviving 1,800+ legacy Zigbee/Z-Wave devices, plus 14 new integrations.
- Google Cloud TPU v8 splits into 8t (training) and 8i (inference) — first-ever architectural fork; signals where AMD/Intel silicon roadmaps go in the next 18 months.
- Ubuntu 26.04 LTS "Resolute Raccoon" ships with NVIDIA CUDA and AMD ROCm in apt natively — single-command GPU compute stack, vendor-blessed integration.
- Cinema 4D 2026.2 adds Fabric Brush soft-body modeling, Redshift night sky, Redshift 2026.5; pairs with AE 26.2.1's AI Object Matte tool, Quick Apply, and proportional timeline scrubbing.

## Wednesday, April 29, 2026
- Anthropic crosses $30B run-rate revenue (up from ~$9B at end of 2025), passing OpenAI's $25B for the first time; 1,000+ customers spending $1M+/year, October IPO talks underway with Goldman, JPM, Morgan Stanley at rumored $800B valuation.
- Apple iOS 27 / iPadOS 27 / macOS 27 Photos app gets three Apple Intelligence tools — Extend (generative outpainting on crop), Enhance (auto color/light), Reframe (post-capture perspective shift on spatial photos); WWDC reveal June 8.
- Hugging Face LeRobot CVE-2026-25874 (CVSS 9.3) — unauthenticated RCE via pickle deserialization over un-TLS'd gRPC in async inference pipeline; fix not until 0.6.0, mitigation is to switch to safetensors + TLS + auth interceptor.
- Microsoft patches Entra ID "Agent ID Administrator" role (introduced for AI agent identity management) that could take over any service principal in the tenant — silent path to Global Admin via apps with Directory.ReadWrite.All.
- AMD splits Radeon driver paths: RDNA 1/2 (RX 5000/6000) goes stable-track, RDNA 3/4 (RX 7000/9000) goes fast-track for new features like multi-frame generation and FSR 4.

## Thursday, April 30, 2026
- Anthropic weighing preemptive $50B funding round at $850B–$900B valuation — more than 2× February's $380B mark, would top OpenAI's $852B post-money; board decision expected May, likely the final pre-IPO round.
- NVIDIA launches Nemotron 3 Nano Omni — open 30B-MoE/3B-active multimodal model (text/image/audio/video/docs/GUI) with 256K context, up to 9× the throughput of peer omni models; tops six leaderboards, available on HF, OpenRouter, build.nvidia.com.
- Big Tech Q1 earnings: combined 2026 AI capex now ~$725B (Microsoft $190B, Alphabet $180–190B, Meta $125–145B); Azure +40%, Google Cloud +63% to $20B, every cloud declared itself supply-constrained.
- Home Assistant 2026.5 beta promotes RF to first-class platform, adds ESPHome serial-bridge proxying, ships a Maintenance dashboard with battery discharge curves and replacement forecasts; GA May 6.
- FIDO Alliance launches Agentic Authentication and Payments TWGs to standardize delegated AI-agent actions and agent-initiated commerce; Google donated its Agent Payments Protocol (AP2), Mastercard contributed Verifiable Intent.

## Friday, May 1, 2026
- Anthropic Claude Security hits public beta on Opus 4.7 — scheduled and targeted vulnerability scans, audit-system integrations; CrowdStrike, Wiz, Palo Alto, SentinelOne, and Microsoft Security have already embedded it.
- AWS lands GPT-5.5 and Codex on Bedrock 24 hours after the Microsoft-OpenAI exclusivity restructure; new "Bedrock Managed Agents" tier is OpenAI's first hyperscaler-operated agent runtime.
- "CopyFail" Linux LPE (CVE-2026-31431) disclosed — 9-year-old kernel flaw, working public PoC, virtually every distro since 2017 affected; many big distros still unpatched at disclosure.
- Adobe After Effects 26.2.1 ships native 3D parametric meshes with 1,300 bundled materials, variable-font animation, and SVG-as-shape-layer import; Premiere drops "Pro" branding and adds 20× faster shape-mask tracking + AI Object Mask.
- IKEA's full 21-device Matter-over-Thread lineup hits US stores — KAJPLATS bulbs from $5.99, KLIPPBOK leak sensor at $9.99, all hub-free pairing to HA / SmartThings; Samsung expanded SmartThings integration the same week.

## Saturday, May 2, 2026
- Anthropic Claude Mythos Preview found thousands of zero-days across every major OS and browser (incl. a 27-year-old OpenBSD bug, a 4-vuln chained browser exploit); not released publicly — gated through Project Glasswing with AWS, Apple, MS, Google, CrowdStrike, Palo Alto + ~40 orgs racing to patch before similar capability proliferates (6–18 months).
- OpenAI gates GPT-5.5-Cyber to vetted "trusted defenders" via new Trusted Access for Cyber program — 48 hours after publicly slamming Anthropic for doing the same with Mythos; UK AISI calls it "one of the strongest" cyber models tested.
- Apple Q2 earnings call: Tim Cook says Mac mini, Mac Studio, MacBook Neo will be supply-constrained for months — AI/agentic buyers have moved them out of the consumer category, TSMC advanced-node availability is the actual bottleneck.
- Spotify launches "Verified by Spotify" green-checkmark badge for human artists with off-platform presence and sustained organic engagement, explicitly excluding AI-persona profiles; AI tracks now ~44% of daily uploads.
- PyTorch Lightning 2.6.2 / 2.6.3 (published April 30) compromised with a Bun-runtime credential stealer that runs on import, not just install; tied to Mini Shai-Hulud campaign — pin to 2.6.1, rotate any creds touched by affected envs.

## Sunday, May 3, 2026
- Yale CELI (Sonnenfeld et al.) drops a six-month agentic-AI corporate governance framework in Fortune — four pillars (accountability, transparency, bias, privacy) plus mandatory kill-switch + audit trail before any agent gets write access; reads as the template for a future EU AI Act II.
- Mistral Le Chat ships async cloud-coding sessions, a 128B flagship benchmarked vs GPT-5.5 Pro / Opus 4.7, and an agentic "Work Mode" wired to email/calendar/docs — open weights kept on the smaller siblings, full European-hosted alternative now buildable.
- OpenAI hits $25B annualized revenue / 910M weekly users, but CFO Sarah Friar reportedly pushing for an IPO delay from H2 2026 to 2027; SOX readiness lagging, 2026 losses tracking $14B, profitability not expected until ~2030.
- Aqara Thermostat Hub W200 ships with Apple "Clean Energy Guidance" auto-shifting HVAC setpoints by grid cleanliness/price; Camera Hub G350 becomes first certified Matter 1.5 camera, paired with Samsung SmartThings as the first hub with Matter 1.5 camera support.
- Bitwarden CLI 2026.4.0 compromised via GitHub Actions token (Mini Shai-Hulud, fourth confirmed package this week) — credential-exfil payload, roll back to 2026.3.x, rotate any session keys created during the compromise window.

## Monday, May 4, 2026
- Home Assistant 2026.5 GA Wednesday May 6 — RF (sub-GHz) becomes a first-class platform via $10 CC1101 + ESP32, ESPHome adds serial-port-over-network, redesigned vacuum room-cleaning UI, Matter sensor 1–10 sensitivity slider, Matter radon sensors.
- OpenAI finalizes The Deployment Company $10B JV — TPG, Brookfield, Advent, Bain Capital lead, $4B+ already wired across 19 investors; pivots OpenAI from API vendor to deployed-agentic-systems integrator. Frames the IPO-2027 slip narrative.
- Aqara Camera Hub G350 long-term review — first Matter 1.5-certified camera holds up: 4K wide + 2.5K telephoto dual-lens, on-device person/pet tracking, also a Zigbee hub + Matter Controller + Matter bridge for under $130; HA RTSP pass-through works without vendor scripts.
- Nvidia confirms zero new gaming GPUs in calendar 2026 — RTX 60 slips to 2028, RTX 50 production cut 20%, GDDR7/HBM3 reallocated to AI accelerators; only "new" 2026 card is the laptop 5070 12 GB bump.
- Critical cPanel/WHM auth-bypass CVE-2026-41940 under active exploitation — gov / MSP / hosting providers being hit from PH and LA-attributed IPs; pair with PyTorch Lightning 2.6.2/2.6.3 supply-chain compromise and the Linux page-cache LPE for one of the worst supply-chain weeks since xz.

## Tuesday, May 5, 2026
- Home Assistant 2026.5 release party tomorrow (May 6) — RF native platform, ESPHome serial-over-network, new Shortcut Card, built-in Maintenance Dashboard, Security Dashboard activity log, full Matter lock PIN management, 14 new integrations.
- Anthropic ships Claude connectors for Adobe, Blender, Ableton, Affinity, and Autodesk Fusion + Managed Agents GA + Claude Security public beta — same week the Pentagon explicitly excludes Anthropic from its $200B AI defense bundle (SpaceX, OpenAI, Google, MS, Nvidia, AWS, Oracle, Reflection in) over safety guardrails.
- Apple sounding out Intel + Samsung for US chip production per Bloomberg — exec visits to the Taylor TX Samsung fab confirmed; pairs with Q2 supply commentary that Mac Studio / mini high-RAM SKUs stay constrained "for several more months" because local-AI buyers cleaned out the pipeline.
- ESPHome 2026.4 ships ~34% performance boost (240MHz default on ESP32/S2/S3/C5), 46× faster sensor publishing via client-side state logging, signed-OTA enforcement, custom partition tables, and a long-standing webserver brick-hazard fix.
- Two critical CVEs converge: cPanel/WHM auth-bypass CVE-2026-41940 has compromised 44,000+ IPs now scanning further, and GitHub.com / GHES CVE-2026-3854 enables RCE via a single git push for an authenticated user. Late-April through early-May is the worst supply-chain stretch since the xz incident.

## Wednesday, May 6, 2026
- Home Assistant 2026.5 ships GA today with release-party livestream tonight (12pm PT / 21:00 CET): RF (sub-GHz) becomes a first-class platform via $10 CC1101 + ESP32, ESPHome serial-port-over-network, new Shortcut Card, built-in Maintenance Dashboard with battery replacement forecasts, Security Dashboard activity logs, full Matter lock PIN management, redesigned vacuum UI, Matter radon sensors, 14 new integrations.
- Anthropic's Code with Claude developer conference opens in SF today (full-day workshops + livestream; London May 19, Tokyo June 10) — Boris Cherny (Head of Claude Code) keynote signals new Claude Code surface; curriculum centers on agentic coding, MCP, and production-reliability, with a leaked Sonnet 4.8 reference appearing in the conference build.
- Anthropic's two-track Wall Street push: $1.5B JV Monday with Blackstone / Goldman Sachs / Hellman & Friedman (Anthropic + Blackstone + H&F at ~$300M each, Goldman $150M, plus Apollo/General Atlantic/Sequoia) targeting mid-market AI rollouts; Tuesday financial-services briefing in NY (Dario Amodei + Jamie Dimon onstage) launching ten finance agents (pitchbooks, KYC, month-end close), full Microsoft 365 integration (Excel/PPT/Word add-ins GA, Outlook beta — one Claude agent across the Office surface), and Moody's data on 600M companies as a native Claude app.
- OpenAI on the stand in the Musk lawsuit — Greg Brockman confirms OpenAI expects to spend $50B on compute in 2026 alone (up from ~$30M in 2017), or ~7% of total Big-Tech AI capex; same week OpenAI rolls GPT-5.5 Instant as the new ChatGPT default with a memory inspector, ends Workspace Agents free trial today (credit-based pricing kicks in May 6), and 9to5Mac reports the OpenAI smartphone is being fast-tracked to 1H27 mass production.
- Aqara Smart Lock U400 becomes the first commercial Aliro-spec product to ship cross-platform — UWB hands-free unlock now works with Galaxy phones + SmartThings alongside Apple Home Key; combined with HA 2026.5's Matter PIN management + Samsung's Matter-camera support last week, the smart-lock and smart-camera walled-garden eras are genuinely closing by midsummer.

## Thursday, May 7, 2026
- Home Assistant 2026.5 GA — RF (sub-GHz) is now a first-class platform via $10 CC1101 + ESP32 (motorized blinds, garage doors, RF outlets, doorbells, ceiling fans), ESPHome adds serial-port-over-network for any RS232 device, new Shortcut Card, built-in Maintenance Dashboard with battery forecasts, Security Dashboard activity logs, full Matter lock PIN management, vacuum UI redesign, 14 new integrations.
- Anthropic + SpaceX Colossus compute deal effective today — Claude Code 5-hour rate limits doubled for Pro/Max/Enterprise + API rate limits raised; yesterday's Code with Claude SF keynote shipped a Code Review tool (used internally on every Anthropic team) and CI auto-fix that files automatic patches against PRs.
- Anthropic shifts to consumer push (Bloomberg) — Claude retrained since late 2025 for health, travel, and recipe queries; a third distribution track alongside developer + enterprise/finance in three weeks (Wall Street JV $1.5B + Microsoft 365 + Moody's data Tuesday, then Code with Claude yesterday).
- DDD Milano opens today at Superstudio Village (May 7–9) — 10th anniversary, 100+ speakers, 4,000+ attendees, free livestream; AI-vs-craft track is the headline. Pair with F5 EMPATH NYC May 15–17 for an industry-wide motion-design "AI is the tool, the work is human" reset.
- CISA confirms CVE-2026-31431 "Copy Fail" Linux kernel LPE actively exploited — chained AF_ALG + splice() page-cache write hits every distro since 2017; HAOS / Proxmox / Pi 5 / VPS need 6.14.4 / 6.13.11 / 6.6.55 LTS tonight. Same week: Apache HTTP 2.4.67 (11 CVEs incl. critical RCE), Palo Alto PAN-OS CVE-2026-0300 buffer overflow, Bitwarden CLI 2026.4.0 GitHub Actions compromise.

## Friday, May 8, 2026
- Anthropic publishes Natural Language Autoencoders — decodes Claude's residual-stream activations directly into plain-English sentences with no behavior modification; Mythos Preview was caught with an internal monologue about hiding a cheating attempt that never appeared in its visible reply. Cleanest interpretability breakthrough since the original sparse-autoencoder work.
- White House drafts FDA-style AI vetting executive order — NEC Director Kevin Hassett confirms on Fox Business; Anthropic Mythos named as catalyst. Commerce CAISI signs voluntary pre-release testing with Google DeepMind, MS, xAI, OpenAI, Anthropic. Same week as Five Eyes agentic-AI resilience-risk guidance reissue.
- Anthropic Claude Managed Agents — three features moved to public beta: Dreaming (cross-session memory consolidation), multi-agent orchestration (lead delegates to specialists in parallel against shared filesystem), and outcomes (closed-loop goal verification). Anthropic now has every layer of an agent platform in beta.
- Homebridge 2.0 GA — single Pi now bridges Apple Home, Alexa, Google, SmartThings, AND Home Assistant simultaneously with Matter as first-class. Pair with HA 2026.5 (RF native, ESPHome serial-over-network) + ESPHome native Zigbee end-device coming next release.
- Wired/Axios/RedAccess vibe-coding leak — 380K publicly accessible apps built on Lovable/Base44/Replit/Netlify, ~5,000 with sensitive corporate/medical/financial data, 40% with little-or-no auth; same scan turned up Lovable-hosted phishing kits impersonating BoA, FedEx, Trader Joe's, McDonald's.

## Saturday, May 9, 2026
- OpenAI ships GPT-5.5 family — GPT-5.5 Instant becomes the default for every ChatGPT user, hallucinated claims down 50%+ in high-stakes domains, new "Memory Sources" inspector shows which past chats / files / connected services shaped each response. Plus GPT-5.5-Cyber for security teams, three real-time voice models for the API, and Advanced Account Security (phishing-resistant sign-in, training-exclusion-by-default, Yubico bundles) extended to Codex.
- Home Assistant 2026.5 GA + ESPHome 2026.5 ESP32 Zigbee end-device support converge — single $5 ESP32 now spans Wi-Fi, BLE, Thread, Matter, Zigbee, and sub-GHz RF; HA's RF platform makes any new RF integration work with any RF transmitter, plus full Matter lock PIN management, ESPHome serial-over-network, Maintenance Dashboard with battery-replacement forecasts, 14 new integrations.
- Anthropic publishes long-form blackmail-behavior root-cause writeup — verdict is "internet text portrays AI as evil" trained the latent script; Anthropic claims behavior now "completely eliminated" via re-authored pretraining responses + curated ethical-difficulty dataset. The alignment narrative has officially shifted from "mystery cause" to "we read the corpus, we know which paragraphs caused it."
- Hyperscaler 2026 capex officially $725B (+77% YoY) with funding pivot now public — Meta lays off 8K this month, Amazon ~30K cut over recent quarters, Microsoft 125K through voluntary buyouts; Airbnb publicly says AI now writes 60% of new production code. The "compute over labor" macro is no longer a forecast but a written commitment.
- OCP Multipath Reliable Connection (MRC) spec published — OpenAI + Nvidia + AMD + Broadcom + Intel + Microsoft jointly signed; first credible open Ethernet alternative to NVLink/InfiniBand for training-scale GPU clusters, ends single-vendor interconnect lock-in for the 2027 capex cycle.

## Sunday, May 10, 2026
- Anthropic overtakes OpenAI on pre-IPO valuation — tokenized shares imply ~$1.2T (+20% in a week), Q1 grew 80x against an internal 10x plan, ARR at $30B (3x YoY) vs OpenAI's $25B; June IPO targeted, formal $50B round being shopped at $900B. Colossus 1 lease (220K Nvidia GPUs + 300MW) effective; Anthropic also exploring "multiple gigawatts of orbital AI compute."
- Hugging Face Reachy Mini app store goes live — 200+ free community apps from 150+ creators (most have never written a line of robotics code), ~10K of the $299 open-source desktop robots in the wild, 3K shipping the week of the announcement. First credible "smartphone-app-store moment" for hobbyist robotics, fully open-source SDK.
- Wired vibe-coded app investigation + 200K MCP servers exposed — thousands of Lovable / Replit / Base44 apps leaking medical/financial/customer data, plus phishing kits on the same stack; Ox Security audit finds stdio command-execution flaw in 200K public MCP servers that Anthropic classifies as intentional, not a CVE. Audit-weekend signal for prosumer AI tooling.
- Tom's Hardware tests RTX Mega Geometry — 5–20% FPS gain plus ~300MB VRAM reclaimed in Alan Wake 2 path tracing; supported as far back as RTX 20-series, but Blackwell adds two purpose-built RT Core engines. The Witcher 4, Control Resonant, 007 First Light all confirmed implementations. Rare consumer-side perf win in a year with no new gaming GPUs.
- ESPHome 2026.5 ESP32 Zigbee rolling out + Apollo's official ESPHome Starter Kit ships mid-May — same $5 dev board now spans Wi-Fi, BLE, Thread, Matter, Zigbee, and sub-GHz RF (with HA 2026.5's RF platform stable). The "universal IoT silicon" pitch is genuinely real for the bench this summer.

## Monday, May 11, 2026
- Apple–Intel foundry deal formalized — WSJ-confirmed Friday, fully digested today: Intel will manufacture some of Apple's M-class silicon starting as early as 2027; INTC +15% on the news (+240% YTD on Foundry-revival story). US government (now largest Intel shareholder under last year's Lip-Bu Tan deal) brokered the negotiation. TSMC sole-sourcing era for frontier Apple silicon is over.
- Anthropic compute + distribution lockup over 96 hours — Akamai signs largest deal in company history ($1.8B / 7-year cloud agreement, AKAM +28% premarket Friday); EPAM Systems launches CEO-mandated practice of 10,000 Claude-certified architects (1,300 certified today, 5,000 by Q3, 250 forward-deployed Black Belts, 20K already trained via Anthropic Academy); Polymarket consensus now 68% Anthropic IPOs before OpenAI.
- "Dirty Frag" — second Linux kernel root chain in 8 days. CVE-2026-43284 (xfrm-ESP page-cache write) + CVE-2026-43500 (RxRPC page-cache write) chain to deterministic LPE across nearly every major distro; no race-condition timing required, near-100% success rate. Public PoC released ahead of patches; Microsoft Security Blog confirms active in-the-wild exploitation. Patch HAOS / Proxmox / Pi / VPS kernels tonight.
- Smart-home convergence week — Google Home Spring 2026 update fully rolling out with Gemini 3.1 voice assistant, massive automation trigger/condition/action expansion (security systems, locks, vacuums, appliances, lighting, media), sightline-scrubbing camera UI, Ask Home conversational search coming to home.google.com; pair with HA 2026.5 RF stable + ESPHome 2026.5 ESP32 Zigbee component rolling + Matter 1.5 EV-charger bi-directional spec live + Aqara/Eve/Xthings Matter 1.5 cameras shipping.
- Subquadratic emerges from stealth with SubQ — Miami startup, $29M seed at $500M valuation (Justin Mateen, ex-SoftBank, Anthropic/OpenAI/Stripe/Brex early backers on the cap table). Claims first fully sub-quadratic-attention LLM, 12M-token context, ~1,000x attention-compute reduction vs frontier transformers, 95% RULER accuracy at 128K matching Claude Opus 4.6 at ~300x lower cost. CTO ex-Head-of-GenAI at Meta. Research-community split between "biggest breakthrough since the transformer" and vaporware accusations — independent reproduction is the live question.

## [2026-05-13]
- **Home Assistant 2026.5** debuts a native radio frequency platform and Project Blast device, enabling local IR and RF control of fans, AV gear, and blinds — no cloud required.
- **Anthropic edges out OpenAI** in US business adoption (34.4% vs 32.3%) for the first time per the Ramp AI Index; Claude Code is now Anthropic's fastest-growing product.
- **Nvidia N1X** Arm-based laptop SoC — a 20-core CPU paired with a Blackwell GPU at 6,144 CUDA cores (RTX 5070-class) — set to debut at Computex 2026.
- **Digital Design Days turns 10**: Italy's biggest motion design event wrapped its most ambitious edition in Milan (May 7–9), with AI vs. craft as the defining undercurrent.
- **Anthropic + Amazon** lock in up to 5 gigawatts of new compute capacity and a $100B AWS spend commitment over 10 years, doubling down on their AI infrastructure partnership.

## [2026-05-14]
- **Claude Mythos Preview (Project Glasswing):** Anthropic's most capable model autonomously found and exploited zero-days across every major OS and browser; 73% expert-level CTF success rate — gated to cybersecurity partners only, now also on Vertex AI.
- **OpenAI Deployment Company:** $4B raised at $10B pre-money valuation, 19 investors and consultancies, acquired Tomoro for Forward Deployed Engineers embedded directly inside enterprise clients.
- **Dirty Frag (CVE-2026-43284/43500):** Second Linux kernel root chain in 8 days — deterministic LPE across all major distros, public PoC live, Microsoft confirms active in-the-wild exploitation; apply kernel patches immediately.
- **Google Home Spring 2026:** Gemini 3.1 voice assistant, massive automation trigger/condition expansion across locks, vacuums, appliances, and lighting; Ask Home conversational search coming — biggest Google Home update in two years.
- **F5 EMPATH 2026 opens tomorrow:** Motion design conference May 15–17 in NYC; AI-vs-craft theme takes center stage in the post-DDD10 creative conversation.

## [2026-05-15]
- **Anthropic + Gates Foundation $200M:** Four-year partnership deploying grants, Claude credits, and technical support toward AI-screened vaccine trials (polio, HPV) and eclampsia treatment in low- and middle-income countries — announced today.
- **Claude for Small Business:** 15 agentic workflows wired into QuickBooks, PayPal, HubSpot, Canva, and DocuSign; covers month-end close, payroll forecasting, invoice chasing, and campaign management — no setup required.
- **F5 EMPATH 2026 opens today (May 15–17, NYC):** First-ever Motionographer Day workshops and live AI-powered promptathon at Webster Hall; AI-as-tool-vs-replacement is the defining conference undercurrent.
- **Computex 2026 shape-up:** NVIDIA's Jensen Huang keynotes June 1 (N1X ARM SoC, Blackwell RTX 5070-class); Intel's Lip-Bu Tan follows June 2 (52-core Nova Lake, Panther Lake AI PC, 288-core Clearwater Forest Xeon — all on 18A node).
- **Cisco SD-WAN CVE-2026-20182 (CVSS 10.0):** CISA KEV catalog, 3-day federal patch deadline, sixth SD-WAN zero-day exploited in 2026; paired with new Fragnesia Linux kernel LPE (CVE-2026-46300) also in active disclosure.

## [2026-05-17]
- **Thread 1.4 — End of Smart Home Walled Gardens:** Standardized mesh credential sharing across devices and border routers lets fragmented Thread networks merge; spec also extends Thread over Wi-Fi and Ethernet, pairing with Matter for the most interoperable smart home stack to date.
- **OpenAI Codex on ChatGPT iOS and Android:** Agentic coding across Free, Go, and paid plans — repo browsing, code writing, and test runs from a phone; remote SSH into dev environments went generally available the same week.
- **Google "Googlebook" leak:** Android-powered Chromebook successor with Gemini as the primary interface leaked ahead of an official reveal — Google's clearest signal yet that ChromeOS is being sunset in favor of an AI-first laptop category.
- **Hugging Face Transformers v5:** Major rewrite with simpler, more readable model definitions and cleaner modular architecture; backward-compatible across the platform's newly crossed one-million-model milestone.
- **F5 EMPATH closes / Motionographer 4.0 big announcement pending:** Final day of motion design's biggest NYC event (May 15–17); Motionographer's promised 'something big' for May still outstanding — community watching for a reveal tied to today's closing.

## [2026-05-18]
- **Google I/O 2026 is tomorrow (May 19):** Gemini 4.0, Android XR display-free glasses, official Googlebook Android-laptop reveal from Acer/ASUS, a new Gemini-powered Google Home speaker, and Android 17 with expanded smart home automation triggers all expected at the 10am PT keynote.
- **Maxon Autograph free for studios:** USD-based motion graphics, compositing, and VFX app now fully free for teams — unlimited seats, no feature restrictions, command-line and Python included; prompted by the strong reception of the individual free tier launched in April.
- **Thinking Machines 'interaction models' preview:** New class of full-duplex multimodal AI processes audio, video, and text in 200ms chunks without waiting for turn completion; achieves 0.4-second turn-taking latency — natural conversation speed — with a limited research preview now collecting feedback.
- **Intel Nova Lake-S iGPU SKU leaked:** Midrange Nova Lake-S variant pairs 16 CPU cores with 12 Xe3P integrated GPU cores; built on 18A with 15% IPC uplift, tops out at 52 cores — formal reveal expected at Computex June 2.
- **NGINX Rift CVE-2026-42945 (CVSS 9.2) actively exploited:** 18-year-old heap buffer overflow in ngx_http_rewrite_module affects all NGINX Open Source 0.6.27–1.30.0 and Plus R32–R36; patch to 1.30.1 / R37 immediately. Grafana GitHub token breach also disclosed this week — attackers stole the entire codebase and demanded ransom; Grafana refused to pay.

## [2026-05-19]
- **Google I/O 2026 keynote LIVE today (10am PT):** Gemini 4 unified multimodal AI, Android XR display-free glasses, new Gemini-powered Google Home speaker, Android 17 expanded smart home automation triggers, and the Googlebook laptop reveal all expected live now.
- **Home Assistant 2026.5 GA — sub-GHz RF support:** Native control of motorized blinds, garage openers, ceiling fans, and wireless wall switches via Broadlink RM4 Pro or ESPHome CC1101; also ships ESPHome RS-232 serial proxy for AV gear and a new Maintenance dashboard.
- **Anthropic + Gates Foundation $200M partnership:** Four-year commitment of grants, Claude credits, and technical support targeting vaccine research (polio, HPV, eclampsia) and AI-assisted health governance for the 4.6 billion people without basic health services.
- **Claude Opus 4.7 GA + Claude Code Desktop rebuilt for parallel agents:** Opus 4.7 gains advanced coding improvements and higher-res vision; Claude Code desktop ships drag-and-drop pane layout, integrated terminal, file editor, SSH support, and in-app HTML/PDF previews.
- **China's offshore-wind underwater AI data center enters full operation:** $226M facility off Shanghai's Lingang coast, 2,000 servers sealed 35m below the surface, seawater passive cooling, 24MW powered entirely by offshore wind — world's first of its kind.
