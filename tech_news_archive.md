# Tech News Archive

## 2026-05-20
- Anthropic acquires Stainless for $300M+, pulling shared SDK/MCP infrastructure away from OpenAI and Google and winding down all hosted Stainless products.
- zunzunbee Slate Switch joins Works with Home Assistant — snap-on Zigbee 3.0 scene controller, no wiring, fully local, official HA blueprints, 2-year battery.
- Microsoft Surface for Business refreshed with Intel Panther Lake — claims 35% better GPU than M5 MacBook Air, 120 Hz 3:2 display, starting at $1,299.
- Seedance 2.0 sets new AI video benchmark with cross-scene character/environment locking, eliminating generative video's character-drift problem.
- Cerebras IPO pops 68% on Nasdaq debut, raising $5.55B at a $95B market cap — largest U.S. tech IPO since Uber.

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

## [2026-05-21]
- **Anthropic projects first-ever profitable quarter:** $10.9B Q2 2026 revenue (up from $4.8B in Q1), $559M operating profit — two years ahead of its own 2028 forecast; growth rate outpacing Zoom, Google, and Facebook at their historical peaks.
- **NVIDIA Q1 FY2027 all-time records:** $81.6B revenue (+85% YoY), $58.3B net income (+200%), data center alone at $75.2B; Q2 guidance raised to $91B; $80B buyback and dividend hike from $0.01 to $0.25/share announced.
- **OpenAI self-serve Ads Manager launches inside ChatGPT:** CPC bidding, no $50K minimum spend, integrations with Dentsu/Omnicom/WPP/Adobe/Criteo; targeting $2.5B ad revenue in 2026 with rollout to UK, Japan, Brazil.
- **Computex 2026 preview (June 1–5, Taipei):** Jensen Huang keynotes June 1; Intel's Lip-Bu Tan reveals 52-core Nova Lake desktop on 18A June 2; NVIDIA N1X Arm laptop chip expected to challenge Qualcomm's Windows-on-Arm lead; AMD Ryzen Z2 handhelds.
- **Google Gemini Spark unveiled at I/O:** Always-on personal AI agent that drafts, monitors, and makes purchases even when devices are locked — the clearest preview yet of ambient home AI.

## [2026-05-22]
- **OpenAI files confidential S-1 with SEC:** Goldman Sachs + Morgan Stanley underwriting a Q4 2026 IPO at ~$852B valuation; Musk loses all claims in jury trial, clearing the last legal overhang before the offering.
- **SpaceX S-1 reveals Anthropic's $45B compute deal:** Anthropic pays $1.25 billion per month for exclusive access to SpaceX's Colossus I and II GPU clusters (200,000+ NVIDIA GPUs) through May 2029.
- **AMD Ryzen 9 9950X3D2 reviews land:** $900 dual V-Cache CPU delivers under 1% average gaming improvement over the $659 predecessor; 27% higher power draw; GamersNexus titled its review "DO NOT BUY."
- **North Korean hackers use Hugging Face as malware CDN:** Fake npm packages (terminal-logger-utils, pretty-logger-utils) drop a full RAT via postinstall hook — keylogging, clipboard theft, shell access; HF trust bypasses most security filters.
- **Hackaday: "Why The Smart Home Bubble Popped":** Editorial tracing IoT arc from X10 (1975) to today's abandoned devices — cloud lock-in, competing standards, subscription creep, and vendor exits within two years compounded into a broken promise.

## 2026-05-23
- Anthropic set to close $30B+ round at ~$900B valuation as soon as next week — surpassing OpenAI in private market value, Q2 revenue projected at $10.9B with first operating profit two years ahead of schedule.
- Home Assistant 2026.5 adds first-class sub-gigahertz RF support — motorized blinds, garage door openers, ceiling fans, and wireless doorbells now integrate locally with no cloud dependency.
- Software Freedom Conservancy confirms two AGPLv3 violations by Bambu Lab, launches "baltobu" open-source replacement project; Bambu also C&D'd a Polish OrcaSlicer fork developer.
- Autograph motion design tool goes free for studios — Maxon extends zero-cost license to full teams, making it a serious alternative to After Effects for animation workflows.
- GPT-5.5 Instant is now ChatGPT's default model for all users — 52.5% fewer hallucinations on high-stakes topics, 30% shorter answers, better personalization.

## 2026-05-24
- Computex 2026 opens June 2 in Taipei — Jensen Huang keynotes June 1 with NVIDIA Vera Arm CPU (forecast 1.5× x86 performance); Intel's Lip-Bu Tan follows June 2 with 52-core Nova Lake on the 18A node.
- Cohere releases Command A+ as fully open-source under Apache 2.0 — 218B sparse MoE enterprise model, activates 25B parameters per step, runs on just two H100 GPUs via lossless W4A4 quantization.
- Anthropic opens Milan office as EMEA becomes fastest-growing region — revenue up 9× and large-business accounts up 10× year-on-year; international headcount set to triple.
- OpenAI's internal reasoning model autonomously disproves the 1946 Erdős unit-distance conjecture in discrete geometry — the first AI-resolved open mathematical problem of this class.
- Hackaday publishes "Why The Smart Home Bubble Popped" — editorial traces IoT broken promises from X10 (1975) to today: cloud lock-in, proprietary standards, vendor exits, and subscription creep.

