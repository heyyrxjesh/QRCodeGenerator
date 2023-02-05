import datetime
import os
import re
from tkinter import messagebox
import tkinter
import customtkinter
import qrcode


class QRCodeGenerator:
    def __init__(self) -> None:
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        self.app = customtkinter.CTk()
        self.app.geometry("720x478")
        self.app.resizable(False, False)
        self.app.title("QR Code generator")

        title = customtkinter.CTkLabel(
            self.app, text="Insert any link", font=("Verdana", 16))
        title.pack(padx=10, pady=10)

        url_var = tkinter.StringVar()
        self.link = customtkinter.CTkEntry(
            self.app, width=400, height=40, textvariable=url_var)
        self.link.pack()

        generate = customtkinter.CTkButton(
            self.app, text="Generate", font=("Verdana", 16), command=self.start_generate)
        generate.pack(padx=10, pady=20)

        copyRight = customtkinter.CTkLabel(
            self.app, text="Copyright (C) 2023: Made by Hardik Jaiswal", font=("Verdana", 16))
        copyRight.pack(side="bottom", fill="x", pady=10)

    def start_generate(self):
        try:
            folder_name = "QR Codes"
            desktop = os.path.join(os.path.join(
                os.environ['USERPROFILE']), 'Desktop')
            folder_path = os.path.join(desktop, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                os.chdir(folder_path)

                qrLink = self.link.get()
                if (self.is_url(qrLink)):
                    img = qrcode.make(qrLink)
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    img.save(f"result_at_{current_time}.png")

                    messagebox.showinfo(
                        "Success", "Generating QR code complete")
                else:
                    messagebox.showerror(
                        "Error", "Please enter a valid link or URL")
                self.link.delete(0, tkinter.END)
            else:
                os.chdir(folder_path)

                qrLink = self.link.get()
                if (self.is_url(qrLink)):
                    img = qrcode.make(qrLink)
                    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    img.save(f"result_at_{current_time}.png")

                    messagebox.showinfo(
                        "Success", "Generating QR code complete")
                else:
                    messagebox.showerror(
                        "Error", "Please enter a valid link or URL")
                self.link.delete(0, tkinter.END)
        except Exception as e:
            messagebox.showerror("Error", e)

    def is_url(self, text):
        pattern = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            # domain...
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(pattern, text) is not None

    def run(self):
        self.app.mainloop()


if __name__ == '__main__':
    QRCodeGenerator().run()
