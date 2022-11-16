#Soru: (x,y) şeklinde verilen bir üçgende sonradan verilen (x,y) ikililerin alanın
#içinde olup olmadığını kontrol eden program.

Ax = int(input("A noktasının x koordinatı?"))
Ay = int(input("A noktasının y koordinatı?"))

Bx = int(input("B noktasının x koordinatı?"))
By = int(input("B noktasının y koordinatı?"))

Cx = int(input("C noktasının x koordinatı?"))
Cy = int(input("C noktasının y koordinatı?"))

Dx = int(input("Aranacak noktanın x koordinatı?"))
Dy = int(input("Aranacak noktanın y koordinatı?"))

bx = Bx-Ax
by = By-Ay
cx = Cx-Ax
cy = Cy-Ay
x = Dx-Ax
y = Dy-Ay

d = (bx*cy)-(cx*by)

WA = (x*(by-cy) + y*(cx-bx) + bx*cy-cx*by)/d
WB = (x*cy - y*cx)/d
WC = (y*bx - x*by)/d

if WA<1 and WA>0 and WB<1 and WB>0 and WC<1 and WC>0:
    print("Nokta üçgenin içinde")
else:
    print("Nokta üçgenin içinde değil")

