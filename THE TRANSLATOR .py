#   THESE ARE IMPORTANT LIBRARIES   ----------------------------
from PyQt5.QtWidgets import *
from googletrans import Translator
import sys

# CREATE A LIST ( THE_TEXT ) TO MAKE A HISTORY
THE_TEXT = []

# CREATE TRANSLATOR ( translator )
translator = Translator()

# CREATE APPLICATION ( app ) AND WINDOW ( window )
app = QApplication(sys.argv)
window = QWidget()

# SET A WINDOW TITLE ( " The Translator Program in Python with Gui " )
window.setWindowTitle(" The Translator Program in Python with Gui ")

# CREATE LABEL 1 ( Label1 )
Label1 = QLabel(" < b > The Translator  < / b > ", window)
Label1.move(625, 100)
Label1.show()

# CREATE LABEL 2 ( Label2 )
Label2 = QLabel(" < b > TRANSLATION FROM الترجمة من : < / b > ", window)
Label2.move(910, 130)
Label2.show()

# CREATE LABEL 3 ( Label3 )
Label3 = QLabel(" < b > TRANSLATION TO الترجمة إلي : < / b > ", window)
Label3.move(110, 150)
Label3.show()

# CREATE LINE EDIT 1 (L_E1)
L_E1 = QLineEdit(window)
L_E1.setGeometry(784, 175, 476, 200)
L_E1.setPlaceholderText(" Inter The Input Here ")
L_E1.show()

# SET THE DEFAULT LANGUAGE
from_l = "auto"
to = "ar"


# CREATE A FUNCTION TO THE RADIO BUTTON 1 (  chosen1() )
def chosen1():
    global from_l
    from_l = "auto"


# CREATE A FUNCTION TO THE RADIO BUTTON 2 (  chosen2() )
def chosen2():
    global from_l
    from_l = "en"


# CREATE A FUNCTION TO THE RADIO BUTTON 3 (  chosen3() )
def chosen3():
    global from_l
    from_l = "ar"


# CREATE A FUNCTION TO THE RADIO BUTTON 4 (  chosen4() )
def chosen4():
    global to
    to = "ar"


# CREATE A FUNCTION TO THE RADIO BUTTON 5 (  chosen5() )
def chosen5():
    global to
    to = "en"


# CREATE BUTTON GROUP 1 (b_g1)
b_g1 = QButtonGroup(window)

# CREATE BUTTON GROUP 2 (b_g2)
b_g2 = QButtonGroup(window)

# CREATE RADIO BUTTON 1 (r_b1)
r_b1 = QRadioButton(window)
r_b1.setText(" DETECT LANGUAGE الكشف عن اللغة ")
r_b1.move(1055, 150)
b_g1.addButton(r_b1)
r_b1.setChecked(True)
r_b1.toggled.connect(chosen1)

# CREATE RADIO BUTTON 2 (r_b2)
r_b2 = QRadioButton(window)
r_b2.setText(" ENGLISH اللغة الإنجليزية ")
r_b2.move(915, 150)
b_g1.addButton(r_b2)
r_b2.toggled.connect(chosen2)

# CREATE RADIO BUTTON 3 (r_b3)
r_b3 = QRadioButton(window)
r_b3.setText(" ARABIC اللغة العربية ")
r_b3.move(785, 150)
b_g1.addButton(r_b3)
r_b3.toggled.connect(chosen3)

# CREATE RADIO BUTTON 4 (r_b4)
r_b4 = QRadioButton(window)
r_b4.setText(" ARABIC اللغة العربية ")
r_b4.move(445, 150)
b_g2.addButton(r_b4)
r_b4.setChecked(True)
r_b4.toggled.connect(chosen4)

# CREATE RADIO BUTTON 5 (r_b5)
r_b5 = QRadioButton(window)
r_b5.setText(" ENGLISH اللغة الإنجليزية ")
r_b5.move(300, 150)
b_g2.addButton(r_b5)
r_b5.toggled.connect(chosen5)


# CREATE A FUNCTION TO THE PUSH BUTTON 1 (  on_click1() )
def on_click1():
    the_text = L_E1.text()

    # TO AVOID WHITESPACES AND NO WORDS
    n_o_s = (the_text.count(' '))
    l_o_w = len(the_text)

    if the_text == "" or the_text == " ":

        # CREATE A MESSAGE BOX 1 ( m_b1 ) TO WARNING
        m_b1 = QMessageBox()
        m_b1.move(520, 256)
        m_b1.setIcon(QMessageBox.Information)
        m_b1.setText(" PLEASE  ENTER  A  WORD  TO  TRANSLATE  IT  . ")
        m_b1.setInformativeText(" PRESS  OK  AND  TRY  AGAIN  . ")
        m_b1.setWindowTitle("Warning")
        m_b1.exec_()

    elif l_o_w == n_o_s:
        # CREATE A MESSAGE BOX 2 ( m_b2 ) TO WARNING
        m_b2 = QMessageBox()
        m_b2.move(450, 256)
        m_b2.setIcon(QMessageBox.Information)
        m_b2.setText("PLEASE  DON'T  ENTER  A SPACES , PLEASE  ENTER  A WORD  TO  TRANSLATE  IT .")
        m_b2.setInformativeText("PRESS  OK  AND  TRY  AGAIN  . ")
        m_b2.setWindowTitle("Warning")
        m_b2.exec_()

    else:

        # THE PROGRAM IS HERE

        try:

            # src=Source_language, dest=Destination_language
            translated = translator.translate(the_text, src=from_l, dest=to)
            THE_TEXT.append(the_text)
            THE_TEXT.append(translated.text)
            print(translated)
            L_E2.setText(translated.text)

        except:

            # TO SOLVE THE INTERNET PROBLEM
            THE_TEXT.append('make sure there is an internet connection')
            m_b2 = QMessageBox()
            m_b2.move(520, 256)
            m_b2.setIcon(QMessageBox.Critical)
            m_b2.setText(" MAKE  SURE  THERE  IS  AN  INTERNET  CONNECTION  . ")
            m_b2.setInformativeText(" PRESS  OK  AND  TRY  AGAIN  . ")
            m_b2.setWindowTitle("Warning")
            m_b2.exec_()


# CREATE PUSH BUTTON 1 (P_B1)
P_B1 = QPushButton(" Translate ", window)
P_B1.setGeometry(605, 260, 150, 40)
P_B1.setToolTip(" Click To Send The Input ")
P_B1.clicked.connect(on_click1)
P_B1.show()

# CREATE LINE EDIT 2 (L_E2)
L_E2 = QLineEdit(window)
L_E2.setGeometry(100, 175, 476, 200)
L_E2.setPlaceholderText("The result is here")
L_E2.show()

# SHOW
window.showMaximized()
app.exec_()

# _____________________________________________
#   THE PROGRAM HAS END
print(THE_TEXT)
