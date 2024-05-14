import hashlib
import secrets

def hash_and_average(*values):
    # Hash each input value
    hashed_values = [hashlib.sha256(str(val).encode()).hexdigest() for val in values]
    
    # Calculate the average of the hashed values
    total_hash = sum(int(h, 16) for h in hashed_values)
    average_hash = total_hash // len(hashed_values)
    
    # Use the average hash as the seed for random password generation
    secrets.seed(average_hash)
    password = secrets.token_urlsafe(12)  # Adjust the length as needed
    
    return password

def main():
    username = input("Enter your username: ")
    password_category = input("Enter the password category (e.g., email, website): ")
    password = hash_and_average(username, password_category, input("Enter your password: "))
    
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
