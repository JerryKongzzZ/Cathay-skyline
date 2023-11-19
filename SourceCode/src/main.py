import json
import requests
import Cathay_GPT_2
from datetime import date
import PySimpleGUI as sg
import time

API_key = '7vkjinjkwg6CCJY7qp32xMwWCzziNrwq'
url = 'https://developers.cathaypacific.com/hackathon-apigw'


# Example PID: 510892B000014EBB, SID: 5009A2B00005D613, FID: CX491

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

def check_connection(API_key):
    headers = {'apiKey': API_key}
    response = requests.get(url, headers=headers)
    return response.status_code

def main():
    today_date = date.today()
    date_str = "Today is: " + str(today_date)
    layout = [
        [sg.Text("Welcome to Cathay SwiftServe AI System made by Team_068: Cathay skyline")],
        [sg.Text(date_str)],
        [sg.Button("Enter", key="-ENTER-")],
        [sg.Text("", key="-STATUS-", auto_size_text=True, visible=False)]
    ]

    window = sg.Window("Cathay SwiftServe AI", layout, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-ENTER-":
            window["-STATUS-"].update("Connecting to Cathay Network, please wait a second...", visible=True)
            window.refresh()

            #Call your connect_function here
            connected = check_connection(API_key)
            if connected == 200:
                layout_main = [
                    [sg.Text("Connected successfully!", key ="-CON-", auto_size_text=True)]
                ]
                window.close()
                window = sg.Window("Success", layout_main, finalize=True)
                time.sleep(5)
                window.close()
            #    window["-STATUS-"].update("Connected successfully!")
            #    print("Connected successfully!")
            else:
                fail_code = 'Connect failed with Status Code = ' + connected
                layout_connection = [
                    [sg.Text(fail_code, key ="-MAIN-", auto_size_text=True)]
                ]
                window.close()
                window = sg.Window("Failed", layout_connection, finalize=True)
                time.sleep(5)
                window.close()
            window.refresh()
    window.close()

    #connected = check_connection(API_key)
    #while connected == 200:
    styling = '*' * 50
    styling_str = str(styling) 
    layout_main = [
        [sg.Text(styling_str)],
        [sg.Text("Table of Functions: \n 1.Search passengers based on passenger ID. \n 2.Search passengers bag allowance based on passenger ID and segment ID. \n 3.Search passengers regulatory requirements based on passenger ID and segment ID. \n 4.Search passengers seatMap based on passenger ID and segment ID. \n 5.Search flight details based on flight number. \n 6. Pre-order food choices for your upcoming flight")],
        [sg.Text("Input 1, 2, 3, 4, 5 or 6 for one of the functions, otherwise automatically terminating: ")],
        [sg.Input(key='-IN-')],
        [sg.Button('Enter'), sg.Button('Exit')],
        #[sg.Text("",key='-CON-', auto_size_text=True, visible=False)]
        ]
    window = sg.Window('Table of Functions', layout_main, finalize=True)
    pidinput = "Please input your Passenger ID: "
    sidinput = "Please input your Segment ID: "
    fidinput = "Please input your Flight ID: "
    while True: 
        event, values = window.read()
        if event ==sg.WIN_CLOSED or event == 'Exit':
            #window['-CON-'].update("The program has terminated!", auto_size_text=True, visible=True)
            window.close()
            #window = sg.Window("Success", layout_main, finalize=True)
            #time.sleep(3)
            #window.close()
            #input("The program has terminated!")
    #if event =='Enter':
        # layout_basic = [
        #     [sg.Text("", key="-DYNAMIC-")],
        #     [sg.Input(key='-IN-')],
        #     [sg.Button("Submit", key='-SUBMIT-')]
        #     [sg.Text("", key="-REPLY-", visible=False)]
        #     [sg.Button("Back to Main", key="-END-", visible=False)]
        # ]
        #window2 = sg.Window("Reply", layout_basic, finalize=True)
        #while True:
        #    event, values = window2.read()
        reply = values['-IN-']
        match reply:
            case '1':
                layout_basic = [
                [sg.Text(pidinput, key="-DYNAMIC-")],
                [sg.Input(key='-IN-')],
                [sg.Button("Send")],
                [sg.Text("", key="-REPLY-", visible=False)],
                [sg.Button("Back to Main", key="-END-", visible=True)]
                ]
                window2 = sg.Window("Reply", layout_basic, finalize=True)

                while True:
                    event, values = window2.read()
                #window2['-DYNAMIC-'].update(pidinput)
                    if event =='Send':
                        ans = ['-IN-']
                        window2['-REPLY-'].update(passengers(ans), visible=True)
                    if event == "-END-" or event == sg.WINDOW_CLOSED and window2 is not None:
                        window2.close()
            case '2':
                layout_basic = [
                [sg.Text(pidinput)],
                [sg.Input(key='-IN-')],
                [sg.Text(sidinput)],
                [sg.Input(key='-IN2-')],
                [sg.Button("Send")],
                [sg.Text("", key="-REPLY-", visible=False)],
                [sg.Button("Back to Main", key="-END-", visible=True)]
                ]
                window2 = sg.Window("Reply", layout_basic, finalize=True)
                while True:
                    event, values = window2.read()
                    if event=='Send':
                        ans = ['-IN-']
                        ans2 = ['-IN2-']
                        window2['-REPLY-'].update(bagAllowance(ans, ans2), visible=True)
                    if event == "-END-" or event == sg.WIN_CLOSED and window2 is not None:
                        window2.close()
                #window['-REPLY-'].update(bagAllowance(pidinput(), sidinput()), visible=True)
            case '3':
                layout_basic = [
                [sg.Text(pidinput)],
                [sg.Input(key='-IN-')],
                [sg.Text(sidinput)],
                [sg.Input(key='-IN2-')],
                [sg.Button("Send")],
                [sg.Text("", key="-REPLY-", visible=False)],
                [sg.Button("Back to Main", key="-END-", visible=True)]
                ]
                window2 = sg.Window("Reply", layout_basic, finalize=True)
                while True:
                    event, values = window2.read()
                    if event=='Send':
                        ans = ['-IN-']
                        ans2 = ['-IN2-']
                        window2['-REPLY-'].update(regulatoryRequirements(ans, ans2), visible=True)
                    if event == "-END-" or event == sg.WIN_CLOSED and window2 is not None:
                        window2.close()
                #window['-REPLY-'].update(regulatoryRequirements(pidinput(), sidinput()), visible=True)
            case '4':
                layout_basic = [
                [sg.Text(pidinput)],
                [sg.Input(key='-IN-')],
                [sg.Text(sidinput)],
                [sg.Input(key='-IN2-')],
                [sg.Text(fidinput)],
                [sg.Input(key='-IN3-')],
                [sg.Button("Send")],
                [sg.Text("", key="-REPLY-", visible=False)],
                [sg.Button("Back to Main", key="-END-", visible=True)]
                ]
                window2 = sg.Window("Reply", layout_basic, finalize=True)
                while True:
                    event, values = window2.read()
                    if event=='Send':
                        ans = ['-IN-']
                        ans2 = ['-IN2-']
                        ans3 = ['-IN3-']
                        window2['-REPLY-'].update(seatMap(ans, ans2, ans3), visible=True)
                    if event == "-END-" or event == sg.WIN_CLOSED and window2 is not None:
                        window2.close()
                #window['-REPLY-'].update(seatMap(pidinput(), sidinput(), fidinput()), visible=True)
            case '5':
                layout_basic = [
                [sg.Text(fidinput, key="-DYNAMIC-")],
                [sg.Input(key='-IN-')],
                [sg.Button("Send")],
                [sg.Text("", key="-REPLY-", visible=False)],
                [sg.Button("Back to Main", key="-END-", visible=True)]
                ]
                window2 = sg.Window("Reply", layout_basic, finalize=True)

                while True:
                    event, values = window2.read()
                #window2['-DYNAMIC-'].update(pidinput)
                    if event =='Send':
                        ans = ['-IN-']
                        window2['-REPLY-'].update(flightDetails(ans), visible=True)
                    if event == "-END-" or event == sg.WINDOW_CLOSED and window2 is not None:
                        window2.close()
                #window['-REPLY-'].update(flightDetails(fidinput()), visible=True)
            case '6':
                layout_basic = [
                [sg.Text(pidinput, key="-DYNAMIC-")],
                [sg.Input(key='-IN-')],
                [sg.Button("Send")],
                [sg.Text("", key="-REPLY-", visible=False)],
                [sg.Button("Back to Main", key="-END-", visible=True)]
                ]
                window2 = sg.Window("Reply", layout_basic, finalize=True)

                while True:
                    event, values = window2.read()
                #window2['-DYNAMIC-'].update(pidinput)
                    if event =='Send':
                        ans = ['-IN-']
                        window2['-REPLY-'].update(preorderSystem(ans), visible=True)
                    if event == "-END-" or event == sg.WINDOW_CLOSED and window2 is not None:
                        window2.close()

            case '_':
                break
        window2["-END-"].update(visible=True)
        #[sg.Text("", key="-END-", visible=False)]
        #input("Press any key to return to main table...")
        #print("")
        #reply = input("Input 1, 2, 3, 4 or 5 for one of the functions, otherwise automatically terminating: ")

        

        # def pidinput():
        #return input("Please input your Passenger ID: ")
#def sidinput():
#    return input("Please input your Segment ID: ")
#def fidinput():
#    return input("Please input your Flight ID: ")

    #ui.theme('GreenBlue')
    #layout = [[ui.Text("Welcome to Cathay SwiftServe AI System made by Team_068: Cathay skyline"), ui.Text(size= (15,1),key = '-START-')],
    #          [ui.Text("Today is :", date.today())]
    #          [ui.Input(key='-IN-')],
    #          [ui.Button('Show'), ui.Button('Exit')]]
    #window = ui.Window('Cathay SwiftServe Ai', layout)

    #while True:
    #    event, values = window.read()
    #    print(event, values)
    #    if event == ui.WIN_CLOSED or event =='Exit':
    #        break
    #    if event == 'Show':
    #        window['-OUTPUT-'].update(values['-IN-'])
    
    #window.close()

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
            case '0':
                Cathay_GPT_2.main()
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
            case '6':
                print(preorderSystem(pidinput()))
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
    flag = False
    passengerChoice = ""
    days = int(getRemainingDays(getDate(PassengerID)))
    foodList = getFoodList()
    while days <= 1:
        flag = True
        passengerChoice = mainui()
        conf = input("Please press 'Y' to save your choice until the ordering period is closing: ")
        if conf == 'Y':
            print("Your choice have been saved successfully!")
        else:
            print("Your choice have not been saved!")
    if flag: return passengerChoice
    else: return "Sorry, the pre-ordering service closed."


def getDate(PassengerID):
    str_data = passengers(PassengerID).decode("utf-8")
    dict_data = json.loads(str_data)
    datedFlightID = dict_data['data']['segmentDeliveries']['collection'][0]['ref'][-16:]
    date0 = dict_data['included']['segmentDeliveries'][datedFlightID]['flightSegment']['departure']['at'][:10]
    return date0


def getFoodList():
    foodList = []
    food1 = "food1"
    food2 = "food2"
    foodList.append(food1)
    foodList.append(food2)
    return foodList


def getRemainingDays(reserveDate):
    return (date(int(reserveDate[:4]), int(reserveDate[5:7]), int(reserveDate[-2:])) - date(int(str(date.today())[:4]),
                                                                                            int(str(date.today())[5:7]),
                                                                                            int(str(date.today())[
                                                                                                -2:]))).days


def button1(text):
    return sg.B(text, pad=(2, 2), size=(12, 4), font=('Calibri', 24), button_color='black')


def button2(text):
    return sg.B(text, pad=(1, 1), size=(50, 4), font=('Calibri', 18), button_color='black')


def mainui():
    x = -1
    layout = [
        [button1(i) for i in '123'],
        [button2(i) for i in ['Save']]
    ]
    window = sg.Window('Cathay SwiftServe AI', layout)
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
        if event == 'Save':
            break
    return x


main()
