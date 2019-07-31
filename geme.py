from tkinter import *
root=Tk()
x1=StringVar()
x2=StringVar()
x3=StringVar()
x4=StringVar()
x5=StringVar()
x6=StringVar()
x7=StringVar()
x8=StringVar()
x9=StringVar()
g1=0
g2=2
g3=3
g4=4
g5=5
g6=6
g7=7
g8=8
g9=9
var = 0
w1=0
w2=0
w3=0
w4=0
w5=0
w6=0
w7=0
w8=0
w9=0
u=0
la=StringVar()
can=Canvas(root)
lab=Label(root,textvariable=la)
lab.place(x=0,y=120)
def fun1(event):
    global var
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    global g8
    global g9
    global w1
    global w2
    global w3
    global u
    w1=1
    if g1==0 :
      if var%2==0:
            x1.set("X")
            g1 = 1
      else:
            x1.set("O")
            g1 = 10
    if u==0:
      if w1==w2 and w2==w3 and w3==w4 and w5==w4 and w5==w6 and w6==w7 and w7==w8 and w8==w9 :
        la.set("draw")
    if ((g1 == g2)and(g2 == g3))or((g1 == g5)and(g5 == g9))or((g1 == g4)and(g4 == g7))or((g3 == g5)and(g5 == g7))or((g3 == g6)and(g6 == g9))or((g7 == g8)and(g8 == g9))or((g4 == g5)and(g5 == g6))or((g2==g5)and(g5==g8)):
       la.set("win")
       if ((g1 == g2)and(g2 == g3)):
         can.create_line(10,10,60,10)
       if ((g1 == g5)and(g5 == g9)):
           can.create_line(10, 10, 60, 60)
       if (g1 == g4)and(g4 == g7):
           can.create_line(10,10,10,60)
       if (g3 == g5)and(g5 == g7) :
           can.create_line(70, 10, 10, 70)
       if (g3 == g6)and(g6 == g9):
           can.create_line(70, 10, 70, 70)
       if (g7 == g8) and (g8 == g9) :
           can.create_line(10, 70, 70, 70)
       if (g4 == g5)and(g5 == g6):
           can.create_line(10, 40, 60, 40)
       if (g2==g5)and(g5==g8):
            can.create_line(40, 10, 40, 60)
       u = 1
       g1 = 20
       g2 =30
       g3 =40
       g4 =50
       g5 =60
       g6 =70
       g7 =80
       g8 =90
       g9 = 100
    var+=1

def fun2(event):
    global var
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    global g8
    global g9
    global w2
    global w3
    global u
    w2= 1
    if g2 == 2:
     if var%2==0:
            x2.set("X")
            g2 = 1
     else:
            x2.set("O")
            g2 = 10
    if u == 0:
        if w1==w2 and w2==w3 and w3==w4 and w5==w4 and w5==w6 and w6==w7 and w7==w8 and w8==w9 :
          la.set("draw")
    if ((g1 == g2)and(g2 == g3))or((g1 == g5)and(g5 == g9))or((g1 == g4)and(g4 == g7))or((g3 == g5)and(g5 == g7))or((g3 == g6)and(g6 == g9))or((g7 == g8)and(g8 == g9))or((g4 == g5)and(g5 == g6))or((g2==g5)and(g5==g8)):
       la.set("win")
       u = 1
       if ((g1 == g2) and (g2 == g3)):
           can.create_line(10, 10, 60, 10)
       if ((g1 == g5) and (g5 == g9)):
           can.create_line(10, 10, 60, 60)
       if (g1 == g4) and (g4 == g7):
           can.create_line(10, 10, 10, 60)
       if (g3 == g5) and (g5 == g7):
           can.create_line(70, 10, 10, 70)
       if (g3 == g6) and (g6 == g9):
           can.create_line(70, 10, 70, 70)
       if (g7 == g8) and (g8 == g9):
           can.create_line(10, 70, 70, 70)
       if (g4 == g5) and (g5 == g6):
           can.create_line(10, 40, 60, 40)
       if (g2 == g5) and (g5 == g8):
           can.create_line(40, 10, 40, 60)
       g1 = 20
       g2 = 30
       g3 = 40
       g4 = 50
       g5 = 60
       g6 = 70
       g7 = 80
       g8 = 90
       g9 = 100
    var+=1

