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
