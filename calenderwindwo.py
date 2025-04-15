import tkinter as tk
import calendar

# Create main window
root = tk.Tk()
root.title("Calendar")
root.geometry("600x600")

# Year to display
year = 2025

# Create a calendar instance
text_cal = calendar.TextCalendar(calendar.SUNDAY)
cal_text = text_cal.formatyear(year, 2, 1, 6, 3)

# Create a Text widget to show calendar
text_widget = tk.Text(root, font=("Courier", 10))
text_widget.pack(expand=True, fill="both")

# Insert calendar text into the widget
text_widget.insert(tk.END, cal_text)

# Make text read-only
text_widget.config(state="disabled")

# Run the GUI loop
root.mainloop()
