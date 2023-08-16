import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

choice = ""

def printoptions():
    print("Please pick an option from the following and enter the corresponding number! ")
    print("1. Store some data to a QR code")
    print("2. Read the data from a QR code")
    print("3. Quit out of the system")
    print()
    return input()

print("Hello and welcome to the QR code system!")

choice = printoptions()

while choice != "3":
    if choice == "1":
        print("Let's get storing!")
        print()
        data = input("please enter what you would like the qr code to read! ")

        change = input("Would you like to make any special adjustments to the formatting (y|n)? ")

        if change == "y":
            comp = input("please enter how complex you would like the qr to be (1 - 40)! ")
            size = input("please enter how large you would like the qr code to be (1 - 20)! ")
            bordersize = input("please enter how wide you would like the borders to be (0 - 20)! ")
        else:
            comp = 1
            size = 10
            bordersize = 5

        qr = qrcode.QRCode(version = int(comp), box_size = int(size), border = int(bordersize))
        qr.add_data(data)
        img = qr.make_image(fill_color = "black", back_color = "white")

        qr.make(fit=True)

        name = input("Please enter the name you'd like to assign to the new/overwritten QR code! ")
        img.save('C:/Users/david/OneDrive/Desktop/' + name + '.png')

        print("You got it! You're new QR code is on its way to the desktop now!")
        print()

    elif choice == "2":
        print("Let's get reading!")
        print()

        name = input("Please enter the name of the QR code you'd like to read, as it is named on your PC: ")
        result =  decode(Image.open('C:/Users/david/OneDrive/Desktop/' + name + '.png'))

        decoded = str(result[0].data)
        decoded = decoded.replace("b'","")
        decoded = decoded.replace("'","")

        print("The data within the QR code was: " + str(decoded))
        print()

    else:
        print("That wasn't one of the options!")
        print()

    choice = printoptions()

print("Thank you for using the QR code system!")
