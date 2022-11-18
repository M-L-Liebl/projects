from tkinter import *
from dateutil import parser
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import pickle
from typing import List
from typing import Tuple


class Event:
    """
    Event Class
    """
    def __init__(self, name: str, date: datetime) -> None:
        self.name = name
        self.date = date
    
    def daysLeft(self) -> int:
        return (self.date - datetime.today()).days
        
    def __lt__(self, other):
        return self.daysLeft() < other.daysLeft()

class View:
    def __init__(self, events: List[Event]) -> None:
        self.MAX_COLUMNS = 16
        self.events = events
        self.window = Tk()
        self.window.title("Event Timer")
        # TODO: autoscale plot when resizing window 
        # self.window.geometry("")
        self.fig = Figure(figsize=(14, 8), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=self.MAX_COLUMNS)
        self.button_new = Button(master=self.window,text="show",command=self.display_events)
        self.button_new2 = Button(master=self.window,text="show",command=self.display_events)
        Label(self.window, text="Event Name").grid(row=1, column=0)
        Label(self.window, text="Event Date").grid(row=2, column=0)
        self.name_entry = Entry(self.window)
        self.date_entry = Entry(self.window)
        self.name_entry.grid(row=1, column=1)
        self.date_entry.grid(row=2, column=1)
        self.button_add_editEvent = Button(master=self.window, text="Add/Edit Event", command=self.add_edit_event)
        self.button_deleteEvent = Button(master=self.window, text="Delete Event", command=self.delete_event)
        self.button_add_editEvent.grid(row=1, column=3)
        self.button_deleteEvent.grid(row=1, column=4)
        self.infobox = Label(self.window, textv="")
        self.infobox.grid(row=1, column=10, columnspan=6)


    def plot(self) -> int:
        """
        returns 1 and creates plot if there are events
        returns 0 and does not create plot if there are no events
        """
        self.events.sort() # sort list for correct order of events in plot
        y=[e.name for e in self.events]
        x=[e.daysLeft() for e in self.events]
        if not y:
            return 0
        plot1 = self.fig.add_subplot(111)
        plot1.set_xlabel("days remaining")
        plot1.barh(y, x, linewidth=0.5)
        plot1.grid(b=True, which='major', axis='x')
        return 1


    def display_events(self):
        self.fig.clear()
        if self.plot():
            # update figure shown in canvas
            self.canvas.draw_idle()
        else:
            self.canvas.draw_idle()
            self.show_info("There are no events to display")


    def check_entry(self, name: str, date: datetime) -> bool:
        """
        Checks if input was incorrect.
        """
        if not name or name in [e.name for e in self.events]:
            return False
        try:
            parser.parse(date)
            return True
        except:
            return False


    def add_edit_event(self) -> bool:
        """
        adds event from entry in window if event is new. If event exists, it sets new date. Returns true if event was added/edited,
        returns false if event cannot be added/edited because input was incorrect.
        """
        name = self.name_entry.get()
        date = self.date_entry.get()
        self.delete_Entries()
        if self.check_entry(name, date):
            self.events.append(Event(name, parser.parse(date)))
            self.display_events()
        else:
            self.show_info("You have to enter a new name and a date in the form of yyyy.mm.dd")
            return
        self.show_info("")

    def delete_Entries(self) -> None:
        self.name_entry.delete(0, "end")
        self.date_entry.delete(0, "end")


    def delete_event(self) -> None:
        name = self.name_entry.get()
        for e in self.events:
            if e.name == name:
                self.events.remove(e)
                self.show_info("Event removed")
                self.display_events()
                self.delete_Entries()
                return
        self.show_info("Event not found")
        self.delete_Entries()


    def show_info(self, newtext: str):
        self.infobox.config(text=newtext)


        
        


def get_Events() -> List[Event]:
    """
    Load Events from file, returns empty List if no events are found
    """
    try:
        events_file = open("/home/reed/Documents/projects/eventTimer/events.pickle", "rb")
        events = pickle.load(events_file)
        events_file.close()
        return events
    except:
        return []


def save_Events(events: List[Event]) -> bool:
    """
    saves Events to file after window is closed
    """
    events_file = open("/home/reed/Documents/projects/eventTimer/events.pickle", "wb")
    pickle.dump(events, events_file)
    events_file.close()



if __name__ == "__main__":
    v = View(get_Events())
    v.display_events()
    v.window.mainloop()
    save_Events(v.events)
