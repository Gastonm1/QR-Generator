import qrcode

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#013220", back_color="white")
    img.save(file_name)

if __name__ == '__main__':
    text = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWloM2Q5ZXh0dnI2dnlvamhkMDVzODd6Z2o2Ynh2eGU2MDM3NjVydSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTiIzJSKB4l7xTouE8/giphy.gif"
    file_name = 'hello_there_qr_code.png'

    generate_qr_code(text, file_name)
    print(f"QR Code saved as {file_name}")