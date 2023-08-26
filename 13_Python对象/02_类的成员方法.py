"""
演示类的成员方法
"""


class Student:
    name = None
    age = None

    def say_hi(self):
        print(f'Hi大家好，我是{self.name}')

    def say_hi2(self,msg):
        print(f'Hi大家好，我是{self.name},{msg}')


stu_1 = Student()
stu_1.name = '1'

stu_1.say_hi()

stu_1.say_hi2('2')