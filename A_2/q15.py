def main():
    name_marks_list = []

    for _ in range(10):
        name = str(input("Enter the name: "))
        marks = int(input("Enter the marks: "))

        name_marks_list.append(name)
        name_marks_list.append(marks)

    print(name_marks_list)

main()