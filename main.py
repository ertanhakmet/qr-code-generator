import tkinter as tk
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox

qr = qrcode.QRCode(version=1, box_size=5, border=1)


# generate function
def generate():
    try:
        link = url_entry.get()
        if not link:
            messagebox.showwarning("Warning", "Please enter a URL")
            return

        qr.clear()
        qr.add_data(link)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        qr_img_tk = ImageTk.PhotoImage(qr_img)
        qr_label.config(image=qr_img_tk)
        qr_label.image = qr_img_tk
    except:
        messagebox.showerror("Error", "Invalid URL")


# save function
# save function
def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_img = qr.make_image(fill_color="black", back_color="white")
        qr_img.save(file_path)


# window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("280x450")

# url label
url_label = tk.Label(window, text="Enter your URL:")
url_label.grid(row=0, column=0, padx=15, pady=15)

# url entry
url_entry = tk.Entry(window)
url_entry.grid(row=0, column=1, padx=15, pady=15)

# generate button
generate_button = tk.Button(window, text="Generate", command=generate)
generate_button.grid(row=1, column=0, columnspan=2, pady=15)

# qr label
qr_label = tk.Label(window)
qr_label.grid(row=2, column=0, columnspan=2, pady=15)

# save button
save_button = tk.Button(window, text="Save Image", command=save_image)
save_button.grid(row=3, column=0, columnspan=2, pady=15)

# Start the tkinter event loop
window.mainloop()
