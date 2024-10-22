import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QSlider, QVBoxLayout, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        # Инициализация медиаплеера
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # Устанавливаем заголовок окна
        self.setWindowTitle("Минималистичный видеоплеер")
        self.setGeometry(100, 100, 800, 600)

        # Создаем виджет для видео
        self.video_widget = QWidget()
        self.setCentralWidget(self.video_widget)

        # Создаем кнопки управления
        self.create_controls()

        # Устанавливаем соединения
        self.media_player.positionChanged.connect(self.update_slider)
        self.media_player.durationChanged.connect(self.update_duration)

    def create_controls(self):
        # Основной layout
        layout = QVBoxLayout()

        # Кнопка выбора файла
        self.select_button = QPushButton("Выбрать видео")
        self.select_button.clicked.connect(self.open_file)
        layout.addWidget(self.select_button)

        # Метка для отображения пути к видео
        self.label = QLabel("Выберите видео файл")
        layout.addWidget(self.label)

        # Кнопки управления
        self.play_button = QPushButton("Воспроизвести")
        self.play_button.clicked.connect(self.play_video)
        layout.addWidget(self.play_button)

        self.pause_button = QPushButton("Пауза")
        self.pause_button.clicked.connect(self.pause_video)
        layout.addWidget(self.pause_button)

        self.stop_button = QPushButton("Остановить")
        self.stop_button.clicked.connect(self.stop_video)
        layout.addWidget(self.stop_button)

        # Ползунок для регулировки времени
        self.slider = QSlider(Qt.Horizontal)
        self.slider.sliderMoved.connect(self.set_position)
        layout.addWidget(self.slider)

        # Ползунок для регулировки громкости
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)  # Устанавливаем начальную громкость на 50
        self.volume_slider.valueChanged.connect(self.set_volume)
        layout.addWidget(self.volume_slider)

        # Устанавливаем layout на виджет
        self.video_widget.setLayout(layout)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Выбрать видео файл", "", "Video Files (*.mp4 *.avi *.mov)")
        if file_name:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.label.setText(file_name)

    def play_video(self):
        self.media_player.play()

    def pause_video(self):
        self.media_player.pause()

    def stop_video(self):
        self.media_player.stop()

    def set_volume(self, volume):
        self.media_player.setVolume(volume)

    def set_position(self, position):
        self.media_player.setPosition(position)

    def update_slider(self, position):
        self.slider.setValue(position)

    def update_duration(self, duration):
        self.slider.setRange(0, duration)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Создаем и показываем видеоплеер
    player = VideoPlayer()
    player.show()

    sys.exit(app.exec_())
