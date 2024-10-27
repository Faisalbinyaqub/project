import sys
import random
from question_bank import seerah_questions, quran_questions, fiqh_questions, general_questions

def main():
    # Display the introductory message and rules of the quiz
    intro()

    # Loop to handle user's decision to start or exit
    while True:
        try:
            user_input1 = input('Do you want to START or EXIT?: ').strip().lower()
            # Start quiz if user inputs a valid start command
            if start_or_exit(user_input1):
                # Display available quiz subjects
                list_subjects()
                break
            # Exit program if user inputs an exit command
            elif not start_or_exit(user_input1):
                sys.exit("We're sad to see you exit😢. See you again soon")
            else:
                raise ValueError  # Handle invalid entries
        except ValueError:
            print('\t\tInvalid Entry! Enter either "start" or "exit"')
    
    # Let the user select a subject and retrieve the question list
    question_list, selected_subject = select_subject()
    # Run the quiz and calculate final score
    final_score, total_questions = run_quiz(question_list, selected_subject)
    score_percentage = (final_score / (total_questions * 3)) * 100

    # Calculate grade based on score percentage
    grade = grading(score_percentage)
    # Determine pass/fail status based on the grade
    status = determine_status(grade)
    # Display the final result report
    final_report = final_result(final_score, status, selected_subject, total_questions)
    print(final_report)

    # Option to restart the quiz or exit
    restart_or_exit()


def intro():
    # Prints introduction and instructions for the quiz
    print("\n                   **********************"
          "\n                      ISLAMI QUIZ GAME "
          "\n                   ********************** \n"
          "\nAs-salāmu ʿalaykum, This is an Islamic quiz program that"
          "\nwill help you test your knowledge about Quran, Seerah, Fiqh "
          "\nand General knowledge in Islam."
          "\nAll questions are multiple choice. You have three (3) attempts to "
          "\nanswer each question correctly. Points decrease with each attempt:"
          "\n+3 for first attempt, +2 for second, and +1 for third.\n"
          "\n             [START]                  [EXIT]  \n")


def start_or_exit(user_input):
    # Determines if the user wants to start/restart or exit
    if user_input in ["start", "restart", "play", "continue"]:
        return True
    elif user_input in ["exit", "close", "end", "stop"]:
        return False
    else:
        raise ValueError


def list_subjects():
    # Prints the list of subjects available for the quiz
    print("\n----------------------------------------")
    print("Select a subject to continue")
    subjects = ["Seerah", "Quran", "Fiqh", "General Knowledge"]
    for i, subject in enumerate(subjects, start=1):
        print(f"{i}. {subject}")
    print("---------------------------------------- ")


def select_subject():
    # Prompts the user to select a subject for the quiz
    while True:
        try:
            user_input2 = int(input("Enter Subject Number: ").strip())
            if 1 <= user_input2 <= 4:
                return [seerah_questions, quran_questions, fiqh_questions, general_questions][user_input2 - 1], \
                       ["Seerah", "Quran", "Fiqh", "General Knowledge"][user_input2 - 1]
            else:
                print("Incorrect choice, enter a number from 1-4")
        except ValueError:
            print("Incorrect choice, enter a number")


def run_quiz(questions, subject):
    # Main quiz logic, including question display and scoring
    score = 0
    random.shuffle(questions)
    selected_questions = random.sample(questions, k=5)
    total_questions = len(selected_questions)

    print(f"\n                    {subject.upper()}")
    print("                    --------------             ")

    for i, question in enumerate(selected_questions, start=1):
        print(f"Q{i}. {question['question']}")
        attempt = 1  # Reset attempt count for each question

        while attempt <= 3:
            answer = input("ANSWER (A/B/C/D): ").strip().lower()

            if answer in "abcd":
                if answer == question["answer"]:
                    # Award points based on attempt count
                    points = 4 - attempt
                    score += points
                    print(f"Correct answer🥰! on attempt {attempt}, you have +{points} points")
                    break
                elif attempt == 3:
                    # Reveal answer after three incorrect attempts
                    print(f"Wrong again 😔! The correct answer is {question['answer'].upper()}")
                else:
                    print(f"Wrong answer🤪! {3 - attempt} more chances. Try again")
                attempt += 1
            else:
                print("Invalid input! Answer must be A, B, C, or D.")

        print()
    return score, total_questions


def grading(score_percentage):
    # Assigns grade based on score percentage
    if 100 >= score_percentage >= 90:
        return 'A'
    elif 89 >= score_percentage >= 80:
        return 'B'
    elif 79 >= score_percentage >= 70:
        return 'C'
    elif 69 >= score_percentage >= 60:
        return 'D'
    elif 59 >= score_percentage >= 50:
        return 'E'
    else:
        return 'F'


def determine_status(grade):
    # Returns pass/fail status based on grade
    return "Passed 🥳" if grade in ["A", "B", "C", "D"] else "Failed 😔"


def final_result(total_score, status, quiz_subject, total_questions):
    # Returns formatted result report
    total_possible = total_questions * 3
    return (f"##############################################\n\t\t\tRESULT "
            f"\n\t\tTotal Score: {total_score}/{total_possible} "
            f"\n\t\tStatus: {status} "
            f"\n\t\tQuiz Subject: {quiz_subject} "
            f"\n\t\tNumber of Questions: {total_questions}"
            f"\n##############################################\n"
            "\n        [RESTART]                  [EXIT]  \n")


def restart_or_exit():
    # Handles user choice to restart or exit after viewing results
    while True:
        try:
            re = input('Do you want to RESTART OR EXIT: ').strip().lower()
            if start_or_exit(re):
                list_subjects()
                break
            elif re == "exit":
                sys.exit("Hope you enjoyed the quiz. See you again soon!")
            else:
                raise ValueError
        except ValueError:
            print('\t\tInvalid Entry! Enter either "restart" or "exit"')

    # Restart quiz after selecting a new subject
    question_list, selected_subject = select_subject()
    final_score, total_questions = run_quiz(question_list, selected_subject)
    score_percentage = (final_score / (total_questions * 3)) * 100
    grade = grading(score_percentage)
    status = determine_status(grade)
    final_report = final_result(final_score, status, selected_subject, total_questions)
    print(final_report)
    restart_or_exit()


if __name__ == "__main__":
    main()
