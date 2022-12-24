# LinkedIn Profile Texts

Ready-to-copy texts for LinkedIn profile.

## Headline (220 chars max)

Tech Lead & Senior Backend Engineer | Python · Rust · Crypto Infrastructure | Ex-CTO | Trading Systems & DeFi

## About

When a WASM captcha was the last thing standing between our platform and 10K users, I disassembled it in Ghidra and rewrote the solver in Rust. Execution dropped from 2 seconds to 100 milliseconds.

That's the kind of problem I gravitate toward - the ones where you need to understand systems at the binary level to make them work at scale.

As a backend engineer and technical leader, I build high-throughput distributed systems in Python and Rust. At FenixWB, I inherited an unstable monolith doing ~10 tasks/sec and redesigned it on Temporal.io with ~10 microservices - pushing throughput to 200 jobs/sec (20x) and enabling the product to onboard paying customers.

At Cryptosofters, I was the founding CTO. Built a 9-person engineering team from zero on a $100K annual budget - roughly a tenth of what competitors spent. The force multiplier was an SDK generation pipeline I architected: mitmproxy traffic capture → OpenAPI spec → auto-generated Python SDK. It cut exchange integration from ~1 month to ~1 week across 20+ undocumented APIs.

I'm comfortable across the stack: Kubernetes clusters on bare metal, full observability (Grafana/VictoriaMetrics/Loki), protocol reverse engineering, and enough Rust to reach for it when Python can't sustain the throughput - like the 300 blk/s data ingestion service I built for production.

Currently building quantitative backtesting infrastructure with 260M+ candles on TimescaleDB.

Next step: a team that takes system design as seriously as I do. Open to senior backend, infrastructure, or tech lead roles - remote or relocation.

arkptz@gmail.com | t.me/arkptz

## Experience Descriptions

### Fenixwb | Lead Backend Engineer | Oct 2024 - Sep 2025

Wildberries slot booking service - 200 jobs/sec, 10K+ users

→ Inherited an unstable monolith prototype pushing ~10 tasks/sec - redesigned the entire backend on Temporal.io with ~10 microservices integrated with Elasticsearch and MySQL
→ Pushed throughput from 10 to 200 background jobs/sec (20x), the threshold that let the product handle real user load and start onboarding paying customers
→ Disassembled a WASM captcha binary in Ghidra, then rewrote the solver in Rust - execution dropped from 2s to 0.1s (20x faster), giving clients higher booking success rates than competing bots
→ Migrated from MongoDB to PostgreSQL - simpler queries, fewer ops headaches for a 3-person backend team
→ Sourced and hired 2 engineers (backend + DevOps) from scratch, building the engineering function from zero - owned architecture calls, task allocation, and code review

**Tech:** Rust, Python, Temporal.io, Elasticsearch, MySQL, PostgreSQL, asyncio, Grafana, Victoria Metrics, Loki, Docker, Kubernetes
**LinkedIn Skills:** Python, Rust, Temporal.io, Kubernetes, System Design

### Cryptosofters | Founding CTO / Technical Lead | May 2023 - Nov 2024

Multi-wallet orchestration platform with visual pipeline builder - near-production, drag-and-drop wallet operations

→ Designed multi-wallet orchestration platform with drag-and-drop pipeline constructor - users configured chains of on-chain operations (swaps, bridges, contract calls) without code. Built to near-production before investment stopped
→ Under the hood: event-driven state machine with per-wallet operation queues, automatic retry with exponential backoff, and transaction rollback on partial failures - the engine that made drag-and-drop orchestration reliable enough for real money
→ Zero security incidents across the platform's lifetime. Architected per-user wallet isolation, credential management, and transaction signing in a multi-tenant environment where investor confidence hinged on it
→ Reverse-engineered closed-source smart contracts via on-chain transaction analysis and ABI decoding - often the only way to integrate protocols with no SDK, no docs, and no public API
→ Architected the SDK generation pipeline: mitmproxy traffic capture → OpenAPI spec → auto-generated Python SDK for 20+ CEX APIs. Cut exchange integration from ~1 month to ~1 week (75%) - the force multiplier that made a 9-person team viable on a $100K budget

