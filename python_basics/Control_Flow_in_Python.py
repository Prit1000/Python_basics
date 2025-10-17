for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
'''
1
3
5
7
9
'''
for i in range(10):
     if i == 5:
        continue
     print(i)
print("Outside For Loop")
'''
0
1
2
3
4
6
7
8
9
Outside For Loop
'''
# Count down from 5
count = 5
while count > 0:
    print(count)
    count -= 1
print("Outside While Loop")
'''
5
4
3
2
1
Outside While Loop
'''
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
'''
apple
banana
cherry
'''
# Loop with range
for i in range(10): #[0,1,2,3,4]
     print(i)
'''
0
1
2
3
4
5
6
7
8
9
'''
# Example 1: Checking a condition
num = -50
if num > 0:
    print("Positive Number")
elif num == 0:
     print("Zero")
else:
    print("Negative Number")
'''
Negative Number
'''   
# Example 2: Nested conditions
age = 3
if age > 18:
    if age < 30:
        print("Young Adult")
    else:
        print("Adult")
else:
    print("child")
'''
child
'''




def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def divition(a,b):
    if b != 0:
        return a/b
    else:
        print("division by 0 is not allowed")

while True:
    print("\nMenu")
    print("Press 1 for addition")
    print("Press 2 for substraction")
    print("Press 3 for multiplication")
    print("Press 4 for divition")
    print("Press 5 for exist")
    choice = input("Please give your choice: ")
    if choice == "5":
        print("Exiting programme")
        break
     
    if choice == "1":
        a=float(input("Give your fisrt number: "))
        b=float(input("Give your secound number: "))
        print(f"The answer is: ",addition(a,b))
    elif choice == "2":
        a=float(input("Give your fisrt number: "))
        b=float(input("Give your secound number: "))
        print(f"The answer is: ",substraction(a,b))
    elif choice == "3":
        a=float(input("Give your fisrt number: "))
        b=float(input("Give your secound number: "))
        print(f"The answer is: ",multiplication(a,b))
    elif choice == "4":
        a=float(input("Give your fisrt number: "))
        b=float(input("Give your secound number: "))
        print(f"The answer is: ",divition(a,b))
    else:
        print("Choose from the list")

'''
Menu
Press 1 for addition
Press 2 for substraction
Press 3 for multiplication
Press 4 for divition
Press 5 for exist
Please give your choice: 2
Give your fisrt number: 3
Give your secound number: 6
The answer is:  -3.0

Menu
Press 1 for addition
Press 2 for substraction
Press 3 for multiplication
Press 4 for divition
Press 5 for exist
Please give your choice: 4
Give your fisrt number: 6
Give your secound number: 34
The answer is:  0.17647058823529413

Menu
Press 1 for addition
Press 2 for substraction
Press 3 for multiplication
Press 4 for divition
Press 5 for exist
Please give your choice: 5
Exiting programme
'''

k=[1,2,3,17,8,3]
s=0
for i in k:
    if i > s:
        s=i
print(s)
k=22
s=k
while k!=1:
   k=k-1
   s=s*k
print(s)
'''
17
1124000727777607680000
'''


