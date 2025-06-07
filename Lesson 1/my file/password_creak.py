import itertools
import string

def brute_force_cracker(target_password, max_length=4):
    characters = string.ascii_lowercase + string.digits
    attempts = 0

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess_password = ''.join(guess)
            if guess_password == target_password:
                print(f"[+] Password found: {guess_password} in {attempts} attempts")
                return guess_password

    print("[Oh pass was not found !!!] Password not found.")
    return None

# Example usage
target = "User001"
brute_force_cracker(target, max_length=4)
