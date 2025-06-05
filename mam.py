import tkinter as tk
from tkinter import messagebox
import os

# File to store student records
FILE_NAME = "students.txt"

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x400")

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries
        self.name_label = tk.Label(self.root, text="Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.roll_label = tk.Label(self.root, text="Roll Number")
        self.roll_label.grid(row=1, column=0, padx=10, pady=10)
        self.roll_entry = tk.Entry(self.root)
        self.roll_entry.grid(row=1, column=1, padx=10, pady=10)

        self.marks_label = tk.Label(self.root, text="Marks")
        self.marks_label.grid(row=2, column=0, padx=10, pady=10)
        self.marks_entry = tk.Entry(self.root)
        self.marks_entry.grid(row=2, column=1, padx=10, pady=10)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.grid(row=3, column=0, padx=10, pady=10)

        self.view_button = tk.Button(self.root, text="View Students", command=self.view_students)
        self.view_button.grid(row=3, column=1, padx=10, pady=10)

        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_entries)
        self.clear_button.grid(row=4, column=0, padx=10, pady=10)

        # Listbox for displaying student records
        self.student_listbox = tk.Listbox(self.root, height=10, width=50)
        self.student_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Load existing student records from the file
        self.load_students()

    def add_student(self):
        name = self.name_entry.get()
        roll = self.roll_entry.get()
        marks = self.marks_entry.get()

        if name and roll and marks:
            student_data = f"{name},{roll},{marks}\n"
            with open(FILE_NAME, "a") as file:
                file.write(student_data)
            self.clear_entries()
            self.load_students()
            messagebox.showinfo("Success", "Student added successfully")
        else:
            messagebox.showerror("Error", "All fields are required")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)

    def load_students(self):
        if not os.path.exists(FILE_NAME):
            return

        self.student_listbox.delete(0, tk.END)
        with open(FILE_NAME, "r") as file:
            for line in file:
                self.student_listbox.insert(tk.END, line.strip())

    def view_students(self):
        self.load_students()


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
