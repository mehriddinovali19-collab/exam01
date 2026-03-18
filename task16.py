age = int(input("Please, enter your age: "))
if age <7:
    print(f'Your age: {age}, You have 50% discount')
elif 7 <= age < 17:
    print(f'Your age: {age}, You have 20% discount')
elif age > 60:
    print(f'Your age: {age}, You have 30% discount')
else:
    print("Please, pay fully!")