**Tech:** Python, Web3.py, mitmproxy, OpenAPI, asyncio, PostgreSQL, Redis, Docker
**LinkedIn Skills:** Python, Team Leadership, API Design, System Architecture, Distributed Systems

### Vitrinagram | Python Developer / Tech Lead | Nov 2021 - Apr 2023

Telegram MiniApp e-commerce platform - multi-tenant storefronts, 1,000+ concurrent users per store

→ Built multi-tenant Telegram MiniApp backends handling 1,000+ concurrent users per store - horizontal scaling via Celery + Kubernetes meant cost grew linearly with tenants, not exponentially
→ Automated tenant provisioning: FluxCD + Cloudflare API pipeline, ~3 minutes from commit to live subdomain
→ Developed an S3-compatible proxy API on MinIO for tenant-isolated file storage - eliminated the shared-storage security risk and cut costs vs managed S3
→ Per-tenant observability out of the box: Grafana + Victoria Metrics + Loki + Sentry dashboards clients could use for self-service debugging - ~40% fewer support tickets once clients could self-debug
→ Led backend development across a team of 7, owning architecture decisions for multi-tenant scalability, setting technical direction for the platform, and mentoring mid-level engineers through code review and design discussions that improved team velocity over two quarters

**Tech:** Python, FastAPI, Celery, PostgreSQL, Redis, Docker, Kubernetes, FluxCD, Grafana, Victoria Metrics, Loki, Sentry, MinIO, Cloudflare
**LinkedIn Skills:** Python, FastAPI, Kubernetes, Microservices, Technical Leadership

### Freelance | Python Backend Developer / Lead | Jan 2018 - Present

Crypto infrastructure, trading systems, and data pipelines

→ Built EVM wallet management system for a client with multiple investors: 2,000+ wallets, 5,000+ tx/day, fully autonomous - equivalent of eliminating a full-time ops person
→ Reverse-engineered TradingView's WebSocket protocol and deobfuscated their JavaScript - collected 260M candlesticks in ~1 week covering 20+ years of forex and crypto data. Comparable feeds charge $600+/month
→ Led 3 Go developers building a CEX arbitrage bot with sub-100ms execution latency - cross-language coordination (Python orchestration, Go hot path) where every millisecond was the difference between profit and a missed window
→ Portfolio managers needed consistent exposure across 10+ exchange accounts - built an automated replication system mirroring positions in real-time with near-zero drift between source and mirror
→ Developed a USDT-TON payment gateway with near-instant confirmation for a gaming platform - settlements in seconds vs traditional processing delays (delivered, pre-launch)

**Tech:** Python, Rust, JS/TS, Web3.py, ethers.js, PostgreSQL, Redis, asyncio, NixOS, k3s, Terraform, TimescaleDB, Docker
**LinkedIn Skills:** Python, Rust, PostgreSQL, Blockchain, System Design

## Recommended Skills

**Languages:** Python, Rust, JavaScript/TypeScript, SQL
**Frameworks & Libraries:** FastAPI, aiohttp, asyncio, Celery, Temporal.io, Pydantic, SQLAlchemy
**Databases:** PostgreSQL, Redis, MySQL, Elasticsearch, TimescaleDB
**Cloud & DevOps:** Kubernetes, Docker, FluxCD, GitHub Actions, CI/CD, Helm, Cloudflare, MinIO, NixOS, k3s, Terraform
**Observability:** Grafana, Victoria Metrics, Loki, Sentry
**Blockchain & DeFi:** Web3.py, ethers.js, EVM, DeFi protocols (Uniswap, 1Inch, Stargate, LayerZero), TON SDK, mitmproxy
**ML & Data:** PyTorch, TensorFlow, scikit-learn, pandas, numpy, Feature Engineering, LSTM/CNN
**Security & Analysis:** Web Application Analysis (Burp Suite, Chrome DevTools), JavaScript Deobfuscation, WebSocket Protocol Analysis, On-chain Transaction Analysis, ABI Encoding/Decoding, Traffic Analysis (mitmproxy), WASM Binary Analysis (Ghidra)

## Call to Action

Open to senior backend, infrastructure, and tech lead roles. Remote or relocation. Reach me at arkptz@gmail.com or t.me/arkptz
