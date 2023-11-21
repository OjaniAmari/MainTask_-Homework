def calculate_average(test_scores):
    return sum(test_scores) / len(test_scores)

def calculate_grade(score, grade_c, grade_b, grade_a):
    if score >= grade_a:
        return "A"
    elif score >= grade_b:
        return "B"
    elif score >= grade_c:
        return "C"
    else:
        return "Below C"

def english_grades(test1, test2, grade_c=64, grade_b=84, grade_a=104):
    average_score = calculate_average([test1, test2])
    final_grade = calculate_grade(average_score, grade_c, grade_b, grade_a)
    return average_score, final_grade

def maths_grades(test1, test2, test3, grade_c=56, grade_b=64, grade_a=78):
    average_score = calculate_average([test1, test2, test3])
    final_grade = calculate_grade(average_score, grade_c, grade_b, grade_a)
    return average_score, final_grade

def science_grades(test1, test2, test3, grade_c=96, grade_b=113, grade_a=128):
    average_score = calculate_average([test1, test2, test3])
    final_grade = calculate_grade(average_score, grade_c, grade_b, grade_a)
    return average_score, final_grade

def main():
    
    english_test1 = int(input("Enter English Test 1 score: "))
    english_test2 = int(input("Enter English Test 2 score: "))
    english_average, english_final_grade = english_grades(english_test1, english_test2)

    maths_test1 = int(input("Enter Maths Test 1 score: "))
    maths_test2 = int(input("Enter Maths Test 2 score: "))
    maths_test3 = int(input("Enter Maths Test 3 score: "))
    maths_average, maths_final_grade = maths_grades(maths_test1, maths_test2, maths_test3)

   
    science_test1 = int(input("Enter Science Test 1 score: "))
    science_test2 = int(input("Enter Science Test 2 score: "))
    science_test3 = int(input("Enter Science Test 3 score: "))
    science_average, science_final_grade = science_grades(science_test1, science_test2, science_test3)

    total_marks = english_average + maths_average + science_average

    print(f"\nEnglish: {english_average}/120, Grade: {english_final_grade}")
    print(f"Maths: {maths_average}/100, Grade: {maths_final_grade}")
    print(f"Science: {science_average}/150, Grade: {science_final_grade}")
    print(f"Total Marks: {total_marks}/370")

if __name__ == "__main__":
    main()