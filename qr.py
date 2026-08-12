import qrcode
d="https://github.com/muhammednafih-04/portfolio/blob/main/pro.html"
qr=qrcode.make(d)
qr.save("google_qrcode.png")


'''import qrcode
d=input("enter url:")
qr=qrcode.make(d)
qr.save("user_qrcode.png")
print("code generated")'''
