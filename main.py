

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtGui
from math import *

L32 = [32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448, 480, 512, 544]
L42 = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630, 672, 714]
L53 = [53, 106, 159, 212, 265, 318, 371, 424, 477, 530, 583, 636, 689, 742, 795, 848, 901]
L63 = [63, 126, 189, 252, 315, 378, 441, 504, 567, 630, 693, 756, 819, 882, 945, 1008, 1071]
L73 = [73, 146, 219, 292, 365, 438, 511, 584, 657, 730, 803, 876, 949, 1022, 1095, 1168, 1241]
L83 = [83, 166, 249, 332, 415, 498, 581, 664, 747, 830, 913, 996, 1079, 1162, 1245, 1328, 1411]

#=========PySide Gui===========
class Main(QDialog):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        #===Main Window size/ GUI
        self.setGeometry(400,400,650,300)
        #===Background Color/ HTML #....
        self.setStyleSheet("font-size:14px; background-color:; border: 0.5px solid #B5B5B5 ; border: 0.5px solid #B5B5B5 ; color:#919192")
        #===
        self.label1 = QLabel("Unesi sirinu jezgre (mm):")
        self.label1.setFrameStyle(QFrame.Panel | QFrame.StyledPanel)  # Frame|Sirina
        self.label1.setLineWidth(2)  # Visina Izbocenja
        self.label2 = QLabel("Unesi broj redova (4 - 19):")
        self.label3 = QLabel("Lista Izracuna :")
        self.label2.setFrameStyle(QFrame.Panel | QFrame.StyledPanel)  # Frame|Red
        self.display = QTextBrowser()  # Result display
        self.display2 = QTextBrowser()  # Stored List
        self.lineedit1 = QLineEdit()  # S
        self.lineedit2 = QLineEdit()  # RED
        #===
        #layout = QVBoxLayout()
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)  # ( Razmak  widgeta )
        grid.addWidget(self.label1, 1, 0)  #
        grid.addWidget(self.lineedit1, 2, 0)
        grid.addWidget(self.label2, 3, 0)
        grid.addWidget(self.lineedit2, 4, 0)
        grid.addWidget(self.display, 5, 0)
        grid.addWidget(self.label3, 1, 1, 1, 1)
        grid.addWidget(self.display2, 2, 1, 4, 1)  # ( 1red | 2stupac | 5polja | stretch)
        self.setLayout(grid)  # (layout)
        #===
        self.lineedit1.setFocus()

        self.connect(self.lineedit1,SIGNAL("returnPressed()"),self.width_row)
        self.connect(self.lineedit2,SIGNAL("returnPressed()"),self.width_row)
        self.setWindowTitle("Calculator")

    def width_row(self):
        global width
        global row
        try:
            width = self.lineedit1.text()
            row = self.lineedit2.text()
            self.m_input()
        except:
            pass
            #self.display.append("<font color=red> %s is invalid</font>" % width)
            #self.display.append("<font color=red> %s is invalid</font>" % row)

    def m_input(self):#=========Main Code/Calculation===
        self.display.clear()
        global S
        global Red
        global SRed
        global Rz
        global V
        global x
        try:
            #S = int(raw_input("Unesi sirinu _cm :"))
            S = int(width)
            Red = int(row)
            SRed = S, Red
            self.display2.append(" %s | %s :" % (SRed))

            #Red = int(raw_input("Unesi broj redova _"))
            if S <= 0 or Red <= 0: # True sends back to m_input()/False continues ...
                #return "Unjeli ste nula ili negativan iznos ..."
                self.display.append("Unjeli ste nula ili negativan iznos ...")
                exit()
                self.m_input()
            elif S > 2200 or Red > 19:
                #return "Unos veci od maximuma (220cm)..."
                self.display.append("Unos veci od maximuma (2200mm)...")
                exit()
                self.m_input()
            elif Red <= 3:
                #print "Minimalni broj redova je 4 !"
                self.display.append("Minimalni broj redova je 4 !")
                exit()
                self.m_input()
            elif S < 330:
                #print "Minimana sirina je 330mm "
                self.display.append("Minimana sirina je 330mm ")
                exit()
                self.m_input()
            else:
                pass
            Rz = Red - 1
            V = 50*Red
            x = S - 37 - V
            self.L32L42()
            self.L42L53()
            self.L53L63()
            self.L63L73()
            self.L73L83()
        except TypeError:
            #print "Oops!  That was no valid number.  Try again..."
            self.display.append("Oops!  That was no valid number.  Try again...")
            exit()
            self.m_input()
        except ValueError:
            #return "Ups prazan unos !"
            self.display.append("Ups prazan unos !")
            exit()
            self.m_input()

    def L32L42(self):
        global c
        global d
        global R
        if  (L32[0] * Rz) == x:
            print "*",Rz ,"Razmaka od" , "32mm"
            exit("")
        if  (L42[0] * Rz) == x:
            print "*",Rz , "Razmaka od" , "42mm"
            exit("")
        else:
            for a in L32:
                for b in L42:
                    c = a/32;d = b/42
                    E = c+d;E1 = a+b
                    if E == Rz:
                        if E1-x <= 8 :
                            if E1-x > -8:
                                R = ("%s Razmaka od $s mm, %s Razmaka od %s mm" % (c, L32[0], d, L42[0]))
                                self.display.append(R)
                                #print c ,"Razmaka od", "32mm","+", d,"Razmaka od", "42"
                                self.DB()

    def L42L53(self):
        global c
        global d
        global R
        if  (L42[0] * Rz) == x:
            print "*",Rz ,"Razmaka od" , "42mm"
            exit("")
        if  (L53[0] * Rz) == x:
            print "*",Rz , "Razmaka od" , "53mm"
            exit("")
        else:
            for a in L42:
                for b in L53:
                    c = a/42;d = b/53
                    E = c+d;E1 = a+b
                    if E == Rz:
                        if E1-x <= 8 :
                            if E1-x > -8:
                                R = ("%s Razmaka od %s mm, %s Razmaka od %s mm" % (c, L42[0], d, L53[0]))
                                self.display.append(R)
                                #print c ,"Razmaka od", "42mm","+", d,"Razmaka od", "53mm"
                                self.DB()

    def L53L63(self):
        global c
        global d
        global R
        if  (L53[0] * Rz) == x:
            print "*",Rz ,"Razmaka od" , "53mm"
            exit("")
        if  (L63[0] * Rz) == x:
            print "*",Rz , "Razmaka od" , "63mm"
            exit("")
        else:
            for a in L53:
                for b in L63:
                    c = a/53; d = b/63
                    E = c+d ;E1 = a+b
                    if E == Rz:
                        if E1-x <= 8 :
                            if E1-x > -8:
                                    R = ("%s Razmaka od %s mm, %s Razmaka od %s mm" % (c, L53[0], d, L63[0]))
                                    self.display.append(R)
                                    #self.display.append("%s Razmaka od %s, %s Razmaka od %s" % (c, L53, d, L63))
                                    #print c ,"Razmaka od", "53mm","+", d,"Razmaka od", "63"
                                    self.DB()

    def L63L73(self):
        global c
        global d
        global R
        if  (L63[0] * Rz) == x:
            print "*",Rz ,"Razmaka od" , "63mm"
            exit("")
        if  (L73[0] * Rz) == x:
            print "*",Rz , "Razmaka od" , "73mm"
            exit("")
        else:
            for a in L63:
                for b in L73:
                    c = a/63;d = b/73
                    E = c+d;E1 = a+b
                    if E == Rz:
                        if E1-x <= 8 :
                            if E1-x > -8:
                                R = ("%s Razmaka od %s mm, %s Razmaka od %s mm" % (c, L63[0], d, L73[0]))
                                self.display.append(R)
                                #print c ,"Razmaka od", "63mm","+", d,"Razmaka od", "73"
                                self.DB()

    def L73L83(self):
        global c
        global d
        global R
        if  (L73[0] * Rz) == x:
            print "*",Rz ,"Razmaka od" , "73mm"
            exit("")
        if  (L83[0] * Rz) == x:
            print "*",Rz , "Razmaka od" , "83mm"
            exit("")
        else:
            for a in L73:
                for b in L83:
                    c = a/73;d = b/83
                    E = c+d;E1 = a+b
                    if E == Rz:
                        if E1-x <= 8 :
                            if E1-x > -8:
                                R = ("%s Razmaka od %s mm, %s Razmaka od %s mm" % (c, L73[0], d, L83[0]))
                                self.display.append(R)
                                #print c ,"Razmaka od", "73mm","+", d,"Razmaka od", "83mm"
                                self.DB()
    def  DB(self):
        DBS = {}
        DBS[SRed] = R
        self.display2.append(R)
        self.display2.append("**********")

app = QApplication(sys.argv)
form = Main()
form.show()
app.exec_()
