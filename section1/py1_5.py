'''
Chapter1 Python Advanced(1) - Context Manager(2) 자원의 할당과 반환을 담당
Keyword : 전체 복습, 타이머 클래스 실습, Contextlib 구현
타이머 클래스 : 함수의 실행시간을 알 수 있다.
'''

# Ex1
# Use Class
import time


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

with ExcuteTimer('Start! job!!') as v:
    print('Received start monotonic1 : {}'.format(v))
    # Excute job
    # 여기에 원하는 함수, 테스트 하고 싶은 코드를 넣는다.
    for i in range(10000000):
        pass
    raise Exception('Raise! Exception!!') #강제로 발생