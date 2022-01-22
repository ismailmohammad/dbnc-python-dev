import csv
import requests

URL = 'https://tools.usps.com/tools/app/ziplookup/zipByAddress'


def create_csv(filename, header, content):
    with open(filename, "w", newline='') as output_csv:
        writer = csv.writer(output_csv, delimiter=',')
        writer.writerow(header)
        writer.writerows(content)


def scrape_csv(filename):
    addresses = []
    with open(filename, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        # Store the headers of the CSV File, then carry on with extraction
        headers = next(reader, None)
        for line in reader:
            # Ideally, have some exception handling. As a simple measure here,
            # reject line if a line doesn't have the same length as the headers
            if len(line) == len(headers):
                addresses.append(line)
    return (headers, addresses)


def query_address(address):
    # Without user-agent, exceeds 30 redirects
    headers = {'user-agent': ''}
    data = {
        'companyName': address[0],
        'address1': address[1],
        'address2': '',
        'city': address[2],
        'state': address[3],
        'urbanCode': '',
        'zip': address[4]
    }
    request = requests.post(URL, headers=headers, data=data)
    result = request.json()
    if result['resultStatus'] == "SUCCESS":
        address.append(True)
    else:
        address.append(False)
    return address


if __name__ == "__main__":
    # Scrape the CSV for relevant Data
    headers, addresses = scrape_csv("test/inputData.csv")
    # Query each address found, then output
    for address in addresses:
        query_address(address)
    headers.append("Valid Address")
    create_csv("output.csv", headers, addresses)
