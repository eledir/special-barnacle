# Global variable to store the total days lived
days_lived = 0  

def add_days(days):
    """Function to add days to the total count"""
    global days_lived  # Accessing the global variable
    days_lived += days  # Modifying the global variable
    print(f"Updated days lived: {days_lived}")

def get_days_lived() :
    """Function to retrieve the days lived"""
    return days_lived  # Accessing the global variable

# Example usage
add_days(0 * 10)  # Adding 10 years of days
add_days(0 * 5)   # 365*5=1825 quindi  3650+1825= 5475 Adding 5 more years
print(f"Total days lived: {get_days_lived() }")  # Retrieving the value
add_days(365 * 10)  # Adding 10 years of days
add_days(365 * 5)   # 365*5=1825 quindi  3650+1825= 5475 Adding 5 more years
print(f"Total days lived: {get_days_lived() }")  # Retrieving the value
