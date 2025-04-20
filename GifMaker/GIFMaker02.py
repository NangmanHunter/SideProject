import imageio.v2 as imageio
from PIL import Image
import numpy as np  # 중요!

# 이미지 파일들
images = []
filenames = ["frame1.png", "frame2.png", "frame3.png"]

# 첫 이미지 기준 크기
base = Image.open(filenames[0])
width, height = base.size

for filename in filenames:
    img = Image.open(filename).resize((width, height))
    images.append(np.array(img))  # numpy 배열로 변환 후 저장

# GIF 생성
imageio.mimsave("output.gif", images, duration=1000)


'''
duration
- ms단위

'''