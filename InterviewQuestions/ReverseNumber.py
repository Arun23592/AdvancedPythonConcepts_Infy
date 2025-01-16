def reverse_number(number):
    original_number = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number //= 10
    print("original number: {original_number}")
    print(f"Reversed number: {reverse}")


reverse = 21546
reverse_number(reverse)
