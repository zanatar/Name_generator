import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import generator  # Это наш конвертированный файл дизайна+++
import rusyllab
import os
import random
import string
import script

verbs_collection = []
verbs_counter = []
split = []

class NameGen(QtWidgets.QMainWindow, generator.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.BrouseButton.clicked.connect(self.Browse_folder)
##        self.pushButton.clicked.connect(self.Start)
##        self.listWidget_2.addItem(str(self.horizontalSlider.value()))
        self.checkList.stateChanged.connect(self.Enter_names)
        self.plainTextEdit.setEnabled(False)
        self.StartButton.clicked.connect(self.Start)
        self.pushButton.clicked.connect(self.LetterGen_Start)
        self.SaveButton_1.clicked.connect(self.Save_from_Verbs)
        self.SaveButton_2.clicked.connect(self.Save_from_Letter)
        self.SaveButton_3.clicked.connect(self.Save_to_file)
        self.CleanButton.clicked.connect(self.Clear)

##    def Start(self):
##        self.listWidget.clear()  # На случай, если в списке уже есть элементы
####        self.listWidget.addItem(self.lineEdit.text())
##        for x in range(self.horizontalSlider.value()):    
##            output = script.Parser(self.lineEdit.text(), self.lineEdit_2.text())
##            self.listWidget.addItem(str(output[0]+'   '+output[1]))
        
    def Clear(self):
        self.Results.clear()

        
    def Browse_folder(self): #Вылетает при закрытии окна без выбора!!!!
        self.listWidget.clear()  # На случай, если в списке уже есть элементы
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите текстовый файл", "","*.txt")
        self.plainTextEdit.setEnabled(True)
        f = open(file[0])
        x = f.read().lower().replace(',', '').split()
        self.plainTextEdit.setPlainText(str(x))
        self.checkList.setChecked(True)
        f.close()
        
    def Enter_names(self):
        if self.checkList.isChecked() == True:
            self.plainTextEdit.setEnabled(True)
        else:
            self.plainTextEdit.setEnabled(False)

##    def Start(self):
##        if self.checkScand.isChecked() == True:
##            self.Exec('scand_names.txt') 
##            else:
##                self.Exec('scand_names_f.txt')
##        ##исправить на класс с подклассом parser
                
    def Start(self):
        global verbs_collection
        global split
        verbs_collection = []
        split = []
        self.listWidget.clear()
        if self.checkScand.isChecked() == True:
            self.Parser('scand_names.txt')
        if self.checkGreece.isChecked() == True:
            self.Parser('greece_names.txt')
        if self.checkJewish.isChecked() == True:
            self.Parser('jewish_names.txt')
        if self.checkSlav.isChecked() == True:
            self.Parser('slav_names.txt')
        if self.checkCommon.isChecked() == True:
            self.Parser('common_names.txt')
        if self.checkList.isChecked() == True:
            self.Parser_input()
        if verbs_collection != []:
            for x in range(self.try_counter.value()):
                self.Generator()

    def Parser(self, txt):       
        f = open(txt)
        x = f.read().lower().replace(',', '').replace("'", "").replace("[", "").replace("]", "").replace(".", "").replace("(", "").replace(")", "").replace(";", "").replace(":", "").replace("-", "").split()
        for item in x:
            split = rusyllab.split_words(item.split())
            verbs_collection.extend(split)
        f.close()
        
    def Parser_input(self):
        x = self.plainTextEdit.toPlainText().lower().replace(',', '').replace("'", "").replace("[", "").replace("]", "").replace(".", "").replace("(", "").replace(")", "").replace(";", "").replace(":", "").replace("-", "").split()
        for item in x:
            split = rusyllab.split_words(item.split())
            verbs_collection.extend(split)

    def Generator(self):
        name = ''
        for y in range(self.verb_counter.value()):
            tmp = random.choice(verbs_collection)
            name += tmp
        self.Check(name)
    def Apostrof_add(self,name):
        vowel = ["а", "о", "у", "и", "э", "ы"]
        for x in range(len(name)):
            if name[x] == "ь" and name[x+1] in vowel:
                name = name[:x+1]+"`"+name[x+1:]
                return name
            else:
                return name
                
        

    def Check(self,name):
        name = self.Apostrof_add(name)
        if name != '':
            self.listWidget.addItem(str(name[0].upper()+name[1:]))



    def LetterGen_Start(self):
        self.listWidget_3.clear()  # На случай, если в списке уже есть элементы
##        self.listWidget.addItem(self.lineEdit.text())
        for x in range(self.try_counter_2.value()):   
            output = script.Parser(self.lineEdit.text(), self.lineEdit_2.text())
            self.listWidget_3.addItem(str(output[0]+'   '+output[1]))

    def Save_from_Verbs(self):
        items = []
        if self.listWidget.count() != 0:
            for x in range(self.listWidget.count()):
                item = self.listWidget.item(x)
                self.Results.addItem(item.text())

    def Save_from_Letter(self):
        items = []
        if self.listWidget_3.count() != 0:
            for x in range(self.listWidget_3.count()):
                item = self.listWidget_3.item(x)
                self.Results.addItem(item.text())


    def Save_to_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите текстовый файл", "","*.txt")
        f = open(file[0], 'a')
        if self.Results.count() != 0:
            for x in range(self.Results.count()):
                item = self.Results.item(x)
                f.write(item.text()+ '\n')
        f.close()
                
            
        
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = NameGen()  # Создаём объект класса ExampleApp
    window.show()
    app.exec_()
    

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
