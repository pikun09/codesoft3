import random
import string

def generate_pass(length=12):
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    all_chars = letters + digits + special_chars

    password = ''.join(random.sample(all_chars, length))
    return password

generated_password = generate_pass(16)
print(f"Generated password: {generated_password}")
