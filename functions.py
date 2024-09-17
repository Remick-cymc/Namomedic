#function  to generate random numbers
# 6 random numbers 124978

# def number_generate():
#     import random
#     #import string 
   
#     print(random.randint(100000,999999))






#lowercase letters
# import random
# import string
# def lowercase():
#     print("".join(random.choice(string.ascii_lowercase for x in range(6)))  )

# lowercase()
    
# funtion to check password validity
#lower case
#uppercase
# a digit
#special character

import re

def checkpassword(password):
    # Check for lowercase letters
    haslowercase = re.search(r'[a-z]', password)
    # Check for uppercase letters
    hasuppercase = re.search(r'[A-Z]', password)
    # Check for digits
    hasdigit = re.search(r'\d', password)
    # Check for special characters
    hasspecial = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)  # Added more special characters

    if len(password) < 8:
        return "Your password is too short"
    elif not haslowercase:
        return "Password must contain at least one lowercase letter"
    elif not hasuppercase:
        return "Password must contain at least one uppercase letter"
    elif not hasdigit:
        return "Password must contain at least one digit"
    elif not hasspecial:
        return "Password must contain at least one special character"
    else:
        return True

# Test the function
checkpassword("123abc@eeA")       # Test with a password that fails multiple criteria
# checkpassword("Password1!")       # Test with a strong password
# checkpassword("short")            # Test with a too short password
# checkpassword("NOdigits!")        # Test with missing digits
# checkpassword("nodigits")         # Test with missing digits and special characters


#check phone validity format
#0712345678
#+25412345678
    
import re

def checkphone(phone):
    # Corrected regular expression pattern
    pattern = r"^(07\d{8}|\+254\d{9})$"
    if re.match(pattern, phone):
        print("Valid phone")
        return True
    else:
        print("Not valid")
        return False

# Test the function
# checkphone("712345678")
checkphone("+254712345678")
# checkphone("1234567890")  # Example of an invalid number
#how to hash passwords 
import bcrypt
def hash_password(password):
    # password = b"my secret password"
    # hash_password = bcrypt.hashpw(password,bcrypt.gensalt())
    # print(f("hashed password:{hashed password}"))
    bytes = password.encode("utf-8")
    # print(bytes)
    salt = bcrypt.gensalt()
    # print(salt)
    hash = bcrypt.hashpw(bytes, salt)
    # print(hash)
    return hash.decode()

# hash_password("Olioks@2003")

# hash verify
def hash_verify(originalpassword, hashedpassword):
    bytes = originalpassword.encode("utf-8")
    result = bcrypt.checkpw(bytes, hashedpassword.encode())
    # print(result)
    return result

# hash_verify
# ("Olioks@2003","$2b$12$Fjn7wMOXqY1Ph3suGD5nhOLBqmZjE8Q.NpObKCipMoZkEusExKgnu")
  
#sending sms


import africastalking

africastalking.initialize(

 username="joe2022",

 api_key="aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a"

 # justpaste.it/1nua8 

)

sms = africastalking.SMS

def send_sms(phone, message):
    recipients = [phone]
    sender = "ARICASTALKING"
    response = sms.send(message,recipients )
    print (response)
# send_sms("+254769191897","Thank you for regestration")
# Encryption 
from cryptography.fernet import Fernet
def gen_key():
    key = Fernet.generate_key()
    # print(key)
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# gen_key()
        
# load key
def load_key():
    return open("key.key","rb").read()

# Encription 
def encrypt(data):
    key = load_key()
    # print(key)
    f = Fernet(key)
    # print(f)
    encrypted_data = f.encrypt(data.encode())
    print (encrypted_data.decode)
    return encrypted_data.decode()

# encrypt("this is my data")

# decrypt data
def decrypt (encrypted_data):
    key = load_key()
    f =Fernet(key)

    decrypt_data = f.decrypt(encrypted_data.encode())
    print(decrypt_data)
    return decrypt_data.decode()

# decrypt ("gAAAAABm4tKphlKMDbISH57rGSt3ZylfIaWx7HkAq1_vGOlvbvnbRosCD4jltTcDzhNH4LArAizsmzyRpuv3JYQ9-_UO61XL5w==")

