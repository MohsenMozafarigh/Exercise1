# This code takes the name and grade of the students and saves them.
data_dict = {}
counter = 0
while True:
    name = input("Please write your name, if you want to abort, write exit: ")
    # Checking that user wants to exit or not.
    if name == "exit":
        break
    # If user wants to add new grade the input will be 0, if s/he wants to delete the grade the input will be 1,
    # and if the user wants to search the grade of a stdeunt, input will be 2.
    remove_var = input("Please write 0 if you want to add, and write 1 if you want to delete, 2 for searching: ")
    if int(remove_var) == 0:
        # This part checks that the name was existing before or not. If the name exists, the code wants new name for it.
        if name in data_dict.keys():
            print("This name exists in dataset. Please write another name")
            continue
        grade = input("Please write your grade: ")
        # counter is used here to track the number of imported grades.
        counter += 1
        if counter == 1:
            print("{} grade is added".format(counter))
        else:
            print("{} grades are added".format(counter))
        if grade != "":
            data_dict[name] = grade
        else:
            print("No grade is imported")
            grade = input("Please write the grade")
    # This section is removing the grade of a specific student.
    elif int(remove_var) == 1:
        data_dict.pop(name)
    # This section is for printing the result of the searched student.
    elif int(remove_var) == 2:
        if name in data_dict.keys():
            print("{}'s garde is {}".format(name, data_dict[name]))
        else:
            print("The imported name is not in dataset")
    else:
        print("Wrong number")
    # If the grade is bigger than 100, it will print the error, and removing that grade.
    if int(grade) > 100:
        print("The grade is out of bound")
        data_dict.pop(name)
    