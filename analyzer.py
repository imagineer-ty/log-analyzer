# Log analyzer
# This script reads a log file and extracts useful information such as
# IP address, request method, request path, HTTP version, and response status code.

import sys


def update_count(dictionary, key):
    """
    Update the count of a key in the dictionary.
    If the key exists, increment its count by 1.
    If the key does not exist, initialize its count to 1.
    """
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1


def print_report(title, data, output):
    """
    Print a sorted report for a dictionary.
    Results are sorted from highest count to lowest count.
    """
    print(f"\n{title}", file=output)
    print("-" * len(title), file=output)

    for key, count in sorted(data.items(), key=lambda item: item[1], reverse=True):
        print(f"{key}: {count}", file=output)


def read_log_file(filename):
    # Open log file in read mode
    with open(filename, "r") as file:

        # Dictionaries to store counts
        ip_counts = {}
        status_counts = {}
        url_counts = {}
        method_counts = {}

        # Read every line in the file
        for line in file:

            # Remove whitespace and newline characters
            line = line.strip()

            # Skip comment lines and empty lines
            if line.startswith("#") or not line:
                continue

            # Split log entry into parts
            parts = line.split()

            # Extract IP address (first item)
            ip_address = parts[0]

            # Extract status code (last item)
            status_code = parts[-1]

            # Extract requested URL
            url = parts[5]

            # Extract HTTP request method and remove quotes
            method = parts[4].replace('"', "")

            # Update counters
            update_count(ip_counts, ip_address)
            update_count(status_counts, status_code)
            update_count(url_counts, url)
            update_count(method_counts, method)

        # Print reports after analyzing the entire file
        print_report("Top IP Addresses", ip_counts, sys.stdout)
        print_report("HTTP Status Codes", status_counts, sys.stdout)
        print_report("Top Requested URLs", url_counts, sys.stdout)
        print_report("HTTP Request Methods", method_counts, sys.stdout)


def main():
    # File to analyze
    log_file = "sample.log"

    # Read the log file
    read_log_file(log_file)


# Run program
if __name__ == "__main__":
    main()