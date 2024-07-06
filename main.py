import tkinter as tk
from tkinter import ttk, messagebox

class TravelItineraryPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Itinerary Planner")
        self.itineraries = {}

        
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        
        self.create_widgets()

    def create_widgets(self):

        ttk.Label(self.main_frame, text="Destination:").grid(row=0, column=0, sticky=tk.W)
        self.destination_entry = ttk.Entry(self.main_frame, width=30)
        self.destination_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

        
        ttk.Label(self.main_frame, text="Number of Days:").grid(row=1, column=0, sticky=tk.W)
        self.days_spinbox = tk.Spinbox(self.main_frame, from_=1, to=30, width=5)
        self.days_spinbox.grid(row=1, column=1, sticky=(tk.W, tk.E))

        
        self.add_itinerary_button = ttk.Button(self.main_frame, text="Add Itinerary", command=self.add_itinerary)
        self.add_itinerary_button.grid(row=2, column=0, columnspan=2, pady=10)

        
        self.itinerary_listbox = tk.Listbox(self.main_frame, height=10, width=50)
        self.itinerary_listbox.grid(row=3, column=0, columnspan=2, pady=10)
        self.itinerary_listbox.bind("<<ListboxSelect>>", self.display_itinerary)

        
        self.activities_frame = ttk.Frame(self.root, padding="10")
        self.activities_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        
        self.activities_label = ttk.Label(self.activities_frame, text="Activities for Selected Day:")
        self.activities_label.grid(row=0, column=0, columnspan=2, sticky=tk.W)

        
        ttk.Label(self.activities_frame, text="Day:").grid(row=1, column=0, sticky=tk.W)
        self.day_spinbox = tk.Spinbox(self.activities_frame, from_=1, to=30, width=5)
        self.day_spinbox.grid(row=1, column=1, sticky=(tk.W, tk.E))

        
        ttk.Label(self.activities_frame, text="Activity:").grid(row=2, column=0, sticky=tk.W)
        self.activity_entry = ttk.Entry(self.activities_frame, width=30)
        self.activity_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

        self.add_activity_button = ttk.Button(self.activities_frame, text="Add Activity", command=self.add_activity)
        self.add_activity_button.grid(row=3, column=0, columnspan=2, pady=10)

        
        self.activities_listbox = tk.Listbox(self.activities_frame, height=10, width=50)
        self.activities_listbox.grid(row=4, column=0, columnspan=2, pady=10)

    def add_itinerary(self):
        destination = self.destination_entry.get()
        days = int(self.days_spinbox.get())
        if destination and days:
            self.itineraries[destination] = {day: [] for day in range(1, days + 1)}
            self.itinerary_listbox.insert(tk.END, destination)
            self.destination_entry.delete(0, tk.END)
            self.days_spinbox.delete(0, tk.END)
            self.days_spinbox.insert(0, "1")
        else:
            messagebox.showwarning("Input Error", "Please enter a destination and number of days.")

    def display_itinerary(self, event):
        selected_itinerary = self.itinerary_listbox.get(tk.ACTIVE)
        self.selected_destination = selected_itinerary
        self.update_activities_list()

    def add_activity(self):
        day = int(self.day_spinbox.get())
        activity = self.activity_entry.get()
        if activity and self.selected_destination:
            self.itineraries[self.selected_destination][day].append(activity)
            self.activity_entry.delete(0, tk.END)
            self.update_activities_list()
        else:
            messagebox.showwarning("Input Error", "Please select an itinerary and enter an activity.")

    def update_activities_list(self):
        self.activities_listbox.delete(0, tk.END)
        if self.selected_destination:
            for day, activities in self.itineraries[self.selected_destination].items():
                self.activities_listbox.insert(tk.END, f"Day {day}:")
                for activity in activities:
                    self.activities_listbox.insert(tk.END, f"  - {activity}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelItineraryPlanner(root)
    root.mainloop()
