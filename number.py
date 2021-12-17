from num import plates_list

var_1 = plates_list
x = input("Please,enter your number : ")

print('your number is ', (var_1.index(x.upper())), "on the list")

number = x[2:6]
a = int(x[2])
b = int(x[3])
c = int(x[4])
d = int(x[5])
e = a + b + c + d
print('sum of numbers', e)

x = set(plates_list)

print(f"in th   e list", {len(x)}, "unique number")