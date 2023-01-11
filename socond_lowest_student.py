# I am given a list of lists which includes name of student with its sorce
# Output should be extract the second lowest score and prit the name or names
# process would be like this:
# create the list of lists
# sort the list by the score
# convert it to set
# find the second lowest score
# find the students that have that score

if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
        scores.append(score)

    students.sort(key=lambda students: students[1])
    scores.sort()
    unique_scores = list(set(scores))
    second_lowest = unique_scores[1]

    output = []
    for student in students:
        if second_lowest == student[1]:
            output.append(student[0])

    output.sort()
    for item in output:
        print(item)
