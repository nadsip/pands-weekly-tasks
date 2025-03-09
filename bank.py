# bank.py

# Prompt the user to enter the first amount in cents
amount1 = int(input("Enter amount1 (in cent): "))

# Prompt the user to enter the second amount in cents
amount2 = int(input("Enter amount2 (in cent): "))

# Add the two amounts together
total_cents = amount1 + amount2

# Convert the total amount from cents to euros and cents
total_euros = total_cents // 100  # Get the euro part
total_remaining_cents = total_cents % 100  # Get the remaining cents

# Print the result in a human-readable format with a euro sign and decimal point
print(f"The sum of these is €{total_euros}.{total_remaining_cents:02d}")