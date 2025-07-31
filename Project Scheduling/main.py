from CODE import sheetsManager
from CODE import calendarManager
from CODE import jsonManager
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

small = "600x400"
big = "600x525"
title_font = ("Helvetica", 18, "bold")
button_style = {
    "font": ("Helvetica", 12),
    "bg": "#5B4CAF",
    "fg": "white",
    "activebackground": "#45a049",
    "activeforeground": "white",
    "width": 20,
    "height": 2,
    "bd": 0,
    "relief": "flat",
    "cursor": "hand2"
}
label_style = {
    "font": title_font,
    "bg": "#f5f5f5",
    "fg": "#333"
}

def create_button(parent, text, command):
    return tk.Button(parent, text=text, command=command, **button_style)

def create_label(parent, text):
    return tk.Label(parent, text=text, **label_style)

def addWindow(main_window, prev, sheet):
    prev.withdraw()
    new_win = tk.Toplevel()
    title = "Add a new person" if sheet else "Add entry to data"
    new_win.title(title)
    new_win.geometry(small)
    new_win.configure(bg="#f5f5f5")

    create_label(new_win, title).pack(pady=20)

    tk.Label(new_win, text="Name", **{"font": ("Helvetica", 12, "bold"), "bg": "#f5f5f5", "fg": "#333"}).pack(pady=5)
    name_entry = tk.Entry(new_win, font=("Helvetica", 12), width=30)
    name_entry.pack(pady=5)

    tk.Label(new_win, text="Email", **{"font": ("Helvetica", 12, "bold"), "bg": "#f5f5f5", "fg": "#333"}).pack(pady=5)
    email_entry = tk.Entry(new_win, font=("Helvetica", 12), width=30)
    email_entry.pack(pady=5)

    def submit():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        if sheet:
            messagebox.showinfo("Submit message", sheetsManager.addPerson(name, email))
        else:
            messagebox.showinfo("Submit message", jsonManager.create(name, email))

    create_button(new_win, "Submit", submit).pack(pady=15)

    def go_back():
        prev.destroy()
        new_win.destroy()
        main_window.deiconify()

    create_button(new_win, "Go home", go_back).pack(pady=10)

def deleteWindow(main_window, prev, sheet):
    prev.withdraw()
    new_win = tk.Toplevel()
    string = "a person" if sheet else "an entry in data"
    title = "Delete " + string
    new_win.title(title)
    new_win.geometry(small)
    new_win.configure(bg="#f5f5f5")

    create_label(new_win, title).pack(pady=20)

    tk.Label(new_win, text="Name", **{"font": ("Helvetica", 12, "bold"), "bg": "#f5f5f5", "fg": "#333"}).pack(pady=5)
    name_entry = tk.Entry(new_win, font=("Helvetica", 12), width=30)
    name_entry.pack(pady=5)

    def submit():
        name = name_entry.get().strip()
        if sheet:
            messagebox.showinfo("Delete message", sheetsManager.deletePerson(name))
        else:
            messagebox.showinfo("Delete message", jsonManager.delete(name))

    create_button(new_win, "Delete", submit).pack(pady=15)

    
    def go_back():
        prev.destroy()
        new_win.destroy()
        main_window.deiconify()
    create_button(new_win, "Go home", go_back).pack(pady=10)

def updateWindow(main_window, prev, sheet):
    prev.withdraw()
    new_win = tk.Toplevel()
    string = "a name" if sheet else "a name in data"
    title = "Update " + string
    new_win.title(title)
    new_win.geometry(small)
    new_win.configure(bg="#f5f5f5")

    create_label(new_win, title).pack(pady=20)
    
    tk.Label(new_win, text="Old Name", **{"font": ("Helvetica", 12, "bold"), "bg": "#f5f5f5", "fg": "#333"}).pack(pady=5)
    name_entry = tk.Entry(new_win, font=("Helvetica", 12), width=30)
    name_entry.pack(pady=5)

    tk.Label(new_win, text="New Name", **{"font": ("Helvetica", 12, "bold"), "bg": "#f5f5f5", "fg": "#333"}).pack(pady=5)
    new_name_entry = tk.Entry(new_win, font=("Helvetica", 12), width=30)
    new_name_entry.pack(pady=5)

    def submit():
        name = name_entry.get().strip()
        new_name = new_name_entry.get().strip()
        if sheet:
            messagebox.showinfo("Update name message", sheetsManager.updateName(name, new_name))
        else:
            messagebox.showinfo("Update name message", jsonManager.updateName(name, new_name))

    create_button(new_win, "Update name", submit).pack(pady=15)


    def go_back():
        prev.destroy()
        new_win.destroy()
        main_window.deiconify()
    create_button(new_win, "Go home", go_back).pack(pady=10)

