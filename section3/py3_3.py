'''
Chapter 3.
Chapter 3
Python Advanced(3) - Meta Class(3)

:keyword
1. Type inheritance(상속)
2. Custom Meta class > type 클래스를 상속받으면, 커스텀 메타 클래스 생성!
3. 메타 클래스 상속 실습
'''

'''
메타클래스 상속
1. type 클래스 상속
2. metaclass 속성 사용
3. 커스텀 메타 클래스 생성
    - 클래스 생성 가로채기
    - 클래스 수정
    - 클래스 개선(기능추가)
    - 수정된 클래스 반환

'''


# Ex1
# 커스텀 메타 클래스 생성 예제(type 상속x)

def cus_mul(self, d):  # self는 인스턴스 자기 자신, 리스트!
    for i in range(len(self)):
        self[i] = self[i] * d


def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


# list를 상속받는 메소드를 2개 추가한 커스텀 메타 클래스
CustomList1 = type('CustomeList1',
                   (list,),  # 리스트 상속
                   dict(desc='커스텀 리스트1', cus_mul=cus_mul, cus_replace=cus_replace))

c1 = CustomList1([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 초기화 진행 => 인스턴스화
c1.cus_mul(1000)

print('Ex1 >', c1)
# Ex1 > [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]

c1.cus_replace(1000, 7777)
print('Ex1 >', c1)
print('Ex1 >', c1.desc)  # Ex1 > 커스텀 리스트1
print('Ex1 > ', dir(c1))


# Ex2
# 커스텀 메타클래스 생성 예제(Type 상속 o)

# class MetaClassName(type):
# def __new__(netacls, name, bases,namespace)

# 내부적 실행 원리를 코드로 풀어쓴 것
# new-> init -> call : 실행순서
class CustomListMeta(type):
    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print('__init__ ->', self, object_or_name, bases, dict)
        super().__init__(object_or_name, bases, dict)

    # 인스턴스 실행
    def __call__(self, *args, **kwargs):
        print('__call__ ->', self, *args, **kwargs)
        return super().__call__( *args, **kwargs)

    # 클래스 인스턴스 생성(메모리 초기화)
    def __new__(metacls, name, bases, namespace):
        print('__init__ ->', metacls, name, bases, namespace)
        namespace['desc'] = '커스텀 리스트2'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace

        return type.__new__(metacls, name, bases, namespace)


CustomeList2 = CustomListMeta(
    'CustomList2',
    (list,),
    {}
)

c2 = CustomeList2([1, 2, 3, 4, 5, 6, 7, 8, 9])
c2.cus_mul(1000)
c2.cus_replace(1000, 7777)
print('Ex2 >', c2)
print('Ex2 >', c2.desc)


# 상속 확인
print(CustomeList2.__mro__)
# (<class '__main__.CustomList2'>, <class 'list'>, <class 'object'>)
# CustomList2는 list를 상속했고, list는 object를 상속했다.