def fun3(event):
    global var
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    global g8
    global g9
    global w3
    global u
    w3= 1
    if g3 == 3:
     if var%2==0:
            x3.set("X")
            g3 = 1
     else:
            x3.set("O")
            g3 = 10
    if u == 0:
        if w1==w2 and w2==w3 and w3==w4 and w5==w4 and w5==w6 and w6==w7 and w7==w8 and w8==w9 :
         la.set("draw")
    if ((g1 == g2)and(g2 == g3))or((g1 == g5)and(g5 == g9))or((g1 == g4)and(g4 == g7))or((g3 == g5)and(g5 == g7))or((g3 == g6)and(g6 == g9))or((g7 == g8)and(g8 == g9))or((g4 == g5)and(g5 == g6))or((g2==g5)and(g5==g8)):
       la.set("win")
       u = 1
       if ((g1 == g2) and (g2 == g3)):
           can.create_line(10, 10, 60, 10)
       if ((g1 == g5) and (g5 == g9)):
           can.create_line(10, 10, 60, 60)
       if (g1 == g4) and (g4 == g7):
           can.create_line(10, 10, 10, 60)
       if (g3 == g5) and (g5 == g7):
           can.create_line(70, 10, 10, 70)
       if (g3 == g6) and (g6 == g9):
           can.create_line(70, 10, 70, 70)
       if (g7 == g8) and (g8 == g9):
           can.create_line(10, 70, 70, 70)
       if (g4 == g5) and (g5 == g6):
           can.create_line(10, 40, 60, 40)
       if (g2 == g5) and (g5 == g8):
           can.create_line(40, 10, 40, 60)
       g1 = 20
       g2 = 30
       g3 = 40
       g4 = 50
       g5 = 60
       g6 = 70
       g7 = 80
       g8 = 90
       g9 = 100
    var+=1

def fun4(event):
    global var
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    global g8
    global g9
    global w4
    global u
    w4= 1
    if g4 == 4:
     if var%2==0:
            x4.set("X")
            g4 = 1
     else:
            x4.set("O")
            g4 = 10
    if u == 0:
       if w1 == w2 and w2 == w3 and w3 == w4 and w5 == w4 and w5 == w6 and w6 == w7 and w7 == w8 and w8 == w9:
           la.set("draw")
    if ((g1 == g2)and(g2 == g3))or((g1 == g5)and(g5 == g9))or((g1 == g4)and(g4 == g7))or((g3 == g5)and(g5 == g7))or((g3 == g6)and(g6 == g9))or((g7 == g8)and(g8 == g9))or((g4 == g5)and(g5 == g6))or((g2==g5)and(g5==g8)):
       la.set("win")
       u = 1
       if ((g1 == g2) and (g2 == g3)):
           can.create_line(10, 10, 60, 10)
       if ((g1 == g5) and (g5 == g9)):
           can.create_line(10, 10, 60, 60)
       if (g1 == g4) and (g4 == g7):
           can.create_line(10, 10, 10, 60)
       if (g3 == g5) and (g5 == g7):
           can.create_line(70, 10, 10, 70)
       if (g3 == g6) and (g6 == g9):
           can.create_line(70, 10, 70, 70)
       if (g7 == g8) and (g8 == g9):
           can.create_line(10, 70, 70, 70)
       if (g4 == g5) and (g5 == g6):
           can.create_line(10, 40, 60, 40)
       if (g2 == g5) and (g5 == g8):
           can.create_line(40, 10, 40, 60)
       g1 = 20
       g2 = 30
       g3 = 40
       g4 = 50
       g5 = 60
       g6 = 70
       g7 = 80
       g8 = 90
       g9 = 100
    var+=1

def fun5(event):
    global var
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    global g8
    global g9
    global w5
    global u
    w5= 1
    if g5 == 5:
     if var%2==0:
            x5.set("X")
            g5 = 1
     else:
            x5.set("O")
            g5 = 10
    if u == 0:
      if w1==w2 and w2==w3 and w3==w4 and w5==w4 and w5==w6 and w6==w7 and w7==w8 and w8==w9 :
        la.set("draw")
    if ((g1 == g2)and(g2 == g3))or((g1 == g5)and(g5 == g9))or((g1 == g4)and(g4 == g7))or((g3 == g5)and(g5 == g7))or((g3 == g6)and(g6 == g9))or((g7 == g8)and(g8 == g9))or((g4 == g5)and(g5 == g6))or((g2==g5)and(g5==g8)):
       la.set("win")
       u = 1
       if ((g1 == g2) and (g2 == g3)):
           can.create_line(10, 10, 60, 10)
       if ((g1 == g5) and (g5 == g9)):
           can.create_line(10, 10, 60, 60)
       if (g1 == g4) and (g4 == g7):
           can.create_line(10, 10, 10, 60)
       if (g3 == g5) and (g5 == g7):
           can.create_line(70, 10, 10, 70)
       if (g3 == g6) and (g6 == g9):
           can.create_line(70, 10, 70, 70)
       if (g7 == g8) and (g8 == g9):
           can.create_line(10, 70, 70, 70)
       if (g4 == g5) and (g5 == g6):
           can.create_line(10, 40, 60, 40)
       if (g2 == g5) and (g5 == g8):
           can.create_line(40, 10, 40, 60)
       g1 = 20
       g2 = 30
       g3 = 40
       g4 = 50
       g5 = 60
       g6 = 70
       g7 = 80
       g8 = 90
       g9 = 100
    var+=1

