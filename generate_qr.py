import qrcode

# 要生成二维码的网页链接
url = "https://trans-for-learn.github.io/"

# 创建QRCode对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 将网页链接添加到QRCode对象中
qr.add_data(url)
qr.make(fit=True)

# 创建二维码图片
img = qr.make_image(fill_color="black", back_color="white")

# 保存二维码图片
img.save("webpage_qr_code.png")