def updateEmail(main_window, prev):
    prev.withdraw()
    new_win = tk.Toplevel()
    title = "Update email"
    new_win.title(title)
    new_win.geometry(small)
    new_win.configure(bg="#f5f5f5")

    create_label(new_win, title).pack(pady=20)

    tk.Label(new_win, text="Name", **{"font": ("Helvetica", 12, "bold"), "bg": "#f5f5f5", "fg": "#333"}).pack(pady=5)
    name_entry = tk.Entry(new_win, font=("Helvetica", 12), width=30)
    name_entry.pack(pady=5)

    tk.Label(new_win, text="New Email", **{"font": ("Helvetica", 12, "bold"), "bg": "#f5f5f5", "fg": "#333"}).pack(pady=5)
    email_entry = tk.Entry(new_win, font=("Helvetica", 12), width=30)
    email_entry.pack(pady=5)

    def submit():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        messagebox.showinfo("Submit message", jsonManager.update(name, email))

    create_button(new_win, "Submit", submit).pack(pady=15)

    def go_back():
        prev.destroy()
        new_win.destroy()
        main_window.deiconify()

    create_button(new_win, "Go home", go_back).pack(pady=10)

def findDate(main_window, prev):
    prev.withdraw()
    main_window.withdraw()
    new_win = tk.Toplevel()
    new_win.title("Find availability")
    new_win.geometry(small)
    new_win.configure(bg="#f5f5f5")

    create_label(new_win, "Find availability").pack(pady=20)

    datetime_frame = tk.Frame(new_win, bg="#f5f5f5")
    datetime_frame.pack(pady=10)

    entry_width = 14  # Each entry width
    label_font = ("Helvetica", 12, "bold")
    entry_font = ("Helvetica", 12)

    date_frame = tk.Frame(datetime_frame, bg="#f5f5f5")
    date_frame.pack(side="left", padx=(0, 14))  # Small horizontal gap

    tk.Label(date_frame, text="Date", font=label_font, bg="#f5f5f5", fg="#333").pack()
    date_entry = tk.Entry(date_frame, font=entry_font, width=entry_width)
    date_entry.pack()

    time_frame = tk.Frame(datetime_frame, bg="#f5f5f5")
    time_frame.pack(side="left")

    tk.Label(time_frame, text="Time", font=label_font, bg="#f5f5f5", fg="#333").pack()
    time_entry = tk.Entry(time_frame, font=entry_font, width=entry_width)
    time_entry.pack()

    def submit():
        date = date_entry.get().strip()
        time = time_entry.get().strip()
        people = sheetsManager.getPeopleDateTime(date, time)
        if people == False:
            messagebox.showinfo("Send Message", "Invalid input")
        elif people == []:
            messagebox.showinfo("Send Message", "Noone is available")
        else:
            name = ", ".join(people)
            result = messagebox.askyesno("Send Message", "People available: " + name + "\nSend them an invite?")
            if result:
                calendarManager.sendInvite(name, date, time, "Shooting Sophie's series")




    create_button(new_win, "Submit", submit).pack(pady=8)


    def go_back():
        prev.destroy()
        new_win.destroy()
        main_window.deiconify()
    create_button(new_win, "Go home", go_back).pack(pady=10)

def findPerson(main_window, prev):
    prev.withdraw()
    main_window.withdraw()
    new_win = tk.Toplevel()
    new_win.title("Find when a person is available")
    new_win.geometry(small)
    new_win.configure(bg="#f5f5f5")
    create_label(new_win, "Find when a person is available").pack(pady=20)

    datetime_frame = tk.Frame(new_win, bg="#f5f5f5")
    datetime_frame.pack(pady=10)

    entry_width = 14  # Each entry width
    label_font = ("Helvetica", 12, "bold")
    entry_font = ("Helvetica", 12)

    date_frame = tk.Frame(datetime_frame, bg="#f5f5f5")
    date_frame.pack(side="left", padx=(0, 14))  # Small horizontal gap

    tk.Label(date_frame, text="Name", font=label_font, bg="#f5f5f5", fg="#333").pack()
    name_entry = tk.Entry(date_frame, font=entry_font, width=entry_width)
    name_entry.pack()

    time_frame = tk.Frame(datetime_frame, bg="#f5f5f5")
    time_frame.pack(side="left")

    tk.Label(time_frame, text="Date", font=label_font, bg="#f5f5f5", fg="#333").pack()
    date_entry = tk.Entry(time_frame, font=entry_font, width=entry_width)
    date_entry.pack()

    def submit():
        name = name_entry.get().strip()
        date = date_entry.get().strip()
        messagebox.showinfo("Find person availability", sheetsManager.getPerson(name, date))

    def go_back():
        new_win.destroy()
        prev.destroy()
        main_window.deiconify()

    create_button(new_win, "Submit", submit).pack(pady=8)
    create_button(new_win, "Go home", go_back).pack(pady=(0,10))


