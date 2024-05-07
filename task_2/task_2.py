from typing import Callable
import re

def generator_numbers(text: str):
    for n in re.findall(r'(\d+\.\d+)', text):
        yield n

def sum_profit(text: str, func: Callable):
    sum = 0
    for profit in func(text):
        sum += float(profit)
    return sum

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == '__main__':
    main()