'''

Chapter2
Python Advanced(2) - Context Manager Annotation
keyword : @contextlib.contextmanager, __enter__, __exit__

'''

'''
가장 대표적인 with 구문 이해
Contextlib 데코레이터 사용
코드 직관적이고, 예외 처리가 용이해진다.

'''

import contextlib
import time


# Ex1
# Use Decorator
# 함수가 클래스보다 재사용성이 더 좋다.

@contextlib.contextmanager
def my_file_writer(file_name, method):
    f = open(file_name, method)
    yield f  # __enter__
    f.close()  # __exit__
    # decorator 사용하면서 간단해진 코드,
    # generator 조사하기


with my_file_writer('testfile4.txt', 'w') as f:
    f.write('Context Manager Test4.\n Contextlib test4.')

'''
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
        
'''


# Ex2
# Use decorator

@contextlib.contextmanager  # 이 데코레이터를 사용하면서 자원 할당, ~ 분석이 가능해짐
def ExcuteTimerDc(msg):
    start = time.monotonic()
    try:  # __enter__
        yield start
    except BaseException as e:
        print('Loggin Exception {} : {}'.format(msg, e))
        raise
    else:  # __exit__
        print('{} : {}s'.format(msg, time.monotonic() - start))


with ExcuteTimerDc('Start Job!') as v:
    print('Received start monotonic2 : {}'.format(v))
    # Excute job
    for i in range(100000000):
        pass
    #raise
    raise ValueError('occured.')
'''
class ExcuteTimer(object):  # 모든 클래스는 object를 할당받는다. (생략해도 됌)
    def __init__(self, msg):
        self._msg = msg

    def __enter__(self):
        self._start = time.monotonic()  # 시간을 숫자형태로 가져와서, 저장
        return self._start  # with문에 들어오는 시점이 저장된다.

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:  # 예외 : 프로그램 처리에 문제, 에러 : pc정전, 하드디스크 문제 같은 상황 (물리적인 문제)
            print("Logging exception {}".format((exc_type, exc_val, exc_tb)))
        else:
            print('{} : {} s'.format(self._msg, time.monotonic() - self._start))
        return True  # 정확히 with문을 빠져나왔음을 의미
'''
