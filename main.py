import os
import argparse
import csv
import matplotlib.pyplot as plt


CSV_FILE_PREFIX = 'Toggl_summary_report_'
CSV_FILE_SUFFIX = '.csv'


def main(time_tracking_dir: str):
    csv_files = [f for f in os.listdir(time_tracking_dir)
                 if os.path.isfile(os.path.join(time_tracking_dir, f))
                 and f.startswith(CSV_FILE_PREFIX) and f.endswith(CSV_FILE_SUFFIX)]
    csv_files.sort()

    weeks = []
    projects = {}
    for w, csv_file in enumerate(csv_files):
        week = csv_file[len(CSV_FILE_PREFIX): -len(CSV_FILE_SUFFIX)].split("_")[0]
        weeks.append(week)

        with open(os.path.join(time_tracking_dir, csv_file), newline='') as f:
            for i, r in enumerate(csv.reader(f)):
                if i == 0:
                    continue

                project = r[0]
                time_splits = r[3].split(':')
                minutes = int(time_splits[0]) * 60 + int(time_splits[1])

                if project not in projects:
                    projects[project] = [0 for _ in range(len(csv_files))]
                projects[project][w] += minutes

    legends = []
    plots = []
    for project, minutes in projects.items():
        legends.append(project)
        plots.append(minutes)

    plt.figure('Time spend on each "Project" week-by-week')
    plt.xlabel('Week')
    plt.ylabel('Minutes')
    for plot in plots:
        plt.plot(weeks, plot)
    plt.legend(legends)
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Draw charts for my Toggl Track data")
    parser.add_argument('--time-tracking-dir', type=str, default=os.path.expanduser('~/Documents/Meta/Time Tracking'))
    args = parser.parse_args()

    main(args.time_tracking_dir)