## 2026-05-25
- Anthropic tops CNBC 2026 Disruptor 50 as #1 company above OpenAI — $30B ARR, 80× Q1 revenue growth, $900B funding round underway; Claude Code named fastest-growing product.
- AMD officially confirms FSR 4.1 ML upscaling for RX 7000-series (RDNA 3) in July 2026 and RX 6000-series (RDNA 2) in early 2027 — same neural model as RDNA 4, in 300+ supported games.
- Cerebras runs Kimi K2.6 (1T-param open-weight model) at 981 tokens/sec — 6.7× faster than GPU clouds, 29× faster end-to-end; announced days after its Nasdaq IPO.
- AI HBM demand triggers worst smartphone shipment crash in a decade — 12.9% global drop, average device price hits record $523, sub-$100 phones declared "permanently uneconomical" by IDC.
- Computex 2026 T-7 days: Jensen Huang keynotes June 1 with NVIDIA Vera ARM CPU (1.5× x86 forecast); Intel shows 52-core Nova Lake on 18A and Panther Lake gaming handhelds June 2.

## 2026-05-26
- Home Assistant 2026.5 ships native sub-gigahertz RF support via ESPHome CC1101 or Broadlink RM4 Pro — garage doors, motorized blinds, ceiling fans, and RF outlets now in HA with no cloud bridge required.
- OpenAI confidentially files S-1 with the SEC targeting a September 2026 Nasdaq debut at $852B–$1T valuation; $25B ARR but losing $1.22 per $1 earned in Q1; Goldman Sachs and Morgan Stanley lead.
- Anthropic opens Claude Security public beta (Project Glasswing) — Claude Mythos Preview and 50+ partners including Apple, Microsoft, Google, and NVIDIA have found 10,000+ critical zero-day vulnerabilities across every major OS and browser.
- Google I/O 2026 launches Gemini 3.5 Flash (flagship quality at Flash speed), Gemini Spark (background personal agent that takes real actions), and a new Managed Agents API with sandboxed remote Linux environments.
- NVIDIA GTC Taipei keynote set for June 1 ahead of Computex — Jensen Huang to outline "Five-Layer Cake" AI computing strategy; N1X ARM client CPU is the biggest wildcard for whether NVIDIA enters PC silicon in 2026.

## 2026-05-27
- Pope Leo XIV publishes "Magnifica Humanitas," a 42,300-word AI encyclical calling for robust regulation and autonomous-weapons limits; presented at the Vatican alongside Anthropic co-founder Christopher Olah — the most significant moral statement on AI from any religious institution.
- Anthropic set to close $30B+ Series H at $900B+ valuation as soon as this week — second $30B round in one calendar year, surpassing OpenAI as the world's most valuable private AI startup; Sequoia, Dragoneer, Altimeter, Greenoaks each invest ~$2B.
- Jensen Huang arrived in Taipei and declared Vera Rubin "the largest product launch, probably in the history of Taiwan" — 3.5× training and 5× inference over Blackwell at one-seventh the cost; formal Computex keynote June 1, NVIDIA Taiwan HQ groundbreaking this week.
- Anthropic in early talks to rent Microsoft Maia 200 AI chips — 30%+ cost-per-token improvement; would be the first major external customer for Microsoft's custom silicon program.
- Motionographer's teased "something big in May" revealed: "Join the 100" founding membership with lifetime perks, VIP F5 access, private Slack, and six curated Founding Partner studios — alongside the Motion Awards X launch in a "bold new era."

## 2026-05-29
- Anthropic ships Claude Opus 4.8 with dynamic workflows for large-scale Claude Code tasks, user-selectable effort controls (Low/High/Max), 1M-token context window by default, and 4× fewer missed code errors than Opus 4.7; fast mode is 2.5× quicker at 3× lower cost.
- Home Assistant 2026.6 beta drops weather tile temperature forecast bar charts, automation notes that travel with exported blueprints, and opt-in custom card suggestions in the card picker; GA and release-party livestream June 3.
- Mistral rebrands Le Chat as "Vibe" (Vibe for Work + Vibe for Code), enters industrial AI with Airbus, BMW, and ASML, announces a 10 MW Paris inference data center, and says it may design its own chips.
- Oura Ring 5 launches as the world's smallest smart ring — 40% smaller than Ring 4, rebuilt sensors tracking 30+ biometrics, new blood pressure signals, six titanium finishes, starts at $399, ships June 4.
- NVIDIA Computex June 1 preview: Vera Rubin NVL72 rack is 100% liquid-cooled with cable-free modular trays cutting install time from two hours to five minutes; Jensen Huang also presents Vera ARM CPU and a co-developed MediaTek consumer chip.

## 2026-05-30
- Anthropic closes $65B Series H at $965B post-money valuation — near $1 trillion, run-rate revenue crossed $47B, Altimeter/Dragoneer/Greenoaks/Sequoia co-lead; likely the final private fundraise before IPO.
- NVIDIA Vera Rubin NVL72 wins Computex Best Choice Golden Award and Sustainable Tech Award; Jensen Huang keynotes June 1 with Vera ARM CPU and N1X laptop SoC.
- OpenAI launches Rosalind Biodefense (trusted GPT-Rosalind access for U.S. government biopreparedness partners) and publishes Frontier Governance Framework aligning safety practices with global AI regulations.
- AI data center bans multiplying across U.S.: 69 jurisdictions now blocking new builds, four permanently; federal moratorium on 20MW+ facilities proposed; developers pivot to unincorporated rural land.
- HiDream-O1-Image 8B open-sourced on Hugging Face with reasoning-driven prompt agent, layout and skeleton conditioning — motion-design-relevant open image generation model debuting #8 in the Artificial Analysis arena.

