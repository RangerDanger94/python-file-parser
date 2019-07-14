import csv
import sys
from enum import Enum
from collections import Counter

class FileHeaders(Enum):
    IP_ADDRESS = 1
    REQUEST_URL = 2

# Just the headers we care about at the moment
FILE_HEADERS = { FileHeaders.IP_ADDRESS: 0, FileHeaders.REQUEST_URL: 5 }

def most_frequent(List, top):
    occurence_count = Counter(List)
    return occurence_count.most_common(top)

class FileRecord:
    ip_address = ''
    request_url = ''

    def __init__(self, ip_address, request_url):
        self.ip_address = ip_address
        self.request_url = request_url

    def __str__(self):
        return f'IP: {self.ip_address}, URL: {self.request_url}'

    def __repr__(self):
        return str(self)

class File:
    records = []

    def ip_addresses(self): 
        return list(map(lambda x : x.ip_address, self.records))

    def request_urls(self):
        return list(map(lambda x : x.request_url, self.records))

    def __init__(self, records):
        self.records = records

    def active_ips(self, top):
        return most_frequent(self.ip_addresses(), top)

    def active_urls(self, top):
        
        return most_frequent(self.request_urls(), top)

    def distinct_ips(self): 
        return len(set(self.ip_addresses()))


def process_file(filepath):
    records = []

    with open(filepath, mode='r') as input_file:
        reader = csv.reader(input_file, delimiter=' ', quotechar='"')
        for row in reader:
            if (len(row) <= FILE_HEADERS[FileHeaders.REQUEST_URL]): 
                print(f'Row {reader.line_num} is malformed, expecting at least ' +
                    f'{FILE_HEADERS[FileHeaders.REQUEST_URL]} columns: "{" ".join(row)}"')
                continue

            ip_address = row[FILE_HEADERS[FileHeaders.IP_ADDRESS]]
            request_url = row[FILE_HEADERS[FileHeaders.REQUEST_URL]]

            records.append(FileRecord(ip_address, request_url))

    return File(records)

def main():
    if (len(sys.argv) < 2):
        sys.exit('ERROR: Expected path to input file as first argument. e.g. "py main.py <FILE_PATH>"')

    filepath = sys.argv[1]
    
    file = process_file(filepath)

    active_ips = file.active_ips(3)
    active_urls = file.active_urls(3)
    distinct_ips = file.distinct_ips()

    print(f'Top 3 IP Addresses were: {active_ips}')
    print(f'Top 3 URLS were: {active_urls}')
    print(f'There were {distinct_ips} distinct IP Addresses in this file')

if __name__ == '__main__':
    main()

