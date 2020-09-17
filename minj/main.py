import argparse
from sleep_log import sleep_log
from metrics_log import metrics_log

def main():
    parser = argparse.ArgumentParser(description='Minimalist Journal on CLI')
    parser.add_argument('function', choices=['metrics', 'sleep'], help='Function to call')
    
    args, unknown_args = parser.parse_known_args()
    program = args.function

    if program == 'metrics':
        metrics_log(unknown_args)
    if program == 'sleep':
        sleep_log(unknown_args)

if __name__ == "__main__":
    main()
