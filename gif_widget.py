from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, QPixmap
from PySide2.QtCore import QPoint
from gif import Gif


class GifWidget(QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.gif: Gif = None

    def paintEvent(self, event) -> None:
        if not self.gif: return super().paintEvent(event)

        painter = QPainter(self)

        pixmap: QPixmap = self.gif.current_pixmap
        x = (self.width() - pixmap.width()) / 2
        y = (self.height() - pixmap.height()) / 2

        painter.drawPixmap(QPoint(x, y), pixmap)

    def load(self, path: str):
        self.gif = Gif(path)
        self.gif.play(self)
