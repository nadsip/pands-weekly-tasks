# bank.py
# author: Nadyarini Sianipar

# read the two amounts in cents from the user
amount1 = int(input("Enter amount1(in cent): "))
amount2 = int(input("Enter amount2(in cent): "))

# Add the two amounts
total_cents = amount1 + amount2

# Convert total cents into euros and cents
euros = total_cents // 100
cents = total_cents % 100

# Print the result in a human-readable format with a euro sign and decimal point
print(f"The sum of these is €{euros}.{cents:02d}")