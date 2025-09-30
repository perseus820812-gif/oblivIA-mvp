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
    # 1) 讀 sample
    if not os.path.isfile(SAMPLE_CSV):
        raise FileNotFoundError(f"Sample not found: {SAMPLE_CSV}")
    df = pd.read_csv(SAMPLE_CSV)

    # 2) 做一點點簡單統計（label 計數）
    counts = df["label"].value_counts().rename_axis("label").reset_index(name="count")

    # 3) 輸出 CSV + HTML
    ensure_dir(REPORT_DIR)
    counts.to_csv(CSV_OUT, index=False, encoding="utf-8")

    # 簡易 HTML 報告
    items = []
    for _, row in df.iterrows():
        items.append(f"<li><b>{row['subreddit']}</b>: {row['text']} → <code>{row['label']}</code></li>")

    html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>OblivIA Demo Report</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, "Noto Sans", "PingFang TC", "Microsoft JhengHei", sans-serif; margin: 24px; }}
    h1 {{ margin-bottom: 0; }}
    .muted {{ color: #666; margin-top: 4px; }}
    .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin-top: 16px; }}
    .card {{ border: 1px solid #e5e7eb; border-radius: 10px; padding: 12px; }}
    code {{ background: #f3f4f6; padding: 1px 4px; border-radius: 4px; }}
    ul {{ line-height: 1.5; }}
    table {{ border-collapse: collapse; margin-top: 12px; }}
    th, td {{ border: 1px solid #e5e7eb; padding: 6px 8px; text-align: left; }}
  </style>
</head>
<body>
  <h1>OblivIA Demo Report</h1>
  <div class="muted">This report is generated from sample data (<code>data_sample/clean_sample.csv</code>).</div>

  <div class="cards">
    <div class="card">
      <h3>Sample Items</h3>
      <ul>
        {''.join(items)}
      </ul>
    </div>
    <div class="card">
      <h3>Label Counts</h3>
      <table>
        <thead><tr><th>label</th><th>count</th></tr></thead>
        <tbody>
          {''.join(f"<tr><td>{r['label']}</td><td>{r['count']}</td></tr>" for _, r in counts.iterrows())}
        </tbody>
      </table>
      <div class="muted">CSV exported to <code>{CSV_OUT}</code></div>
    </div>
  </div>
</body>
</html>
"""
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✓ Demo report generated:\n - {HTML_OUT}\n - {CSV_OUT}")

def main():
    parser = argparse.ArgumentParser(description="Generate DoD report (demo only).")
    parser.add_argument("--demo", action="store_true", help="Run demo with sample data")
    args = parser.parse_args()

    if args.demo:
        run_demo()
    else:
        print("This public repo only supports --demo mode. For full pipeline, use the private project.")

if __name__ == "__main__":
    main()
