# OblivIA: Turning Crypto Noise into Market Signals

> **One-liner:** OblivIA cleans crypto noise and turns it into actionable market signals — so traders don’t drown in spam.

OblivIA is an AI-powered pipeline that cleans noisy crypto chatter from social media (e.g. Reddit) and transforms it into structured **signals**.

---

## 🚀 Features (MVP)
- **Data Cleaning** – Remove spam, airdrops, and irrelevant text with simple, reproducible filters (demo).
- **Classification** – Logistic Regression + TF-IDF baseline (concept showcased in demo).
- **Signal Layer** – Daily & DoD (Day-over-Day) style outputs to surface emerging narratives.
- **Demo Mode** – One command generates a sample HTML + CSV report.

---

## ⚡ Quick Start

### Option A — Python
```bash
git clone https://github.com/perseus820812-gif/oblivIA-mvp.git
cd oblivIA-mvp
pip install -r requirements.txt
python tools/generate_dod_report_clean.py --demo
# OblivIA: Turning Crypto Noise into Market Signals > **One-liner:** OblivIA cleans crypto noise and turns it into actionable market signals — so traders don’t drown in spam. OblivIA is an AI-powered pipeline that cleans noisy crypto chatter from social media (e.g. Reddit) and transforms it into structured **signals**. --- ## 🚀 Features (MVP) - **Data Cleaning** – Remove spam, airdrops, and irrelevant text with simple, reproducible filters (demo). - **Classification** – Logistic Regression + TF-IDF baseline (concept showcased in demo). - **Signal Layer** – Daily & DoD (Day-over-Day) style outputs to surface emerging narratives. - **Demo Mode** – One command generates a sample HTML + CSV report. --- ## ⚡ Quick Start ### Option A — Python
bash
git clone https://github.com/perseus820812-gif/oblivIA-mvp.git
cd oblivIA-mvp
pip install -r requirements.txt
python tools/generate_dod_report_clean.py --demo
Option B — PowerShell (Windows)
powershell
複製程式碼
.\tools\run_dod_clean.ps1
Outputs

reports/demo_report.html – sample visual report

reports/demo_report.csv – label counts

This public repo only supports --demo with data_sample/. The full internal pipeline is private.

📂 Project Structure
pgsql
複製程式碼
oblivIA-mvp/
 ├─ tools/
 │   ├─ run_dod_clean.ps1
 │   └─ generate_dod_report_clean.py
 ├─ data_sample/
 │   ├─ reddit_raw_sample.json
 │   └─ clean_sample.csv
 ├─ reports/
 │   └─ demo_report.html
 ├─ requirements.txt
 └─ README.md
🛡️ What’s NOT Included (by design)
Full labeled datasets and internal cleaning rules (stopwords / allowlist / regex)

Merged term lists (e.g., crypto_terms_merged.txt)

Trained models or retraining pipeline

🌱 Roadmap
 Scale labeled dataset (500 → 5k)

 Real-time dashboard (API + frontend)

 Multi-platform ingestion (X/Telegram/Discord)

 Stronger models & evaluation (LLM-assisted filtering)

🏆 Hackathon Context
Prepared for Colosseum – Cypherpunk Track.
Goal: demonstrate a working path from noise → clean data → simple signals.

📜 License
MIT — see LICENSE.