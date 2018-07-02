from random import randint

def generate_random_number(nb_digit):
    n = ""
    for i in range(nb_digit):
        n += str(randint(0, 9))
    return n

class MemoNumber(object):
    nb_good_answer = 0
    counter_memorized_number = 0
    file_number = []
    counter_answer = 0

    def __init__(self, digit_number, question_number):
        self.digit_number = digit_number
        self.question_number = question_number
        while len(self.file_number) < self.question_number:
            self.generate_number()

    def generate_number(self):
        number = generate_random_number(self.digit_number)
        self.file_number.append(number)

    def get_mode(self):
        if self.counter_memorized_number < self.question_number:
            return 0
        elif self.counter_answer == self.question_number:
            return 2
        elif self.counter_memorized_number == self.question_number:
            return 1

    def get_number(self):
        number = self.file_number[self.counter_memorized_number]
        self.counter_memorized_number += 1
        return number

    def check_number(self, number):
        rep = int(number) == int(self.file_number[self.counter_answer])
        self.counter_answer += 1
        if rep:
            self.nb_good_answer += 1
        return rep


if __name__ == "__main__":
    MEMO = 0
    REMEMO = 1
    END = 2
    memo = MemoNumber(1, 3)
    while memo.get_mode() == MEMO:
        print(memo.get_number())
        print(f"mode: {memo.get_mode()}")
    while memo.get_mode() == REMEMO:
        nb = input("number: ")
        print(memo.check_number(nb))
        print(f"mode: {memo.get_mode()}")
