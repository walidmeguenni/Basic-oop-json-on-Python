def main():
    try:
        # read from test file
        readfile = open('test.txt', "r")
        for line in readfile:  # this will read from file line by line
            print(line)
        readfile.close()
    except IOError:
        print("File doesn't exist")
    else:
        print("file show up")


if __name__ == '__main__':
    main()
