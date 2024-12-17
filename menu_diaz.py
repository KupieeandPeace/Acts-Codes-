# Activity 1
print("Hello World")
print("\n" + "*" * 50 + "\n")

# Activity 2
name = input("Hi! What's your name? ")
age = input("How old are you? ")
email = input("What is your email address? ")
print("Hi, " + name + "!")
print("You are " + age + " years old.")
print("Your email address is: " + email)
print("Your name has " + str(len(name)) + " characters.")
num1 = eval(input("Please input a number: "))
num2 = eval(input("Please input another number: "))
print(num1, "divided by", num2, "is", num1 / num2)
print("\n" + "*" * 50 + "\n")

# Activity 3
name = input("Please enter your name: ")
add = input("Please enter your address: ")
age = eval(input("Enter your age: "))
print(f"Hi {name}! You live in {add}, and you are {age} years old.")
print("\n" + "*" * 50 + "\n")


# Activity 4
fah = float(input("Please enter the temperature in FAHRENHEIT: "))  # Convert input to float
c = (fah - 32) * (5/9)
print(f"{fah} degrees Fahrenheit converted to Celsius is {round(c, 2)} degrees.")
print("\n" + "*" * 50 + "\n")


# Activity 5
x = 10
print(x)
x += 5
print(x)
x -= 15
print(x)
x *= 24
print(x)
x /= 23
print(x)
print("\n" + "*" * 50 + "\n")

# Activity 6
passcode = "Mamamo23"
mypass = input("Enter the password: ")
if mypass.lower() == passcode:
    print("ACCESS GRANTED BOSSING")
    print("YOU CAN NOW USE THE SYSTEM")
elif mypass.lower() == "hehehe":
    print("ACCESS GRANTED NA BOSSING")
    print("YOU CAN NOW USE THE SYSTEM")
else:
    print("ACCESS DENIED™")
    print("TRY HARDER")
print("\n" + "*" * 50 + "\n")

# Activity 7
print("__-DLL Scholarship Grant Application System---")
name = input("Hi! Please input your name: ")
enrolled = input("Are you currently enrolled here in DLL? (yes/no): ")
if enrolled.lower() == "yes":
    print(f"Hi! {name}, welcome to the DLL Scholarship Grant Application System.")
    age = eval(input("Please enter your age: "))
    if age >= 18 and age <= 35:
        print("Your age has complied with the age restrictions.")
        grades = eval(input("Please enter your GWA: "))
        if grades >= 86 and grades <= 100:
            print("Your GWA has complied with the GWA requirement.")
            is4ps = input("Is your family currently enrolled/subscribed to the 4Ps Program? (yes/no): ")
            if is4ps.lower() == "yes":
                print("Congratulations, you are now granted a scholarship. Goodluck sa pag aaral!!.")
            else:
                print("Sorry, this scholarship is for 4Ps beneficiaries only. takaw mo Hahahaha.")
        else:
            print("Sorry, you did not pass the GWA requirement.")
    else:
        print("Sorry, you have exceeded the age limit.")
else:
    print("Thank you For using my System")
           
print("\n" + "*" * 50 + "\n")

# Activity 8
for num in range(1, 11):
    print(num, 'Hello World')
name = input('Please enter your name: ')
print(f'Hello {name}!')
print("\n" + "*" * 50 + "\n")

# Activity 9
start = eval(input("Please enter a number: "))
limit = 0
factorial = 1
for x in range(start, limit, -1):
    factorial *= x
    print(x)
print(f"The factorial of {start} is: {factorial}")
print("\n" + "*" * 50 + "\n")

# Activity 10
for x in range(1, 11):
    for y in range(1, x + 1):
        print("*", end=" ")
    print()
print("\n" + "*" * 50 + "\n")

# Activity 11
for c in range(1, 11):
    print(c, end="*")
    for p in range(1, c):
        print("*", end=" ")
    print()
print("\n" + "*" * 50 + "\n")

# Activity 12
for a in range(1, 6):
    for b in range(1, a + 1):
        print(" ", end=" ")
    for c in range(6, a, -1):
        print("*", end=" ")
    for a in range(6, a, -1):
        print("*", end=" ")
    print()
