import datetime

print("DATE")

# Create a date object
date = datetime.date(2000, 1, 23)
print(date)

# Format a date
print(date.strftime("%B %d, %Y"))  # January 23, 2000
