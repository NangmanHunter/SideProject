import qrcode

data = "https://www.google.com/"

qr = qrcode.QRCode(
    version=1,  # QR 코드 크기 (1~40, 숫자가 클수록 크기가 커짐)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 오류 복원 수준
    box_size=10,  # 각 박스 크기
    border=4  # 테두리 크기
)
qr.add_data(data)
qr.make(fit=True)

# QR 코드 이미지를 생성하고 저장
img = qr.make_image(fill="black", back_color="white")
img.save("C:/github-nangmanhunter/ToyProject/02QRCodeGenerator/qrcode.png")

print("QR 코드가 'qrcode.png'로 저장되었습니다.")