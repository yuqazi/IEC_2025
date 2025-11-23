import tkinter as tk
from tkinter import ttk
from gui import create_window
from gui import random_code

class SliderApp:
    """
    A simple Tkinter application demonstrating a Scale widget (slider),
    a Label that displays the slider's current value, and a Submit button
    that calls a function from another file.
    """
    def __init__(self, master):
        self.master = master
        master.title("Integer Slider (0 to 20) Example")
        master.geometry("400x250")
        master.resizable(False, False)

        # Variable to hold the slider's current value
        self.slider_value = tk.DoubleVar()
        self.slider_value.set(10.0)  # Start in the middle

        # Stores the result of running random_code() early
        self.precomputed_code = None

        # Slider
        self.slider = tk.Scale(
            master,
            from_=0,
            to=20,
            resolution=1,
            orient='horizontal',
            length=300,
            variable=self.slider_value,
            command=self.on_slider_change
        )
        self.slider.pack(pady=20)

        # Label to show current value
        self.label_text = tk.StringVar()
        self.value_label = ttk.Label(
            master,
            textvariable=self.label_text,
            font=('Arial', 14, 'bold')
        )
        self.value_label.pack(pady=10)

        # Submit button
        self.submit_button = ttk.Button(
            master,
            text="Submit",
            command=self.submit_value
        )
        self.submit_button.pack(pady=15)

        # Initialize label text & pre-run code
        self.on_slider_change(self.slider_value.get())

    def on_slider_change(self, value):
        """Runs BEFORE create_window — executed every time the slider moves."""
        try:
            int_value = int(float(value))
            self.label_text.set(f"Selected Count: {int_value}")

            # Pre-run the function using current slider value
            self.precomputed_code = random_code(int_value)

        except ValueError:
            self.label_text.set("Error")
            self.precomputed_code = None

    def submit_value(self):
        """Calls create_window but uses the already precomputed code."""
        current_value = int(self.slider_value.get())

        # Use the precomputed version instead of running random_code here
        create_window(self.precomputed_code, current_value)


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = SliderApp(root)
    root.mainloop()
