def user_input():
    # read in line of code and seperate data and add to the table
    line_code = input("enter line of code")
    split = line_code.split()
    for temp in split:
        print (temp)

def main():
    user_input()


if __name__ == "__main__":
    main()