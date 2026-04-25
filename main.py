from typing import Generator

class FibonacciGenerator:
    def __init__(self, limit: int) -> None:
        self.limit = limit

    def generate(self) -> Generator[int, None, None]:
        a, b = 0, 1
        count = 0

        while count < self.limit:
            yield a
            a, b = b, a + b
            count += 1


if __name__ == "__main__":
    fib = FibonacciGenerator(10)
    for num in fib.generate():
        print(num)
