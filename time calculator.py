def calculate_minutes(time_str):
    # Split the time string into days, hours, and minutes
    days, hours, minutes = map(int, time_str.split(":"))

    # Calculate the total number of minutes
    total_minutes = days * 24 * 60 + hours * 60 + minutes

    return total_minutes

# Example usage:
time_str = "10:12:30"
total_minutes = calculate_minutes(time_str)
print(f"Total minutes: {total_minutes}")
