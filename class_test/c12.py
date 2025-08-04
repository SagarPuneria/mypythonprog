# Exception handling basics
try:
    # x = 10  # Define variable x before using it
    print(x)
    # print("Hello")
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")
