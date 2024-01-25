import sys
import time

def is_prime(num):
    """
    Check if a number is prime.

    Args:
    - num (int): Number to check.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorize_number(number):
    """
    Factorize a number into two prime numbers: p and q.

    Args:
    - number (int): Number to factorize.

    Returns:
    - tuple or None: Two prime factors (p, q) such that p * q = number, or None if no factorization is found.
    """
    for i in range(2, number):
        if number % i == 0 and is_prime(i) and is_prime(number // i):
            return i, number // i

    return None

def main(file_path):
    """
    Main function to read numbers from a file, factorize, and print results.

    Args:
    - file_path (str): Path to the file with numbers to factorize.
    """
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for num in numbers:
        result = factorize_number(int(num))
        
        if result:
            print(f"{num}={result[0]}*{result[1]}")
        else:
            print(f"No factorization found for {num}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()
    main(file_path)
    end_time = time.time()

    print("\nTiming Info:")
    print(f"Real Time: {end_time - start_time:.3f} seconds")
