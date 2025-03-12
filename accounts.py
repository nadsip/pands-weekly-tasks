# accounts.py

def mask_account(account):
    """
    Masks all characters except the last 4 with 'X's.
    Assumes:
    1. Account numbers should have ≥4 characters
    2. Non-numeric characters are allowed in input
    3. Preserves original character type (letters/digits)
    """
    if len(account) < 4:
        return "Error: Account number must have at least 4 characters"
    return 'X' * (len(account) - 4) + account[-4:]

def main():
    account = input("Please enter an 10 digit account number: ").strip()
    print(mask_account(account))

if __name__ == "__main__":
    main()