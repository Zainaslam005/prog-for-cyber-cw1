
# Task 2 - Security Event Logger

from datetime import datetime


correct_username = "admin"
correct_password = "Cyber123!"


ip_address = "192.168.1.25"


event_id = 3971


while True:

    username = input("\nEnter username: ")
    password = input("Enter password: ")

    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
    if username == correct_username and password == correct_password:

        event = "Successful login"

    else:

        event = "Failed login"

    
    print("\n========== SECURITY EVENT LOG ==========")
    print("Event ID:", event_id)
    print("Username:", username)
    print("IP Address:", ip_address)
    print("Event:", event)
    print("Timestamp:", timestamp)
    print("========================================")

    
    event_id += 1

    
    if event == "Successful login":

        print("\nAuthentication successful!")
        print("Access granted.")
        break

    else:

        print("\nAuthentication failed. Please try again.")
