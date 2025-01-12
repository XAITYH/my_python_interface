import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

appWidth, appHeight = 600, 600

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("XAITYH")
        self.geometry(f"{appWidth}x{appHeight}")
        self.resizable(False, False)
        
        self.my_name_frame = ctk.CTkFrame(master=self, fg_color="#F5F5F5")
        self.my_name_frame.grid(row=0, column=0, sticky="nsew")
        
        self.my_name_font = ctk.CTkFont(family="Helvetica", size=44,
            weight="bold", slant="italic", underline=True)
        self.my_name_var = tk.StringVar()
        self.my_name = ctk.CTkLabel(
            master=self.my_name_frame, text="It's me, XAITYH!",
            font=self.my_name_font,
            justify="center",
            width=600,
            text_color="#48CFCB"
        )
        self.my_name.grid(row=0, column=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()
        