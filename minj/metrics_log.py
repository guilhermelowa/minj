import argparse
from random import shuffle
from os.path import isfile
from datetime import datetime
from config import LOGS_PATH

def get_metrics(topic):
    return int(input(f'{topic}: '))

def write_file(topics, metrics, file_name="metrics.csv"):
    file_path = LOGS_PATH + file_name
    if not isfile(file_path):
        header = 'time,' + ','.join(topics)
        with open(file_path, "w") as f:
            f.write(f'{header}\n')

    entry = datetime.now().strftime('%Y-%m-%d %H:%M')
    for topic in topics:
        entry += ',' + str(metrics[topic])
    with open(file_path, "a") as f:
        f.write(f'{entry}\n')

def metrics_log(input_args=None):
    topics = ['alertness', 'motivation', 'emotions', 'social', 'productivity', 'restness', 'memory', 'workout intensity', 'self-control']

    parser = argparse.ArgumentParser(description="Log metrics")
    parser.add_argument('-a', '--add', help="Add topic to log. Begins recording new topic")
    parser.add_argument('-r', '--remove', help="Remove topic from log. No longer records given topic")
    parser.add_argument('-ls', '--list', help="List currently recorded topics",
                        action="store_true")
    args = parser.parse_args(input_args)
    
    if args.add:
        #TODO
        print("TODO")

    elif args.remove:
        #TODO
        print("TODO")
    
    elif args.list:
        for topic in topics:
            print(topic)

    else:
        metrics = {}
        for topic in topics:
            metrics[topic] = -1

        # Show topics in different order each tim
        order = [num for num in range(len(topics))]
        shuffle(order)
        for num in order:
            topic = topics[num]
            metrics[topic] = get_metrics(topic)
        write_file(topics, metrics)

if __name__ == "__main__":
    metrics_log()

