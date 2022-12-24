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

Looking for senior backend, infrastructure, or tech lead roles where I can do deep technical work inside a strong engineering organization. Remote or open to relocation.

arkptz@gmail.com | t.me/arkptz

## Experience Descriptions

### Fenixwb | Lead Backend Engineer | Oct 2024 - Sep 2025
Inherited an unstable monolith prototype pushing ~10 tasks/sec - redesigned the entire backend on Temporal.io with ~10 microservices integrated with Elasticsearch and MySQL Pushed throughput from 10 to 200 background jobs/sec (20x), the threshold that let the product handle real user load and start onboarding paying customers Disassembled a WASM captcha binary in Ghidra, then rewrote the solver in Rust - execution dropped from 2s to 0.1s (20x faster), giving clients higher booking success rates than competing bots Migrated from MongoDB to PostgreSQL - simpler queries, fewer ops headaches for a small team Sourced and hired 2 engineers (backend + DevOps) from scratch, building the engineering function from zero - owned architecture calls, task allocation, and code review Traced a critical throughput bottleneck via hypothesis-driven load testing - the root cause fix is what took us from ~10 to 200 tasks/sec

### Cryptosofters | Founding CTO / Technical Lead | May 2023 - Nov 2024
Designed multi-wallet orchestration engine for 2,000+ EVM wallets executing 5,000+ daily transactions with zero manual intervention - clients operated at scale without needing an ops team The visual pipeline constructor was our key differentiator - users configured chains of on-chain operations (swaps, bridges, contract calls) without writing code, cutting setup from hours to minutes Zero security incidents across the platform's lifetime. Architected per-user wallet isolation, credential management, and transaction signing in a multi-tenant environment where investor confidence hinged on it Reverse-engineered closed-source smart contracts via on-chain transaction analysis and ABI decoding - often the only way to integrate protocols with no SDK, no docs, and no public API Architected the SDK generation pipeline: mitmproxy traffic capture → OpenAPI spec → auto-generated Python SDK for 20+ CEX APIs. Cut exchange integration from ~1 month to ~1 week (75%) - the force multiplier that made a 9-person team viable on a $100K budget Delivered 20+ DeFi protocol integrations (Uniswap, 1Inch, Stargate, LayerZero) with a unified interface via web3.py - per-protocol time dropped from ~1 week to ~1 day (~80%), and any team member could add protocols, not just the specialists

### Vitrinagram | Python Developer / Tech Lead | Nov 2021 - Apr 2023
Built multi-tenant Telegram MiniApp backends handling 1,000+ concurrent users per store - horizontal scaling via Celery + Kubernetes meant cost grew linearly with tenants, not exponentially Automated subdomain provisioning end-to-end: FluxCD + GitHub Actions + Cloudflare API. Tenant onboarding went from a manual multi-step process to a ~3-minute GitOps pipeline Developed an S3-compatible proxy API on MinIO for tenant-isolated file storage - eliminated the shared-storage security risk and cut costs vs managed S3 Per-tenant observability out of the box: Grafana + Victoria Metrics + Loki + Sentry dashboards clients could use for self-service debugging - support ticket volume dropped as a result Led backend development across a team of 7, owning architecture decisions for multi-tenant scalability and setting technical direction for the platform Spotted a technical leadership vacuum that was slowing delivery - escalated to the CEO, which led to team restructuring and a noticeable improvement in sprint completion rates

### Freelance | Python Backend Developer / Lead | Jan 2018 - Present
Built EVM wallet management system for a client with multiple investors: 2,000+ wallets, 5,000+ tx/day, fully autonomous - equivalent of eliminating a full-time ops person Reverse-engineered TradingView's WebSocket protocol and deobfuscated their JavaScript - collected 260M candlesticks in ~1 week covering 20+ years of forex and crypto data. Comparable feeds charge $600+/month Led 3 Go developers building a CEX arbitrage bot with sub-100ms execution latency - cross-language coordination (Python orchestration, Go hot path) where every millisecond was the difference between profit and a missed window Built automated trade replication system mirroring positions across exchange accounts in real-time - portfolio managers maintained consistent exposure without manual sync Developed a USDT-TON payment gateway with near-instant confirmation for a gaming platform - settlements in seconds vs traditional processing delays (delivered, pre-launch) Chose Rust for the Polymarket transaction parser because Python couldn't sustain the throughput - 300 blk/s from distributed event sources, production data ingestion

## Recommended Skills

Python, Rust, JavaScript/TypeScript, SQL, FastAPI, aiohttp, asyncio, Celery, Temporal.io, Pydantic, SQLAlchemy, PostgreSQL, Redis, MySQL, Elasticsearch, TimescaleDB, Kubernetes, Docker, FluxCD, GitHub Actions, CI/CD, Helm, Cloudflare, MinIO, NixOS, k3s, Terraform, Grafana, Victoria Metrics, Loki, Sentry, Web3.py, ethers.js, EVM, DeFi protocols (Uniswap, 1Inch, Stargate, LayerZero), TON SDK, mitmproxy, Team Building (up to 9), Code Review, Architecture Decisions, Hiring, Budget Management, Agile, PyTorch, TensorFlow, scikit-learn, pandas, numpy, Feature Engineering, LSTM/CNN, Web Application Analysis (Burp Suite, Chrome DevTools), JavaScript Deobfuscation, WebSocket Protocol Analysis, On-chain Transaction Analysis, ABI Encoding/Decoding, Traffic Analysis (mitmproxy), WASM Binary Analysis (Ghidra)

## Call to Action

Open to senior backend, infrastructure, and tech lead roles. Remote or relocation. Reach me at arkptz@gmail.com or t.me/arkptz
