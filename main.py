import tkinter as tk
import webbrowser
from pynput import mouse
import threading
import queue


class MouseDebugApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Debugger")
        self.root.attributes('-topmost', True)
        self.create_widgets()
        # Start the listener thread
        self.listener_thread = threading.Thread(target=self.run_listener)
        self.listener_thread.daemon = True
        self.listener_thread.start()
        self.event_queue = queue.Queue()

        self.scroll_reset_delay = 100  # milliseconds
        self.scroll_up_reset_job = None
        self.scroll_down_reset_job = None
        self.mouse_position = (0, 0)

        self.update_mouse_position()

    def run_listener(self):
        with mouse.Listener(
                on_click=self.on_click,
                on_scroll=self.on_scroll,
                on_move=self.on_move) as listener:
            listener.join()

    def create_widgets(self):
        self.left_btn = tk.Label(self.root, text="Left Button", bg="lightgrey", width=20, height=4)
        self.left_btn.grid(row=0, column=0, padx=0, pady=0)

        self.scroll_buttons_frame = tk.Frame(self.root, width=5, height=4)
        self.scroll_buttons_frame.grid(row=0, column=1, padx=1, pady=1)

        self.scroll_up_btn = tk.Label(self.scroll_buttons_frame, bg="lightgrey", width=5, height=2)
        self.scroll_up_btn.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=1, pady=(0, 1))

        self.scroll_down_btn = tk.Label(self.scroll_buttons_frame, bg="lightgrey", width=5, height=2)
        self.scroll_down_btn.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=1, pady=(1, 0))

        self.scroll_mid_btn = tk.Label(self.scroll_buttons_frame, text="Mid", bg="lightgrey", width=3, height=2,
                                       highlightbackground="white", highlightthickness=1)
        self.scroll_mid_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.right_btn = tk.Label(self.root, text="Right Button", bg="lightgrey", width=20, height=4)
        self.right_btn.grid(row=0, column=2, padx=0, pady=0)

        # Real-time debugging information
        self.debug_frame = tk.Frame(self.root)
        self.debug_frame.grid(row=1, column=0, columnspan=3, pady=5, sticky="ew")

        self.debug_frame.columnconfigure(0, weight=1)  # Make the column expand
        self.debug_frame.columnconfigure(1, weight=1)  # Ensure the second column also expands

        self.position_label = tk.Label(self.debug_frame, text="Position: (0, 0)")
        self.position_label.grid(row=0, column=0, padx=5, sticky='w')

        # Pack propagate to resize the root window
        self.root.update_idletasks()
        self.root.geometry("")
        self.root.pack_propagate(False)

        self.footer_text = tk.Text(self.root, width=40, height=1, font=("Arial", 8), bd=0, bg=self.root.cget("bg"),
                                   wrap="word")
        self.footer_text.grid(row=3, column=0, columnspan=3, pady=0, sticky="e")
        self.footer_text.insert(tk.END, "Leave a star on the ")
        self.footer_text.insert(tk.END, "GitHub repo", ("hyperlink",))
        self.footer_text.insert(tk.END, " if you like it.")
        self.footer_text.tag_config("hyperlink", foreground="blue", underline=True)
        self.footer_text.tag_bind("hyperlink", "<Button-1>", lambda e: self.open_github())
        self.footer_text.tag_configure("right", justify='right')
        self.footer_text.tag_add("right", "1.0", "end")
        self.footer_text.config(state=tk.DISABLED)

    def on_click(self, x, y, button, pressed):
        status = "Pressed" if pressed else "Released"
        self.event_queue.put(("click", button, status))

    def on_scroll(self, x, y, dx, dy):
        self.event_queue.put(("scroll", dy))

    def on_move(self, x, y):
        self.event_queue.put(("move", x, y))

    def process_events(self):
        while not self.event_queue.empty():
            event = self.event_queue.get()
            if event[0] == "click":
                button, status = event[1], event[2]
                if button == mouse.Button.left:
                    self.left_btn.config(bg="blue" if status == "Pressed" else "lightgrey")
                elif button == mouse.Button.right:
                    self.right_btn.config(bg="blue" if status == "Pressed" else "lightgrey")
                elif button == mouse.Button.middle:
                    self.scroll_mid_btn.config(bg="blue" if status == "Pressed" else "lightgrey")
            elif event[0] == "scroll":
                dy = event[1]
                if dy > 0:
                    self.scroll_up_btn.config(bg="blue")
                    if self.scroll_up_reset_job:
                        self.root.after_cancel(self.scroll_up_reset_job)
                    self.scroll_up_reset_job = self.root.after(self.scroll_reset_delay, self.reset_scroll_up_btn)
                elif dy < 0:
                    self.scroll_down_btn.config(bg="blue")
                    if self.scroll_down_reset_job:
                        self.root.after_cancel(self.scroll_down_reset_job)
                    self.scroll_down_reset_job = self.root.after(self.scroll_reset_delay, self.reset_scroll_down_btn)
            elif event[0] == "move":
                x, y = event[1], event[2]
                self.mouse_position = (x, y)

    def update_mouse_position(self):
        self.position_label.config(text=f"Position: {self.mouse_position}")
        self.process_events()
        self.root.after(1, self.update_mouse_position)

    def reset_scroll_up_btn(self):
        self.scroll_up_btn.config(bg="lightgrey")

    def reset_scroll_down_btn(self):
        self.scroll_down_btn.config(bg="lightgrey")

    def open_github(self):
        webbrowser.open_new("https://github.com/Weikang01/mouse_debugger")

    def on_close(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MouseDebugApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
