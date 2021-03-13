"""
Chapter 1
Python Advanced(1) - Python Variable Scope
Keyword - scope, global, nonlocal, locals, globals
"""

"""
전역변수는 주로 변하지 않는 고정 값에 사용한다. 
지역변수 사용 이유 : 지역변수는 함수 내에 로직 해결에 국한되어 있다.
지역변수의 소멸주기는 함수 실행 해제 시 
전역 변수를 주로 지역내에서 수정되는 것은 권장하지 않는다.
"""

# Ex1
a = 10  # global variable : 전역변수


def foo():
    # Read global variable
    print('Ex1 >', a)


foo()

# Read global variable
print('Ex1 >', a)

# Ex2
b = 20


def bar():
    b = 30  # local variable
    print('Ex2 >', b)  # Read local variable
    # 로컬 scope에서 먼저 찾고, 값이 없으면 밖으로 나가서 찾는다.
    # 따라서 b의 값은 30이 출력된다.


bar()
print('Ex2 >', b)  # Read global variable

# Ex3
c = 40


def foobar():
    # c = c + 10
    # c=10
    # c+=100
    # >> 예외 발생 시키는 예시
    # UnboundLocalError
    # 전역에 있는 값을 지역에서 어떠한 예약 없이 수정이 가능하다.
    print('Ex3 >', c)


foobar()

# Ex4
d = 50


def barfoo():
    global d  # global 사용을 자제하자. 유지보수시 좋지 않을 수 있기에
    d = 60
    d += 100
    print('Ex4 >', d)


barfoo()
print('Ex4 >', d)


# Ex5 : 코테에서도 나옴, 중요하다
def outer():
    e = 70

    def inner():
        # e += 10 #UnboundLocalError
        nonlocal e  # 상위 지역변수의 값을 수정할 땐 nonlocal을 사용한다.
        e += 10
        print('Ex5 >', e)

    return inner


# >> 클로저 알아볼 것
in_test = outer()  # Closure
in_test()
in_test()
in_test()


# Ex6
def func(var):
    x = 10

    def printer():
        print('Ex6 >', "Printer Func Inner")

    print("Func Inner", locals())
    # 해당 영역에 있는 모든것들을 딕션형태로 출력해주는 게 locals()
    # 지역 전체 출력

func('Hi')

# Ex7
print('Ex7 >', globals()) #전역 전체 출력
test_variable = 100
# globals()['test_variable']=100 이런식으로 내부에서 돌아간다.
print('Ex7 >', globals())

# 전역에 있는 값들을 다 출력해준다 globals()

# Ex8(지역 -> 전역 변수 생성)
for i in range(1,10):
    for k in range(1,10):
        globals()['plus_{}_{}'.format(i,k)]=i+k
print(globals())
print('Ex8> ',plus_5_5) #동적으로 변수 생성이 가능