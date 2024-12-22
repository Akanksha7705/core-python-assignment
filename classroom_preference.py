def calc_avg(students):
    averages = {}
    for name, marks in students.items():
        averages[name] = round(sum(marks) / len(marks), 2)
    return averages


def topper(averages):
    top_student = max(averages, key=averages.get)
    return top_student


students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}


avg = calc_avg(students)
toppers = topper(avg)


print("Average Marks:", avg)
print("Top Performer:", toppers)