print("\n" + "*" * 50 + "\n")

# Activity 13
hi = eval(input('Enter a number form 1 to 10: '))
for e in range(1, 11):
    for f in range(1, hi):
        print(e * f, end=" ")
    print()
no = eval(input('Enter a number---> '))
for e in range(1, 11):
    for f in range(1, no + 1):
        print(f'{e} × {f} = {e * f}', end=" ")
    print()
print("\n" + "*" * 50 + "\n")

# Activity 14
no = eval(input('Enter a number: '))
for x in range(1, 6):
    for i in range(1, no + 1):
        for y in range(1, x + 1):
            print("*", end=" ")
    for z in range(6, x, -1):
        print(" ", end=" ")
    print()
print("\n" + "*" * 50 + "\n")

# Activity 15
Repeat = True
Nt = 0  # Initialize Nt here, so it starts at 0

while Repeat:
    var = input('Do you wish to add more triangles? (yes/no): ')

    if var.lower() == 'no':
        print('Loop has been stopped')
        break  

    elif var.lower() == "yes":
        Nt += 1  
        for x in range(1, 6):  
            for y in range(1, Nt + 1):  
                for z in range(1, x + 1):  
                    print("*", end="   ")

            
                for q in range(6, x, -1):  
                    print("  ", end="  ")

                print()  
    else:
        print("Input not accepted")
        print("Please only enter 'yes' or 'no'.")
print("\n" + "*" * 50 + "\n")

# Activity 16
Repeat = True
sum = 0
while Repeat:
    num = eval(input("Enter a number: "))
    if num == 0:
        print("Loop Terminated!")
        break
        Repeat = False
    else:
        sum += num
        print(f"The sum of all numbers is {sum}")
print("\n" + "*" * 50 + "\n")

# Activity 17
def greetings():
    print(f"Hello there {name}, I hope you're having a wonderful day!")

def right_triangle():
    for x in range(1, 6):
        for y in range(1, x + 1):
            print("*", end=" ")
        for z in range(6, x, -1):
            print(" ", end=" ")
        print()

def factorial(number):
    fact = 1
    for a in range(number, 0, -1):
        fact *= a
    print(f"The factorial of {number} is {fact}")

def user_info(name, age):
    print(f"Hi {name}, {age} years old")

name = input("Enter your name: ")
age = eval(input("Enter your age: "))
user_info(name, age)

Repeat = True
while Repeat:
    print()
    print("****************************")
    greetings()
    print("Welcome to my Compilation Program 🙂 ")
    print("How would you like to proceed?")
    print("1 ------ Create a Right Triangle")
    print("2 ------ Create a Number Factorial")
    print("3 ------ Greet Someone")
    print("4 ------ Exit")

    answer = eval(input("Enter your choice (1, 2, 3, 4) ---> "))
    print()

    if answer == 1:
        print("This is what a Right Triangle looks like!")
        right_triangle()
        continue
    elif answer == 2:
        print("This program calculates the factorial of any number")
        number = eval(input("Enter a number: "))
        factorial(number)
        continue
    elif answer == 3:
        print("This program lets you greet anyone")
        name = input("Who would you like to greet? ")
        greetings()
        continue
    elif answer == 4:
        print("Thank you for running my program! 🙂 ")
        break
    else:
        print("Your choice is invalid")
print("\n" + "*" * 50 + "\n")

# Activity 18
def factorial(number):
    fact = 1
    for x in range(number, 0, -1):
        fact *= x
    return fact

# Activity 19
print(f"The factorial of 24 is {factorial(24)}")
print("\n" + "*" * 50 + "\n")

# Activity 20
fruits = ["pinya", "durian", "watermelon", "suha", "ramburat"]
print(fruits)
print(f"My favorite fruit is {fruits[2]}")
fruits.append("kiwi")
print(fruits)
fruits.append("ubas")
print(fruits)
fruits.insert(3, "pomelo")
print(fruits)
print("\n" + "*" * 50 + "\n")

