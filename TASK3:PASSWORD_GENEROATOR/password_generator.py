import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        

        self.root.geometry("200x200")
        
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()
        
        self.length_label = tk.Label(root, text="Length of Password:")
        self.length_label.pack()
        
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()
        
        self.generated_password_label = tk.Label(root, text="")
        self.generated_password_label.pack()
        
        self.accept_button = tk.Button(root, text="Accept", command=self.accept_password, state=tk.DISABLED)
        self.accept_button.pack()
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack()
        
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                messagebox.showerror("Error", "Please enter a valid length greater than 0.")
                return
            
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            
            self.generated_password_label.config(text="Generated Password: " + password)
            self.accept_button.config(state=tk.NORMAL)
        
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
    
    def accept_password(self):
        username = self.username_entry.get()
        password = self.generated_password_label.cget("text").split(": ")[1]
        
        messagebox.showinfo("Password Accepted", f"Username: {username}\nPassword: {password}\nPassword set successfully!")
        
    def reset(self):
        self.username_entry.delete(0, tk.END)
        self.length_entry.delete(0, tk.END)
        self.generated_password_label.config(text="")
        self.accept_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
