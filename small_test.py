def hello_world() -> str:
    return "Hello, world!"

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Factorial of {number} is {factorial(number)}")

