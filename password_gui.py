import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import secrets
import string
import math

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Password Generator Pro")
        self.root.geometry("600x700")
        self.root.configure(bg="#2c3e50")
        
        # Character sets
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.ambiguous_chars = "0O1lI|`~"
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg="#2c3e50", padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🔐 Password Generator Pro", 
                              font=("Arial", 18, "bold"), 
                              fg="#ecf0f1", bg="#2c3e50")
        title_label.pack(pady=(0, 20))
        
        # Settings Frame
        settings_frame = tk.LabelFrame(main_frame, text="Password Settings", 
                                     font=("Arial", 12, "bold"),
                                     fg="#ecf0f1", bg="#34495e", 
                                     relief="raised", bd=2)
        settings_frame.pack(fill="x", pady=(0, 20))
        
        # Password Length
        length_frame = tk.Frame(settings_frame, bg="#34495e")
        length_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(length_frame, text="Password Length:", 
                font=("Arial", 10), fg="#ecf0f1", bg="#34495e").pack(side="left")
        
        self.length_var = tk.StringVar(value="16")
        length_spinbox = tk.Spinbox(length_frame, from_=4, to=128, 
                                   textvariable=self.length_var,
                                   width=10, font=("Arial", 10))
        length_spinbox.pack(side="right")
        
        # Character Type Checkboxes
        checkbox_frame = tk.Frame(settings_frame, bg="#34495e")
        checkbox_frame.pack(fill="x", padx=10, pady=10)
        
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_lowercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)
        self.exclude_ambiguous = tk.BooleanVar(value=False)
        
        checkboxes = [
            ("Include Uppercase (A-Z)", self.include_uppercase),
            ("Include Lowercase (a-z)", self.include_lowercase),
            ("Include Numbers (0-9)", self.include_digits),
            ("Include Special (!@#$%)", self.include_special),
            ("Exclude Ambiguous (0,O,1,l)", self.exclude_ambiguous)
        ]
        
        for i, (text, var) in enumerate(checkboxes):
            row = i // 2
            col = i % 2
            
            if row >= len(checkbox_frame.grid_slaves()):
                checkbox_row = tk.Frame(checkbox_frame, bg="#34495e")
                checkbox_row.grid(row=row, column=0, columnspan=2, sticky="w", pady=2)
            else:
                checkbox_row = checkbox_frame.grid_slaves(row=row)[0]
            
            cb = tk.Checkbutton(checkbox_row, text=text, variable=var,
                               fg="#ecf0f1", bg="#34495e", 
                               selectcolor="#3498db",
                               font=("Arial", 9))
            cb.pack(side="left" if col == 0 else "right", padx=(0, 20))
        
        # Number of Passwords
        count_frame = tk.Frame(settings_frame, bg="#34495e")
        count_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(count_frame, text="Number of Passwords:", 
                font=("Arial", 10), fg="#ecf0f1", bg="#34495e").pack(side="left")
        
        self.count_var = tk.StringVar(value="5")
        count_spinbox = tk.Spinbox(count_frame, from_=1, to=20, 
                                  textvariable=self.count_var,
                                  width=10, font=("Arial", 10))
        count_spinbox.pack(side="right")
        
        # Generate Button
        generate_btn = tk.Button(main_frame, text="🔑 Generate Passwords", 
                               command=self.generate_passwords,
                               font=("Arial", 14, "bold"),
                               bg="#e74c3c", fg="#000000",
                               relief="raised", bd=4,
                               padx=25, pady=12,
                               activebackground="#c0392b", activeforeground="#000000")
        generate_btn.pack(pady=10)
        
        # Results Frame
        results_frame = tk.LabelFrame(main_frame, text="Generated Passwords", 
                                    font=("Arial", 12, "bold"),
                                    fg="#ecf0f1", bg="#34495e",
                                    relief="raised", bd=2)
        results_frame.pack(fill="both", expand=True, pady=(10, 0))
        
        # Password Display
        self.password_display = scrolledtext.ScrolledText(results_frame, 
                                                         height=12,
                                                         font=("Courier", 11),
                                                         bg="#ecf0f1", fg="#2c3e50",
                                                         wrap=tk.WORD)
        self.password_display.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Copy Button
        copy_frame = tk.Frame(results_frame, bg="#34495e")
        copy_frame.pack(fill="x", padx=10, pady=(0, 10))
        
        copy_btn = tk.Button(copy_frame, text="📋 Copy Selected Password", 
                           command=self.copy_selected,
                           font=("Arial", 10),
                           bg="#3498db", fg="white",
                           relief="raised", bd=2)
        copy_btn.pack(side="left")
        
        clear_btn = tk.Button(copy_frame, text="🗑️ Clear Results", 
                            command=self.clear_results,
                            font=("Arial", 10),
                            bg="#95a5a6", fg="white",
                            relief="raised", bd=2)
        clear_btn.pack(side="right")
        
    def generate_password(self, length, include_uppercase=True, include_lowercase=True, 
                         include_digits=True, include_special=True, exclude_ambiguous=False):
        """Generate a secure password with specified requirements."""
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
            
        # Build character set
        char_set = ""
        required_chars = []
        
        if include_lowercase:
            chars = self.lowercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous_chars)
            char_set += chars
            required_chars.append(secrets.choice(chars))
            
        if include_uppercase:
            chars = self.uppercase
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous_chars)
            char_set += chars
            required_chars.append(secrets.choice(chars))
            
        if include_digits:
            chars = self.digits
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous_chars)
            char_set += chars
            required_chars.append(secrets.choice(chars))
                
        if include_special:
            chars = self.special_chars
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous_chars)
            char_set += chars
            required_chars.append(secrets.choice(chars))
        
        if not char_set:
            raise ValueError("At least one character type must be included")
            
        if len(required_chars) > length:
            raise ValueError(f"Cannot meet requirements with length {length}")
        
        # Generate remaining characters randomly
        remaining_length = length - len(required_chars)
        random_chars = [secrets.choice(char_set) for _ in range(remaining_length)]
        
        # Combine and shuffle
        all_chars = required_chars + random_chars
        password_list = list(all_chars)
        
        # Shuffle to avoid predictable patterns
        for i in range(len(password_list)):
            j = secrets.randbelow(len(password_list))
            password_list[i], password_list[j] = password_list[j], password_list[i]
            
        return ''.join(password_list)
    
    def calculate_entropy(self, password):
        """Calculate password entropy in bits."""
        charset_size = 0
        if any(c in self.lowercase for c in password):
            charset_size += 26
        if any(c in self.uppercase for c in password):
            charset_size += 26
        if any(c in self.digits for c in password):
            charset_size += 10
        if any(c in self.special_chars for c in password):
            charset_size += len(self.special_chars)
            
        return len(password) * math.log2(charset_size) if charset_size > 0 else 0
    
    def generate_passwords(self):
        try:
            # Get settings
            length = int(self.length_var.get())
            count = int(self.count_var.get())
            
            # Validate at least one character type is selected
            if not any([self.include_uppercase.get(), self.include_lowercase.get(),
                       self.include_digits.get(), self.include_special.get()]):
                messagebox.showerror("Error", "Please select at least one character type!")
                return
            
            # Clear previous results
            self.password_display.delete(1.0, tk.END)
            
            # Generate passwords
            results = []
            results.append("🔐 GENERATED PASSWORDS 🔐")
            results.append("=" * 50)
            results.append("")
            
            for i in range(count):
                password = self.generate_password(
                    length=length,
                    include_uppercase=self.include_uppercase.get(),
                    include_lowercase=self.include_lowercase.get(),
                    include_digits=self.include_digits.get(),
                    include_special=self.include_special.get(),
                    exclude_ambiguous=self.exclude_ambiguous.get()
                )
                
                entropy = self.calculate_entropy(password)
                results.append(f"{i+1:2d}. {password}")
                
            # Add analysis for first password
            first_password = self.generate_password(
                length=length,
                include_uppercase=self.include_uppercase.get(),
                include_lowercase=self.include_lowercase.get(),
                include_digits=self.include_digits.get(),
                include_special=self.include_special.get(),
                exclude_ambiguous=self.exclude_ambiguous.get()
            )
            entropy = self.calculate_entropy(first_password)
            
            results.append("")
            results.append("📊 STRENGTH ANALYSIS")
            results.append("-" * 30)
            results.append(f"Length: {length} characters")
            results.append(f"Entropy: {entropy:.1f} bits")
            results.append(f"Estimated attempts to crack: {2**(entropy-1):,.0f}")
            
            # Display results
            self.password_display.insert(tk.END, "\n".join(results))
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
    
    def copy_selected(self):
        """Copy selected password to clipboard."""
        try:
            selected_text = self.password_display.get(tk.SEL_FIRST, tk.SEL_LAST)
            if selected_text:
                self.root.clipboard_clear()
                self.root.clipboard_append(selected_text)
                messagebox.showinfo("Success", "Selected text copied to clipboard!")
            else:
                messagebox.showwarning("Warning", "Please select text to copy!")
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select text to copy!")
    
    def clear_results(self):
        """Clear the password display."""
        self.password_display.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()