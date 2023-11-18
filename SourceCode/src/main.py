import requests
import json
from datetime import date
import PySimpleGUI as ui

API_key = '7vkjinjkwg6CCJY7qp32xMwWCzziNrwq'
url = 'https://developers.cathaypacific.com/hackathon-apigw'


# Search passengers based on passenger ID
def passengers(PassengerID):
    headers = {'apiKey': API_key, 'accept': 'application/json'}
    res = requests.get(url + "/airport/customers/" + PassengerID + "/details", headers=headers)
    data = res.content
    return data


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
        print("1.Search passengers based on passenger ID.")
        print("2.Search passengers bag allowance based on passenger ID and segment ID.")
        print("3.Search passengers regulatory requirements based on passenger ID and segment ID.")
        print("4.Search passengers seatMap based on passenger ID and segment ID.")
        print("5.Search flight details based on flight number.")
        reply = input("Input 1, 2, 3, 4 or 5 for one of the functions, otherwise automatically terminating: ")
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


def pidinput():
    return input("Please input your Passenger ID: ")


def sidinput():
    return input("Please input your Segment ID: ")


def fidinput():
    return input("Please input your Flight ID: ")


def preorderSystem(PassengerID):
    passengerChoice = ""
    days = int(getRemainingDays(getDate(PassengerID)))
    foodList = getFoodList()
    while days > 1:
        passengerChoice = mainui()
        conf = input("Please press 'Y' to save your choice until the ordering period is closing: ")
        if conf == 'Y':
            print("Your choice have been saved successfully!")
        else:
            print("Your choice have not been saved!")
    return passengerChoice


def getDate(PassengerID):
    with open(passengers(PassengerID)) as d:
        datadic = json.load(d)
    datedFlightID = datadic['data']['segmentDeliveries']['collection']['ref'][-16:]
    date0 = datadic['included']['segmentDeliveries'][datedFlightID]['flightSegment']['departure']['at'][:10]
    return date0


def getFoodList():
    foodList = []
    food1 = "food1"
    food2 = "food2"
    foodList.append(food1)
    foodList.append(food2)
    return foodList


def getRemainingDays(reserveDate):
    return (date(reserveDate[:4], reserveDate[5:7], reserveDate[-2:]) - date(date.today()[:4], date.today()[5:7],
                                                                             date.today()[-2:])).days


def button1(text):
    return ui.B(text, pad=(2, 2), size=(12, 4), font=('Calibri', 24), button_color='black')


def button2(text):
    return ui.B(text, pad=(1, 1), size=(50, 4), font=('Calibri', 18), button_color='black')


def mainui():
    x = -1
    layout = [
        [button1(i) for i in '123'],
        [button2(i) for i in ['Confirm']]
    ]
    window = ui.Window('Cathay SwiftServe AI', layout)
    while True:
        event = window.read()
        if event is None:
            break
        if event == '1':
            x = 1
        if event == '2':
            x = 2
        if event == '3':
            x = 0
        if event == 'Confirm':
            break
    return x


main()
