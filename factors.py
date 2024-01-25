import sys
import time

def factorize_number(number):
    """
    Factorize a number into two smaller numbers: p and q.

    Args:
    - number (int): Number to factorize.

    Returns:
    - tuple: Two factors (p, q) such that p * q = number.
    """
    for i in range(2, number):
        if number % i == 0:
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
