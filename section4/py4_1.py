'''
Chapter 4
python Advanced(4) - 나만의 패키지 만들기
keyword - opensource to gif, pil, image

'''

'''
패키지 작성
-> 정적이미지(jpg, png) -> gif(애니메이션 이미지 변환 패키지)

'''
import glob  # 폴더에 잇는 다양한 이미지들을 한 번에 가져와서 리스트 형태로 반환해줌
from PIL import Image

# 이미지, 결과 생성 경로
path_in = '../section4/image/*.jpg'  # 확장자 지정해주고 원하는 걸 뽑아올 수 있다
path_out = '../section4/image_out/result.gif'

# 첫 번째 이미지 & 모든 이미지 리스트
# img, *images = [Image.open(f) for f in sorted(glob.glob(path_in))]

# 이미지 크기 통일시키기
img, *images = [Image.open(f).resize((320,240),Image.ANTIALIAS) for f in sorted(glob.glob(path_in))]

# 이미지 저장
img.save(
    fp=path_out,
    format='GIF',
    append_images=images,
    save_all=True,
    duration=500,  # 크기가 클 수록 화면 전환 속도가 느려짐
    loop=0
)
