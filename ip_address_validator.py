
# Task 3 - IP Address Validator




def validate_ip(ip_address):

    
    ip_address = ip_address.strip()

    
    if ip_address.count(".") != 3:
        return False

    
    parts = ip_address.split(".")

    
    if len(parts) != 4:
        return False

    
    for part in parts:

        
        if not part.isdigit():
            return False

        
        number = int(part)

        
        if number < 0 or number > 255:
            return False

    return True



print("================================")
print("      IP ADDRESS VALIDATOR")
print("================================")

ip = input("Enter an IP address: ")

if validate_ip(ip):
    print("Valid IP address.")
else:
    print("Invalid IP address.")
