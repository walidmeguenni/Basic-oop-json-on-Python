def main():
    age = input("enter your age : ")
    if int(age) >= 18:
        print('welcome sir')
    elif 18 > int(age) > 0:
        print('your age under law')
    else:
        print("enter valid value")


if __name__ == '__main__':
    main()
