# Get the time string from user input
time_str = input("Enter a time string in the format DD:HH:MM: ")

# Split the time string into days, hours, and minutes
days, hours, minutes = time_str.split(":")

# Convert the days, hours, and minutes to integers
days = int(days)
hours = int(hours)
minutes = int(minutes)

# Calculate the total number of minutes
total_minutes = days * 24 * 60 + hours * 60 + minutes

# Print the total number of minutes
print(f"Total minutes: {total_minutes}")
 