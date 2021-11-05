import urllib.request
import json


def main():
    data = urllib.request.urlopen("https://jsonplaceholder.typicode.com/todos").read()
    print(data, type(data))
    Format = json.loads(data.decode('utf-8'))
    # print(Format, type(Format))
    for row in Format:
        print(row["title"])


if __name__ == '__main__':
    main()
