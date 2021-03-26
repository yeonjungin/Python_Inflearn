'''
언어를 깊게 배운다 -> 가장 큰 무기
Chapter 3
Python Advanced(3) - Meta Class(2)

클래스를 객체라고 생각하고,
클래스를 만들어내는 어떤것에 해당하는 게 메타클래스
메타를 기반으로 붕어빵 찍듯이 만드는 것이고
메타를 만들어내는 게 type이다.
type 자신의 메타는 자기 자신이다.
오픈 소스, 오픈 api , Django같은 것들이 메타클래스를 활용해서 만든 것

[Keyword]
- Type(name,base,dct) : type은 3개의 인자를 받음.
- Dynamic Metaclass
- 메타 클래스 코딩 이점

메타 클래스
1. 메타클래스 동적 생성 중요
2. 동적 생성한 메타 클래스 -> 커스텀 메타클래스 생성
3. 의도하는 방향으로 직접 클래스 생성에 관여할 수 있는 큰 장점이 있다. (범용적 프레임워크 필수적)
'''


# Ex1
# type 동적 클래스 생성 에제

# Name(클래스이름),Bases(상속되는 클래스), Dct(속성, 메소드)

class Sample1():
    pass


# >> 정적 클래스

s1 = type('sample1', (), {})  # >> 동적 클래스
print('Ex1 >', s1)  # Ex1 > <class '__main__.sample1'>
print('Ex1 > ', type(s1))  # Ex1 >  <class 'type'>
print('Ex1 >', s1.__base__)  # 클래스는 object 클래스를 상속받는다.
# Ex1 > <class 'object'>
print('Ex1 >', s1.__dict__)


# 동적 생성 + 상속
class Parent1:
    pass


class Sample2(Parent1):
    attr1 = 100
    attr2 = 'hi'


s2 = type(
    'sample2',
    (Parent1,),
    {'attr1': 100, 'attr2': 'hi'}
)  # {} == dict(attr1=100,attr2='hi')

print('Ex2 >', s2)
print('Ex2 >', type(s2))
print('Ex2 >', s2.__base__)
print('Ex2 >', s2.__dict__)
print('Ex2 >', s2.attr1, s2.attr2)

'''
Ex2 > <class '__main__.sample2'>
Ex2 > <class 'type'>
Ex2 > <class '__main__.Parent1'> parent1을 기반으로 만들어졌다.
Ex2 > {'attr1': 100, 'attr2': 'hi', '__module__': '__main__', '__doc__': None}
Ex2 > 100 hi
'''

print()


# Ex2 메소드도 동적으로 만들기!
# type 동적 클래스 생성 + 메소드

class SampleEx:  # 정적 클래스
    attr1 = 30
    attr2 = 100

    def add(self, n, m):
        return n + m

    def mul(self, n, m):
        return n * m


ex = SampleEx()
print('Ex3 > ', ex.attr1)
print('Ex3 > ', ex.attr2)
print('Ex3 > ', ex.add(100, 200))
print('Ex3 > ', ex.mul(100, 20))

s3 = type('sample3',
          (object,),
          dict(attr1=30, attr2=100, add=lambda x, y: x + y, mul=lambda x, y: x * y)
          )  # ()==(object,)

# 한 번 쓰고 말 함수는 lambda로!

print('Ex4 > ', s3.attr1)
print('Ex4 > ', s3.attr2)
print('Ex4 > ', s3.add(100, 200))
print('Ex4 > ', s3.mul(100, 20))

