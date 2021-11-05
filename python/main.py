def main():
    # dict is mutable type that's mean you can change its value
    # student = dict(id="o5z5re7", name = 'walid' ) first way for create dict
    student = {
        'id': 'lgq5787',
        'name': "walid",
        'lastname': "meguenni"
    }  # second way to create dict
    data = []  # create empty list // List is too mutable type
    print(student, type(student))
    data.append(student)  # add new item to the List
    print(data)
    student['name'] = "mostafa"  # edit the value of the key on dict
    student['age'] = 12  # add new item (key, value) on dict
    print("nouvel dic : ", student)
    print('nouvel list : ', data)
    del student['id']  # delete item from dict


if __name__ == '__main__':
    main()
