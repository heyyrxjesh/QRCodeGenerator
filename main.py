import qrcode
import tkinter as tk
from PIL import Image, ImageTk

def generate_qr_code(text):
    if(text == ""):
        return
    img = qrcode.make(text)
    img.save(f"result.png")
    return img

def display_qr_code(root, text):
    if(text == ""):
        return
    img = generate_qr_code(text)
    img = ImageTk.PhotoImage(img.resize((250, 250)))
    label = tk.Label(root, image=img)
    label.image = img
    label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x350")
    root.title("QR Code Generator")
    entry = tk.Entry(root)
    entry.pack()
    generate_button = tk.Button(root, text="Generate", command=lambda: display_qr_code(root, entry.get()))
    generate_button.pack()
    label = tk.Label(root, text="Copyright (C) 2023: Made with ❤️ by Hardik")
    label.pack(side="bottom", fill="x")
    root.mainloop()
