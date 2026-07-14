#log analyzer
#this script reads a log file and extracts useful info such as IP address, request method, request path, HTTP version, and response status code.


def read_log_file(filename):
    # open log file in read mode
    with open(filename, "r") as file:

        #read every line in the file
        for line in file:
            print(line.strip())  # print each line without extra whitespace



def main():
    #file to analyze
    log_file = "sample.log"

    #read the log file
    read_log_file(log_file)


#run program
if __name__ == "__main__":
    main()           