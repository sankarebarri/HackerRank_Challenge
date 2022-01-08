def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade <38:
            rounded_grades.append(grade)
        elif grade%5 ==0:
            rounded_grades.append(grade)
        else:
            n1 = grade // 5
            n2 = (n1+1)*5
            if (n2 - grade) < 3:
                rounded_grades.append(n2)
            else:
                rounded_grades.append(grade)
    return rounded_grades