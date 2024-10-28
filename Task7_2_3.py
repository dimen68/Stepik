# Не нажимай красную кнопку!
from itertools import count


class RedButton:

    def __init__(self):
        self.count_ = 0

    def click(self):
        self.count_ +=1
        return print('Тревога!')

    def count(self):
        return self.count_


first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())
