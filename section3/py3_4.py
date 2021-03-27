'''
Chapter3. Python Advanced(3) - Descriptor(1)
keyword
: Descriptor, Get, Set, Del, Property, Descriptor 필요한 이유

'''

'''
Descriptor
1. 객체(클래스)에서 서로 다른 객체를 속성값으로 가지는 것을 의미한다.
2. read,write,delete 등을 미리 정의 가능하다.
3. data descriptor(set,del), non-data descriptor(get)
non-data는 읽기만 함.
4. 읽기 전용 객체 생성 중심, 클래스를 의도하는 방향으로 생성 가능
& set,del,get 조사, descriptor에 대해 더 자세하게 조사.
왜 쓰는지?
'''


# Ex1
# 기본적인 Descriptor 예제
class DescriptorEx1(object):  # object를 써주는 이유
    def __init__(self, name="Default"):
        self.name = name

    def __get__(self, obj, objtype):
        return "Get method called -> self : {}, obj : {}, objtype : {}, name:{}".format(self, obj, objtype, self.name)

    def __set__(self, obj, name):
        print("set method called")
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string.")  # 추가조사, TypeError

    def __delete__(self, obj):
        print("Delete method called.")
        self.name = None


class Sample1(object):
    name = DescriptorEx1()  # 스페셜 메소드 추가 조사하기
    # 코드간결성, 재사용성 증가, 성능개선 -> descriptor 장점


s1 = Sample1()
# set 호출
s1.name = "Descriptor Test1"  # 알아서 문자열까지 체크하고 name 초기화까지..?
# obj가 이걸 가능하게 함

# s1.name=10 # TypeError: Name should be string.

# attr 확인
# __get__ 호출
print('Ex1 > ', s1.name)

# __delete__ 호출
del s1.name

# 재확인
# __get__ 호출
print('Ex1 > ', s1.name)

print()
print()


# orm 프로젝트를 만들 때 Descriptor를 쓴다!

# Ex2 : Property 클래스 사용, Descriptor 직접 구현
# class property(fget=None,fset=None,fdel=None,doc=None)
class DescriptorEx2(object):
    def __init__(self, value):
        self._name = value

    def getVal(self):
        return "Get method called. -> self:{}, name:{}".format(self, self._name)

    def setVal(self, value):
        print('Set method called. ')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError("Name should be string")

    def delVal(self):
        print("Delete method called.")
        self._name = None

    name = property(getVal, setVal, delVal, "Property 테스트를 하는 name필드입니다. 의미는 없어요 :) ")
    # 프로퍼티를 호출해서

s2=DescriptorEx2("Descriptor Test2")

# 최초 값 확인
print('Ex2 >',s2.name)

# setVal 호출
s2.name='Descriptor Test2 Method'

# 오류값 확인
# s2.name=10

#getVal 호출
print('Ex2>',s2.name)

#delete 호출
del s2.name

#재확인
#getVal 호출
print('Ex2 >',s2.name)

#doc 호출
print('Ex2 >',DescriptorEx2.name.__doc__)
