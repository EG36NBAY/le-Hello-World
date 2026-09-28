import turtle
import time
sekil=turtle.Turtle()
kenarnum=int(input("Kenar Sayısı giriniz:\n"))
kenaraci=int(360/kenarnum)
kalinlik=int(input("Kalınlık giriniz\n"))
Uzunluk=int(input("Uzunluk giriniz:\n"))
icidolsun=str(input("İçi dolsun mu Y/N\n"))
sekil.pensize(kalinlik)


if icidolsun == "Y":
    sekil.begin_fill()

for i in range(kenarnum):
    sekil.forward(Uzunluk)
    sekil.left(kenaraci)

if icidolsun == "Y":
    sekil.end_fill()



turtle.done()
