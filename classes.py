#self must be present in every method inside classes
#by that we can access everything about that particular object



class Point:
    def __init__(self,x,y):  #constructor
        self.x=x;
        self.y=y;
    def func1(self):
        print('inside function 1');
    def func2(self):
        print('inside function 2');

object=Point(12,23);
object.func1();
print(object.x,object.y);


class Person:
    def __init__(self,name,launguage):
        self.name =name;
        self.launguage=launguage;
    def talk(self):
        print(f'{self.name} can talk only {self.launguage}');
        
newObj = Person('messsi','espanoyl');
newObj.talk();



#inheritance

class Common:
    def walk(self):
        print('can be able to walk')
class Dog(Common):      #inheriting Common class in Dog and Cat classes
    def bark(self):
        print('can be able to bark')
class Cat(Common):
    def meow(self):
        print('always meowing')
        
        
dog1 = Dog();
dog1.walk();
cat1=Cat()
cat1.meow();
