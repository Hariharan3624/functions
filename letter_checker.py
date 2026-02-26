b = input("enter a word: ")
a = input("enter a letter: ")
for i in b:
    if (i==a):
        print(a,"is found")
        break
    else:
        print(a,"is not found")