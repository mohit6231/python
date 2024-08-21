from datetime import datetime

# Get the current date and time
current_timestamp = datetime.now()

print("Current Timestamp:", current_timestamp)

# Convert the timestamp to a formatted string
formatted_timestamp = current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

print("Formatted Timestamp:", formatted_timestamp)

# Define a date and time string
date_string = "2024-08-14 12:45:32"

# Convert the string into a datetime object
parsed_timestamp = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

print("Parsed Timestamp:", parsed_timestamp)

# Get the current date and time
current_timestamp = datetime.now()

# Convert the datetime object to a Unix timestamp
unix_timestamp = current_timestamp.timestamp()

print("Unix Timestamp:", unix_timestamp)
