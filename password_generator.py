import os
import secrets
import string
from typing import List, Optional

class PasswordGenerator:
    def __init__(self):
        # Character sets
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        self.ambiguous_chars = "0O1lI|`~"  # Characters that might be confused
        
    def generate_password(self, 
                         length: int, 
                         include_uppercase: bool = True,
                         include_lowercase: bool = True, 
                         include_digits: bool = True,
                         include_special: bool = True,
                         exclude_ambiguous: bool = False,
                         min_special: int = 1,
                         min_digits: int = 1) -> str:
        """
        Generate a secure password with specified requirements.
        
        Args:
            length: Password length
            include_uppercase: Include uppercase letters
            include_lowercase: Include lowercase letters  
            include_digits: Include numbers
            include_special: Include special characters
            exclude_ambiguous: Exclude confusing characters (0,O,1,l,I,|)
            min_special: Minimum number of special characters
            min_digits: Minimum number of digits
        """
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
            # Add required number of digits
            for _ in range(min_digits):
                required_chars.append(secrets.choice(chars))
                
        if include_special:
            chars = self.special_chars
            if exclude_ambiguous:
                chars = ''.join(c for c in chars if c not in self.ambiguous_chars)
            char_set += chars
            # Add required number of special characters
            for _ in range(min_special):
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
    
    def check_password_strength(self, password: str) -> dict:
        """Analyze password strength and return metrics."""
        analysis = {
            'length': len(password),
            'has_lowercase': any(c in self.lowercase for c in password),
            'has_uppercase': any(c in self.uppercase for c in password),
            'has_digits': any(c in self.digits for c in password),
            'has_special': any(c in self.special_chars for c in password),
            'has_ambiguous': any(c in self.ambiguous_chars for c in password),
        }
        
        # Calculate character set size
        charset_size = 0
        if analysis['has_lowercase']: charset_size += 26
        if analysis['has_uppercase']: charset_size += 26
        if analysis['has_digits']: charset_size += 10
        if analysis['has_special']: charset_size += len(self.special_chars)
        
        # Estimate entropy (bits)
        import math
        analysis['entropy_bits'] = len(password) * math.log2(charset_size) if charset_size > 0 else 0
        analysis['charset_size'] = charset_size
        
        return analysis

def get_valid_input(prompt: str, min_val: int = 1, max_val: int = 128) -> int:
    """Get valid integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid number")

def get_yes_no(prompt: str) -> bool:
    """Get yes/no input from user."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes', '1', 'true']:
            return True
        elif response in ['n', 'no', '0', 'false']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no")

def main():
    print("🔐 Enhanced Password Generator")
    print("=" * 40)
    
    generator = PasswordGenerator()
    
    # Get user preferences once
    print("\nPassword Requirements:")
    length = get_valid_input("Password length (4-128): ", 4, 128)
    
    print("\nCharacter Types:")
    include_uppercase = get_yes_no("Include uppercase letters? (y/n): ")
    include_lowercase = get_yes_no("Include lowercase letters? (y/n): ")
    include_digits = get_yes_no("Include numbers? (y/n): ")
    include_special = get_yes_no("Include special characters? (y/n): ")
    exclude_ambiguous = get_yes_no("Exclude ambiguous characters (0,O,1,l,I,|)? (y/n): ")
    
    # Ensure at least one character type is selected
    if not any([include_uppercase, include_lowercase, include_digits, include_special]):
        print("⚠️  At least one character type must be selected. Enabling all types.")
        include_uppercase = include_lowercase = include_digits = include_special = True
    
    while True:
        print(f"\n🎯 Generated Passwords (Length: {length}):")
        print("-" * 50)
        
        try:
            # Generate passwords
            passwords = []
            for i in range(5):
                password = generator.generate_password(
                    length=length,
                    include_uppercase=include_uppercase,
                    include_lowercase=include_lowercase,
                    include_digits=include_digits,
                    include_special=include_special,
                    exclude_ambiguous=exclude_ambiguous
                )
                passwords.append(password)
                print(f"{i+1:2d}. {password}")
            
            # Show strength analysis for first password
            analysis = generator.check_password_strength(passwords[0])
            print(f"\n📊 Strength Analysis (Password #1):")
            print(f"   • Entropy: {analysis['entropy_bits']:.1f} bits")
            print(f"   • Character set size: {analysis['charset_size']}")
            print(f"   • Estimated time to crack: {2**(analysis['entropy_bits']-1):,.0f} attempts")
                
        except ValueError as e:
            print(f"❌ Error: {e}")
            continue
        
        # Ask for more passwords
        if not get_yes_no("\nGenerate more passwords? (y/n): "):
            break
    
    print("\n👋 Thanks for using the Enhanced Password Generator!")
    print("💡 Remember to store your passwords securely!")

if __name__ == "__main__":
    main()
