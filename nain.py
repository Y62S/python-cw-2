my_name = input("what is your name?")
my_age = input("how old are you?")
print(f"my name is {my_name} and i am {my_age} years old")

first_number= int(input("num1"))
secound_number= int(input("num2"))
operation= input ("enter operation")
if operation == "+":
  print(first_number + secound_number)
elif operation == "-":
  print(first_number - secound_number)
elif operation == "*":
  print(first_number * secound_number)
elif operation == "/":
  print(first_number / secound_number)
else: 
  print("the operation is not valid")

bus_capacity = 20
bus_riders= int(input("people in bus"))
bus_waiting= int(input("wants to ride"))
empty_seats=(bus_capacity - bus_riders)
print(empty_seats)
if empty_seats > bus_waiting:
  print(f"there are empty seats{empty_seats}")
elif empty_seats<= bus_waiting:
  print("the bus if full")
