# |이 코드는 클래스를 사용하여 사람과 AI 학생을 나타내는 두 개의 객체를 만들고, 그들의 속성을 출력하는 예제입니다.
# |
# |좋은 점:
# |- 클래스를 사용하여 객체를 만들어서 코드의 가독성이 높아졌습니다.
# |- 생성자 함수를 사용하여 객체를 초기화하고, 객체의 속성을 설정할 수 있습니다.
# |
# |나쁜 점:
# |- 클래스 이름이 Ai_Students와 같이 대문자로 시작하지 않아서, PEP 8 스타일 가이드에 어긋납니다.
# |- Person 클래스와 Ai_Students 클래스가 중복되는 속성을 가지고 있어서, 코드의 중복이 발생합니다. 이를 해결하기 위해서는 상속을 사용하거나, 공통된 속성을 가진 클래스를 만들어서 코드의 중복을 줄일 수 있습니다.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Ai_Students:
  def __init__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex

p1 = Person("John", 36)
p2 = Ai_Students("김정헌", 345, "man")

print(p1.name, p1.age)
print(p2.name, p2.age, p2.sex)



