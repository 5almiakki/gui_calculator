import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.operand = 0
        self.operator = ''
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QHBoxLayout()
        layout_clear_equal = QHBoxLayout()
        layout_number = QGridLayout()
        layout_value = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        label_value = QLabel("Value: ")
        self.value = QLineEdit("")

        ### layout_value_value 레이아웃에 수식, 답 위젯을 추가
        layout_value.addRow(label_value, self.value)

        ### 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 모듈러, 역수, 제곱, 제곱근 버튼 생성
        button_modulo = QPushButton("%")
        button_inverse = QPushButton("1/x")
        button_square = QPushButton("x²")
        button_sqrt = QPushButton("√x")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        button_modulo.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_inverse.clicked.connect(lambda state, operation = "1/x": self.button_operation_clicked(operation))
        button_square.clicked.connect(lambda state, operation = "x^2": self.button_operation_clicked(operation))
        button_sqrt.clicked.connect(lambda state, operation = "x^(1/2)": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_plus)
        layout_operation.addWidget(button_minus)
        layout_operation.addWidget(button_product)
        layout_operation.addWidget(button_division)
        layout_operation.addWidget(button_modulo)
        layout_operation.addWidget(button_inverse)
        layout_operation.addWidget(button_square)
        layout_operation.addWidget(button_sqrt)

        ### =, clear, clear_equation, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_clear_equation = QPushButton("CE")
        button_backspace = QPushButton("Backspace")

        ### =, clear, clear_equation, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_clear_equation.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, clear_equation, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_clear_equation)
        layout_clear_equal.addWidget(button_clear)
        layout_clear_equal.addWidget(button_backspace)
        layout_clear_equal.addWidget(button_equal)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼과 +/- 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_plus_minus = QPushButton("+/-")
        button_plus_minus.clicked.connect(lambda state, operation = "+/-": self.button_operation_clicked(operation))
        layout_number.addWidget(button_plus_minus, 3, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_value)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        value = self.value.text()
        value += str(num)
        self.value.setText(value)

    def button_operation_clicked(self, operation):
        if operation == '1/x':
            value = 1 / float(self.value.text())
        elif operation == 'x^2':
            value = float(self.value.text()) ** 2
        elif operation == 'x^(1/2)':
            value = float(self.value.text()) ** (1/2)
        elif operation == '+/-':
            value = 0 - float(self.value.text())
        else:
            value = ''
            self.operand = float(self.value.text())
            self.operator = operation
        self.value.setText(str(value))

    def button_equal_clicked(self):
        value = float(self.value.text())
        if self.operator == '+':
            value = self.operand + value
        elif self.operator == '-':
            value = self.operand - value
        elif self.operator == '*':
            value = self.operand * value
        elif self.operator == '/':
            value = self.operand / value
        elif self.operator == '%':
            value = self.operand % value
        self.value.setText(str(value))

    def button_clear_clicked(self):
        self.value.setText("")
        self.value.setText("")

    def button_backspace_clicked(self):
        value = self.value.text()
        value = value[:-1]
        self.value.setText(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())