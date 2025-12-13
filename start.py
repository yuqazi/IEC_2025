import tkinter as tk
from tkinter import ttk
from gui import create_window, random_code, create_botwindow


class SliderApp:
    """
    Tkinter App with:
    - A slider (0–20)
    - Label showing slider value
    - A checkbox to choose bot function on/off
    - Submit button that calls create_window() in gui.py
    - Precomputes random_code() during slider movement
    """
    def __init__(self, master):
        self.master = master
        master.title("Integer Slider (0 to 10)")
        master.geometry("400x300")
        master.resizable(False, False)

        # Holds live slider value
        self.slider_value = tk.IntVar(value=10)

        # Store precomputed random_code() result
        self.precomputed_code = None

        # Slider widget
        self.slider = tk.Scale(
            master,
            from_=0,
            to=10,
            resolution=1,
            orient='horizontal',
            length=300,
            variable=self.slider_value,
            command=self.on_slider_change
        )
        self.slider.pack(pady=20)

        # Label showing current value
        self.label_text = tk.StringVar()
        self.value_label = ttk.Label(
            master,
            textvariable=self.label_text,
            font=('Arial', 14, 'bold')
        )
        self.value_label.pack(pady=10)

        # Checkbox for enabling bot
        self.bot_enabled = tk.BooleanVar(value=False)
        self.bot_checkbox = ttk.Checkbutton(
            master,
            text="Enable Bot Function",
            variable=self.bot_enabled
        )
        self.bot_checkbox.pack(pady=5)

        # Submit button
        self.submit_button = ttk.Button(
            master,
            text="Submit",
            command=self.submit_value
        )
        self.submit_button.pack(pady=15)

        # Initialize
        self.on_slider_change(self.slider_value.get())

    def on_slider_change(self, value):
        """Updates label and precomputes random_code() for faster Submit."""
        int_value = int(float(value))
        self.label_text.set(f"Selected Count: {int_value}")

        # Pre-run the external function so Submit is instant
        self.precomputed_code = random_code(int_value)

    def submit_value(self):
        """Calls create_window() in gui.py using the precomputed result."""
        count = self.slider_value.get()
        bot_value = self.bot_enabled.get()
        if bot_value:
            print("Bot function is enabled.")
            create_botwindow(self.precomputed_code, count)
        else:
            create_window(self.precomputed_code, count)


# Only run the GUI if executed directly
if __name__ == "__main__":
    root = tk.Tk()
    app = SliderApp(root)
    root.mainloop()
