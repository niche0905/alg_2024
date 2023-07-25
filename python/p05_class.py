class Hello:
  pass # Python 에서는 줄을 비워 두면 안될 때 pass 를 써야 한다.

print('-- 타입 이름에 괄호를 열고 닫으면 해당 타입의 객체를 생성하는 것이다')
print('   함수 호출과 문법이 동일하다 --')
h = Hello() # 함수 호출과 문법이 동일하다

def func():
  return 'This is a string'

flags = [ True, False, True ]
for flag in flags:
  todo = Hello if flag else func
  obj = todo() # 함수 호출과 객체 생성이 동일한 문법 구조에 의해 일어난다
  print('flag 값은:', flag, '이번에 얻은 것은:', obj)

h1 = Hello()
h2 = Hello()
print('\n-- Python 의 class 객체는 임의의 속성(멤버변수) 을 런타임에 추가할 수 있다 --')
h1.name = 'David'
h2.age = 20
for obj in h1, h2:
  for attr in 'name', 'age':
    has = '있다' if hasattr(obj, attr) else '없다'
    print(f'객체 {obj} 는 속성 {attr} 이 {has}')

print('\n-- 생성될때부터 속성을 가지고 있게 하려면 생성자(constructor) 를 만든다 --')
class World:
  def __init__(self): # C++/Java 의 this 대신 self 를 사용한다. 멤버함수는 첫번째 인자가 self 이다.
    self.name = 'Unknown'
    self.age = 0
w1 = World()
print(f'name={w1.name}, age={w1.age}')
w2 = World()
w2.name = 'David'
print(f'name={w2.name}, age={w2.age}')

print('\n-- 객체에 종속된 동작을 하게 하려면 클래스 내에 함수를 정의한다 --')
class HelloWorld:
  def __init__(self, name='Unknown', age=0):
    self.name = name
    self.age = age
  def print(self):
    print(f'name={self.name}, age={self.age}')

hw1 = HelloWorld('David', 20)
hw2 = HelloWorld('John', 23)
hw1.print()
hw2.print()

print('\n-- Python 은 상속 없이도 Polymorphism 이 가능하다 --')
class Barista:
  def work(self):
    print("열심히 커피 만들어요")
class Casher:
  def work(self):
    print("주문 받고 돈받아요")
class Cleaner:
  def work(self):
    print("구석구석 깨끗이 청소해요")
workers = [ Barista(), Casher(), Cleaner() ]
for worker in workers:
  worker.work()