# weekday.py
#
# Author: Nadyarini Sianipar

from datetime import datetime

# Get the day of the week
day = datetime.today().weekday()

if day < 5: # 0-4 Monday-Friday
    print("Yes, unfortunately today is a weekday.")
else: 
    print("It is the weekend, yay!")