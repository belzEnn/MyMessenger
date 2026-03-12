from customtkinter import CTk, CTkFrame, CTkButton, CTkScrollableFrame, CTkTextbox, CTkLabel

class ChatList(CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.configure(fg_color="transparent")
        
        chats = [
            "ExampleUser1",
            "ExampleUser2",
            "ExampleUser3",
            "ExampleUser4",
            "ExampleUser5"
        ]

        for chat in chats:
            btn = CTkButton(self, text=chat,fg_color="transparent",text_color="white",hover_color="#333333",anchor="w",height=35,corner_radius=8,command=lambda t=chat: self.select_chat(t))
            btn.pack(fill="x", pady=2, padx=5)

    def select_chat(self, title):
        print(f"Chat: {title}")



class Chat(CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

    def add_message(self, text, is_my=True):
        side = "e" if is_my else "w"  # e - right (East), w - left (West)
        color = "#1f538d" if is_my else "#3d3d3d"
        
        msg_label = CTkLabel(
            self, 
            text=text, 
            fg_color=color, 
            corner_radius=12,
            padx=12, pady=8,
            wraplength=300 # To wrap a long text
        ).pack(side="top", anchor=side, pady=5, padx=10)
        

class Send_Message(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.button = CTkButton(self, text="Send", width=100, command=self.master.send) 
        self.button.pack(side="right", padx=5)

        self.textbox = CTkTextbox(self, width=400, height=70, corner_radius=0)
        self.textbox.pack(side="left", fill="x", expand=True)

class App(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("800x480")
 
        self.menu = ChatList(self)
        self.menu.pack(side="left", fill="y")

        self.chat_display = Chat(self)
        self.chat_display.pack(side="top", fill="both", expand=True)

        self.message_input = Send_Message(self)
        self.message_input.pack(side="bottom", fill="x", padx=10, pady=10)

    def send(self):
        text = self.message_input.textbox.get("1.0", "end-1c") 
        if text.strip():
            self.chat_display.add_message(text, is_my=True)
            self.message_input.textbox.delete("1.0", "end")

app = App()
app.mainloop()