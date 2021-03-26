'''
언어를 깊게 배운다 -> 가장 큰 무기
Chapter 3
Python Advanced(3) - Meta Class(1)

[Keyword]
- Class of class
- Type, Meta Class
- Custom Meta Class
'''

'''
메타클래스
1. 클래스를 만드는 역할을 한다. -> 의도하는 방향으로 클래스를 커스텀하겠다!
2. 프레임워크 작성 시 필수! 
3. 동적 생성을 가능하게 한다 (type함수가), 커스텀 생성도 가능하게 한다(type함수가)
4. 커스텀 클래스 -> 검증 클래스 등을 만들 수 있다. 설게해놓은 원칙대로 클래스 생성이 가능
5. 엄격한 class 사용 요구 , 프레임워크는 뼈대니까 엄격하게 메타클래스를 바탕으로 선언해놓고,
그것을 가지고 커스텀마이징해서 쓸 수 있다. 
데이터베이스와 클래스를 1대1로 매칭해서 설계한다. 
메소드 오버라이드 요구도 가능하다.
'''


# Ex1
# type 예제

class SampleA():  # 런타임시 메모리에 클래스 자체가 올라간다.
    pass


obj1 = SampleA()
# 클래스를 인스턴스화했다
# 변수에 할당도 가능, 복사 가능, 새로운 속성 추가도 가능, 함수의 인자로 넘기기 가능

# obj1 -> SampleA instance
# SampleA -> type meta class
# type -> type meta class

print('Ex1 > ', obj1.__class__)
# Ex1 >  <class '__main__.SampleA'>

print('Ex1 >', type(obj1))
# Ex1 > <class '__main__.SampleA'>
print('Ex1 >', obj1.__class__ is type(obj1))
# Ex1 > True
print('Ex1 >', obj1.__class__.__class__)
# Ex1 > <class 'type'>
print('Ex1 >', obj1.__class__.__class__ is type(obj1).__class__)
# Ex1 > True

# 모든 클래스의 메타(원형)는 type 클래스다.
# type 클래스를 조작할 수 있다면, 필요한 클래스를 만들어낼 수 있다.
# 동적으로 변화해야하는 기능들은 메타클래스를 사용할 수 밖에 없다.

# 객체지향에서 Object는?
# 휴대폰, 컴퓨터, 사람 등등, 현실세계에 있는 오브젝트를 클래스 형태로 만드는 게 객체지향이다.
# 클래스와 객체라는 용어를 같이 사용한다. (파이썬에서는) Class == Object

# Ex2
# type meth (Ex1 증명)

# int, dict
n = 10  # int자체도 클래스
d = {'a': 10, 'b': 20}  # dict도 클래스, 파이썬에 존재하는 자료구조 형태는 클래스로 변환되서 실행된다.


class SampleB():
    pass


obj2 = SampleB()
for o in (n, d, obj2):
    print('Ex2 > {} {} {}'.format(type(o), type(o) is o.__class__, o.__class__.__class__))
    # Ex2 > <class '__main__.SampleB'> True <class 'type'>

print()

for t in int, float, list, tuple:
    print('Ex2 > {}'.format(type(t)))  # Ex2 >  <class 'type'>
print('Ex2 > ', type(type))  # Ex2 >  <class 'type'>
