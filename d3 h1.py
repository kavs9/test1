def is_perfect_number(number):
    divisors_sum = 1  
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:  
                divisors_sum += number // i
    return divisors_sum == number
def print_perfect_numbers_in_range(start, end):
    for num in range(start, end + 1):
        if is_perfect_number(num):
            print(f"Perfect number: {num}")
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))
print_perfect_numbers_in_range(start_range,end_range)
