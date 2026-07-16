#log analyzer
#this script reads a log file and extracts useful info such as IP address, request method, request path, HTTP version, and response status code.

def update_count(dictionary, key):
    """
    Update the count of a key in the dictionary. If key exists, increment its count by 1. If key does not exist, initialize its count to 1.
    """
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1

def print_report(title, data):
    """
    print a sorted report for a dictionary
    """
    print(f"\n{title}")
    print("-" * len(title))

    for key, count in sorted(data.items(), key=lambda item: item[1], reverse=True):
        print(f"{key}: {count}")

def read_log_file(filename):
    # open log file in read mode
    with open(filename, "r") as file:


        #dictionary to store ip addresses and their counts
        ip_counts = {}

        #dictionary to store status codes and their counts
        status_counts = {}

        #dictionary to store urls and their counts
        url_counts = {}

        #dictionary to store request methods and their counts
        method_counts = {}

        #read every line in the file
        for line in file:
            
            #remove whitespace and newline characters
            line = line.strip()

            # skip comment lines and empty lines
            if line.startswith("#") or not line:
                continue
            
            #print the log entry
            #print(f"Log Entry: {line}")

            #split log entry into parts
            parts = line.split()

            #extract ip address (first item in the line)
            ip_address = parts[0]

            #extract the status code (last item in the line)
            status_code = parts[-1]

            #extract the url
            url = parts[5]

            #extract the http request method
            method = parts[4].replace('"', '')  #remove quotes from method

            #update counts using the update_count function
            update_count(ip_counts, ip_address)
            update_count(status_counts, status_code)
            update_count(url_counts, url)
            update_count(method_counts, method)

        #print the reports
            print_report("Top IP Addresses", ip_counts)
            print_report("HTTP Status Codes", status_counts)
            print_report("Top Requested URLs", url_counts)
            print_report("HTTP Request Methods", method_counts)

def main():
    #file to analyze
    log_file = "sample.log"

    #read the log file
    read_log_file(log_file)


#run program
if __name__ == "__main__":
    main()           