import http.client
import requests

API_key = '7vkjinjkwg6CCJY7qp32xMwWCzziNrwq'
url = 'https://developers.cathaypacific.com/hackathon-apigw'


def passengers(PassengerID):  # Search passengers based on passenger ID
    conn = http.client.HTTPSConnection("developers.cathaypacific.com")
    conn.request("GET", "/hackathon-apigw/airport/customers/" + PassengerID + "/details")
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def bagAllowance(PassengerID, SegmentID):  # Search passengers bag allowance based on passenger ID and segment ID
    conn = http.client.HTTPSConnection("developers.cathaypacific.com")
    conn.request("POST", "/hackathon-apigw/airport/customers/" + PassengerID + SegmentID + "/bagallowance")
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def regulatoryRequirements(PassengerID,SegmentID):  # Search passengers regulatory requirements based on passenger ID and segment ID
    conn = http.client.HTTPSConnection("developers.cathaypacific.com")
    conn.request("POST", "/hackathon-apigw/airport/customers/" + PassengerID + SegmentID + "/regulatoryrequirements")
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def seatMap(PassengerID, SegmentID):  # Search passengers seatMap based on passenger ID and segment ID
    conn = http.client.HTTPSConnection("developers.cathaypacific.com")
    conn.request("POST",
                 "/hackathon-apigw/airport/flights/" + PassengerID + SegmentID + "/seatmaps?fid=%3CSOME_STRING_VALUE%3E")
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def flightDetails(FlightID):  # Search flight details based on flight number
    conn = http.client.HTTPSConnection("developers.cathaypacific.com")
    conn.request("POST", "/hackathon-apigw/airport/flights?fid=" + FlightID)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))


def main():
    print("Welcome to Cathay SwiftServe AI System made by Team_068: Cathay skyline")
    print("Connecting to Cathay Network, please wait a second...")
    headers = {'Authorization': API_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Connected successfully!")
    else:
        print('Connect failed with Status Code = ', response.status_code)
    while response.status_code == 200:
        print('*' * 50)
        print("Table of Funtions:")
        print("1.Search passengers based on passenger ID.")
        print("2.Search passengers bag allowance based on passenger ID and segment ID.")
        print("3.Search passengers regulatory requirements based on passenger ID and segment ID.")
        print("4.Search passengers seatMap based on passenger ID and segment ID.")
        print("5.Search flight details based on flight number.")
        Reply = input("Input 1, 2, 3, 4 or 5 for one of the functions, otherwise automatically terminating: ")
        match Reply:
            case '1':
                passengers(pidinput())
            case '2':
                bagAllowance(pidinput(), sidinput())
            case '3':
                regulatoryRequirements(pidinput(), sidinput())
            case '4':
                seatMap(pidinput(), sidinput())
            case '5':
                flightDetails(fidinput())
            case _:
                break
        print("")
        input("Press any key to return to main table...")
        print("")
    input("The program has already terminated!")


def pidinput():
    PassengerID = input("Please input your Passenger ID: ")
    return PassengerID


def sidinput():
    SegmentID = input("Please input your Segment ID: ")
    return SegmentID


def fidinput():
    FlightID = input("Please input your Flight ID: ")
    return FlightID


main()
