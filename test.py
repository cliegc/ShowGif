from PySide2.QtWidgets import QApplication
from gif_widget import GifWidget

_test_path = r"C:\Users\15310\Desktop\3525e1e9380593e4009a7d27169deefa1625714661167.gif"

app = QApplication()
win = GifWidget()
win.resize(960, 640)
win.load(_test_path)
win.show()
app.exec_()

