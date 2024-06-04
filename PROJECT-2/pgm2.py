import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)
link = input("Enter link here: ")
qr.add_data(link)
qr.make(fit=True)
fill_cl = input("Enter fill colour: ")
back_cl = input("Enter background colour: ")
img = qr.make_image(fill_color=fill_cl, back_color=back_cl)
img.save("qrcode.png")
