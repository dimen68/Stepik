# Работа не волк
class Programmer:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        if self.grade == 'Junior':
            self.sale = 10
        elif self.grade == 'Middle':
            self.sale = 15
        elif self.grade == 'Senior':
            self.sale = 20
        else:
            print('Нет такой должности!')
        self.worktime = 0
        self.totalmount = 0

    def work(self, work_time):
        self.worktime += work_time
        self.totalmount += work_time * self.sale

    def rise(self):
        if self.grade == 'Junior':
            self.grade = 'Middle'
            self.sale = 15
        elif self.grade == 'Middle':
            self.grade = 'Senior'
            self.sale = 20
        else:
            self.sale += 1

    def info(self):
        return self.name + ' ' + str(self.worktime) + 'ч. ' + str(self.totalmount) + 'тгр.'

programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())