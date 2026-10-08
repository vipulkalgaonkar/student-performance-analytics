def calculate_total(row):
    return row[["Math", "Physics", "CS"]].sum()

def calculate_average(row):
    return row[["Math", "Physics", "CS"]].mean()

def assign_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"