def fun6(event):
    global var
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    global g8
    global g9
    global w6
    global u
    w6= 1
    if g6 == 6:
     if var%2==0:
            x6.set("X")
            g6 = 1
     else:
            x6.set("O")
            g6 = 10
    if u == 0:
      if w1==w2 and w2==w3 and w3==w4 and w5==w4 and w5==w6 and w6==w7 and w7==w8 and w8==w9 :
        la.set("draw")
    if ((g1 == g2)and(g2 == g3))or((g1 == g5)and(g5 == g9))or((g1 == g4)and(g4 == g7))or((g3 == g5)and(g5 == g7))or((g3 == g6)and(g6 == g9))or((g7 == g8)and(g8 == g9))or((g4 == g5)and(g5 == g6))or((g2==g5)and(g5==g8)):
       la.set("win")
       u = 1
       if ((g1 == g2) and (g2 == g3)):
           can.create_line(10, 10, 60, 10)
       if ((g1 == g5) and (g5 == g9)):
           can.create_line(10, 10, 60, 60)
       if (g1 == g4) and (g4 == g7):
           can.create_line(10, 10, 10, 60)
       if (g3 == g5) and (g5 == g7):
           can.create_line(70, 10, 10, 70)
       if (g3 == g6) and (g6 == g9):
           can.create_line(70, 10, 70, 70)
       if (g7 == g8) and (g8 == g9):
           can.create_line(10, 70, 70, 70)
       if (g4 == g5) and (g5 == g6):
           can.create_line(10, 40, 60, 40)
       if (g2 == g5) and (g5 == g8):
           can.create_line(40, 10, 40, 60)
       g1 = 20
       g2 = 30
       g3 = 40
       g4 = 50
       g5 = 60
       g6 = 70
       g7 = 80
       g8 = 90
       g9 = 100
    var+=1

def fun7(event):
    global var
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    global g8
    global g9
    global w7
    global u
    w7 = 1
    if g7 == 7:
     if var%2==0:
            x7.set("X")
            g7 = 1
     else:
            x7.set("O")
            g7 = 10
    if u == 0:
      if w1==w2 and w2==w3 and w3==w4 and w5==w4 and w5==w6 and w6==w7 and w7==w8 and w8==w9 :
        la.set("draw")
    if ((g1 == g2) and (g2 == g3)) or ((g1 == g5) and (g5 == g9)) or ((g1 == g4) and (g4 == g7)) or ((g3 == g5) and (g5 == g7)) or ((g3 == g6) and (g6 == g9)) or ((g7 == g8) and (g8 == g9)) or ((g4 == g5) and (g5 == g6))or((g2==g5)and(g5==g8)):
            la.set("win")
            u = 1
            if ((g1 == g2) and (g2 == g3)):
                can.create_line(10, 10, 60, 10)
            if ((g1 == g5) and (g5 == g9)):
                can.create_line(10, 10, 60, 60)
            if (g1 == g4) and (g4 == g7):
                can.create_line(10, 10, 10, 60)
            if (g3 == g5) and (g5 == g7):
                can.create_line(70, 10, 10, 70)
            if (g3 == g6) and (g6 == g9):
                can.create_line(70, 10, 70, 70)
            if (g7 == g8) and (g8 == g9):
                can.create_line(10, 70, 70, 70)
            if (g4 == g5) and (g5 == g6):
                can.create_line(10, 40, 60, 40)
            if (g2 == g5) and (g5 == g8):
                can.create_line(40, 10, 40, 60)
            g1 = 20
            g2 = 30
            g3 = 40
            g4 = 50
            g5 = 60
            g6 = 70
            g7 = 80
            g8 = 90
            g9 = 100
    var+=1

