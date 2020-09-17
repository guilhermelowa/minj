# TODO:
# Add script to add to crontab
# Perform input validation

import argparse
from os.path import isfile
from datetime import datetime, date, time

def calc_duration(sleep_time, wakeup_time):
    sleep_time = datetime.strptime(sleep_time, "%H:%M").time()
    wakeup_time = datetime.strptime(wakeup_time, "%H:%M").time()

    delta = datetime.combine(date.min, wakeup_time) - datetime.combine(date.min, sleep_time)
    hours_sleeping = int(delta.seconds / 3600)
    minutes_sleeping = int((delta.seconds % 3600) / 60)
    sleep_duration = time(hour=hours_sleeping, minute=minutes_sleeping).isoformat(timespec="minutes")

    return sleep_time, wakeup_time, sleep_duration

def format_time(sleep_time, wakeup_time):
    sleep_time = sleep_time.isoformat(timespec="minutes")
    wakeup_time = wakeup_time.isoformat(timespec="minutes")
    return sleep_time, wakeup_time

def write_file(day, sleep_time, wakeup_time, sleep_duration, file_name="sleep_times.csv"):
    if not isfile(file_name):
        with open(file_name, "w") as f:
            f.write("day, sleep_time, wakeup_time, sleep_duration\n")
            
    with open(file_name, "a") as f:
        f.write(f'{day},{sleep_time},{wakeup_time},{sleep_duration}\n')


def sleep_log(input_args=None):
    parser = argparse.ArgumentParser(description="Log sleep")
    parser.add_argument('sleep_time', help="Format: HH:MM")
    parser.add_argument('wakeup_time', help="Format: HH:MM")
    parser.add_argument('-d', "--day", help="Day woke up - in case you need to log some missing day. Format: YYYY-MM-DD. Default: today", 
                        default=datetime.now().date())
    parser.add_argument('-f', "--file", help="File name. Default: sleep_times.csv", 
                        default="sleep_times.csv")
    
    args = parser.parse_args(input_args)
    day = args.day
    sleep_time = args.sleep_time
    wakeup_time = args.wakeup_time
    file_name = args.file
    
    sleep_time, wakeup_time, sleep_duration = calc_duration(
                                sleep_time, wakeup_time)
    sleep_time, wakeup_time = format_time(
                                sleep_time, wakeup_time)
    write_file(day, sleep_time, wakeup_time, sleep_duration, file_name)

if __name__ == "__main__":
    sleep_log()
