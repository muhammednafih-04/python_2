import qrcode
d="https://www.MARVEL.com"
qr=qrcode.make(d)
qr.save("google_qrcode.png")


'''import qrcode
d=input("enter url:")
qr=qrcode.make(d)
qr.save("user_qrcode.png")
print("code generated")'''
