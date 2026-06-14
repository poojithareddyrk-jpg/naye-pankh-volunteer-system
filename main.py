import tkinter as tk
from tkinter import messagebox
import csv

def add_volunteer():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    with open("volunteers.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone])

    messagebox.showinfo(
        "Success",
        "Volunteer Saved Successfully!"
    )

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def search_volunteer():
    name = name_entry.get()

    with open("volunteers.csv", "r") as file:
        data = file.readlines()

    found = False

    for row in data:
        if name.lower() in row.lower():
            messagebox.showinfo("Volunteer Found", row)
            found = True
            break

    if not found:
        messagebox.showerror("Not Found", "Volunteer not found")

def generate_report():
    with open("volunteers.csv", "r") as file:
        data = file.readlines()

    total = len(data)

    with open("report.txt", "w") as report:
        report.write("Volunteer Report\n")
        report.write("=================\n")
        report.write(f"Total Volunteers: {total}\n\n")

        for row in data:
            report.write(row)

    messagebox.showinfo("Report", "Report Generated Successfully!")

def delete_volunteer():
    name = name_entry.get()

    with open("volunteers.csv", "r") as file:
        rows = file.readlines()

    with open("volunteers.csv", "w") as file:
        deleted = False

        for row in rows:
            if name.lower() not in row.lower():
                file.write(row)
            else:
                deleted = True

    if deleted:
        messagebox.showinfo("Success", "Volunteer Deleted")
    else:
        messagebox.showerror("Error", "Volunteer Not Found")


root = tk.Tk()
root.title("Volunteer Management System")
root.geometry("500x400")

title = tk.Label(root, text="Volunteer Management System", font=("Arial", 16))
title.pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

tk.Button(
    root,
    text="Add Volunteer",
    command=add_volunteer
).pack(pady=10)

tk.Button(
    root,
    text="Search Volunteer",
    command=search_volunteer
).pack(pady=5)

tk.Button(
    root,
    text="Generate Report",
    command=generate_report
).pack(pady=5)

tk.Button(
    root,
    text="Delete Volunteer",
    command=delete_volunteer
).pack(pady=5)

root.mainloop()