if __name__ == "__main__":
    students = ["Max", "Tianji", "Samarth"]
    students.sort()

    print(students)

    first_name = students[0]
    first_name = first_name[:-1]
    print(first_name)
    
    max_length = 0
    max_name = ""
    
    for name in students:
        if len(name) > max_length:
            max_name = name
            max_length = len(name)
    print(max_name)