## 2026-05-31
- NVIDIA GTC Taipei keynote tonight (11 p.m. ET): N1X ARM laptop SoC confirmed with RTX 5070-class GPU and full CUDA stack; Dell, Lenovo, Asus, and MSI readying first devices; Jensen Huang also teasing an unannounced surprise product.
- Anthropic leads enterprise AI adoption for the first time (34.4% vs. OpenAI's 32.3% per Ramp AI Index) and projects its first-ever operating profit in Q2 with revenue doubling to $10.9 billion.
- Google Chrome silently installs 4 GB Gemini Nano on every device without consent — no opt-in, auto-reinstalls after deletion; privacy researcher flags potential EU law breach across ~1 billion machines.
- Home Assistant 2026.6 beta: two-way IR blaster sync, native Matter sirens, Z-Wave smart lock PIN management, BLE-proxy Matter commissioning via ESP32/Shelly, HomeWizard EV charging strategies — GA livestream June 3.
- TSMC faces Samsung-style strike threat after reported 15% bonus cut despite 58% Q1 profit jump; company concedes and promises faster bonus growth in 2026 than 2025.

## 2026-06-01
- NVIDIA RTX Spark unveiled at Computex — first laptop SoC with 20 Arm cores, Blackwell GPU (6,144 CUDA cores, RTX 5070-class), and 128GB unified LPDDR5X memory; Dell, HP, Lenovo, Microsoft, Asus, MSI building fall devices.
- Microsoft Surface Laptop Ultra revealed — first RTX Spark device, 15-inch mini-LED PixelSense Ultra at 2,000 nits HDR, 1 petaflop AI compute, runs 120B-parameter models locally; fall availability TBD.
- Anthropic splits Claude billing June 15 — Agent SDK, Claude Code GitHub Actions, and third-party agents move to a separate non-rolling credit pool ($20 Pro / $100 Max 5× / $200 Max 20×) at full API rates; email notification June 8.
- Intel launches Arc G3 and Arc G3 Extreme for gaming handhelds (14-core CPU + Xe3 GPU, 25–80W) and previews 52-core Nova Lake desktop (Core Ultra Series 4) for late 2026.
- Home Assistant 2026.6 beta: weather tile forecast bar charts, bidirectional IR remote receive support, card picker redesign replacing internal technical names — GA release party livestream June 3.

## 2026-06-02
- Anthropic confidentially files IPO S-1 with the SEC on June 1 — revenue run-rate at $47B in May (up from $10B a year ago), last private raise valued the company at $965B; fall debut targeting ~$1 trillion.
- Intel Computex 2026 keynote: Panther Lake confirmed as first consumer chip on Intel's own 18A fab (H2 2026), 52-core Nova Lake desktop previewed, Crescent Island inference GPU scales to 480GB LPDDR5X for agentic AI.
- AMD Radeon RX 9070 GRE launches globally at $549 — formerly China-exclusive RDNA 4 card, 48 CUs, 12GB GDDR6 on 192-bit bus; AMD claims 22% faster than RTX 5060 Ti 16GB across 40+ games.
- Mistral rebrands Le Chat as Vibe — unified agent platform with Work Mode (multi-step tasks) and Code Mode (GitHub-connected dev); industrial AI deals with Airbus, BMW, ASML; €1B revenue targeted for 2026.
- Home Assistant 2026.6 beta deeper dive: bidirectional IR remotes keep HA state in sync with physical remote use; Z-Wave smart lock credential management; Matter siren support; rebuilt card picker; GA livestream June 3.

## 2026-06-03
- Home Assistant 2026.6 GA today — two-way IR receives physical remote signals (automation trigger + state sync), full Z-Wave lock credential/PIN management, Matter siren support, rebuilt dashboard editor cuts card setup from 20 minutes to seconds; release party livestream at 12:00 PT.
- MiniMax M3 launches as the first open-weight model combining 1M-token context, native multimodality, and frontier coding scores (59% SWE-Bench Pro) — surpasses GPT-5.5 and Gemini 3.1 Pro on key benchmarks at 5–10% of the cost; independent verification pending.
- GitHub Copilot usage-based AI Credit billing live since June 1 — devs report bills jumping from $29/month to $750+ for the same agentic coding workloads; Copilot Pro gets $10/month in credits, Pro+ gets $39.
- Microsoft MXC (Execution Containers) announced at Build 2026 — kernel-enforced OS-level sandbox that isolates AI agents with per-agent file/network/app policies and strong auditable identities; OpenAI, Nvidia, Manus at launch; ships Windows 11 24H2 Enterprise later in 2026.
- Anthropic Project Mythos (Glasswing) expands to 150+ organizations in 15+ countries — 10,000+ high/critical vulnerabilities found since launch; Anthropic also confirms Claude stays permanently ad-free.

## 2026-06-04
- Anthropic files confidential S-1 with the SEC — revenue run-rate at $47B in May (up 4× YoY), $965B valuation after $65B Series H; one of the largest AI IPO filings ever attempted.
- NVIDIA RTX Spark Superchip detailed at Computex 2026 — 20 Arm CPU cores, Blackwell GPU with 6,144 CUDA cores, 128GB LPDDR5X unified memory at 300 GB/s; runs 120B-param models locally, first devices fall 2026.
- Intel Crescent Island AI GPU detailed at Computex — Xe3P architecture, up to 480GB LPDDR5X (bypassing HBM shortages), 350W PCIe card targeting data center inference; H2 2026 launch.
- NVIDIA Nemotron 3 Nano Omni launches — open 30B-param multimodal model activating only 3B per pass; unifies vision, audio, and language on a single GPU at 9× higher throughput than comparable open omni models.
- Anthropic launches Claude Partner Network Services Track — three-tier certification program (Select/Preferred/Global Premier) for enterprise consulting firms; 40K+ applications and 10K certifications since March launch.

## 2026-06-05
- Holo3.1 (H Company) releases local computer-use agents running at 140ms on a 12GB GPU — 74.2% OS-World accuracy, 79.3% AndroidWorld, native function-calling; open weights with FP8/Q4 GGUF/NVFP4 on Hugging Face.
- Anthropic's Code with Claude developer conference opens in Tokyo (June 5–6); Claude Code simultaneously ships the renamed 'ultracode' trigger for dynamic workflows, faster background sessions, and Windows/WSL fixes.
- Computex 2026 closes (Day 4) — Tom's Hardware flags a deep B2B shift; Phison demonstrates PCIe 6.0 X3 SSD at 28 GB/s and 6.8M IOPS, ASUS debuts the world's first 540Hz 1080p OLED gaming monitor.
- MO:DE Festival 2026 heads to London June 18–19 — two-day animation, AI, and emerging creative tech event for motion designers with international speakers, workshops, and live demos.
- Matter and Thread cross 700+ and 1,000+ certified devices respectively in 2026 — a tenfold jump from 2024; analysts say protocol wars are largely settled, platform competition now the defining smart home battleground.

## 2026-06-06
- Anthropic reveals Claude writes over 80% of its production code (up from under 10% in early 2025) and proposes a coordinated global AI pause mechanism if recursive self-improvement accelerates beyond human oversight.
- OpenAI launches ChatGPT Dreaming V3 memory overhaul — background synthesis replaces manual memory lists, factual recall up to 82.8%; Lockdown Mode rolls out to all accounts to block prompt-injection attacks.
- Home Assistant 2026.6 ships rebuilt card picker with live previews (dashboard setup drops from 20 min to seconds), bidirectional IR remote support, Z-Wave PIN management, and transparent automation entity counts.
- Alibaba releases Qwen3.7-Plus — multimodal model with vision, video, 1M-token context at $0.40/$1.60 per million tokens; ships API-only, breaking Alibaba's open-weight tradition.
- NVIDIA RTX Spark Superchip post-Computex: Dell, HP, Lenovo, ASUS, MSI commit to fall 2026 devices; AMD RX 9070 GRE launches globally at $549 with RDNA 4 at 22% faster than RTX 5060 Ti.

## 2026-06-07
- Apple WWDC 2026 opens tomorrow (June 8) — revamped Siri powered by Google's Gemini is the headline expected announcement, alongside iOS 27 and expanded Apple Intelligence tools.
- Anthropic expands Project Glasswing to 200 organizations in 15+ countries — Claude Mythos Preview has found 23,000+ high/critical vulnerabilities in open-source software since the program launched in April.
- Claude Code ships a real-time security review plugin that flags vulnerabilities as agents write code, paired with Opus 4.8 as the new default (4× fewer unremarked code flaws than Opus 4.7).
- Home Assistant 2026.6 adopts MQTT 5 as the default protocol with a silent auto-migration; community custom cards now surface as suggestions in the rebuilt card picker.
- Writer launches event-triggered autonomous enterprise AI agents that detect business signals across Gmail, Slack, and Gong and execute multi-step workflows without human initiation.

## 2026-06-08
- Apple WWDC 2026 opens: Gemini-powered Siri unveiled, iOS 27 adds Extensions letting users set Claude or Gemini as their default assistant; Apple pays Google ~$1B/year for a custom 1.2T-parameter cloud model.
- NVIDIA and SK Hynix sign a multi-year memory co-development and supply deal targeting Vera Rubin and future platforms — addressing AI-driven development cycle delays.
- Home Assistant 2026.6 gains an IR receiver event entity, letting physical remote button presses trigger automations for the first time; Labs purpose triggers renamed "each" and "all."
- MiniMax M3 debuts as an open-weight model with 1M-token context and 59% SWE-Bench Pro scores at 5–10% the cost of GPT-5.5; open weights ship in roughly 10 days.
- iOS 27 Photos gets three on-device generative tools: Extend (outpainting), Enhance (auto color/light), and Reframe (spatial perspective shift on spatial photos) — no cloud required.

## 2026-06-09
- Hugging Face debuts on NASDAQ as "HFCE" — $42/share IPO raises $2.1B at a $15B market cap, oversubscribed 3×; marks the first major open-source AI platform to list publicly.
- Anthropic ships Claude support for Apple's Foundation Models framework — new Swift package implements the LanguageModel protocol so iOS 27/macOS 27 apps can route queries to Claude by swapping one SPM dependency; Xcode 27 dual-engine coding assistant uses the same system.
- Intel Crescent Island AI GPU confirmed at Computex — Xe3P architecture, 480GB LPDDR5X (no HBM), 350W PCIe add-in card targeting agentic inference workloads; H2 2026 launch.
- LG CNS signs group-wide Claude Enterprise agreement with Anthropic covering all 30+ LG affiliates including LG Electronics (ThinQ platform), LG Chem, and LG Display.
- NVIDIA GeForce RTX 50 Super series back on track for Q3 2026, headlined by an RTX 5060 Super with 12GB GDDR7 — a 50% VRAM increase over the current RTX 5060.

## 2026-06-10
- Anthropic releases Claude Fable 5 (Mythos-class) to the public — most powerful Claude ever released broadly; free on Pro/Max/Team/Enterprise through June 22; Stripe compressed months of engineering into one day in beta.
- Home Assistant 2026.6 overhauled the dashboard card picker with entity-first live previews and added two-way IR remote support so physical remotes now update HA device state in real time.
- OpenAI's ChatGPT Dreaming V3 memory expands to Free-tier users — background synthesis replaces manual memory lists, achieving 82.8% factual recall accuracy; time-aware updates auto-correct stale facts.
- GPU pricing crisis deepens: RTX 5090 doubles to $3,999 as AI infrastructure demand outbids gaming for GDDR7 and HBM4 wafers; memory now accounts for up to 80% of a GPU's bill of materials.
- Microsoft June Patch Tuesday sets a record with ~200 vulnerabilities fixed in a single update, covering critical flaws in Windows, Edge, and core system services.

## 2026-06-11
- OpenAI files confidential S-1 with the SEC, targeting a September 2026 IPO at an analyst-expected $1T+ valuation; Goldman Sachs, Morgan Stanley, and JPMorgan are underwriting.
- MiniMax M3 debuts as the first open-weight model to beat GPT-5.5 on SWE-Bench Pro (59%), with a 1M-token context window and native multimodality at 5–10% of proprietary model cost.
- Holo3.1 brings local computer-use agents to 12GB GPUs — 74.2% OS-World score, web/desktop/mobile support, FP8/GGUF quantized checkpoints, Apache 2.0; no cloud required.
- AI data centers are on track to consume 600 billion gallons of water annually by 2030, with two-thirds of 809 new U.S. facilities planned in drought-stressed regions.
- Anthropic expands Project Glasswing to ~150 new organizations across 15+ countries; early partners using Claude Mythos Preview have found 10,000+ high-severity security flaws.

## 2026-06-12
- OpenAI acquires cloud startup Ona to power Codex background agents — persistent cloud environments let the coding assistant run multi-hour tasks without an active session; Codex now has 5M+ weekly users, up 400% this year.
- Nvidia RTX Spark Superchip debuts at Computex 2026 — Arm CPU + Blackwell GPU + 128GB LPDDR5X unified memory in one package; runs 120B-param LLMs locally, edits 12K video, plays AAA at 1440p 100+ FPS; systems arrive fall 2026.
- Home Assistant 2026.6 ships with bidirectional IR support (physical remote presses update HA state), MQTT 5 as the new default protocol, and a redesigned live-preview card picker that cuts dashboard setup from 20 minutes to seconds.
- Apple WWDC 2026 closes — Gemini-powered Siri AI, iOS 27, and macOS "Golden Gate" headline the week; Apple also revised its divisive Liquid Glass design language following widespread pushback from designers and developers.
- AMD denies researcher a $10,000 bug bounty after patching a critical auto-updater RCE vulnerability in 124 days — company ruled the man-in-the-middle attack vector "out of scope" despite issuing a CVE and attribution.

## 2026-06-13
- SpaceX lists on Nasdaq as SPCX — shares surge 19% to ~$161 on first trading day; $75B raise at a $1.75 trillion market cap makes it the largest IPO in stock market history.
- Anthropic's Claude Fable 5 (released June 9) leads nearly every AI benchmark with a 1M-token context window, 128K output tokens, and always-on adaptive thinking; free on Pro/Max/Team/Enterprise plans through June 22.
- "Atomic Arch" supply chain attack backdoors 400+ Arch Linux AUR packages with an eBPF rootkit and credential stealer — orphaned package takeover; detection tools available on GitHub, all affected packages removed.
- OpenAI confidentially files S-1 with the SEC on June 8, targeting a ~$1 trillion valuation for a late-2026 IPO with Goldman Sachs and Morgan Stanley leading — one week after rival Anthropic's own S-1.
- Intel Crescent Island AI GPU (Xe3P) details emerge at Computex 2026 — scales to 480GB LPDDR5X (beating Nvidia Rubin and AMD MI450X on capacity), air-cooled at 350W, targeting agentic inference; ships late 2026.

## 2026-06-14
- U.S. government issues emergency export control June 12 ordering Anthropic to suspend Claude Fable 5 and Mythos 5 for all foreign nationals, citing a suspected jailbreak as a national security risk; both models taken offline globally pending review.
- Anthropic's "When AI Builds Itself" paper reveals Claude now authors 80%+ of merged production code (up from near zero in early 2025), engineers merge 8× more daily; Anthropic simultaneously calls for a global option to pause frontier AI development.
- Nvidia RTX Spark Superchip unveiled at Computex 2026 — Blackwell GPU + 20 Arm cores + 128GB unified LPDDR5X; 30+ laptops from Dell, HP, Lenovo, and Microsoft arriving fall 2026, directly challenging Apple M5.
- Home Assistant 2026.6 adds bidirectional IR control (physical remote presses now sync HA device state), redesigned card picker with live preview, Matter siren support, and Z-Wave smart lock credential management.
- AMD Radeon RX 9070 XT enters the May 2026 Steam Hardware Survey at 1.33% share, landing 25th overall just behind Nvidia's RTX 5080 — confirming strong RDNA 4 adoption roughly one year after launch.

## 2026-06-15
- Anthropic files confidential S-1 with the SEC — $965B valuation after $65B Series H, revenue up 4.7× YoY to $47B run-rate; joins OpenAI and SpaceX in a 2026 AI public-market supercycle.
- Microsoft Surface Laptop Ultra hands-on reviews land — RTX Spark delivers 1 petaflop AI compute and RTX 5070-class graphics; 2,000-nit mini-LED display is the brightest ever shipped in a Surface; called the best Windows laptop ever made.
- Fable 5 and Mythos 5 remain offline; Anthropic now describes the export-control action as a "misunderstanding" and is working with the U.S. Commerce Department to restore access.
- Home Assistant 2026.5 sub-GHz RF support highlighted: motorized blinds, garage door openers, ceiling fans, and RF outlets now natively integrated without Wi-Fi, Zigbee, or Matter.
- AMD RDNA 5 gaming GPUs slip to late 2027 or 2028 per Computex board partner reports — AI chip demand consuming TSMC capacity that would otherwise supply consumer GPUs.

## 2026-06-16
- Anthropic's "When AI Builds Itself" report reveals Claude now writes 80%+ of its own merged code (up from under 10% in early 2025) and calls for a global option to pause frontier AI development before recursive self-improvement becomes uncontrollable.
- Holo3.1 from Hcompany releases local computer-use agents (0.8B–35B) on Hugging Face — 140ms latency, 74.2% OS-World accuracy, runs on a 12GB GPU with no cloud required; adds mobile automation and native function-calling.
- Home Assistant 2026.6 GA: bidirectional IR turns physical remotes into automation triggers (via ESPHome), redesigned card picker with live entity previews slashes dashboard setup time; Android 2026.6.2 beta patches URI hijack flaw.
- AMD announces 6GW Instinct GPU deal with Meta — largest single AI infrastructure commitment ever; EPYC Venice (256-core Zen 6, PCIe Gen 6, 1.6 TB/s memory bandwidth) confirmed for H2 2026.
- Motion Awards X standard entry deadline is today (June 16) — late fees begin tonight for the tenth anniversary edition, which introduces the first-ever audience vote category.

## 2026-06-17
- Trump administration orders Anthropic to suspend all foreign-national access to Fable 5 and Mythos 5 — Commerce Department cites a jailbreak by a foreign actor; Anthropic complied but warned the standard would "essentially halt all new model deployments" industry-wide.
- Nvidia RTX Spark Superchip unveiled at Computex 2026 — Arm CPU + Blackwell GPU + 128GB LPDDR5X unified memory in one package; runs 120B-parameter models locally, Fall 2026 availability in laptops and mini-PCs.
- Hugging Face ML Intern open-source agent autonomously runs the full ML research loop (arXiv → train → eval) and outscored Claude Code on GPQA scientific reasoning (32% vs 22.99%) in under 10 hours.
- Intel Xeon 6+ Clearwater Forest launches with 288 E-cores on Intel 18A — the company's first 18A data center chip; flagship 6990E+ claims 30% better per-thread performance than AMD's 192-core EPYC 9965.
- Adobe Creative Cloud June 2026 update ships redesigned Roto Brush in After Effects, Global Audio Mute, and Marker Search; Premiere gains new AI masking and high-volume editing tools.

## 2026-06-18
- Google Home Speaker launches June 25 at $99.99 — first Gemini-native smart speaker with 360-degree audio, Pet Memory for Nest Cams, and six months of Home Premium included; pre-orders open today.
- Anthropic Project Vend Phase 2: AI agents (upgraded to Claude Sonnet 4.5) now autonomously run full businesses — hiring staff, managing supply chains, and passing government labor inspections with no human decision-makers.
- North Korean APT Sapphire Sleet backdoored 144 @mastra/* npm packages in an 88-minute campaign on June 17 — any developer machine or CI runner that installed Mastra AI packages after June 16 is potentially compromised.
- GPT-5.6 imminent: OpenAI's chief scientist confirmed a meaningful capability leap over GPT-5.5; Polymarket assigns 83% probability to a June 22-28 launch window with a rumored 1.5M-token context window.
- Adobe After Effects June 2026 deep-dive: Roto Brush replaced by AI Object Matte (Quick Selection, Object Selection, Refine Edge), new 3D Displacement Maps, and SVG-to-editable-shape-layer import.

## 2026-06-19
- SpaceX acquires Cursor (Anysphere) for $60B in all-stock deal — xAI gains dominant developer AI tooling foothold; SPCX +17%, now 4th most valuable U.S. company.
- Anthropic Seoul office opens as 3rd Asia-Pacific location; SK Telecom confirmed as Fable 5 ban trigger; Anthropic says model access to return "within days."
- GPT-5.6 expected this week — 1.5M-token context and one-third GPT-5.5 pricing rumored; Polymarket 83% probability on June 22-28 launch window.
- Sensereo MSC-1 joins Works with Home Assistant as the first Matter-over-Thread smoke and CO alarm — fully local, no cloud required, air quality sensors planned.
- ASUS ROG Rapture GT-BN98 Pro unveiled as world's first Wi-Fi 8 router, claiming up to 2× real-world throughput over Wi-Fi 7.

## 2026-06-20
- Trump tells Axios Anthropic is "no longer a national security threat" after G7 lunch with CEO Dario Amodei in Évian-les-Bains; Amodei and DeepMind's Hassabis jointly proposed a U.S.-led democratic AI coalition — Commerce Dept. ban on Fable 5 and Mythos 5 stays in force, June 20 is the subscriber refund deadline.
- GPT-5.6 codename iris-alpha leaked: 1.5M-token context window, cleaner frontend code generation from minimal prompts, reward-hacking training fix from April post-mortem; Polymarket 83% on June 22-28 launch window, API pricing rumored at one-third GPT-5.5 rates.
- Google Home Speaker pre-orders live for June 25 launch at $99.99 — Gemini for Home replaces Google Assistant with sub-100ms on-device NPU; first new Google smart speaker in six years; Nest Mini and Nest Audio discontinued.
- Qualcomm in talks to acquire Jim Keller's Tenstorrent for $8–10B — QCOM +4% on the report; would be Qualcomm's largest-ever deal and signal a major push from mobile into AI silicon and data-center inference.
- Adobe CC June 2026: Photo to Video (Firefly + Google Veo motion from stills), Object Matte replaces Roto Brush, Channel Blur / Gradient / Noise FX in After Effects — largest motion design toolset expansion in years.

## 2026-06-21
- Nobel laureate John Jumper (AlphaFold 2 co-creator) leaves Google DeepMind after nine years to join Anthropic, signaling a push into scientific AI and drug discovery pre-IPO.
- ChatGPT's global AI assistant share fell to 46.4% in May 2026 — the first sub-50% reading ever; Gemini at 27.7%, Claude at 10.3% as the market expanded 22%.
- Matter 1.6 released June 17: NFC commissioning (pair before mains power is on), Joint Fabric (shared multi-platform device network), and standardized AI Thermostat Suggestions.
- AMD Ryzen AI Halo launches at $3,999 — $700 below NVIDIA's DGX Spark (now $4,699) — with 128GB LPDDR5X unified memory, Windows 11, and up to 14% faster LLM throughput.
- Qualcomm Investor Day June 24 will formally unveil a data center AI strategy; $3B+ FY2027 target, hyperscaler custom silicon shipping late 2026, Tenstorrent talks still live.

## 2026-06-22
- CNN: "AI regulation is a mess, and Anthropic is caught in the crosshairs" — Fable 5 and Mythos 5 remain offline day 10; Amazon confirmed as the trigger; Trump called Anthropic "no longer a threat" but the Commerce Dept. ban holds.
- KPMG survey: 33% of enterprises now deploying AI agents in production, up nearly 3× from 11% just two quarters ago — the fastest enterprise adoption ramp since cloud.
- GPT-5.6 ("iris-alpha") expected this week at 83% Polymarket odds — rumored 1.5M-token context window and API pricing at one-third of GPT-5.5; OpenAI shipped health intelligence on June 18.
- Amazon Prime Day 2026 starts June 23 (through June 26): RX 9070 at $559 cheapest ever, Intel Arc B570 at $259 with 10GB VRAM; AI demand makes GPU deals rarer than prior years.
- ASUS ROG Rapture GT-BN98 Pro launches as the world's first Wi-Fi 8 router, claiming 2× real-world throughput over Wi-Fi 7 — relevant for dense smart home and always-on agent setups.

## 2026-06-23
- OpenAI launches GPT-5.5-Cyber (85.6% CyberGym) and "Patch the Planet" with Trail of Bits and HackerOne — full automated vuln-to-patch pipeline across Python, cURL, Go, and Sigstore open-source projects.
- Claude Fable 5 exits free subscription access today (June 23) — moves to usage-credit API billing at $10/$50 per million tokens; model still offline Day 11 of export ban, 57% odds of restoration before July 1.
- Amazon Prime Day 2026 goes live (June 23–26): RTX 5070 Ti at $900 cheapest ever, RTX 5080 at $1,249 at Newegg; SSDs and RAM near all-time lows amid AI infrastructure demand squeeze.
- SpaceX signs $6.3B compute deal with open-source AI startup Reflection for Colossus 2 NVIDIA GB300 access at $150M/month through 2029; SPCX falls 10% on investor concern over compute-rental focus.
- Gemini 3.5 Pro enters its GA window (June 23–30) — 2M-token context window (largest in any production frontier model), Deep Think reasoning, $15/$60 per million tokens.

## 2026-06-24
- Qualcomm Investor Day in New York reveals "Dragonfly" data center brand with AI200/AI250 inference accelerators and names the unnamed hyperscaler ASIC customer; initial shipments on track for H2 2026, BofA sees $2–5B addressable by FY2028.
- Legion AI sues US Commerce Department in DC federal court over Fable 5 export ban; Fable 5 and Mythos 5 remain offline Day 12, with Anthropic-Commerce talks active and July 8 as the next key restoration milestone.
- Noam Shazeer (Transformer paper co-author, Gemini co-lead) joins OpenAI as Architecture Research Lead after less than two years back at Google; Nobel laureate John Jumper (AlphaFold 2) departed for Anthropic the same week; Alphabet -7%.
- Google Home Speaker launches tomorrow June 25 at $99.99 — on-device Gemini via NPU, Wi-Fi 6 + Thread 1.3 + Matter built in as Thread border router; Nest Mini and Nest Audio discontinued.
- Open-weight models surge as Fable 5 ban hits Day 12: DeepSeek V4.1 tops Hugging Face trending, GLM-5.2 (MIT) becomes the top international alternative, Chinese models hold five of HF's top ten download slots.

## 2026-06-25
- Google Home Speaker launches today at $99.99 in 18 countries — on-device Gemini via NPU, 58mm 360-degree driver, Wi-Fi 6 + Thread 1.3 + Matter with Thread border router; first new Google smart speaker in six years.
- Anthropic accuses Alibaba's Qwen lab of the largest-known AI distillation attack: 25,000 fraudulent accounts, 28.8 million Claude exchanges from April 22–June 5, targeting agentic reasoning and software engineering; letter filed with Senate and White House.
- OpenAI and Broadcom unveil Jalapeño, OpenAI's first custom AI inference chip — a reticle-sized ASIC built in nine months at ~50% lower cost than GPU; initial deployment end of 2026 with multi-generation roadmap.
- Fable 5 ban Day 13: Tom Brown (Anthropic co-founder) replaces Dario Amodei in Commerce Department negotiations; Polymarket odds for model return next week jump from ~15% to 60%.
- Two more senior Google Gemini researchers — Jonas Adler and Alexander Pritzel — set to join Anthropic, accelerating Alphabet's AI talent exodus following John Jumper and Noam Shazeer's departures this month.

## 2026-06-26
- Google loses 4 AI researchers to Anthropic in one week — Jumper, Adler, Pritzel, and Conmy (all AlphaFold contributors); Bloomberg ties the exits to a $270B Alphabet market cap drop and deepening DeepMind retention concerns.
- Home Assistant 2026.7 beta drops with natural-language automations as the new default — purpose-specific triggers graduate from Labs; release party streams on YouTube July 1 at 20:00 GMT.
- TwelveLabs launches Rodeo — a creator-facing AI video agent that searches and assembles footage via natural language; powered by Marengo 3.0, supports up to one hour of video, featured on Motionographer.
- Google delays Gemini 3.5 Pro to July 2026 — quality benchmarks not yet hitting internal targets; analysts link the slip directly to this week's talent exodus from Google DeepMind.
- OpenAI Codex expands with 'Sites' (instantly hosted interactive dashboards) and six role-specific enterprise plugins covering 62 apps including Snowflake, Figma, and Salesforce; non-developers now 20% of 5M weekly users.

## 2026-06-27
- Home Assistant Matter Server 9.0 ships as a drop-in Rust replacement for the Python-based server — faster device recovery, graphical Thread and Wi-Fi network map tabs, NFC commissioning support, more reliable OTA updates.
- GPT-5.6 Sol begins government-staged limited release — 1.5M-token context window, redesigned alignment pipeline fixing reward-hacking; White House requested phased rollout over cybersecurity capabilities; public access "coming weeks."
- Fable 5 ban Day 15: US government clears Mythos 5 for US critical infrastructure organizations; Fable 5 general restoration still pending; Tom Brown leads Commerce Dept. talks; Polymarket ~60% odds for next-week return.
- GPT-4.5 officially retired from ChatGPT today — final GPT-4 family model gone; all conversations continue on GPT-5.5; o3 follows August 26; GPT-5.3 Instant update ships improved tone and reduced teaser-style phrasing.
- Anthropic Economic Index "Cadences" report maps Claude usage to human rhythms — morning news peaks, weekday work dips on weekends, sleep advice spikes at 5 a.m.; paying consumer revenue up 75% since January 2026.

## 2026-06-28
- Home Assistant 2026.7 beta "Automations That Speak Your Language" — write automations in plain English, AI converts to YAML automatically; full release scheduled July 2, 2026.
- OpenAI + Broadcom unveil Jalapeño, OpenAI's first custom AI inference chip — built in nine months using AI-assisted chip design, 50% cost savings over GPU clusters; initial deployment end of 2026.
- TwelveLabs launches Rodeo on Motionographer — AI video production agents that find and assemble footage from natural language descriptions; first application-layer product from TwelveLabs.
- Alibaba HappyHorse 1.1 rises to global No. 2 in AI video rankings — full API open with enterprise licensing, filling gap left by OpenAI Sora shutdown (March 2026) and ByteDance Seedance exit.
- Samsung SmartThings becomes first platform to support Matter cameras — Matter 1.5 camera spec, simultaneous multi-ecosystem viewing across Apple Home, Google, and Alexa.

## 2026-06-29
- OpenAI GPT-5.6 Sol, Terra &amp; Luna debut in government-gated limited preview — three-tier model family (~20 approved companies), Sol is flagship with strongest safety stack yet; broader GA in weeks.
- Fable 5 offline Day 17; Mythos 5 cleared for US Annex A critical-infrastructure orgs and foreign staff only — Fable 5 general restoration still awaiting Commerce Dept. sign-off; Polymarket ~60% odds for next-week return.
- Home Assistant 2026.7 beta adds Thread/Wi-Fi diagnostic sensors for Matter devices (channel, routing role, RSSI), Matter 1.5 soil moisture sensor support, and biggest Activity feed (Logbook) redesign in years; full release July 2.
- TSMC hiking prices across all advanced nodes — 74% of wafer business affected; will ripple to consumer GPUs, smartphones, and smart home silicon by late 2026.
- China's CPU-only supercomputer dethrones US El Capitan atop Top500 at 2.198 exaflops — no GPUs in the cluster, first CPU-only #1 in years.

## 2026-06-30
- California × Anthropic first-of-its-kind deal: all state agencies, cities, and counties get Claude at 50% off — first US state to authorize a broad AI tool under a single centralized contract; CA DMV and Medicaid already in production.
- Fable 5 ban Day 18: return described as "imminent" by source close to Anthropic; Pentagon and NSA sign-off still pending; Anthropic adds ID verification checks ahead of restoration; end-of-June Manifold market resolves today.
- GPT-5.6 pricing revealed: Sol $5/$30, Terra $2.50/$15, Luna $1/$6 per million tokens; Sol adds ultra mode with subagents; broader GA expected within weeks.
- Claude Mythos Preview (claude-mythos-preview) officially retired June 30 — developers must migrate to claude-mythos-5 via platform.claude.com migration guide.
- After Effects 26.3: 3D Displacement Maps, Depth of Field across all 3D layer types, Variable Font animation via keyframes, and SVG import as editable shape layers — biggest motion design update in the June cycle.
