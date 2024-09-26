from customtkinter import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import calendar
from bs4 import BeautifulSoup
import json
import customtkinter    

# Create the Tkinter window and buttons
root = CTk()
root.title("To-do List - November 2023")
root.geometry("780x720")

set_appearance_mode("light")

root.resizable(False, False)
obj = calendar.Calendar()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

global curr_year
curr_year = 2023
global num_curr_month
num_curr_month = 11
global curr_month
curr_month = months[num_curr_month - 1]
text_cal = calendar.HTMLCalendar(firstweekday = 0)
global curr_day
global date
global newWindow
global windowPain
calendar_list = []
year_dates = [[[] for col in range(31)], 
              [[] for col in range(28)], 
              [[] for col in range(31)], 
              [[] for col in range(30)], 
              [[] for col in range(31)], 
              [[] for col in range(30)], 
              [[] for col in range(31)], 
              [[] for col in range(31)], 
              [[] for col in range(30)], 
              [[] for col in range(31)], 
              [[] for col in range(30)], 
              [[] for col in range(31)]]

leap_year_dates = [[[] for col in range(31)], 
                   [[] for col in range(29)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)]]

current_year = []
global saved_data
saved_data = []
Lato = CTkFont(family = "Lato", size = 20, weight = 'bold')
LatoBtn = CTkFont(family = "Lato", size = 15, weight = 'bold')
LatoText = CTkFont(family = "Lato", size = 15, weight = 'bold')
LatoLabel = CTkFont(family = "Lato", size = 18, weight = 'bold')
tabs = CTkTabview(root, width = 730, height=660)
tabs.pack()

tabs.add("Month View")
tabs.set("Month View")

# test = []
# test.append(year_dates)
# test.append(year_dates)
# print(leap_year_dates)
# test[1][0][0].append(9999999999999)
# print(test)

for day in obj.itermonthdays2(curr_year, num_curr_month):
    if (day[0] == 1):
        curr_day = day[1]
    if (day[0] != 0):
        date = day[0]
def json_write(assignment, filename = 'assignments.json'):
    with open(filename, 'r+') as assignments_json:
        assignments = json.load(assignments_json)
        assignments['data'].append(assignment)
        assignments_json.seek(0)
        json.dump(assignments, assignments_json, indent = 4)

def add_calendar_years(year):
    global saved_data
    latest_year = len(calendar_list) + curr_year - 1
    years_to_add = year - latest_year
    if (years_to_add > 0):
        for i in range(years_to_add):
            year_days = obj.yeardayscalendar(latest_year + (i + 1))
            calendar_list.append(year_days)
            if (latest_year + (i + 1)) % 4 == 0:
                saved_data.append([[[] for col in range(31)], 
                   [[] for col in range(29)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)]])
            else:
                saved_data.append([[[] for col in range(31)], 
                   [[] for col in range(28)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)], 
                   [[] for col in range(30)], 
                   [[] for col in range(31)]])

add_calendar_years(2023)



def next_month():
    global num_curr_month
    global curr_year
    global curr_month

    if num_curr_month == 12:
        curr_month = months[0]
        num_curr_month = 1
        curr_month = months[num_curr_month - 1]
        curr_year = curr_year + 1
    else: 
        curr_month = months[num_curr_month]
        num_curr_month += 1
        curr_month = months[num_curr_month]
        num_curr_month += 1
    setRows()
    
def last_month():
    global num_curr_month
    global curr_month
    global curr_year

    if num_curr_month == 1:
        curr_month = months[11]
        num_curr_month = 12
        curr_year = curr_year - 1
    else:
        num_curr_month -= 1
        num_curr_month -= 1
        curr_month = months[num_curr_month-1]
    setRows()

def highlight():
    pass
windowPain = None

def button_click(text):
    global windowPain
    global saved_data
    if windowPain == None or not windowPain.winfo_exists():
        windowPain = CTkToplevel(root)
        windowPain.geometry("450x400")
        for assignment in saved_data[curr_year - 2023][num_curr_month - 1][int(text) - 1]:
            urgency = int(assignment[2])
            match urgency:
                case 1:
                    textColor ="#AB2328"
                    fgColor = "#FF7276"
                case 2:
                    textColor = "#DC582A"
                    fgColor = "#FCD299"
                case 3:
                    textColor = "#F6BE00"
                    fgColor = "#F1EB9C"
                case 4:
                    textColor = "#009A17"
                    fgColor = "#77DD77"
                case 5:
                    textColor = "#00A3E1"
                    fgColor = "#A4DBE8"

            assignment_text = '[' + assignment[4] + '] ' + assignment[0] + ' (' + assignment[5] + ')'
            assignment_label = CTkLabel(windowPain, width = 350, height = 50, font = LatoLabel, fg_color = fgColor, text_color = textColor, corner_radius = 10, text = assignment_text).pack(pady = 10)
        windowPain.after(100, windowPain.lift)
    else:
        windowPain.focus()

count = 1


