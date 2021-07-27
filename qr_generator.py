import qrcode
site = input("Enter the site name in which you want to go through QR_Code: ")
img = qrcode.make(f"https://www.{site}.com/")
img.save(f"{site}Qr.jpg")