def fun8(event):
    global var
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    global g8
    global g9
    global w8
    global u
    w8 = 1
    if g8 == 8:
     if var%2==0:
            x8.set("X")
            g8 = 1
     else:
            x8.set("O")
            g8 = 10
    if u == 0:
      if w1==w2 and w2==w3 and w3==w4 and w5==w4 and w5==w6 and w6==w7 and w7==w8 and w8==w9 :
        la.set("draw")
    if ((g1 == g2) and (g2 == g3)) or ((g1 == g5) and (g5 == g9)) or ((g1 == g4) and (g4 == g7)) or ((g3 == g5) and (g5 == g7)) or ((g3 == g6) and (g6 == g9)) or ((g7 == g8) and (g8 == g9)) or ((g4 == g5) and (g5 == g6))or((g2==g5)and(g5==g8)):
            la.set("win")
            u = 1
            if ((g1 == g2) and (g2 == g3)):
                can.create_line(10, 10, 60, 10)
            if ((g1 == g5) and (g5 == g9)):
                can.create_line(10, 10, 60, 60)
            if (g1 == g4) and (g4 == g7):
                can.create_line(10, 10, 10, 60)
            if (g3 == g5) and (g5 == g7):
                can.create_line(70, 10, 10, 70)
            if (g3 == g6) and (g6 == g9):
                can.create_line(70, 10, 70, 70)
            if (g7 == g8) and (g8 == g9):
                can.create_line(10, 70, 70, 70)
            if (g4 == g5) and (g5 == g6):
                can.create_line(10, 40, 60, 40)
            if (g2 == g5) and (g5 == g8):
                can.create_line(40, 10, 40, 60)
            g1 = 20
            g2 = 30
            g3 = 40
            g4 = 50
            g5 = 60
            g6 = 70
            g7 = 80
            g8 = 90
            g9 = 100
    var+=1

def fun9(event):
    global var
    global g1
    global g2
    global g3
    global g4
    global g5
    global g6
    global g7
    global g8
    global g9
    global w9
    global u
    w9 = 1
    if g9 == 9:
     if var%2==0:
            x9.set("X")
            g9 = 1
     else:
            x9.set("O")
            g9 = 10
    if u == 0:
      if w1==w2 and w2==w3 and w3==w4 and w5==w4 and w5==w6 and w6==w7 and w7==w8 and w8==w9 :
        la.set("draw")
    if ((g1 == g2) and (g2 == g3)) or ((g1 == g5) and (g5 == g9)) or ((g1 == g4) and (g4 == g7)) or ((g3 == g5) and (g5 == g7)) or ((g3 == g6) and (g6 == g9)) or ((g7 == g8) and (g8 == g9)) or ((g4 == g5) and (g5 == g6))or((g2==g5)and(g5==g8)):
        la.set("win")
        u=1
        if ((g1 == g2) and (g2 == g3)):
            can.create_line(10, 10, 60, 10)
        if ((g1 == g5) and (g5 == g9)):
            can.create_line(10, 10, 60, 60)
        if (g1 == g4) and (g4 == g7):
            can.create_line(10, 10, 10, 60)
        if (g3 == g5) and (g5 == g7):
            can.create_line(70, 10, 10, 70)
        if (g3 == g6) and (g6 == g9):
            can.create_line(70, 10, 70, 70)
        if (g7 == g8) and (g8 == g9):
            can.create_line(10, 70, 70, 70)
        if (g4 == g5) and (g5 == g6):
            can.create_line(10, 40, 60, 40)
        if (g2 == g5) and (g5 == g8):
            can.create_line(40, 10, 40, 60)
        g1 = 20
        g2 = 30
        g3 = 40
        g4 = 50
        g5 = 60
        g6 = 70
        g7 = 80
        g8 = 90
        g9 = 100
    var+=1


can.place(anchor=NW)
can.create_line(25,0,25,80)
can.create_line(55,0,55,80)
can.create_line(0,25,80,25)
can.create_line(0,55,80,55)

label1=Label(can,textvariable=x1)
label1.bind("<Button-1>",fun1)
label1.place(x=0,y=0,width=25)
label2=Label(can,textvariable=x2)
label2.bind("<Button-1>",fun2)
label2.place(x=30,y=0,width=25)
label3=Label(can,textvariable=x3)
label3.bind("<Button-1>",fun3)
label3.place(x=60,y=0,width=25)
label4=Label(can,textvariable=x4)
label4.bind("<Button-1>",fun4)
label4.place(x=0,y=30,width=25)
label5=Label(can,textvariable=x5)
label5.bind("<Button-1>",fun5)
label5.place(x=30,y=30,width=25)
label6=Label(can,textvariable=x6)
label6.bind("<Button-1>",fun6)
label6.place(x=60,y=30,width=25)
label7=Label(can,textvariable=x7)
label7.bind("<Button-1>",fun7)
label7.place(x=0,y=60,width=25)
label8=Label(can,textvariable=x8)
label8.bind("<Button-1>",fun8)
label8.place(x=30,y=60,width=25)
label9=Label(can,textvariable=x9)
label9.bind("<Button-1>",fun9)
label9.place(x=60,y=60,width=25)

root.mainloop()