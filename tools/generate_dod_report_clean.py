# tools/generate_dod_report_clean.py
import argparse
import os
import pandas as pd

SAMPLE_CSV = os.path.join("data_sample", "clean_sample.csv")
REPORT_DIR = "reports"
HTML_OUT = os.path.join(REPORT_DIR, "demo_report.html")
CSV_OUT = os.path.join(REPORT_DIR, "demo_report.csv")

def ensure_dir(path: str):
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)

def run_demo():
    if not os.path.isfile(SAMPLE_CSV):
        raise FileNotFoundError(f"Sample not found: {SAMPLE_CSV}")
    df = pd.read_csv(SAMPLE_CSV)
    counts = df["label"].value_counts().rename_axis("label").reset_index(name="count")
    ensure_dir(REPORT_DIR)
    counts.to_csv(CSV_OUT, index=False, encoding="utf-8")

    items = []
    for _, row in df.iterrows():
        items.append(f"<li><b>{row['subreddit']}</b>: {row['text']} → <code>{row['label']}</code></li>")

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>OblivIA Demo Report</title></head>
<body>
<h1>OblivIA Demo Report</h1>
<ul>{''.join(items)}</ul>
<p><b>Label counts saved to:</b> {CSV_OUT}</p>
</body></html>
"""
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ Demo report generated at {HTML_OUT} and {CSV_OUT}")

def main():
    parser = argparse.ArgumentParser(description="Generate DoD report (demo only).")
    parser.add_argument("--demo", action="store_true", help="Run demo with sample data")
    args = parser.parse_args()
    if args.demo:
        run_demo()
    else:
        print("This public repo only supports --demo mode.")

if __name__ == "__main__":
    main()
