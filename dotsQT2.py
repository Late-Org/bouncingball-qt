import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random

class Dot:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0 or self.x > 1000:
            self.dx *= -1
        if self.y < 0 or self.y > 1000:
            self.dy *= -1

class DotsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.dots = []
        for i in range(10):
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            radius = random.randint(10, 50)
            dot = Dot(x, y, radius)
            self.dots.append(dot)
        self.timer = self.startTimer(10)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for dot in self.dots:
            painter.setBrush(dot.color)
            painter.drawEllipse(dot.x - dot.radius, dot.y - dot.radius, dot.radius * 2, dot.radius * 2)

    def timerEvent(self, event):
        for dot in self.dots:
            dot.move()
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = DotsWidget()
    widget.setGeometry(100, 100, 1000, 1000)
    widget.show()
    sys.exit(app.exec_())