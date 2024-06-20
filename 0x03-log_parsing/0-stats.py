#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics
Printing the stats after each 10 lines
"""
import sys
import re

# Dictionary to keep track of the count of each status code
stats = {"200": 0, "301": 0,
         "400": 0, "401": 0,
         "403": 0, "404": 0,
         "405": 0, "500": 0}


def print_stats(total_file_size, stats):
    """Print the current statistics.

    Args:
        total_file_size (int): total size of each log
        stats (dict): The dictionary tracker
    """
    print(f"File size: {total_file_size}")
    for status_code in sorted(stats.keys()):
        if stats[status_code] != 0:
            print(f"{status_code}: {stats[status_code]}")


def process_log_line(line):
    """Process a single log line and update stats.

    Args:
        line (str): The line to process
        log_regex (re.Pattern): The regex pattern

    Return:
        returns the filesize or 0 if not matched
    """
    match = re.split('- |"|"| " " ', str(line))
    try:
        if match:
            status_code, file_size = match[-1].split()
            if status_code in stats:
                stats[status_code] += 1
            #temporary to cause error for non int so that file_size is not added.
            int(status_code)
            return int(file_size)
    except:
        return 0


def main():
    """The main function that starts all the process"""
    total_file_size, line_count = 0, 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if line:
                file_size = process_log_line(line)
                total_file_size += file_size
                line_count += 1

            if line_count >= 10:
                print_stats(total_file_size, stats)
                total_file_size = line_count = 0
                stats.update((key, 0) for key in stats)

        # Print remaining stats if any lines were processed
        if line_count > 0:
            print_stats(total_file_size, stats)
    except KeyboardInterrupt:
        # Print stats on keyboard interrupt (Ctrl+C)
        print_stats(total_file_size, stats)
        sys.exit()


if __name__ == "__main__":
    main()
