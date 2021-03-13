"""
Chapter 1
Python Advanced(1) - lambda, Reduce, Map, Filter Functions
keyword - lambda, reduce, map, filter
빠른 연산 시간을 기대할 수 있는 함수들
"""

"""
lambda 장점 : 익명, 힙 영역사용 즉시 소멸 (메모리 아낄 수 있음), pythonic, 파이썬 가비지 컬렉션(불필요한 정보를 알아서 처리해줌),
익명이 왜 장점인가? **
일반함수 : 재사용성을 위해 메모리에 저장한다.
한 번 쓰고 말거다? lambda 사용 / 재사용할거면 일반 함수를 사용하기
시퀀스형 전처리에 Reduce, Map, Filter 주로 사용한다.
시퀀스형 전처리? **
"""

# Ex1
# cul = lambda a,b,c : a*b+c #lambda 매개변수 : 리턴값
# print(cul(10,15,20))

# Ex2
# 리스트에 있는 모든 원소들을 내가 지정한 함수에 의해 수행된 결과를 iterator하게 객체로 넘겨주는 것
digits1 = [x * 10 for x in range(1, 11)]
print(digits1)

result = list(map(lambda i: i ** 2, digits1))  # map(func,list))
print('Ex2 >', result)  # map함수를 list로 감싸서 형변환 시켜야한다.


# Ex2_2
def also_square(nums):
    def double(x):
        return x ** 2

    return map(double, nums)


print('Ex2 > ', list(also_square(digits1)))

# Ex3 Filter
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, digits2))
print('Ex3 >', result)


def also_evens(nums):
    def is_evens(x):
        return x % 2 == 0

    return filter(is_evens, nums)


print('Ex3 >', list(also_evens(digits2)))

# Ex4
# reduce -> 여러 순회 가능한 시퀀스 데이터에서 누적으로 더하기, 합계를 해줄 때 사용
from functools import reduce

digits3 = [x for x in range(1, 101)]
result = reduce(lambda x, y: x + y, digits3)
# 결과값이 내가 지정해놓은 마지막 최종 결과값을 반환해준다.
# 문자열도 가능
print('Ex4 >', result)

def also_add(nums):
    def add_plus(x,y):
        return x+y
    return reduce(add_plus,nums)
print('Ex4 >', also_add(digits3))