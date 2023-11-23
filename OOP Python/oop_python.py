"""
@property

Свойство property упрощает работу с классом и позволяет через одну переменную работать и с геттером, и с сеттером
атрибутов класса.

Если в классе атрибут как обьект-свойство, то в первую очередь выбирается оно, даже если в экземпляре класса
есть локальное свойство с таким же именем.

Так можно гибко работать с приватными локальными свойствами с помощью единого интерфейса объекта свойства property


"""

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)
            #или
    old = property()
    old = old.setter(set_old)
    old = old.getter(get_old)
            #или
    @property
    def old(self):
        return self.__old
    @old.setter
    def old(self, old):
        return self.__old
    @old.deleter
    def old(self):
        del self.__old


p = Person('Соня', 22)
print(p.__dict__) #__dict__ выводит все обьекты в словаре
del p.old
print(p.__dict__)

print('///////////////////////////////////////////////////////////')
'''
a.getter()
a.setter()
a.deleter()
'''
print('ДЕСКРИПТОРЫ')

"""
Дескриптор - это класс, который содержит или один магический метод get, или класс, в котором дополнительно прописаны 
методы set и/или del

при создании класса Integer автоматически вызывается метод set_name, в котором параметр self является ссылкой на 
создаваемый экземпляр класса
При считывании данных дескриптора автоматически срабатывает геттер, в котором self - это ссылка на обьект Integer

дескрипторы данных имеют больший приоритет, чем простые аттрибуты.
"""

class Integer:
    def __set_name__(self, owner, name):
        self.name = " " + name

class Point3D():
    x = Integer()
    y = Integer()
    z = Integer()

