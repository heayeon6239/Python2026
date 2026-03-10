num1 = int(input("첫 번째 숫자를 입력하세요:"))
num2 = int(input("두 번째 숫자를 입력하세요:"))

cal1 = num1 + num2
cal2 = num1 - num2
cal3 = num1 * num2
cal4 = float(num1 / num2)

print("-"*50)
print(f"{num1} + {num2} = {cal1}")
print(f"{num1} - {num2} = {cal2}")
print(f"{num1} * {num2} = {cal3}")
print(f"{num1} / {num2} = {cal4}")
print("-"*50)