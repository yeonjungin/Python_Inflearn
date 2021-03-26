'''
Chapter2. Property(1) - Underscore
keyword: Python Underscore, 다양한 언더스코어 사용, 접근지정자 이해
'''

'''
다양한 언더스코어 활용
파이썬 접근지정자 설명
'''

# Ex1
# Use underscore
# 1. 인터프리터 , 2. 값 무시, 3. 네이밍에 따라서 접근 지정자가 달라진다. (구체화, 자릿수)

# Unpacking -> packing, unpacking 추가 조사 필요 &&
x, _, y = (1, 2, 3)
print(x, y)  # result= 1,3

a, *_, b = (1, 2, 3, 4, 5)
print(a, b)  # result=1,5

for _ in range(10):  # 로직만 10번 돌릴 때
    pass

for _, val in enumerate(range(10)):
    pass


# Ex2
# 접근지정자 네이밍 규칙 && 추가 조사 필요
# name : public
# _name : protected
# __name : private, 캡슐화 추가 조사 필요
# 파이썬-> Public은 강제가 아니다. 약속된 규약에 따라 코딩을 장려한다. (자유도 책임감 장려)
# 자바나 고랭은 private 변수 값을 변경못하지만, 파이썬은 할 수 있다.
# 타 클래스 (클래스 변수, 인스턴스 변수 값 쓰기 장려 안한다) -> Naming Mangling  추가조사 &&
# 타 클래스에서는 __로 시작하는 변수는 접근하지 않는 게 원칙이다.
# 파이써닉 추가 조사 &&

# No user Property
class SampleA:
    def __init__(self):
        self.x = 0  # public 변수
        self.__y = 0  # private 변수
        self._z = 0  # protected 변수


a = SampleA()  # 인스턴스화
a.x = 1

print('Ex2 > x : {}'.format(a.x))
# print('Ex2 > y : {}'.format(a.__y))
# 'SampleA' object has no attribute '__y'
# #SampleA는 __y라는 속성을 가지고 있지 않다.
print('Ex2 > z : {}'.format(a._z))

print('Ex2 > ', dir(a))  # '_SampleA__y'

a._SampleA__y = 2  # 수정은 가능하지만 약속된 규약이니까 바꾸지 말자
print('Ex2 > y : {}'.format(a._SampleA__y))  # y=2


# Ex3
# 직접 접근하지 않고 값 수정할 때? : 메소드 활용 : Getter, Setter &&

class SampleB():
    def __init__(self):
        self.x = 0
        self.__y = 0  # _SampleB__y

    def get_y(self):  # 이렇게 하면 _SampleB__y 이런식으로 직접 접근을 안 해도 됌
        return self.__y

    def set_y(self, value):
        self.__y = value

b=SampleB()
b.x=1
b.set_y(2)
print('Ex3 > x : {} , y : {}'.format(b.x,b.get_y()))

#*****************************************#
# packing
def my_family(father,mother,*siblings):
    print('아버지 : {}'.format(father))
    print('어머니 : {}'.format(mother))
    count=0
    for sibling in siblings:
        count+=1
        print('형제자매{} : {}'.format(count,sibling))
my_family('홍길동','심사임당','김태희','윤아')

#unpacking
def my_family_unpacking(father,mother,I):
    print(father+","+mother+","+I)
family=['hong','kim','park']
my_family_unpacking(*family)
#hong,kim,park

#unpacking2
def cal(first,op,second):
    if op=='+':
        return first+second
    if op=='-':
        return first-second
    if op=='/':
        return first/second
    if op=='*':
        return first*second

prob={
    'first':12,
    'op':'*',
    'second':10
}
print(cal(**prob))

#enumerate
fruits=['apple','banana','strawberry']
for idx,fruit in enumerate(fruits):
    print('{} : {}'.format(idx,fruit))

# enumerate을 이용하면, len을 쓰지 않아도 인덱스를 가져올 수 있다.
# enumerate(arr,start=number)로 시작 번호도 정할 수 있다.

#iterator (반복자)
name='kim'
it_name=iter(name)
print(next(it_name))
print(next(it_name))
print(next(it_name))
#print(next(it_name)) #StopIteration

def three_generator():
    a=[1,2,3]
    yield from a # iterable한 객체를 yield 할땐 yield from iterable로 값 전달 가능
gen=three_generator()
print(list(gen))



