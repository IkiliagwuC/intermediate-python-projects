import qrcode

qr = qrcode.QRCode(
    version = 1, 
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)

qr.add_data("https://docs.python.org/3/library/__main__.html#:~:text=level%20code%20environment-,__main__%20%E2%80%94%20Top%2Dlevel%20code%20environment,py%20file%20in%20Python%20packages.")
img = qr.make_image()

img.save("pydocsQRcode.jpg")

# optional
# pip install qrcode[pil] to edit the colora
#img= qr.make_image(fill_color = 'green', back_color = 'white')
