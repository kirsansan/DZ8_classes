# This is a not_very_simple Python script. ;-)
# HomeWork from lesson 8.2. Python 20 groupe
# writted by Kirill.S

from config.config import FILE_FOR_QUESTIONS, SCORE_FOR_RIGHT
from my_new_input.my_input import InputAndCheckString
from questions.questions import Questions
from jdata.utils import load_from_json_file
from pprint import pprint

def print_statistics(list_quest: list[Questions:]):
    """ calculate statistics and print it
    use list of class Questions objects
    """
    score_summ: int = 0
    right_counter: int = 0
    answer_counter: int = 0
    # tmp_q = Questions()
    for tmp_q in list_quest:
        if tmp_q.has_answer_requested:
            answer_counter += 1
            if tmp_q.is_correct():
                score_summ += tmp_q.get_points()
                right_counter += 1
    print("Вот и всё!")
    print(f"Отвечено на {right_counter} вопросов из {answer_counter}")
    print(f"Набрано баллов  {score_summ}")

def create_list_of_questions_from_long_data(some_data_from_json) -> list[Questions:] :
    """read from_long_data and fill objects like class Questions then append it to the list
    this list will be returned
    """
    questions = []
    for tmp_data in some_data_from_json:
        # print(_data)
        one_question: Questions = Questions(right_answer_str=tmp_data['a'],
                                            dificulty_str=tmp_data['d'],
                                            question_str=tmp_data['q'],
                                            score4right=SCORE_FOR_RIGHT)
        questions.append(one_question)
    return questions


# main block
if __name__ == '__main__':

    print("Ok")
    not_seeking_data = load_from_json_file(FILE_FOR_QUESTIONS)

    questions: list[Questions:] = create_list_of_questions_from_long_data(not_seeking_data)

    # dialog with user block
    input_and_check: InputAndCheckString = InputAndCheckString()

    for tmp_question in questions:
        print("А ну ко угадай ко")
        print(tmp_question.build_question())
        input_and_check.input_while_correct(">")
        # if input_and_check.input_string == tmp_question.right_answer_str:
        tmp_question.user_answer = input_and_check.input_string  # need rewrite as set_answer() and get_answer()
        # tmp_question.is_correct()
        print(tmp_question.build_feedback())

    # print statistics block -
    print_statistics(questions)
    if True:
        print("Приятно поиграли ")
    else:
        print("Если вы проверяете этот код - помогите мне получить доступ к урокам с 10 по 13!!")

# this is the end of this short history