#PROGRAMCHALLENGE 1
print("\t\t\t\t\t\t* \n\t\t\t\t\t*\t*\t* \n\t\t\t\t*\t*\t*\t*\t* \n\t\t\t*\t*\t*\t*\t*\t*\t* \n\t\t\t\t*\t*\t*\t*\t* \n\t\t\t\t\t*\t*\t* \n\t\t\t\t\t\t* ")
print("\n" + "*" * 50 + "\n")



#PROGCHALLENGE2
name = input("What is your name? ")
print("\t\t\t\t\t\t* \n\t\t\t\t\t*\t*\t* \n\t\t\t\t*\t*\t*\t*\t* \n\t\t\t*\t*\t* Hi! " + name + " \t*\t*\t* \n\t\t\t\t*\t*\t*\t*\t* \n\t\t\t\t\t*\t*\t* \n\t\t\t\t\t\t* ")
print("\n" + "*" * 50 + "\n")


#PROGCHALLENGE 3

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")


sum_result = int(first_number) + int(second_number)
print(f"The sum of {first_number} and {second_number} is {sum_result}")


difference = int(first_number) - int(second_number)
print(f"The difference of {first_number} and {second_number} is {difference}")


product = int(first_number) * int(second_number)
print(f"The product of {first_number} and {second_number} is {product}")


quotient = int(first_number) / int(second_number)
print(f"The quotient of {first_number} and {second_number} is {quotient}")


exponent = int(first_number) ** int(second_number)
print(f"The exponent of {first_number} and {second_number} is {exponent}")


remainder = int(first_number) % int(second_number)
print(f"The remainder of {first_number} and {second_number} is {remainder}")


floor_division = int(first_number) // int(second_number)
print(f"The floor division of {first_number} and {second_number} is {floor_division}")
print("\n" + "*" * 50 + "\n")




#PROGCHALLENGE 4
user_name = input("Enter your name: ")
deposit = eval(input("Enter your deposit: "))
print(f"Hello {user_name}, your deposit breakdown in denominations is as follows:")

thousand_bills = deposit // 1000
remaining_after_thousand = deposit % 1000
print(thousand_bills, "1000")

five_hundred_bills = remaining_after_thousand // 500
remaining_after_five_hundred = remaining_after_thousand % 500
print(five_hundred_bills, "500")

two_hundred_bills = remaining_after_five_hundred // 200
remaining_after_two_hundred = remaining_after_five_hundred % 200
print(two_hundred_bills, "200")

one_hundred_bills = remaining_after_two_hundred // 100
remaining_after_one_hundred = remaining_after_two_hundred % 100
print(one_hundred_bills, "100")

fifty_bills = remaining_after_one_hundred // 50
remaining_after_fifty = remaining_after_one_hundred % 50
print(fifty_bills, "50")

twenty_bills = remaining_after_fifty // 20
remaining_after_twenty = remaining_after_fifty % 20
print(twenty_bills, "20")

ten_bills = remaining_after_twenty // 10
remaining_after_ten = remaining_after_twenty % 10
print(ten_bills, "10")

five_bills = remaining_after_ten // 5
remaining_after_five = remaining_after_ten % 5
print(five_bills, "5")

one_bills = remaining_after_five // 1
remaining_after_one = remaining_after_five % 1
print(one_bills, "1")
print("\n" + "*" * 50 + "\n")


#progchallenge 5

name = input("Please enter your name: ")
grade = float(input("Please input your grade: "))


excellent = 90 - 100
very_good = 85 - 89
good = 80 - 84
passing = 75 - 79
failing = 74


if grade >= 75:
    print(f"Good job, {name}! You passed!")
else:
    print(f"Sorry, {name}. You failed. Better luck next time!")
print("\n" + "*" * 50 + "\n")

#progchallenge 6
age = int(input("Enter your age: "))

if age < 0:
    category = "Invalid age"
elif age < 8:
    category = "Toddler"
elif age <= 14:
    category = "Preteen"
elif age < 18:
    category = "Teenager"
elif age < 27:
    category = "Early Adult"
elif age <= 44:
    category = "Middle Adult"
elif age <= 59:
    category = "Past Adult"
else:
    category = "Senior"

print(f"You are a {category}.")
print("\n" + "*" * 50 + "\n")

