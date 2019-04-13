from tkinter import *
from PIL import ImageTk,Image
import time
anim=Tk()
anim.title('Save Water')
c=Canvas(anim,width=900,height=500,bg='yellow')
c.pack()

#for tap
l=c.create_line(30,50,100,50,fill='black')
l2=c.create_line(100,50,120,90,fill='black')
l3=c.create_line(120,90,90,90,fill='black')
l4=c.create_line(90,90,80,70,fill='black')
l5=c.create_line(80,70,30,70,fill='black')
l6=c.create_line(30,70,30,50,fill='black')
l7=c.create_line(65,50,65,20,fill='black')
l8=c.create_line(40,20,90,20,fill='black')
l9=c.create_line(30,60,10,60,fill='black')
l10=c.create_line(30,65,15,65,fill='black')
l11=c.create_line(15,65,15,350,fill='black')
l12=c.create_line(10,60,10,350,fill='black')

#for drop
drop=c.create_oval(100,100,105,120,fill='blue')

#for hand
h1=c.create_line(-80,250,-150,250)
h2=c.create_line(-80,250,-50,200)
h3=c.create_line(-50,200,-90,230)
h4=c.create_line(-90,230,-150,230)
h5=c.create_line(-150,230,-200,300)
h6=c.create_line(-150,250,-185,300)

#for moving the drop 
for i in range(185):
     c.move(drop,0,1) #moves the drop from top to bottom
     anim.update()
     time.sleep(0.01) #moves the drop at an interval of  seconds
drop1=c.create_oval(95,100,100,120,fill='blue')
for i in range(185):
     c.delete(drop)
     c.move(drop1,0,1)
     anim.update()
     time.sleep(0.01)
drop2=c.create_oval(105,100,110,120,fill='blue')
for i in range(103):
     c.delete(drop1)
     c.move(drop2,0,1)
     anim.update()
     time.sleep(0.01)
     #for moving hand
     c.move(h1,2.2,0)
     c.move(h2,2.2,0)
     c.move(h3,2.2,0)
     c.move(h4,2.2,0)
     c.move(h5,2.2,0)
     c.move(h6,2.2,0)
     anim.update()
     t5=c.create_text(500,150,fill='darkblue',font='Times 30 italic bold',text='Water is Life')
time.sleep(4)    
c.delete('all') #deletes the canavas

s1=c.create_rectangle(0,0,900,500,fill='white')
b1=c.create_oval(110,90,210,180,fill='#FFE0BD')
b2=c.create_polygon(114,180,223,180,223,350,114,350,fill='yellow')
b3=c.create_polygon(114,350,100,450,150,450,165,350,fill='red')
b4=c.create_polygon(165,350,190,450,235,450,223,350,fill='red')
b5=c.create_polygon(100,450,50,470,150,470,150,450)
b6=c.create_polygon(235,450,285,470,190,470,190,450)
b7=c.create_polygon(114,180,30,300,80,300,130,220,fill='#FFE0BD')
b8=c.create_polygon(223,180,300,290,250,290,203,220,fill='#FFE0BD')
b9=c.create_arc(130,150,190,170,style=ARC,extent=180,fill='red',outline='red')
b11=c.create_oval(125,120,135,135,fill='black')
b10=c.create_arc(116,130,203,90,style=CHORD,extent=180,fill='black')
b12=c.create_oval(170,120,180,135,fill='black')

t=c.create_text(990,50,fill='purple',font='Times 20 bold',text='2 MILLION')
t1=c.create_text(1050,100,fill='black',font='Times 20 bold',text='PEOPLE\nMOSTLY CHILDREN')
t2=c.create_text(990,300,fill='red',font='Times 20 bold',text='DIE')
t3=c.create_text(990,300,fill='black',font='Times 20 bold',text='EACH')
t4=c.create_text(990,380,fill='black',font='Times 20 bold',text='YEAR FROM\nDIARRHEAL\n DISEASES\nALONE')

for i in range(100):
     c.move(t,-4,0)
     c.move(t1,-4,0)
     time.sleep(0.0001)
     anim.update()
time.sleep(2)
for i in range(100):
     c.move(t2,-4.75,0)
     c.move(t3,-4,0)
     c.move(t4,-4,0)
     time.sleep(0.0001)
     anim.update()
time.sleep(4)
c.delete('all')
s2=c.create_rectangle(0,0,900,500,fill='white')
t9=c.create_text(600,-15,font='Times 20 bold',text='OUT OF THE')
t10=c.create_text(620,-10,fill='green',font='Times 50 bold',text='3%')
t11=c.create_text(630,-5,font='Times 20 bold',text='FRESHWATER\nON EARTH')
t12=c.create_text(640,500,font='Times 20 bold',text='ONLY')
t13=c.create_text(650,550,fill='red',font='Times 50 bold',text='1%')
t14=c.create_text(660,600,font='Times 20 bold',text='IS AVAILABLE FOR HUMANS')
img = ImageTk.PhotoImage(Image.open("earth.jpg"))  
c.create_image(0, 0, anchor=NW, image=img)
for i in range(100):
     c.move(t9,0,1)
     c.move(t10,0,1.5)
     c.move(t11,0,2)
     time.sleep(0.0001)
     anim.update()
for i in range(100):
     c.move(t12,0,-2)
     c.move(t13,0,-2)
     c.move(t14,0,-2)
     time.sleep(0.0001)
     anim.update()
time.sleep(4)
c.delete('all')

img1 = ImageTk.PhotoImage(Image.open("sw.jpg"))  
c.create_image(0, 0, anchor=NW, image=img1)
t7=c.create_text(-60,50,fill='darkblue',font='Times 20 bold',text='SO \nCONSERVE WATER')
t8=c.create_text(990,200,fill='darkblue',font='Times 20 bold',text='CONSERVE LIFE')
for i in range(100):
     c.move(t7,3,0)
     c.move(t8,-3,0)
     time.sleep(0.0001)
     anim.update()
anim.mainloop()
