print('Hello what is your name?')
user_name = input()
print('Welcome', user_name)
def loop():
    print('May I take your order?')
    order = input()
    print(order, 'Is this your order? Type yes or no')
    confirmation = input()
    if confirmation == "yes":
        print('I will be back with your order')

    elif confirmation == "no":
        print('I will try again')
        loop()
loop()