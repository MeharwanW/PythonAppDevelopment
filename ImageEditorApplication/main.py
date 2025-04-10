from PyQt5.QtWidgets import QWidget , QApplication , QLabel , QPushButton , QListWidget , QComboBox , QHBoxLayout , QVBoxLayout
from PyQt5.QtCore import Qt


app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Image Editor Application")
main_window.resize(900 ,900)

btn_folder = QPushButton("Directory")
file_list = QListWidget()




contrast = QPushButton("Contrast")
sharpness = QPushButton("Sharpness")
blur = QPushButton("Blur")
left = QPushButton("Left")
right = QPushButton("Right")
mirror = QPushButton("Mirror")


filter_box = QComboBox()
filter_box.addItem("Original")
filter_box.addItem("contrast")
filter_box.addItem("sharpness")
filter_box.addItem("blur")
filter_box.addItem("left")
filter_box.addItem("right")
filter_box.addItem("mirror")


master_layout = QHBoxLayout()


picture_box = QLabel("Your Picture")

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(left)
col1.addWidget(right)
col1.addWidget(sharpness)
col1.addWidget(mirror)
col1.addWidget(contrast)


col2.addWidget(picture_box)

master_layout.addLayout(col1 , 50)
master_layout.addLayout(col2 , 90)

main_window.setLayout(master_layout)


main_window.show()
app.exec()