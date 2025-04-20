from PIL import Image

filenames = ["frame1.png", "frame2.png", "frame3.png"]
frames = [Image.open(fn) for fn in filenames]

# 첫 프레임을 기준으로 나머지 이어붙이기
frames[0].save(
    "output.gif",
    format="GIF",
    save_all=True,
    append_images=frames[1:],
    duration=500,     # 각 프레임당 500ms
    loop=0            # 0이면 무한 반복
)
