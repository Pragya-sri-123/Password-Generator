import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Label for instructions
        self.label = tk.Label(self.root, text="Select password criteria", font=("Arial", 14))
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Length input
        self.length_label = tk.Label(self.root, text="Password Length:", font=("Arial", 10))
        self.length_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.length_entry = tk.Entry(self.root, width=10, font=("Arial", 12))
        self.length_entry.grid(row=1, column=1, padx=10, pady=5)

        # Checkbox options for including different characters
        self.lowercase_var = tk.BooleanVar(value=True)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)

        self.lowercase_check = tk.Checkbutton(self.root, text="Include Lowercase", variable=self.lowercase_var, font=("Arial", 10))
        self.lowercase_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.uppercase_check = tk.Checkbutton(self.root, text="Include Uppercase", variable=self.uppercase_var, font=("Arial", 10))
        self.uppercase_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.digits_check = tk.Checkbutton(self.root, text="Include Digits", variable=self.digits_var, font=("Arial", 10))
        self.digits_check.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.special_check = tk.Checkbutton(self.root, text="Include Special Characters", variable=self.special_var, font=("Arial", 10))
        self.special_check.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        # Generate Password Button
        self.generate_button = tk.Button(self.root, text="Generate Password", width=20, font=("Arial", 12), command=self.generate_password)
        self.generate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

        # Display Generated Password
        self.password_label = tk.Label(self.root, text="Generated Password:", font=("Arial", 12))
        self.password_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        
        self.password_display = tk.Entry(self.root, width=30, font=("Arial", 12), state="readonly")
        self.password_display.grid(row=7, column=1, padx=10, pady=10)

    def generate_password(self):
        # Get the password length from the entry field
        try:
            length = int(self.length_entry.get())
        except ValueError:
            self.password_display.config(state="normal")
            self.password_display.delete(0, tk.END)
            self.password_display.insert(tk.END, "Enter a valid length!")
            self.password_display.config(state="readonly")
            return

        # Character sets
        characters = ""
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.digits_var.get():
            characters += string.digits
        if self.special_var.get():
            characters += string.punctuation

        # If no characters selected, show an error
        if not characters:
            self.password_display.config(state="normal")
            self.password_display.delete(0, tk.END)
            self.password_display.insert(tk.END, "Select at least one character type!")
            self.password_display.config(state="readonly")
            return

        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the generated password
        self.password_display.config(state="normal")
        self.password_display.delete(0, tk.END)
        self.password_display.insert(tk.END, password)
        self.password_display.config(state="readonly")

# Create the main window
root = tk.Tk()

# Initialize the PasswordGenerator app
app = PasswordGenerator(root)

# Run the application
root.mainloop()
