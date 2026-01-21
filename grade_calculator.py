# Student Grade Calculator

def get_grade_and_message(marks):
    if marks >= 90 and marks <= 100:
        return "A", "Excellent work! Keep shining!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good effort! You can do even better!"
    elif marks >= 60:
        return "D", "You passed! Work harder next time!"
    else:
        return "F", "Don't give up! Try again with more practice!"
    
def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if marks >= 0 and marks <= 100:
                return marks
            else:
                print("Invalid marks! Please enter between 0 and 100.")
        except:
            print("Invalid input! Please enter numbers only.")


def main():
    name = input("Enter student name: ")
    marks = get_valid_marks()
    
    grade, message = get_grade_and_message(marks)
    
    print("\nRESULT FOR", name.upper())
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)


main()