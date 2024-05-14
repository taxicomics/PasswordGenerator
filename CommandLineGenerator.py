import hashlib
import random
import string

def hash_and_average(*values):
    # Hash each input value
    hashed_values = [hashlib.sha256(str(val).encode()).hexdigest() for val in values]
    
    # Calculate the average of the hashed values
    total_hash = sum(int(h, 16) for h in hashed_values)
    average_hash = total_hash // len(hashed_values)
    
    # Use the average hash as the seed for random password generation
    random.seed(average_hash)
    
    # Generate a random password
    password_length = 24  # Adjust the length as needed
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(password_length))
    
    return password

def main():
    username = input("Enter your username: ")
    password_category = input("Enter the password category (e.g., email, website): ")
    password = hash_and_average(username, password_category, input("Enter your password: "))
    
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
