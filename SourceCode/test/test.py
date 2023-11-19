import requests
from datetime import date

API_key = '7vkjinjkwg6CCJY7qp32xMwWCzziNrwq'
url = 'https://developers.cathaypacific.com/hackathon-apigw'

def main():
    print("Welcome to Cathay SwiftServe AI System made by Team_068: Cathay skyline")
    print("Today is :", date.today())
    print("Connecting to Cathay Network, please wait a second...")
    headers = {'apiKey': API_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
            print("Connected successfully!")
    else:
            print('Connect failed with Status Code = ', response.status_code)
    while response.status_code == 200:
        print('*' * 50)
        print("Table of Funtions:")
        print("0.Use Cathay Basic Information Chatbot.")
        print("1.Search passengers based on passenger ID.")
        print("2.Search passengers bag allowance based on passenger ID and segment ID.")
        print("3.Search passengers regulatory requirements based on passenger ID and segment ID.")
        print("4.Search passengers seatMap based on passenger ID and segment ID.")
        print("5.Search flight details based on flight number.")
        print("6.Open pre-ordering System.")
        reply = input("Input 0, 1, 2, 3, 4, 5 or 6 for one of the functions, otherwise automatically terminating: ")
        match reply:
            case '1':
                    passengers(pidinput())
            case '2':
                    bagAllowance(pidinput(), sidinput())
            case '3':
                    regulatoryRequirements(pidinput(), sidinput())
            case '4':
                    seatMap(pidinput(), sidinput(), fidinput())
            case '5':
                    flightDetails(fidinput())
            case _:
                    break
        print("")
        input("Press any key to return to main table...")
        print("")
    input("The program has terminated!")

# Example PID: 510892B000014EBB, SID: 5009A2B00005D613, FID: CX491

# Search passengers based on passenger ID
def passengers(PassengerID):
    headers = {'apiKey': API_key, 'accept': 'application/json'}
    res = requests.get(url + "/airport/customers/" + PassengerID + "/details", headers=headers)
    data = res.content
    print(data)


# Search passengers bag allowance based on passenger ID and segment ID
def bagAllowance(PassengerID, SegmentID):
    headers = {'apiKey': API_key, 'accept': 'application/json'}
    res = requests.get(url + "/airport/customers/" + PassengerID + SegmentID + "/bagallowance", headers=headers)
    data = res.content
    return data

             
# Search passengers regulatory requirements based on passenger ID and segment ID
def regulatoryRequirements(PassengerID, SegmentID):
    headers = {'apiKey': API_key, 'accept': 'application/json'}
    res = requests.get(url + "/airport/customers/" + PassengerID + SegmentID + "/regulatoryrequirements",
                       headers=headers)
    data = res.content
    return data


# Search passengers seatMap based on passenger ID and segment ID
def seatMap(PassengerID, SegmentID, FlightID):
    headers = {'apiKey': API_key, 'accept': 'application/json'}
    res = requests.get(url + "/airport/flights/" + PassengerID + SegmentID + "/seatmaps?fid=" + FlightID,
                       headers=headers)
    data = res.content
    return data


# Search flight details based on flight number
def flightDetails(FlightID):
    headers = {'apiKey': API_key, 'accept': 'application/json'}
    res = requests.get(url + "/airport/flights?fid=" + FlightID, headers=headers)
    data = res.content
    return data


def pidinput():
    return input("Please input your Passenger ID: ")


def sidinput():
    return input("Please input your Segment ID: ")


def fidinput():
    return input("Please input your Flight ID: ")

main()