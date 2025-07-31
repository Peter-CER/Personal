import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from CODE import jsonManager

DATES = [
    "8/14", "8/15", "8/16", "8/17", "8/18", "8/19", "8/20", "8/21", "8/22", "8/23",
    "8/24", "8/25", "8/26", "8/27", "8/28", "8/29", "8/30", "8/31", "9/1", "9/2",
    "9/3", "9/4", "9/5", "9/6", "9/7", "9/8", "9/9", "9/10", "9/11", "9/12",
    "9/13", "9/14", "9/15", "9/16", "9/17", "9/18", "9/19", "9/20", "9/21", "9/22",
    "9/23", "9/24", "9/25", "9/26", "9/27", "9/28", "9/29", "9/30", "10/1", "10/2",
    "10/3", "10/4", "10/5", "10/6", "10/7", "10/8", "10/9", "10/10", "10/11", "10/12",
    "10/13", "10/14", "10/15", "10/16", "10/17", "10/18", "10/19", "10/20", "10/21", "10/22",
    "10/23", "10/24", "10/25", "10/26", "10/27", "10/28", "10/29", "10/30", "10/31", "11/1",
    "11/2", "11/3", "11/4", "11/5", "11/6", "11/7", "11/8", "11/9", "11/10", "11/11",
    "11/12", "11/13", "11/14", "11/15", "11/16", "11/17", "11/18", "11/19", "11/20", "11/21",
    "11/22", "11/23", "11/24", "11/25", "11/26", "11/27", "11/28", "11/29", "11/30", "12/1",
    "12/2", "12/3", "12/4", "12/5", "12/6", "12/7", "12/8", "12/9", "12/10", "12/11",
    "12/12", "12/13", "12/14", "12/15", "12/16"
]

TIMES = [
    "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM",
    "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00:00 PM", "10:00 PM",
    "11:00 PM", "12:00 AM"
]


SERVICE_ACCOUNT_FILE = r'API\project-scheduling-467119-b99ec1ec0022.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
key = '1fDR2zxoT3kEAPV4lkjwMwSQs6yEpD1qbdilwuaYATIc'


creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)


spreadsheet = client.open_by_key(key)

worksheets = spreadsheet.worksheets()

def getPeopleDateTime(date, time):
    people = []
    if date in DATES and time in TIMES:
        for sheet in worksheets:
                value = sheet.cell(DATES.index(date)+3, TIMES.index(time)+3).value
                if value:
                    people.append(sheet.title)
    else:
        return False
    print("On " + date + " at " + time + " are available: " + ", ".join(people))
    return people

def getPeople():
    people = []
    date = input("What date?")
    time = input("What time?")
    if date in DATES and time in TIMES:
        for sheet in worksheets:
                value = sheet.cell(DATES.index(date)+3, TIMES.index(time)+3).value
                if value:
                    people.append(sheet.title)
    else:
        print("incorrect format")
    print("On " + date + " at " + time + " are available: " + ", ".join(people))
    return people

def getPerson(name, date):
    if name not in [ws.title for ws in spreadsheet.worksheets()]:
        return "Incorrect name"
    dateTimes = []
    if date in DATES:
        for sheet in worksheets:
                if sheet.title == name:
                    for j in range(DATES.index(date)+3, DATES.index(date)+6):
                        for i in range(3,19):
                            value = sheet.cell(j, i).value
                            dateTime = DATES[j-3] + " " + TIMES[i-3]
                            if value:
                                dateTimes.append(dateTime)
    else:
        return ("incorrect format")
    return (name + " is available on " + ", ".join(dateTimes))


def addPerson(name, email):
    template_sheet = spreadsheet.worksheet('Template')
    if name not in [ws.title for ws in spreadsheet.worksheets()]:
        jsonManager.create(name, email)
        new_sheet = template_sheet.duplicate(new_sheet_name=name)
        return (f"Created new sheet: {new_sheet.title}")
    else:
        return ("Sheet "+ name +" already exists.")

def deletePerson(name):
    try:
        worksheet = spreadsheet.worksheet(name)
        spreadsheet.del_worksheet(worksheet)
        jsonManager.delete(name)
        return (f"Deleted sheet: {name}")
    except gspread.exceptions.WorksheetNotFound:
        return (f"Sheet '{name}' not found.")

def updateName(old_name, new_name):
    try:
        sheet = spreadsheet.worksheet(old_name)
        sheet.update_title(new_name)
        jsonManager.updateName(old_name, new_name)
        return (f"Renamed sheet from '{old_name}' to '{new_name}'")
    except gspread.exceptions.WorksheetNotFound:
        return (f"Sheet '{old_name}' not found.")
    except Exception as e:
        return (f"Error: {e}")
