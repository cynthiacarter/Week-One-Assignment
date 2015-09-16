__author__ = 'daniel.neumann'
# Edit by Cynthia Carter
# CIS 125 Fall 2015
# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 2 * x * (1 - x)
        print(x)

main()