def findWindow(main_window):
    main_window.withdraw()
    new_win = tk.Toplevel()
    new_win.title("Find availability")
    new_win.geometry(small)
    new_win.configure(bg="#f5f5f5")

    create_label(new_win, "Find availability").pack(pady=20)

    def go_back():
        new_win.destroy()
        main_window.deiconify()

    create_button(new_win, "Available on date",lambda: findDate(main_window, new_win)).pack(pady=10)
    create_button(new_win, "Availability of a person",lambda: findPerson(main_window, new_win)).pack(pady=10)    
    create_button(new_win, "Back", go_back).pack(pady=10)

def inviteWindow(main_window):
    main_window.withdraw()
    new_win = tk.Toplevel()
    new_win.title("Send invites")
    new_win.geometry(small)
    new_win.configure(bg="#f5f5f5")

    create_label(new_win, "Send invites").pack(pady=20)

    def go_back():
        new_win.destroy()
        main_window.deiconify()

    tk.Label(new_win, text="Names", **{"font": ("Helvetica", 12, "bold"), "bg": "#f5f5f5", "fg": "#333"}).pack(pady=5)
    names_entry = tk.Entry(new_win, font=("Helvetica", 12), width=30)
    names_entry.pack(pady=5)

    datetime_frame = tk.Frame(new_win, bg="#f5f5f5")
    datetime_frame.pack(pady=10)

    entry_width = 14  # Each entry width
    label_font = ("Helvetica", 12, "bold")
    entry_font = ("Helvetica", 12)

    date_frame = tk.Frame(datetime_frame, bg="#f5f5f5")
    date_frame.pack(side="left", padx=(0, 14))  # Small horizontal gap

    tk.Label(date_frame, text="Date", font=label_font, bg="#f5f5f5", fg="#333").pack()
    date_entry = tk.Entry(date_frame, font=entry_font, width=entry_width)
    date_entry.pack()

    time_frame = tk.Frame(datetime_frame, bg="#f5f5f5")
    time_frame.pack(side="left")

    tk.Label(time_frame, text="Time", font=label_font, bg="#f5f5f5", fg="#333").pack()
    time_entry = tk.Entry(time_frame, font=entry_font, width=entry_width)
    time_entry.pack()

    tk.Label(new_win, text="Description", **{"font": ("Helvetica", 12, "bold"), "bg": "#f5f5f5", "fg": "#333"}).pack(pady=5)
    desc_entry = tk.Entry(new_win, font=("Helvetica", 12), width=30)
    desc_entry.pack(pady=5)


    def submit():
        name = names_entry.get().strip()
        date = date_entry.get().strip()
        time = time_entry.get().strip()
        desc = desc_entry.get().strip()
        messagebox.showinfo("Send Message", calendarManager.sendInvite(name, date, time, desc))


    create_button(new_win, "Send", submit).pack(pady=8)

    create_button(new_win, "Back", go_back).pack(pady=(0,10))

def editWindow(main_window):
    main_window.withdraw()
    new_win = tk.Toplevel()
    new_win.title("Edit Sheets/Data")
    new_win.geometry(big)
    new_win.configure(bg="#f5f5f5")

    create_label(new_win, "Edit Sheets and Data").pack(pady=20)

    def go_back():
        new_win.destroy()
        main_window.deiconify()

    create_button(new_win, "Add a person",lambda: addWindow(main_window, new_win, True)).pack(pady=(0,10))
    create_button(new_win, "Update a name",lambda: updateWindow(main_window, new_win, True)).pack(pady=(0,10))    
    create_button(new_win, "Delete a person",lambda: deleteWindow(main_window, new_win, True)).pack(pady=(0,10))
    create_button(new_win, "Update email",lambda: updateEmail(main_window, new_win)).pack(pady=(0,10))
    create_button(new_win, "Add entry in data",lambda: addWindow(main_window, new_win, False)).pack(pady=(0,10))
    create_button(new_win, "Update name in data",lambda: updateWindow(main_window, new_win, False)).pack(pady=(0,10))
    create_button(new_win, "Delete entry in data",lambda: deleteWindow(main_window, new_win, False)).pack(pady=(0,10))
    create_button(new_win, "Back", go_back).pack(pady=(0,10))

def main():
    window = tk.Tk()
    window.title("Scheduling App")
    window.geometry(small)
    window.configure(bg="#f5f5f5")

    create_label(window, "Sophie's Scheduling App").pack(pady=20)

    def find():
        findWindow(window)

    def send():
        inviteWindow(window)
    def edit():
        editWindow(window)

    create_button(window, "Find availability", find).pack(pady=10)
    create_button(window, "Send Invites", send).pack(pady=10)
    create_button(window, "Edit Sheets/Data", edit).pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
