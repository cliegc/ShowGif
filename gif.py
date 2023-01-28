from PIL import Image, ImageSequence, ImageQt
from PySide2.QtCore import QTimer


class Gif:

    def __init__(self, path: str) -> None:
        self.display_widget = None

        self.all_frames = ImageSequence.Iterator(Image.open(path))
        self.curr_index = 0
        self.curr_frame = self.all_frames[self.curr_index]

        self.timer = QTimer()
        self.timer.timeout.connect(self.__update_frame)

    def __update_frame(self):
        self.curr_frame = self.all_frames[self.curr_index]
        self.timer.setInterval(self.curr_frame.info["duration"])
        self.curr_index += 1
        if self.curr_index == self.curr_frame.n_frames:
            self.curr_index = 0
        self.display_widget.repaint()

    def play(self, display_widget):
        self.display_widget = display_widget
        self.timer.start()

    @property
    def current_pixmap(self):
        return ImageQt.toqpixmap(self.curr_frame)