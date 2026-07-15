#log analyzer
#this script reads a log file and extracts useful info such as IP address, request method, request path, HTTP version, and response status code.


def read_log_file(filename):
    # open log file in read mode
    with open(filename, "r") as file:


        #dictionary to store ip addresses and their counts
        ip_counts = {}

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

            #first item is the IP address
            ip_address = parts[0]

            #if ip is already seen increase count
            if ip_address in ip_counts:
                ip_counts[ip_address] += 1
            else:
                ip_counts[ip_address] = 1

        print("\nTop IP Addresses by Request Count:")
        print("-----------------------------------")

        for ip, count in ip_counts.items():
            print(f"{ip}: {count}")


def main():
    #file to analyze
    log_file = "sample.log"

    #read the log file
    read_log_file(log_file)


#run program
if __name__ == "__main__":
    main()           