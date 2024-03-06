import textwrap
import keyboard
from typing import *
import sys
import os


n_ranking = 6
data = [
    "Il est important qu'un enseignant comprenne les sentiments des élèves",
    "Les bons enseignants encouragent toujours les élèves à réfléchir aux "
    "réponses par eux-mêmes",
    "L'apprentissage signifie que les élèves ont de nombreuses opportunités "
    "d'explorer, de discuter et d'exprimer leurs idées",
    "Dans de nombreuses classes, il y a une atmosphère démocratique libre "
    "qui stimula la réflexion et l'interaction des élèves",
    "Chaque enfant est unique ou spécial et mérite une éducation adaptée à "
    "ses besoins particuliers"
]


class Interface:

    def __init__(self, data):
        self.text_width = 70
        self.data = data
        self.n = len(data)
        self.answers = [None] * self.n  # List[Optional[int]]

        self.idx = -1  # current question
        self.n_char = []  # number of printed characters for questions up to
        # current question

    def print_line(self, i=None):
        if i is None:
            self.idx += 1
            i = self.idx
        question = self.data[i]
        self.n_char.append(0)
        lines = textwrap.wrap(question, self.text_width)
        for j, line in enumerate(lines):
            line += ' '*(self.text_width - len(line))
            if j == 0:
                marks = ' 1  2  3  4  5  6 '
                answer = self.answers[i]
                # print(self.answers)
                if answer is not None:
                    # replace the space by parentheses around the answer
                    marks = list(marks)
                    marks[3*answer-3] = '('
                    marks[3*answer-1] = ')'
                    marks = ''.join(marks)
                line = f'{i+1:2d} | {line} |{marks}'
            else:
                line = f'   | {line} |'
            print(line)
            self.n_char[i] += len(line) + 1

    def erase_line(self):
        if self.idx < 0:
            return
        print('\b'*self.n_char[self.idx])
        self.n_char = self.n_char[:self.idx]
        self.idx -= 1

    def print_all(self):
        # re-display everything...
        os.system('cls')
        for i in range(min(self.idx + 1, self.n)):
            self.print_line(i)

    def fill_form(self):

        self.print_line()
        while self.idx < self.n:
            key = keyboard.read_key(suppress=True)
            key = keyboard.read_key(suppress=True)  # bug: we also read the
            # key-up event!
            if key in ['1', '2', '3', '4', '5', '6']:
                # mark answer for current question
                self.answers[self.idx] = int(key)
                self.erase_line()
                self.print_line()
                # show next question
                if self.idx < self.n-1:
                    self.print_line()
                else:
                    break
            elif key == 'backspace' and self.idx > 0:
                # turn back to previous question
                self.erase_line()
                # erase its answer and display it again
                self.answers[self.idx] = None
                self.erase_line()
                self.print_line()
            elif key == 'esc':
                break

    def fill_form2(self):

        self.idx = 0

        while self.idx < self.n:
            self.print_all()
            key = keyboard.read_key(suppress=True)
            key = keyboard.read_key(suppress=True)  # bug: we also read the
            # key-up event!
            if key in ['1', '2', '3', '4', '5', '6']:
                # mark answer for current question
                self.answers[self.idx] = int(key)
                # go to next question
                self.idx += 1
            elif key == 'backspace' and self.idx > 0:
                # turn back to previous question
                self.idx -= 1
                # erase its answer
                self.answers[self.idx] = None
            elif key == 'esc':
                break

        self.print_all()




form = Interface(data)
form.fill_form2()

# sys.stdout.write('hello\n')
# os.system('cls')
# sys.stdout.write('\roij')

