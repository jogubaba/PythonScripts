name = input("Input your password ")
length = (len(name))
print('The length of your password is ' + str(length))

if length == 18:
    print("your password is now set")
elif length > 18:
    print("its over specified limit, Please re-enter your password")
else:
    print("Its below password length, please re-try giving a new password")
