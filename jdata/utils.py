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

    fh.close()   # paranoid closer =)))   I know that "with" have already closed it
    # at this point we can decipher data and put to my structure
    # but in first version we will return all data 'as is'
    return data

def test():
    questions_data = load_from_json_file()
    if len(questions_data) != 0:
        print("file QUESTIONS was opened and data were load")
        pprint(questions_data)
    else:
        print("we have some troubles with opening file 'QUESTIONS'")



# this block for a self-test
if __name__ == '__main__':
    test()
