import PyQt5.QtWidgets as qtw
from cashierdesigncode import Ui_MainWindow
class Main_window(qtw.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.apples_number_value = 0
        self.banana_number_value = 0
        self.guave_number_value = 0
        self.sukari_number_value = 0
        self.owesi_number_value = 0
        self.total_value = 0
        self.apples_button.clicked.connect(self.apples)
        self.bananas_button.clicked.connect(self.bananas)
        self.guaves_button.clicked.connect(self.guaves)
        self.mangosokari_button.clicked.connect(self.sukari)
        self.mangoowesi_button.clicked.connect(self.owesi)
    def apples(self):
            self.apples_number_value+=1
            self.total_value+=2.4
            self.update_display()
    def bananas(self):
            self.banana_number_value+=1
            self.total_value+=6
            self.update_display()
    def guaves(self):
            self.guave_number_value+=1
            self.total_value+=4.5
            self.update_display()
    def sukari(self):
            self.sukari_number_value+=1
            self.total_value+=4.5
            self.update_display()
    def owesi(self):
            self.owesi_number_value+=1
            self.total_value+=7
            self.update_display()
    def update_display(self):
        self.apples_number.display(self.apples_number_value)
        self.banana_number.display(self.banana_number_value)
        self.guave_number.display(self.guave_number_value)
        self.sukari_number.display(self.sukari_number_value)
        self.owesi_number.display(self.owesi_number_value)
        self.Total.display(self.total_value)


         
app=qtw.QApplication([])
application_window=Main_window()
application_window.show()
app.exec_()