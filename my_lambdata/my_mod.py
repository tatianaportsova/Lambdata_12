# my_lambdata/my_mod.py


def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

# this code breakes our ability to omport enlarge from other files
# print("HELLO")
# y = int(input("Please choose a number"))
# print(y, enlarge(y))

if __name__ == "__main__":
    # only runs the code IF script is invoked from the command-line
    # not if it is imported from another
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))


