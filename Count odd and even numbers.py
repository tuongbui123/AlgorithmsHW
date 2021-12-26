def count_digits(num):
  if type(num) == int:
    arr = str(num)

    result = {
      'odd': 0,
      'even': 0

    }

    for digit in arr:
      if int(digit) % 2 == 0:
        result['even'] += 1
      else:
        result['odd'] += 1

    return result
  else:
    return False

number = input("Enter a whole number: ")
n = int(number)

print(f"Odd and even numbers in the entered whole number is: {count_digits(n)}")
