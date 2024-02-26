from .const import *
import tkinter as tk
import customtkinter as ctk
from .speed_meter import SpeedMeter


class App:
    def __init__(self):
        self.root = ctk.CTk(fg_color=IGNORED_COLOR)
        self.__init_window()
    

    def __init_window(self):
        self.root.geometry(APP_GEOMETRY)
        self.root.geometry(f"+{APP_POSITION_X}+{APP_POSITION_Y}")
        self.root.lift()
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-toolwindow", True)
        self.root.overrideredirect(True)
        self.root.wm_attributes("-transparentcolor", IGNORED_COLOR)
        self.root.protocol("WM_DELETE_WINDOW", self.exit_app)
        self.root.bind("<Escape>", self.exit_app)
        self.root.after(NET_SPEED_UPDATE_DELAY, self.update)

    def setup(self):
        self._font_1 = ctk.FontManager.load_font("app/src/font/Bulletto Killa.ttf")
        self._font_2 = ctk.FontManager.load_font("app/src/font/sofachrome rg.otf")

        f1 = ctk.CTkFrame(self.root, height=13,)
        f1.pack(fill=tk.X, expand=True)
        ctk.CTkLabel(
            f1,
            text="Up",
            width=50,
            corner_radius=5,
            font=ctk.CTkFont(self._font_1, size=15, weight="bold"),
            fg_color=rgb(100, 212, 20),
            cursor=CURSORS[CURRENT_CURSOR],
        ).pack(side=tk.LEFT)
        
        self.upload_text = ctk.CTkLabel(f1, text="Calculating", font=ctk.CTkFont(self._font_1, size=15, weight="bold"))
        self.upload_text.pack(side=tk.RIGHT,anchor=tk.CENTER, expand=True, fill=tk.X)


        f2 = ctk.CTkFrame(self.root, height=13,)
        f2.pack(fill=tk.X, expand=True)
        ctk.CTkLabel(
            f2,
            width=50,
            text="Down",
            font=ctk.CTkFont(self._font_1, size=15, weight="bold"),
            fg_color=rgb(170, 41, 10),
            cursor=CURSORS[CURRENT_CURSOR],
            corner_radius=5,
        ).pack(side=tk.LEFT)

        self.download_text = ctk.CTkLabel(f2, text="Calculating", font=ctk.CTkFont(self._font_1, size=15, weight="bold"))
        self.download_text.pack(side=tk.RIGHT,anchor=tk.CENTER, expand=True, fill=tk.X)

        f3 = ctk.CTkFrame(self.root, height=13,)
        f3.pack(fill=tk.X, expand=True)
        ctk.CTkLabel(
            f3,
            width=50,
            text="Total",
            font=ctk.CTkFont(self._font_1, size=15, weight="bold"),
            fg_color=rgb(70, 141, 210),
            cursor=CURSORS[CURRENT_CURSOR],
            corner_radius=5,
        ).pack(side=tk.LEFT)

        self.total_text = ctk.CTkLabel(f3, text="Calculating", font=ctk.CTkFont(self._font_1, size=15, weight="bold"))
        self.total_text.pack(side=tk.RIGHT,anchor=tk.CENTER, expand=True, fill=tk.X)

        self.upload_text.bind("<Button-3>", self.open_setting_window)
        self.download_text.bind("<Button-3>", self.open_setting_window)
        self.total_text.bind("<Button-3>", self.open_setting_window)

        self.transparency = tk.IntVar(value=APP_TRANSPARENCY)
        self.positon_y = tk.IntVar(value=APP_POSITION_Y)
        self.cursor = tk.StringVar(value=CURSORS[0])

        self.root.attributes('-alpha', self.transparency.get() / 100)
        
        
        self.today_label = None

        self.speed_meter = SpeedMeter()
        self.top_level_open = False 

    def update(self):
        self.speed_meter.update()

        self.upload_text.configure(
            text=f"{self.speed_meter.convert_speed(self.speed_meter.upload_speed)}/s"
        )
        self.download_text.configure(
            text=f"{self.speed_meter.convert_speed(self.speed_meter.download_speed)}/s"
        )
        self.total_text.configure(
            text=f"{self.speed_meter.convert_speed(self.speed_meter.total_speed)}/s"
        )

        if self.today_label:
            gb = round(self.speed_meter.now_total * BYTE_TO_GB, 5)
            self.today_label.configure(text=f"Today : {gb} GB")

        self.root.after(NET_SPEED_UPDATE_DELAY, self.update)

    def open_setting_window(self, event):
        if self.top_level_open:
           return
         
        self.top_level = ctk.CTkToplevel(fg_color=rgb(50, 50, 70))
        self.top_level.geometry("300x270")
        self.top_level.maxsize(300, 270)
        self.top_level.title("Created By - @SudipOP")
        self.top_level.protocol("WM_DELETE_WINDOW", self.handle_toplevel_destroy)
        self.today_label = ctk.CTkLabel(
            self.top_level, text="Today : 000 GB", font=ctk.CTkFont(self._font_1, 15)
        )
        self.today_label.pack(fill=tk.X, anchor=tk.N, padx=10, pady=10)

        ctk.CTkLabel(self.top_level, text="Select Cursor").pack(
            anchor=tk.W, padx=10, pady=(10, 2)
        )
        ctk.CTkComboBox(
            self.top_level, values=CURSORS, command=self.set_cursor, variable=self.cursor
        ).pack(fill=tk.X, anchor=tk.N, side=tk.TOP, padx=10, pady=(0, 10))

        ctk.CTkLabel(self.top_level, text="Transparency").pack(
            anchor=tk.W, padx=10, pady=(10, 2)
        )
        ctk.CTkSlider(
            self.top_level,
            command=self.set_transparency,
            variable=self.transparency,
            from_=10,
            to=100,
        ).pack(fill=tk.X, padx=10, pady=(0, 10))

        ctk.CTkLabel(self.top_level, text="Position").pack(
            anchor=tk.W, padx=10, pady=(10, 2)
        )
        ctk.CTkSlider(
            self.top_level,
            command=self.set_position_y,
            variable=self.positon_y,
            from_=0,
            to=Display.get_size()[1] - APP_HEIGHT,
        
        ).pack(fill=tk.X, padx=10, pady=(0, 10))
        self.top_level_open = True
        
        
    def handle_toplevel_destroy(self):
        self.today_label = None
        self.top_level_open = False
        self.top_level.destroy()
        

    def set_cursor(self, e):
        self.set_cursor_to_widget(self.upload_text)
        self.set_cursor_to_widget(self.download_text)
        self.set_cursor_to_widget(self.total_text)

    def set_cursor_to_widget(self, widget):
        widget.configure(cursor=self.cursor.get())

    def set_transparency(self, e):
        self.root.attributes("-alpha", self.transparency.get() / 100)

    def set_position_y(self, e):
        self.root.geometry(f"+{APP_POSITION_X}+{self.positon_y.get()}")

    def exit_app(self, event):
        SaveSystem.saveData(SaveSystem.ALPHA_PATH, self.transparency.get())
        SaveSystem.saveData(SaveSystem.POS_PATH, self.positon_y.get())
        self.root.destroy()

    def run(self):
        self.setup()
        self.root.mainloop()
