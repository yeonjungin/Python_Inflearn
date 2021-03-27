'''
Chapter 3. Descriptor(2)
keyword
- Descriptor vs Property >> 차이점
- Low level(descriptor) vs high level(Property)

'''

'''
디스크립터
1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
2. Property와 달리 reuse(재사용) 가능
3. ORM 프레임워크 사용에도 중요하다.
'''

# Ex1
# Descriptor Ex1
import os


class DirectoryFileCount:  # = Descriptor 역할, 재사용이 가능하게 함
    def __get__(self, obj, objtype=None):
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))


class DirectoryPath:
    # Descriptor instance
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname


# 현재 경로에 있는 파일 개수
s = DirectoryPath('./')  # 상대경로

# 이전 경로
g = DirectoryPath('../')

# 헷갈릴 때 출력 용도
print('Ex1 >', dir(DirectoryPath))
print('Ex1 >', DirectoryPath.__dict__)
# 클래스로 접근해서 dict 구조를 보는 게 가장 정확하다.

print(s.size)
print(g.size)

# Ex2
# 로그 출력 예제
import logging

logging.basicConfig(
    format='%(asctime)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)


class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value

    def __get__(self, obj, objtype=None):
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value

    def __set__(self, obj, value):
        logging.info('Updating %r giving %r', 'score', self.value)
        self.value = value


class Student:
    # Descriptor instance
    score = LoggedScoreAccess()  # 변할 때마다 중요한 필드만 작성

    def __init__(self, name):
        # Regulart instance attribute 인스턴스 변수
        self.name = name


s1 = Student('kim')
s2 = Student('lee')

# 점수 확인
print('Ex2 > ', s1.score)
# 2021-03-26 11:22:55 Accessing 'score' giving 50

s1.score += 20
print('Ex2 > ', s1.score)

# db를 연결하면, 무결성 있게 관리할 수 있다.

# 점수 출력2
print('Ex2 > ', s2.score)
# 2021-03-26 11:22:55 Accessing 'score' giving 50

s2.score += 30
print('Ex2 > ', s2.score)

# __dict__출력
print('Ex2 >',vars(s1)) # 필요한 인스턴스 변수만 확인할 수 있게 함.
print('Ex2 >',vars(s2))
print('Ex2 >',s1.__dict__)
print('Ex2 >',s2.__dict__)
