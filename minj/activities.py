import argparse
import re
import fileinput
from os.path import isfile
from datetime import datetime
from minj.config import LOGS_PATH


MINIMAL_JOURNAL_PATH = LOGS_PATH + "minimal_journal.txt"

def date_exists(date):
    with open(MINIMAL_JOURNAL_PATH, "r") as f:
        for line in f:
            if re.search(date, line):
                return True
        return False

def format_date(date):
    return f"- [{date}] -\n"

def format_activity(activity, time, duration):
    return f"{activity} {time} {duration}\n"
    
def log_activity(activity, date, time, duration=""):
    """
        Writes activities on the log file.
        Each activity is written below its date,
        which means each date is a header.
        Dates are sorted in descending order,
        meaning most recent dates on top of the file.
    
        - - -

        Example:
    
        - [24/10/20] - 
        Foo 9:30 30m
        Bar 10:20 2h 
        Fizz 15:30 30m
        Buzz 18:20 30m

        - [23/10/20] -
        Foo 12:20 30m
    """
    
    if not isfile(MINIMAL_JOURNAL_PATH):
        with open(MINIMAL_JOURNAL_PATH, "w") as f:
            f.write("activity, time, duration\n")
            f.write(format_date(date))
            f.write(format_activity(activity, time, duration))
            f.write("\n")
    else:
        if date_exists(date):
            date_found = False
            with fileinput.input(MINIMAL_JOURNAL_PATH, inplace=True) as f:
                for line in f:
                    if not date_found:
                        if re.search(date, line):
                            date_found = True
                    else:
                        if line == "\n":
                            print(format_activity(activity, time, duration), end="")
                            date_found = False
                    print(line, end="")
        else:
            # Assumes it is the newest date
            # Writes it right after header
            #  and repeat the whole file afterwards
            with fileinput.input(MINIMAL_JOURNAL_PATH, inplace=True) as f:
                first_lines = []
                header = next(f)
                print(header, end="")
                for i in range(3):
                    first_lines.append(next(f))
                print(format_date(date), end="")
                print(format_activity(activity, time, duration), end="")
                print("\n", end="")
                for line in first_lines:
                    print(line, end="")
                for line in f:
                    print(line, end="")

def activities_log(input_args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("activity",
        help="Activity you want to log")
    parser.add_argument("--date", 
        help="Date the activity was done.\
            Format: DD-MM-YYYY. Default: today",
        default=datetime.now().date().strftime('%d/%m/%Y'))
    parser.add_argument("-d", "--duration",
        help = "Duration of the activity.\
            Format: HH:MM",
        default="")
    parser.add_argument("-t", "--time",
        help="Time of the day when the activity was done",
        default=datetime.now().time().isoformat(timespec="minutes"))
    parser.add_argument("-p", "--pomodoro",
        help="Time you intend to dedicate to your activity")

    args = parser.parse_args(input_args)
    activity = args.activity
    date = args.date
    duration = args.duration
    time = args.time
    pomodoro_duration = args.pomodoro

    log_activity(activity, date, time, duration)

if __name__ == "__main__":
    activities_log()