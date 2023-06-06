try: 
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    c = b/a
    print("example for exception")
    print("{} / {} is {}".format(a,b,c))
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except ValueError as e:
    print(e)