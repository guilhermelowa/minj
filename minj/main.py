import argparse
from os.path import isfile, expanduser
from pathlib import Path
from minj.sleep_log import sleep_log
from minj.metrics_log import metrics_log
from minj.activities import activities_log

def main():
    if not isfile("config.py"):
        config()

    parser = argparse.ArgumentParser(description='Minimalist Journal on CLI')
    parser.add_argument('function', choices=['metrics', 'sleep', 'act'], help='Function to call')
    
    args, unknown_args = parser.parse_known_args()
    program = args.function

    if program == 'metrics':
        metrics_log(unknown_args)
    if program == 'sleep':
        sleep_log(unknown_args)
    if program == 'act':
        activities_log(unknown_args)

def config():
    if not isfile("config.py"):
        usr_home = expanduser("~")
        CONFIG_PATH = usr_home + "/.local/share/minj/"
    else:
        from config import CONFIG_PATH

    new_config_path = input(f"Enter path to minj directory.\n\
It will store the configurations and journals.\n\
Default: {CONFIG_PATH}\n")
    if len(new_config_path) == 0:
        new_config_path = CONFIG_PATH
    if new_config_path[-1] == "/":
        new_logs_path = new_config_path + "logs/"
    else:
        new_logs_path = new_config_path + "/logs/"
    
    path = Path(new_logs_path)
    path.mkdir(parents=True, exist_ok=True)

    with open("config.py", "w") as f:
        f.write(f"CONFIG_PATH = \"{new_config_path}\"\n")
        f.write(f"LOGS_PATH = \"{new_logs_path}\"\n")

if __name__ == "__main__":
    main()
