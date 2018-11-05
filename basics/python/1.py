#import os

def main():
    printme ('abc')

def printme (arg):
   string = "Hello," + str(arg) + "!"
   print (string)


if __name__ == "__main__":
    main()