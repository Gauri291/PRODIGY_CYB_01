import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def handle_encrypt():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        encrypted = encrypt(text, shift)
        decrypted = decrypt(encrypted, shift)
        result_var.set(f"Encrypted: {encrypted}\nDecrypted: {decrypted}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for shift.")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher GUI")
root.geometry("400x250")
root.config(bg="#f0f0f0")

tk.Label(root, text="Enter Message:", bg="#f0f0f0").pack(pady=5)
entry_text = tk.Entry(root, width=40)
entry_text.pack()

tk.Label(root, text="Enter Shift Value:", bg="#f0f0f0").pack(pady=5)
entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

tk.Button(root, text="Encrypt & Decrypt", command=handle_encrypt, bg="#4CAF50", fg="white").pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, bg="#f0f0f0", fg="blue").pack(pady=10)

root.mainloop()
