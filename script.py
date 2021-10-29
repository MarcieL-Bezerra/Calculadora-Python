
from PyQt5 import QtWidgets, uic

janela = QtWidgets.QApplication([])
interface = uic.loadUi("calculadora.ui")
num1 = 0
num2 = 0
op = ""

def num_1():
    if interface.txttela.text() == "":
        interface.txttela.setText("1")
    else:        
        linha1 = interface.txttela.text()+ "1"
        interface.txttela.setText(linha1)
        
def num_2():
        if interface.txttela.text() == "":
            interface.txttela.setText("2")
        else:
            linha1 = interface.txttela.text()+ "2"
            interface.txttela.setText(linha1)
def num_3():
         if interface.txttela.text() == "":
             interface.txttela.setText("3")
         else:
            linha1 = interface.txttela.text()+ "3"
            interface.txttela.setText(linha1)
def num_4():
         if interface.txttela.text() == "":
             interface.txttela.setText("4")
         else:
            linha1 = interface.txttela.text()+ "4"
            interface.txttela.setText(linha1)         
def num_5():
         if interface.txttela.text() == "":
             interface.txttela.setText("5")
         else:
             linha1 = interface.txttela.text()+ "5"
             interface.txttela.setText(linha1)
def num_6():
         if interface.txttela.text() == "":
             interface.txttela.setText("6")
         else:
             linha1 = interface.txttela.text()+ "6"
             interface.txttela.setText(linha1)
def num_7():
         if interface.txttela.text() == "":
             interface.txttela.setText("7")
         else:
             linha1 = interface.txttela.text()+ "7"
             interface.txttela.setText(linha1)
def num_8():
         if interface.txttela.text() == "":
             interface.txttela.setText("8")
         else:
             linha1 = interface.txttela.text()+ "8"
             interface.txttela.setText(linha1)
def num_9():
         if interface.txttela.text() == "":
             interface.txttela.setText("9")
         else:
             linha1 = interface.txttela.text()+ "9"
             interface.txttela.setText(linha1)
def num_0():
         if interface.txttela.text() == "":
             interface.txttela.setText("0.")
         else:
             linha1 = interface.txttela.text()+ "0"
             interface.txttela.setText(linha1)
def num_c():
          if op == "+":
             num2 = interface.txttela.text()
             calc1 = float (num1)
             calc2 = float (num2)
             som = calc1 + calc2
             interface.txttela.setText(str (som))
          elif op == "-":
             num2 = interface.txttela.text()
             calc1 = float (num1)
             calc2 = float (num2)
             som = calc1 - calc2
             interface.txttela.setText(str (som))
          elif op == "*":
             num2 = interface.txttela.text()
             calc1 = float (num1)
             calc2 = float (num2)
             som = calc1 * calc2
             interface.txttela.setText(str (som))
          elif op == "/":
             num2 = interface.txttela.text()
             calc1 = float (num1)
             calc2 = float (num2)
             som = calc1 / calc2
             interface.txttela.setText(str (som))
          else:
             interface.txttela.setText("")
         
def num_mai():
        if interface.txttela.text() == "":
             interface.txttela.setText("")
        else:
            global num1
            num1 = interface.txttela.text()
            global op
            op = "+"
            linha1 = ""
            interface.txttela.setText(linha1) 
        
def num_men():
         if interface.txttela.text() == "":
             interface.txttela.setText("")
         else:
            global num1
            num1 = interface.txttela.text()
            global op
            op = "-"
            linha1 = ""
            interface.txttela.setText(linha1)
def num_mul():
         if interface.txttela.text() == "":
             interface.txttela.setText("")
         else:
            global num1
            num1 = interface.txttela.text()
            global op
            op = "*"
            linha1 = ""
            interface.txttela.setText(linha1)
def num_div():
         if interface.txttela.text() == "":
             interface.txttela.setText("")
         else:
            global num1
            num1 = interface.txttela.text()
            global op
            op = "/"
            linha1 = ""
            interface.txttela.setText(linha1)
def num_per():
         if interface.txttela.text() == "":
             interface.txttela.setText("0.")
         else:
             linha1 = interface.txttela.text()+ "."
             interface.txttela.setText(linha1)         
def num_li():
         interface.txttela.setText("")
         
interface.Btn1.clicked.connect(num_1)
interface.Btn2.clicked.connect(num_2)
interface.Btn3.clicked.connect(num_3)
interface.Btn4.clicked.connect(num_4)
interface.Btn5.clicked.connect(num_5)
interface.Btn6.clicked.connect(num_6)
interface.Btn7.clicked.connect(num_7)
interface.Btn8.clicked.connect(num_8)
interface.Btn9.clicked.connect(num_9)
interface.Btn0.clicked.connect(num_0)
interface.Btnc.clicked.connect(num_c)

interface.Btnmai.clicked.connect(num_mai)
interface.Btnmen.clicked.connect(num_men)
interface.Btnmul.clicked.connect(num_mul)
interface.Btndiv.clicked.connect(num_div)
interface.Btnper.clicked.connect(num_per)
interface.Btnli.clicked.connect(num_li)

interface.show()
janela.exec()
