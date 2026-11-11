
# Task 4 - Security Incident Manager



incident = {
    "username": "admin",
    "ip_address": "192.168.1.25",
    "event_type": "Failed login",
    "risk_level": "High"
}


print("SECURITY INCIDENT DETAILS")
print("Username:", incident["username"])
print("IP Address:", incident["ip_address"])


incident["status"] = "Under Investigation"


incident["risk_level"] = "Critical"


del incident["event_type"]


print("\nUPDATED INCIDENT DETAILS")

for key, value in incident.items():
    print(key, ":", value)


print("\nTotal number of key-value pairs:", len(incident))
