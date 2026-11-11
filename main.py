
# Task 5 - Main Cyber Security Program


import security_tools



print("==============================")
print("   CYBER SECURITY UTILITIES")
print("==============================")



password = input("\nEnter a password to validate: ")


if security_tools.validate_password(password):
    print("Password is strong.")
else:
    print("Password is weak.")



ip_address = input("\nEnter an IP address: ")


if security_tools.validate_ip(ip_address):
    print("Valid IP address.")
else:
    print("Invalid IP address.")



print("\nGenerated Strong Password:")
print(security_tools.generate_password())

print("\nThank you for using the Cyber Security Utilities.")
