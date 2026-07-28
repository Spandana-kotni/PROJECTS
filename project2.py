#Random password generator
import random
import string

def generate_password(length):
    """
    Generate a password with unique characters.

    Args:
        length (int): The length of the password.

    Returns:
        str: The generated password or None if invalid.
    """

    # Check if length is sufficient
    if length < 4:
        print("Invalid Password: Length must be at least 4")
        return None

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + punctuation

    # Randomly select one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Keep track of used characters for uniqueness
    used_chars = set(password)

    # Fill the rest of the password with unique characters
    while len(password) < length:
        char = random.choice(all_characters)

        if char not in used_chars:
            password.append(char)
            used_chars.add(char)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    # Verify password requirements
    if (
        any(c in lowercase for c in password)
        and any(c in uppercase for c in password)
        and any(c in digits for c in password)
        and any(c in punctuation for c in password)
    ):
        return "".join(password)

    print("Invalid Password: Failed to meet complexity requirements")
    return None


# Example usage
password = generate_password(8)

if password:
    print("Generated Unique Password:", password)
else:
    print("No valid password generated.")