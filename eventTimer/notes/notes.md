# TODOs
- methods should only do one thing (addEvent should only add event to PriorityQueue, update graph should be done elsewhere)
- set maximal width of bars (problem with only one event, looking stupid)
- autoscale function for resizing (plot has to resize too)
- choose between days/weeks x-axis button
- move window creation from __init__ to createwindow()... -> easier for multiple windows
- change code to Model-View-Controller style
- eventually change pickle to json, more stable with changes in i.e. Event class
- update plot elsewhere, not in add/edit-method
- remove events or not saving events when daysLeft() negative
- make path from events.pickle relative, not static
- make some things immutable, makes sense?
- write "Getting Started" section in README
  - 1. git clone "..."
  - 2. Activate a virtualenv
  - 3. pip install -r requirements.txt
  - 4. python main.py
- write How to autostart section



# Notes/Ideas
- ideas for future: click on bar -> new window with interim steps of event, if interim event is due->red color, checkbox for steps, back button to main menu



# UML with mermaid
