import tkinter

window =tkinter.Tk()
window.title("Data Entry Form")

frame=tkinter.Frame(window)
frame.pack()

#Saving User Information
user_info_frame=tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0,column=0)

first_name_label=tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

first_name_entry=tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

#Saving Course Info
courses_frame=tkinter.LabelFrame(frame)
courses_frame.grid(row=0, column=1, sticky="news", padx=20, pady=0)

Registered_label=tkinter.Label(courses_frame, text="Registration status")
Registered_label.grid(row=0, column=0)
window.mainloop()