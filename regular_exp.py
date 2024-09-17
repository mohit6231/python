import re

# Example string
text = "Hello, my email is example@example.com"

# Search for an email pattern
match = re.search(r'\w+@\w+\.\w+', text)

if match:
    print("Found email:", match.group())


pattern = r'Hello'
text = "Hello, world!"

# Check if the string starts with the pattern
match = re.match(pattern, text)

if match:
    print("Match found:", match.group())


text = "Contact: john@example.com, jane@company.org"

# Find all email addresses in the text
emails = re.findall(r'\w+@\w+\.\w+', text)
print("Emails found:", emails)


text = "My phone number is 123-456-7890."

# Replace the phone number with a generic placeholder
new_text = re.sub(r'\d{3}-\d{3}-\d{4}', '[PHONE NUMBER]', text)

print(new_text)


# Compile a regular expression pattern
email_pattern = re.compile(r'\w+@\w+\.\w+')

# Use the compiled pattern
text = "Send emails to support@service.com or sales@company.com"
matches = email_pattern.findall(text)

print("Found emails:", matches)

text = "John's email is john.doe@example.com"

# Use groups to extract parts of the email
match = re.search(r'(\w+)\.(\w+)@(\w+\.\w+)', text)

if match:
    print("First Name:", match.group(1))
    print("Last Name:", match.group(2))
    print("Domain:", match.group(3))


def validate_email(email):
    # Regex pattern for a valid email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(pattern, email):
        return True
    else:
        return False


# Test the function
print(validate_email("john.doe@example.com"))  # True
print(validate_email("invalid-email"))         # False


text = "Hello\nhello\nHELLO"

# Search case-insensitively
matches = re.findall(r'hello', text, flags=re.IGNORECASE)

print("Matches:", matches)
