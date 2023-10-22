# this is a basic calculator
# prompts you to provide name
name = input("Hello, what is your name?" + " ")
print("Hi " + " " + name)
# asks for your age
your_age = input("How old are you? ")
# asks for your partner's age
partners_age = input("How old is your partner? ")
# performs calculations
# sum
adding = int(your_age) + int(partners_age)
print("The sum of your ages is " + str(adding))
# subtract
minus = int(your_age) - int(partners_age)
print("The difference between your ages is " + str(minus))
# multiply
prod = int(your_age) * int(partners_age)
print("The product between your ages is " + str(prod))
# division
div = int(your_age) / int(partners_age)
print("The quotient of your age to your partner's is " + str(div))
# modulo
mod = int(your_age) % int(partners_age)
print("The quotient of your age by your partner's is " + str(mod))
# floor division
floor_div = int(your_age) // int(partners_age)
print("The floor division of your age by your partner's is " + str(floor_div))
# power
pow = int(your_age) ** int(partners_age)
print("The power of your partner's age to your age is " + str(pow))
# equation
eqn = (int(your_age) ** 2) / (int(partners_age) ** 2)
print("Your compatibility number is " + str(eqn))
