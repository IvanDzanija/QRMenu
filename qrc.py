import qrcode

def qrgen():
    qr_code = qrcode.QRCode()
    qr_code.add_data("https://ivandzanija.github.io/weddingQRMenu/")
    qr_code.make(fit = True)
    image_qr = qr_code.make_image(fill_color = "black", back_color = "yellow")
    image_qr.save("qrcode.png")






