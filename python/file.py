def main():
    out = open("test.txt", 'a')  # create file and define what should doit it "w" : write and "a" add more data on
    # old file
    out.write('\nfine thanks')
    out.close()
    # read from test file
    readfile = open('test.txt', "r")
    for line in readfile:  # this will read from file line by line
        print(line)
    readfile.close()


if __name__ == '__main__':
    main()
