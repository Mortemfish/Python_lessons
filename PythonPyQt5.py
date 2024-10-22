import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Устанавливаем заголовок окна
        self.setWindowTitle('Сигналы и слоты')

        # Создаем вертикальный layout
        self.layout = QVBoxLayout()

        # Создаем метку
        self.label = QLabel('Нажмите кнопку')
        self.label.setAlignment(Qt.AlignCenter)  # Центрируем текст метки
        self.label.setStyleSheet("font-size: 18px; color: blue;")  # Стили для метки
        self.layout.addWidget(self.label)

        # Создаем кнопку
        self.button = QPushButton('Нажми меня')
        self.button.setStyleSheet("background-color: lightgray; font-size: 16px;")  # Стили для кнопки
        self.button.clicked.connect(self.on_button_click)  # Привязываем сигнал нажатия к слоту
        self.layout.addWidget(self.button)

        # Устанавливаем layout на окно
        self.setLayout(self.layout)

    # Слот для обработки нажатия на кнопку
    def on_button_click(self):
        self.label.setText('Кнопка нажата!')

        # Динамически меняем стили
        self.button.setStyleSheet("background-color: green; color: white; font-size: 20px;")
        self.label.setStyleSheet("font-size: 24px; color: red;")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Создаем и показываем окно
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
