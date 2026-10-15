
# student grader application -----
# it includes -- login, password, adding informations and grading 
def student_grader(login_data,password_data):
    counter = 0
    while True:
        login = input("Please enter your login: ")
        password = input("Please enter your password: ")

        if login == login_data and password == password_data:

            print("You have successfully logged in")
            break

        else:
            counter += 1
            if login != login_data  and len(login) > 1:
                print("You have entered the wrong login ID")
            else:
                print("please enter log in")

            if password != password_data:
                    print("Wrong password has been entered")
            if counter >= 3:
                 print("Too many attempts. Returning to the main menu.")
                 
                 return []
            


# log in and password are done

    collection = list()
    while True:
        number_of_students = input("please enter your number of students: ")
        if number_of_students.isdigit():
            number_of_students = int(number_of_students)

            if number_of_students > 0:
                break
            else:
                print("Please enter at least one student")
        else:
            print("Please enter a valid number")


    if type(number_of_students) == int:
        value = 0
        while True:
            value += 1
            if number_of_students < value:
                print("")
                print("you have entered all of students")
                break
            else:
                student_name = input(f"please your {value} student name: ")
# strip helps remove space to calculate it
                if len(student_name.strip()) < 2:
                    print("please enter longer than 2 characters")
                    value-=1
                    continue
                student_grade = input(f"Please enter student {student_name}'s grade: ")

            if student_grade.isdigit():
                collection.append((student_name, int(student_grade)))
            else:
                print("Please enter a numeric grade")
                
        return sorted(collection, key=lambda x: int(x[1]), reverse=True)
    else:
        print("you have directed to main page because of login failure")
        return []


