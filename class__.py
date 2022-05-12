class Student:
    name = 'wanli'
    __age = '25'

    def call(self):
        print(self)

    @classmethod
    def test_classmethod(cls, test):
        print(cls.name)
        print(test)

    def query_age(self):
        print(self.__age)

    @classmethod
    def age(cls):
        print(cls.__age)


st1 = Student()
# st1.name = 'wanli1'
# print(st1.name)
# print(Student.name)
# st1.call()
# Student.test_classmethod('test')
st1.query_age()
Student.age()
print(type(st1))
issubclass()