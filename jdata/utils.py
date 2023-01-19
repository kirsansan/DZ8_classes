""" utils for working with json-format file"""

import json
from pprint import pprint


def load_from_json_file(filename:str='./questions.json') -> dict:
    """ load any information from json-format file and return it"""

    # if we need load from extermal site
    # response = urllib.request.urlopen(external_adr)
    # data = json.loads(response.read())

    # load from file
    with open(filename, 'r', encoding='utf-8') as fh:  # open file
        data = json.load(fh)  # load data

    fh.close()
    # at this point we can decipher data and put to my structure
    # but in first version we will return all data 'as is'
    return data

def get_student_by_pk(pk: int, data: dict = {} ) -> dict:
    """ return dict by the number of record
        return include fields:
        'pk' - str;
        'full_name' - str;
        'skills' - list of str.
    """
    for challanger in data:
        if challanger['pk'] == pk:
            return challanger
    return None

def get_profession_by_title(title: str, data: dict = {}) -> list:
    """ return list of skills-strings  by the string of title"""
    for challanger in data:
        if challanger['title'] == title:
            return challanger['skills']
    print("kak ya suda popal?")     # this string insead exeption
    return None

def check_fitness(student: dict, profession: list) -> dict:
    """ compare student by professions
        and calculate percents of skill which have this student in list of profession
        "has": ["Python", "Linux"],
        "lacks": ["Docker, SQL"],
        "fit_percent": 50
    """
    has: list[str:] = []
    lacks: list[str:] = []

    # print("вот скилы нашего студента: ", student['skills'])
    # print("вот скилы которые хотим найти: ", profession)
    has = list(set(student['skills']) & set(profession))
    lacks = list(set(profession) - set(student['skills']))
    fit_percent: int = round(100*len(has)/len(profession), 0)
    # [has.append(search_prof) for search_prof in profession if student['skills'] in profession['skills'] ]
    return {'has': has, 'lacks': lacks, "fit_percent": int(fit_percent)}


# this block for a self-test
if __name__ == '__main__':

    questions_data = load_from_json_file()
    if len(questions_data) != 0:
        print("file QUESTIONS was opened and data were load")
        pprint(questions_data)
    else:
        print("we have some troubles with opening file 'QUESTIONS'")
    #
    # profession_data = load_from_json_file('./professions.json')
    # if len(profession_data) != 0:
    #     print("file professions was opened and data were load")
    #     pprint(profession_data)
    # else:
    #     print("we have some troubles with opening file 'professoins'")
    #
    # one_student = get_student_by_pk(1, students_data)
    # print("Student: ")
    # pprint(one_student, depth=2)
    # skills_for_search = get_profession_by_title('Backend', profession_data)
    # print("Prof: \n", skills_for_search)
    #
    # some_result = check_fitness(one_student, skills_for_search)
    # print("dict which was filling for a one student :")
    # pprint(some_result)