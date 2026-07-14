print("Welcome to a working calculator.")
print("\n It can preform calculation on tow number.")

a = input("Enter first integer number: ")
b = input("Enter second integer number: ")
c = input("Enter the function you want to perform in symbol format: ")
if(c=="+"):
    print(int(a) + int(b))
if(c=="-"):
    print(int(a) - int(b))
if(c=="*"):
    print(int(a) * int(b))
if(c=="/"):
    print(int(a) / int(b))
if(c=="%"):
    print(int(a) % int(b))
