import sys
import random
from question_bank import seerah_questions, quran_questions, fiqh_questions, general_questions

def main():
    # Display the purpose of the program and the rules
    intro()
    # user can decide on either to close the program or start the quiz after reading the intro
    while True:
        try:
            user_input1 = input('Do you want to START or EXIT?: ').strip().lower()
            # if user chooses to start the quiz
            if start_or_exit(user_input1):
                # list of subjects user can choose to be quizzed on
                list_subjects()
                break
            # if user chooses to exit, end the program
            elif not start_or_exit(user_input1):
                sys.exit("We're sad to see your exit😢. See you again soon")
            # if user does not enter either "start" or "exit", raise Value error
            # prompt the user to make a correct entry
            else:
                raise ValueError
        except ValueError:
            print('\t\tInvalid Entry!, Enter either "start" or "exit"')
    # select a subject for the quiz
    question_list, selected_subject = select_subject()
    # answers multiple choice questions based on the subject chosen
    final_score, total_questions = run_quiz(question_list, selected_subject)
    score_percentage = (final_score / (total_questions * 3)) * 100
    # Grade total score after answering all questions
    grade = grading(score_percentage)
    # Based your participant final score,determine if the participant passed or failed
    status = determine_status(grade)
    # produce final report of the quiz
    final_report = final_result(final_score, status, selected_subject, total_questions)
    print(final_report)
    # after displaying the result of quiz, you may choose to restart the quiz or exit the program
    restart_or_exit()


def intro():
    print("\n                   ********************"
          "\n                   ISLAMIC KNOWLEGE QUIZ  "
          "\n                   ******************** \n"
          "\nAs-salāmu ʿalaykum, This is an islamic quiz program that"
          "\nwill help you test your knowledge about Quran, Seerah, Fiqh "
          "\nand General knowledge in islam."
          "\nAll the questions are multiple choice questions.You have only "
          "\nthree(3) attempts to answer a question correctly. If a Question "
          "\nis answered correctly on the first attempt, you earn +3 points, on a "
          "\nsecond attempt you have +2 points and on the third and last attempt "
          "\nyou have only +1 point."
          "\n\n             [START]                  [EXIT]  \n")


# Continue to the quiz or exit after reading the intro of the program
def start_or_exit(user_input):
    if user_input in ["start", "restart", "play", "continue"]:
        return True
    elif user_input in ["exit", "close", "end", "stop"]:
        return False
    else:
        raise ValueError


# Display the list of subjects user can choose to be quizzed on
def list_subjects():
    print("\n----------------------------------------")
    print("Select a subject to continue")
    subjects = ["Seerah", "Quran", "Fiqh", "General Knowledge"]
    subject_number = 1
    for subject in subjects:
        print(f"{subject_number}. {subject}")
        subject_number += 1
    print("---------------------------------------- ")


# Select a subject for the quiz
def select_subject():
    while True:
        try:
            user_input2 = int(input("Enter Subject Number: ").strip())
            # print()
            if 0 < user_input2 < 5:
                match user_input2:
                    case 1:
                        return seerah_questions, "Seerah"
                    case 2:
                        return quran_questions, "Quran"
                    case 3:
                        return fiqh_questions, "Fiqh"
                    case 4:
                        return general_questions, "General Knowledge"
                break
            else:
                print("Incorrect choice, enter a number from 1-4")
        except ValueError:
            print("Incorrect choice, enter a number")


def run_quiz(list_, subject):
    score = 0
    ques_number = 1
    attempt = 1
    random.shuffle(list_)
    selected_questions = random.sample(list_, k=5)
    total_questions = len(selected_questions)
    print("\n                    {}".format(subject.upper()))
    print("                    --------------             ")

    for question in selected_questions:
        print(f"Q{ques_number}. {question['question']}")

        while attempt <= 3:
            answer = input("ANSWER (A/B/C/D): ").strip().lower()

            try:
                if answer in "abcdABCD":
                    if answer == question["answer"]:
                        if attempt == 1:
                            print("correct answer🥰! on first attempt, you have +3 points")
                            score += 3
                        elif attempt == 2:
                            print("correct answer🥰! on second attempt, you have +2 points")
                            score += 2
                        else:
                            print("correct answer🥰! on last attempt, you have +1 points")
                            score += 1

                        attempt = 1
                        break

                    elif attempt == 3:
                        print("Wrong again 😔!, The Correct answer is {}".format(question['answer'].upper()))
                        attempt = 1
                        break
                    else:
                        remainder = 3 - attempt
                        if remainder == 1:
                            print(f"Wrong answer🤔!, You have {remainder} last chance. Try again")
                        else:
                            print(f"Wrong answer🤪!, You have {remainder} more chances. Try again")
                        score = score
                        attempt += 1
                else:
                    raise ValueError

            except ValueError:
                print("Invalid!, answer must be an alphabet from A-D. Try again ")

        ques_number += 1
        print()
    return score, total_questions


# Grading of quiz result
def grading(x):
    if 100 >= x >= 90:
        return 'A'
    elif 89 >= x >= 80:
        return 'B'
    elif 79 >= x >= 70:
        return 'C'
    elif 69 >= x >= 60:
        return 'D'
    elif 59 >= x >= 50:
        return 'E'
    else:
        return 'F'


def determine_status(grade_):
    if grade_ in ["A", "B", "C", "D"]:
        return "Passed 🥳"
    else:
        return "Failed 😔"


def final_result(total_score, status, quiz_subject, total_questions):
    total = total_questions * 3
    return (f"##############################################\n\t\t\t\tRESULT "
            f"\n\t\t\tTotal Score: {total_score}/{total} "
            f"\n\t\t\tStatus: {status} "
            f"\n\t\t\tQuiz Subject: {quiz_subject} "
            f"\n\t\t\tNumber of Question: {total_questions}"
            f"\n##############################################"
            f"\n\n        [RESTART]                  [EXIT]  \n")


def restart_or_exit():
    while True:
        try:
            re = input('Do you want to RESTART OR EXIT: ').strip().lower()
            if start_or_exit(re):
                list_subjects()
                break
            elif re == "exit":
                sys.exit("Hope you enjoyed the quiz, See you again soon")
            else:
                raise ValueError

        except ValueError:
            print('\t\tInvalid Entry!, Enter either "restart" or "exit"')

    question_list, selected_subject = select_subject()
    # answers multiple choice questions based on the subject chosen
    final_score, total_questions = run_quiz(question_list, selected_subject)
    score_percentage = (final_score / (total_questions * 3)) * 100
    # Grade total score after answering all question
    grade = grading(score_percentage)
    # Based your participant final score,determine if the participant passed or failed
    status = determine_status(grade)
    # produce final report of the quiz
    final_report = final_result(final_score, status, selected_subject, total_questions)
    print(final_report)
    restart_or_exit()


if __name__ == "__main__":
    main()
