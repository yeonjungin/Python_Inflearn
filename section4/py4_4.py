'''
Chapter 4
Python Advanced(4) - 나만의 패키지 만들기 Github 배포!
keyword : Github, build, package deploy
'''

from py4_2 import GifConverter as gfc

# 클래스 생성
c = gfc('../section4/image/*.jpg', '../section4/image_out/result1.gif', (320, 240))

# 실행
c.convert_gif()

'''
패키지 배포 순서(Github)


'''
