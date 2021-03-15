'''

Python Advanced(1)
Context Manager(1)
Keyword : Contextlib, __enter__, __exit__ ( __ 는 매직메소드, 인스턴스가 초기화될 때
파이썬에서 정한 규칙대로 호출되는 것), exception, with 기능 직접 구현

'''

# 운영체제의 자원은 한정되어 있다.
# 컨텍스트 매니저 : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
# 가장 대표적인 with 구문 이해
# 정확한 이해 후 사용해야 함

# Ex1
file = open('./testfile1.txt', 'w')
try:
    file.write('Context manager test1\nContextlib texst1.')
finally:
    file.close()
    # 자원을 할당받았기에 다시 돌려줘야 낭비가 없다.

# Ex2
with open('./testfile2.txt', 'w') as f:
    f.write('Context manager test2\nContextlib texst2.')
    # f.close를 굳이 쓰지 않아도 알아서 자원 반환한다.
    # with 구문 추가 조사, 원리에 대해서도


# Ex3
# Use Class -> Context Manager with exception handling

class MyFileWriter():
    def __init__(self, file_name, method):
        print('MyFileWriter started : __init__')
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print('MyFileWriter started : __enter__')
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('MyFileWriter started : __exit__')
        if exc_type:
            print('Loggin exception {}'.format((exc_type, exc_val, exc_tb)))
        self.file_obj.close()


with MyFileWriter('./testfile3.txt', 'w') as f:
    f.write('Context manager test3\nContextlib text3.')



'''
[추가 조사]
with 구문, 매직 메서드
'''