#progchallenge7
name = input("Please enter your name: ")
print(f"Hi {name}! Welcome to our store!")
print(" *MEAT* Pork = 300, Chicken = 220, Beef = 450")
print(" *DRY GOODS* Rice = 150, Flour = 80, Salt = 20, Pasta = 60")
pur = input("Did you purchase anything today? (yes/no): ")

if pur.lower() == "yes":
    order = input("What did you purchase? ")
    print(f"You purchased: {order}")
else:
    print("Okay, thank you! Let's proceed!")

print("Thank you for visiting our store! 🙂")
print("\n" + "*" * 50 + "\n")

#progchallenge8
sum = 0
for i in range(1, 11):
    num = eval(input(f"Input number #{i}: "))
    sum += num
print(f"The sum of all the numbers given/provided is {sum}")
print("\n" + "*" * 50 + "\n")


#progchallenge9
for x in range(1, 6):
    for b in range(1, x + 1):
        print(" ", end="")
    for c in range(6, x, -1):
        print("*", end=" ")
    print()
print("\n" + "*" * 50 + "\n")

#progchallenge10

for i in range(1, 6):
    for j in range(6, i, -1):  
        print(" ", end=" ")
    for k in range(1, i + 1):  
        print("*", end=" ")
    for k in range(1, i):  
        print("*", end=" ")
    print()

for i in range(4, 0, -1):  
    for j in range(6, i, -1):  
        print(" ", end=" ")
    for k in range(1, i + 1):  
        print("^", end=" ")
    for k in range(1, i):  
        print("^", end=" ")
    print()
print("\n" + "*" * 50 + "\n")


#progchallenge11
for h in range(1, 6):  
    for k in range(h, 6):
        print("  ", end="")  
    for l in range(1, h + 1):
        print("*", end=" ")  
    for i in range(1, h):
        print("*", end=" ")  
    print() 

for x in range(4):  
    for y in range(4):
        print("  ", end="")  
    for z in range(1, 3):
        print("*", end=" ")  
    print()  
print("\n" + "*" * 50 + "\n")


#progchallenge12
for q in range(1, 5):  
    for r in range(5, q, -1): 
        print(" ", end="")
    for x in range(1, q + 1):  
        print("*", end="")
    for t in range(1, q): 
        print("*", end="")
    print()

for g in range(1, 5):  
    for u in range(1, g + 1):  
        print(" ", end="")
    for v in range(4, g - 1, -1):  
        print("*", end="")
    for w in range(4, g, -1):  
        print("*", end="")
    print()
print("\n" + "*" * 50 + "\n")


#progchallenge13
sum = 0  
isRepeat = True  

while isRepeat:
    num = float(input("Enter a number ———> "))  
    sum += num  

    if num == 0:  
        isRepeat = False

print(f'The sum of all the given numbers is {sum}')
print("\n" + "*" * 50 + "\n")


#progchallenge14
def display_filipino_denominations(amount):
    print(f"\nFilipino denominations for PHP {amount}")
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    for denom in denominations:
        if amount >= denom:
            count = amount // denom  
            print(f"{denom} × {count}")
            amount %= denom  

def create_account():
    print("Welcome to the Bank!")
    name = input("Enter your name: ")
    print(f"Account created for {name}.")
    return name

def deposit(balance):
    amount = int(input("\nEnter the amount to deposit: "))
    display_filipino_denominations(amount)  
    balance += amount
    print(f"Deposit successful! Current balance: PHP {balance}")
    return balance

def withdraw(balance):
    amount = int(input("\nEnter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds! Withdrawal denied.")
    else:
        display_filipino_denominations(amount)  
        balance -= amount
        print(f"Withdrawal successful! Current balance: PHP {balance}")
    return balance

def main():
    balance = 0
    name = create_account()  

    print("\nMake an initial deposit to activate your account.")
    balance = deposit(balance)  

    while True:
        print("\nMenu: ")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            balance = deposit(balance)
        elif choice == "2":
            balance = withdraw(balance)
        elif choice == "3":
            print(f"Your current balance is: PHP {balance}")
        elif choice == "4":
            print(f"Thank you for using the bank, {name}!")
            break
        else:
            print("Invalid choice. Please try again.")
main()

