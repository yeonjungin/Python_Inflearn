'''
Chapter 4
Python Advanced(4) - 나만의 패키지 만들기 (3) PyPI 배포!
keyword : PyPI, build, package deploy
'''

from py4_2 import GifConverter as gfc

# 클래스 생성
c = gfc('../section4/image/*.jpg', '../section4/image_out/result1.gif', (320, 240))

# 실행
c.convert_gif()

'''
패키지 배포 순서(PyPI)
1. https://pyp1.org 회원가입
2. 프로젝트 구조 확인
3. __init__.py
4. 프로젝트 Root 필수 파일 작성
    - README.md
    - setup.py
    - setup.cfg(optional)
    - LICENSE
    - NAMIFEST.in
5. pip install setuptools wheel
> 파일을 압축해서 실행파일 형식으로 올려주는 역할이 wheel
> setup파일을 실행해서 바리바리 압축을 해주는 역할
    설치1 - python -m pip install --upgrade setuptools wheel
    설치2 - python -m pip install --user --upgrade setuptools wheel
    빌드 - python setup.py sdist : sdist  bdist_wheel 폴더가 만들어진다.
6. PyPI 배포
설치 : pip install twine > 파이썬 권장
업로드 : python -m twine upload dist/*

7. 설치확인
> python
>> from 패키지명.파일명 import 클래스명
>> dir(클래스명)

'''
