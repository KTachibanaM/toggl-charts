# toggl-charts

Draw charts for my Toggl Track data

# Prerequisites

* `Python 3.7+`

# Prepare

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

# Use

Create a folder to store all weekly reports in CSV

Every Sunday, download a CSV report from your Toggl workspace `https://track.toggl.com/reports/summary/<your_workspace_id>` to the folder

When you download, the CSV files should be named like `Toggl_summary_report_xxxx-xx-xx_xxxx-xx-xx.csv`

Enter virtualenv by using `source ./venv/bin/activate`

Use `python main.py --time-tracking-dir=<path_to_your_csv_folder>` to view a line chart that displays time spent on each `Project` week-by-week
