import sys
import main

from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QRadioButton,
    QListWidget,
    QPushButton,
    QHBoxLayout,
    QMessageBox
)

name_list = main.name_list()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GOODSTUDY WORDS TEST")
        self.resize(600,300)
        self.setStyleSheet("background-color: white;")

        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        topLayout = QFormLayout()
        # Add a label and a line edit to the form layout
        self.lineedit = QLineEdit(self)
        self.lineedit.textChanged.connect(self.upate_name)

        topLayout.addRow("학생 이름 : ", self.lineedit)
        # Create a layout for the checkboxes
        optionsLayout = QVBoxLayout()
        # Add some checkboxes to the layout

        elementary = QRadioButton('초등부', self)
        elementary.toggled.connect(self.update)

        middleschool = QRadioButton('중등부', self)
        middleschool.toggled.connect(self.update)

        highschool = QRadioButton('고등부', self)
        highschool.toggled.connect(self.update)

        optionsLayout.addWidget(elementary)
        optionsLayout.addWidget(middleschool)
        optionsLayout.addWidget(highschool)

        self.list_widget = QListWidget(self)
        self.list_widget.addItems(name_list)
        # self.list_widget.itemClicked.connect(self.listClicked)

        listLayout = QVBoxLayout()
        listLayout.addWidget(self.list_widget)

        print_answer_button = QPushButton('정답지 출력', self)
        print_answer_button.clicked.connect(self.popup_answer)
        print_test_button = QPushButton('시험지 출력', self)
        print_test_button.clicked.connect(self.popup_test)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(print_answer_button)
        buttonLayout.addWidget(print_test_button)


        outerLayout.addLayout(optionsLayout)
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(listLayout)
        outerLayout.addLayout(buttonLayout)
        
        self.setLayout(outerLayout)

    def upate_name(self, input):
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            item.setHidden(input not in item.text())

    def popup_answer(self):
        selReadName = []
        for r in self.list_widget.selectedItems():
            selReadName.append(str(r.text()))

        selectedName = selReadName[0]
        msg = QMessageBox(text="정답지를 출력합니다.")
        msg.setWindowTitle("정답지 출력")
        msg.setIcon(QMessageBox.Icon.Information)

        msg.setInformativeText("{}".format(main.show_term(selectedName)))
        ret = msg.exec()

    def popup_test(self):
        selReadName = []
        for r in self.list_widget.selectedItems():
            selReadName.append(str(r.text()))

        selectedName = selReadName[0]
        msg = QMessageBox(text="시험지를 출력합니다.")
        msg.setWindowTitle("시험지 출력")
        msg.setIcon(QMessageBox.Icon.Information)

        msg.setInformativeText("{}".format(main.show_term(selectedName)))
        ret = msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())