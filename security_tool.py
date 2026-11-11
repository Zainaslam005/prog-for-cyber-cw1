
# Task 1 - Security Tool



correct_username = "admin"
correct_password = "Cyber123!"



def security_event_counter():

    correct_count = 0
    incorrect_count = 0

    
    for attempt in range(10):

        entered_password = input("Enter password: ")

        if entered_password == correct_password:
            correct_count += 1
        else:
            incorrect_count += 1

    
    incorrect_percentage = (incorrect_count / 10) * 100

    print("\nSecurity Event Results")
    print("Correct passwords:", correct_count)
    print("Incorrect passwords:", incorrect_count)
    print("Incorrect percentage:", incorrect_percentage, "%")

    
    if incorrect_percentage > 50:
        print("ALERT: High number of incorrect passwords!")
    else:
        print("No security alert.")



def brute_force_simulation():

    predefined_password = "Secure123!"
    maximum_attempts = 5
    attempts = 0

    
    while attempts < maximum_attempts:

        guess = input("Guess the password: ")
        attempts += 1

        if guess == predefined_password:
            print("Password found!")
            print("Attempts used:", attempts)
            break
        else:
            print("Incorrect password.")
     
    if attempts == maximum_attempts and guess != predefined_password:
        print("Maximum attempts reached!")
        print("Brute-force simulation stopped.")
            
            



def login_authentication():

    failed_attempts = 0
    maximum_attempts = 3

    
    while failed_attempts < maximum_attempts:

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login successful!")
            break

        else:
            failed_attempts += 1
            print("Login failed!")
            print("Failed attempts:", failed_attempts)

    
    if failed_attempts == maximum_attempts:
        print("Account frozen for 24 hours.")


   



print("========================")
print("     SECURITY TOOL")
print("========================")

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:

    print("\nAuthentication successful!")
    print("Welcome to the Security Tool.")

    
    while True:

        print("\n====== SECURITY MENU ======")
        print("1. Security Event Counter")
        print("2. Brute-Force Simulation")
        print("3. Login Authentication")
        print("4. Exit")

        try:
            choice = int(input("Select an option: "))

            if choice == 1:
                security_event_counter()

            elif choice == 2:
                brute_force_simulation()

            elif choice == 3:
                login_authentication()

            elif choice == 4:
                print("Thank you for using the security tool.")
                break

            else:
                print("Invalid option. Please select 1-4.")

        except ValueError:
            print("Please enter a number.")

else:
    print("\nAuthentication failed!")
    print("Access denied.")
