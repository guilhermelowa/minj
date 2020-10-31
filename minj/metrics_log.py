import argparse
import csv
import fileinput
from random import shuffle
from os.path import isfile
from datetime import datetime
from minj.config import CONFIG_PATH, LOGS_PATH

METRICS_PATH = LOGS_PATH + "metrics.csv"
ACTIVE_METRICS_PATH = LOGS_PATH + "active_metrics.txt"

def get_metrics(topic):
    return int(input(f'{topic}: '))

def write_file(topics, metrics):
    if not isfile(METRICS_PATH):
        header = 'timestamp,' + ','.join(topics)
        with open(METRICS_PATH, "w") as f:
            f.write(f'{header}\n')

    # Not iterating directly on dict to not mess up the order
    # on metrics.csv file
    entry = datetime.now().strftime('%Y-%m-%d %H:%M')
    for topic in topics:
        entry += ',' + str(metrics[topic])
    with open(METRICS_PATH, "a") as f:
        f.write(f'{entry}\n')

def set_active_topics(topics: list):
    with open(ACTIVE_METRICS_PATH, "w") as f:
        csvwriter = csv.writer(f, delimiter=",")
        csvwriter.writerow(topics)

def set_new_header(new_topics: list):
    new_header = "," + ",".join(new_topics)
    with fileinput.input(METRICS_PATH, inplace=True) as f:
        header = next(f)
        new_header = header[:-1] + new_header
        print(new_header)
        for line in f:
            print(line, end="")

def remove_timestamp_topic(topics: list):
    timestamp_names = ["time", "timestamp"]
    return [topic for topic in topics if topic not in timestamp_names]

def read_file_header(file_path):
    with open(file_path, "r") as f:
        csvreader = csv.reader(f, delimiter=",")
        header = next(csvreader)
        return remove_timestamp_topic(header)

def get_active_topics():
    if not isfile(ACTIVE_METRICS_PATH):
        topics = ['alertness', 'motivation', 'emotions', 'social', 'productivity', 'restness', 'workout intensity', 'self-control', 'attention']
        set_active_topics(topics)
    else:
        topics = read_file_header(ACTIVE_METRICS_PATH)
    return topics

def get_all_topics():
    if not isfile(METRICS_PATH):
        all_topics = get_active_topics()
    else:
        all_topics = read_file_header(METRICS_PATH)
    return all_topics

def metrics_log(input_args=None):
    parser = argparse.ArgumentParser(description="Log metrics")
    parser.add_argument('-a', '--add', nargs="+", help="Add topic to log. Begins recording new topic")
    parser.add_argument('-r', '--remove', nargs="+", help="Remove topic from log. No longer records given topic")
    parser.add_argument('-ls', '--list', help="List active metrics being recorded",
                        action="store_true")
    parser.add_argument('-ll', '--listall', help="List all metrics ever recorded",
                        action="store_true")
    args = parser.parse_args(input_args)

    if args.add:
        topics = get_active_topics()
        topics += args.add
        set_active_topics(topics)
        set_new_header(args.add)
    elif args.remove:
        topics = get_active_topics()
        topics = [topic for topic in topics if topic not in args.remove]
        set_active_topics(topics)
    elif args.list:
        topics = get_active_topics()
        for topic in topics:
            print(topic)
    elif args.listall:
        all_topics = get_all_topics()
        for topic in all_topics:
            print(topic)
    else:
        all_topics = get_all_topics()
        active_topics = get_active_topics()
        metrics = {}
        for topic in all_topics:
            metrics[topic] = ""

        # Show topics in different order each time
        order = [num for num in range(len(active_topics))]
        shuffle(order)
        for num in order:
            topic = active_topics[num]
            metrics[topic] = get_metrics(topic)
        write_file(all_topics, metrics)

if __name__ == "__main__":
    metrics_log()