def setRows():
    global curr_day
    global date
    global num_curr_month
    global buttons

    for day in obj.itermonthdays2(curr_year, num_curr_month):
        if (day[0] == 1):
            curr_day = day[1]
        if (day[0] != 0):
            date = day[0]

    root.title("To-do List - " + curr_month + " " + str(curr_year))
    
    buttons = []
    days = []
    count = 0
    for day in obj.itermonthdays2(curr_year, num_curr_month):
        days.append(day)
    
    for row in range(6):
            button_row = []
            for col in range(7):
                if (not days[count][0] == 0):
                    day_text = days[count][0]
                else:
                    day_text = ""
                button = CTkButton(tabs.tab("Month View"), text=day_text, anchor = 'ne', font=Lato, height=100, width=100, corner_radius=10, fg_color = "#4158D0", hover_color="#C850C0", border_color="#dbdbdb", border_width=3, command=lambda text = day_text: button_click(text))
                button.grid(row=row, column=col)
                buttons.append(button)
                if count < len(days) - 1:
                    count += 1
    cnt = 0
    for day in obj.itermonthdays2(curr_year, num_curr_month):
        if (day[0] != 0):
            buttons[cnt].configure(text=day[0])
        cnt+=1
    for button in buttons:
        if button.cget('text') == "":
            button.configure(state=DISABLED)
            button.configure(fg_color = "#dbdbdb")

setRows()
        
def closeWindow():
    global nameEntry, dueEntry, urgencyEntry, timeEntry, subjectEntry, categoryEntry
    global name, due, urgency, time, subject, category
    global newWindow
    global saved_data
    name = nameEntry.get()
    due = dueEntry.get()
    urgency = urgencyEntry.get()
    time = timeEntry.get()
    subject = subjectEntry.get()
    category = categoryEntry.get()

    due_date = due

    month = int(due_date[:due_date.index('/')])
    due_date = due_date[due_date.index('/') + 1:len(due_date)]

    day = int((due_date[:due_date.index('/')]))
    due_date = due_date[due_date.index('/') + 1:len(due_date)]

    year = int(due_date)

    assignment = [
        name, 
        due, 
        urgency, 
        time, 
        subject,
        category
    ]
    if year > (len(saved_data) + 2023) - 1:
        add_calendar_years(year)
        print(assignment)
        saved_data[year - 2023][month - 1][day - 1].append(assignment)
        # print(saved_data)
    else:
        saved_data[year - 2023][month - 1][day - 1].append(assignment)

    newWindow.destroy()

newWindow = None

def addAssignment():
    global newWindow
    if newWindow is None or not newWindow.winfo_exists():
        newWindow = CTkToplevel(root)  # create window if its None or destroyed
        newWindow.geometry("400x400")
        global nameEntry, dueEntry, urgencyEntry, timeEntry, subjectEntry, categoryEntry
 
        # sets the title of the
        # Toplevel widget
    
        # A Label widget to show in toplevel

        #name
        nameLabel = CTkLabel(newWindow, text ="Input assignment name:", font = LatoText).pack()
        nameEntry= CTkEntry(newWindow, width= 200, placeholder_text = "Assignment Name...")
        nameEntry.focus_set()
        nameEntry.pack()

        #due date
        dueLabel = CTkLabel(newWindow, text ="Input due date:", font = LatoText).pack()
        dueEntry= CTkEntry(newWindow, width= 200, placeholder_text = "MM/DD/YYYY")
        dueEntry.focus_set()
        dueEntry.pack()

        #urgency
        urgencyLabel = CTkLabel(newWindow, text ="Input urgency:", font = LatoText).pack()
        urgencyEntry= CTkEntry(newWindow, width= 200, placeholder_text = "1-5")
        urgencyEntry.focus_set()
        urgencyEntry.pack()

        #time
        timeLabel = CTkLabel(newWindow, text ="Input estimated length:", font = LatoText).pack()
        timeEntry= CTkEntry(newWindow, width= 200, placeholder_text = "Minutes")
        timeEntry.focus_set()
        timeEntry.pack()

        #subject
        subjectLabel = CTkLabel(newWindow, text ="Input subject:", font = LatoText).pack()
        subjectEntry= CTkEntry(newWindow, width= 200, placeholder_text = "Subject...")
        subjectEntry.focus_set()
        subjectEntry.pack()

        #type
        categoryLabel = CTkLabel(newWindow, text ="Input type (homework, quiz, test):", font = LatoText).pack()
        categoryEntry= CTkEntry(newWindow, width= 200, placeholder_text = "Homework, Quiz, Test")
        categoryEntry.focus_set()
        categoryEntry.pack()

        B = CTkButton(newWindow, width = 150, text = "Submit", font = LatoText, command=closeWindow)
        B.place(x = 125, y = 355)
        newWindow.after(100, newWindow.lift)
    else:
        newWindow.focus()
    
addAssignment_btn = CTkButton(root, text = 'Add Assignment', font = LatoBtn, command = addAssignment).pack(pady = 20)
next_month_btn = CTkButton(root, text = 'Next Month', font = LatoBtn, command = next_month).place(x = 600, y = 680)
last_month_btn = CTkButton(root, text = 'Last Month', font = LatoBtn, command = last_month).place(x = 50, y = 680)


#menu
my_menu = Menu(root)
root.config(menu=my_menu)

root.mainloop()