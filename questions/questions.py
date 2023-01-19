class Questions():
    right_answer_str: str = ""
    dificulty_num: int = 0
    question_str: str = ""
    __is_it_real:bool = True
    has_answer_requested:bool = False
    user_answer:str = ""
    score_for_right:int = 0

    def __init__(self, right_answer_str:str="", dificulty_str:str=0, question_str:str="", score4right=10):
        self.right_answer_str = right_answer_str
        self.dificulty_num = int(dificulty_str)
        self.question_str = question_str
        self.__is_it_real = False
        self.has_answer_requested = False
        self.user_answer = ""
        self.score_for_right = self.dificulty_num*score4right

    def __repr__(self):
        i_will_be_happy_tell_about_me:str = " ".join(["for request:'", self.question_str,"'",
                                                      "answer is: ", "':-P it is a top secret'",
                                                      "and dificulty: ", str(self.dificulty_num),",",
                                                      "user answer is:", self.user_answer, ", and",
                                                      "score for right is: ", str(self.score_for_right)])
        return i_will_be_happy_tell_about_me

    def set_real(self, is_real:bool=True):
        """ setter for a flag __is_it_real"""
        self.__is_it_real = is_real

    def  get_real(self):
        """ getter for a flag __is_it_real """
        return self.__is_it_real

    def get_question_hint(self) -> str:
        """ this func return spoiling question """
        # print("I know question:")
        return self.make_magic_spoil(self.question_str)
        # return self.question_str

    def get_answer_hint(self) -> str:
        # print("I know answer to your question:")
        return self.right_answer_str

    @classmethod
    def make_magic_spoil(cls, some_string:str, spoil_number:int=5) ->str:
        """ func for a joke - change some letters in the string to the * """
        # self.question_sting = "".join([x for x in self.question_sting if x == 'a'])
        hard_str: str = ""
        for index in range(0,len(some_string)):
            if index % spoil_number == 0:  # lets spoil each %spoin_number elements :-E~~ (devil face)
                hard_str += '*'
            else:
                hard_str += some_string[index]
        return hard_str

    def get_points(self) -> int:
        """ only for .score_for_right return"""
        return self.score_for_right

    def is_correct(self) ->bool:
        """ compare user_answer with right_answer and return boolean
            if this func started - it means that user has already answered (one or more times)
        """
        self.has_answer_requested = True
        if self.user_answer == self.right_answer_str:
            return True
        return False

    def build_question(self, mode_nightmare:bool=False) ->str:
        """ build string for preparing request the answer"""
        if mode_nightmare:
            tmp_str = self.make_magic_spoil(self.question_str) + " Сложность:" + f"{self.dificulty_num}"
        else:
            tmp_str = self.question_str + " Сложность:" + f"{self.dificulty_num}"
        return tmp_str

    def build_feedback(self):
        """react for answer. it would use is_correct()"""
        if self.is_correct():
            return f"Ответ верный, получено {self.score_for_right} баллов\n"
        else:
            return f"Ответ неверный, правильный ответ {self.right_answer_str}\n"


# self-testing block
if __name__ == '__main__':

    question_4_test: Questions = Questions(right_answer_str="my_Ok", dificulty_str=8, question_str="say just 'Ok'")
    print(question_4_test)
    print(question_4_test.get_answer_hint()) # can visible right answer, wait for my_Ok
    print(question_4_test.get_question_hint())
    question_4_test.user_answer = "NotOk"
    print(question_4_test.is_correct()) # wait for False
    question_4_test.user_answer = "my_Ok"
    print(question_4_test.is_correct())  # wait for True
    print(question_4_test.build_question())
