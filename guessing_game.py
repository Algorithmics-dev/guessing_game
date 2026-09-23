import random

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt


# ==========================================
# GAME
# ==========================================

secret_number = random.randint(1, 100)
attempts = 7


def check_guess():
    global attempts

    guess = int(number_input.text())

    if guess == secret_number:
        emoji.setText("🏆")
        message.setText("YOU FOUND IT!")
        guess_button.setEnabled(False)

    elif guess < secret_number:
        attempts = attempts - 1
        emoji.setText("🔥")
        message.setText("GO HIGHER! ⬆")

    else:
        attempts = attempts - 1
        emoji.setText("🧊")
        message.setText("GO LOWER! ⬇")

    attempts_number.setText(str(attempts))

    number_input.clear()

    if attempts == 0 and guess != secret_number:
        emoji.setText("💀")
        message.setText(
            "GAME OVER!  The number was "
            + str(secret_number)
        )

        guess_button.setEnabled(False)


# ==========================================
# APP
# ==========================================

app = QApplication([])

window = QWidget()
window.setWindowTitle("Mind Reader Arena")
window.setFixedSize(1000,1000)


# ==========================================
# COLORS
# ==========================================

window_palette = window.palette()
window_palette.setColor(
    QPalette.Window,
    QColor("#070b20")
)
window.setPalette(window_palette)
window.setAutoFillBackground(True)


# ==========================================
# TITLE
# ==========================================

title = QLabel("🧠  MIND READER ARENA  ⚡")
title.setAlignment(Qt.AlignCenter)

title_font = QFont()
title_font.setPointSize(22)
title_font.setBold(True)
title.setFont(title_font)

title_palette = title.palette()
title_palette.setColor(
    QPalette.WindowText,
    QColor("#FFD21F")
)
title.setPalette(title_palette)


# ==========================================
# SUBTITLE
# ==========================================

subtitle = QLabel(
    "Crack the secret number before your attempts run out!"
)

subtitle.setAlignment(Qt.AlignCenter)

subtitle_font = QFont()
subtitle_font.setPointSize(10)
subtitle_font.setBold(True)
subtitle.setFont(subtitle_font)

subtitle_palette = subtitle.palette()
subtitle_palette.setColor(
    QPalette.WindowText,
    QColor("white")
)
subtitle.setPalette(subtitle_palette)


# ==========================================
# SECRET RANGE
# ==========================================

range_title = QLabel("🎯  SECRET RANGE")
range_title.setAlignment(Qt.AlignCenter)

range_title_font = QFont()
range_title_font.setPointSize(11)
range_title_font.setBold(True)
range_title.setFont(range_title_font)

range_title_palette = range_title.palette()
range_title_palette.setColor(
    QPalette.WindowText,
    QColor("#00D9FF")
)
range_title.setPalette(range_title_palette)


range_number = QLabel("1  —  100")
range_number.setAlignment(Qt.AlignCenter)

range_font = QFont()
range_font.setPointSize(26)
range_font.setBold(True)
range_number.setFont(range_font)

range_palette = range_number.palette()
range_palette.setColor(
    QPalette.WindowText,
    QColor("white")
)
range_number.setPalette(range_palette)


# ==========================================
# REACTION
# ==========================================

emoji = QLabel("🧠")
emoji.setAlignment(Qt.AlignCenter)

emoji_font = QFont()
emoji_font.setPointSize(40)
emoji.setFont(emoji_font)


message = QLabel("I'M THINKING OF A NUMBER...")
message.setAlignment(Qt.AlignCenter)

message_font = QFont()
message_font.setPointSize(15)
message_font.setBold(True)
message.setFont(message_font)

message_palette = message.palette()
message_palette.setColor(
    QPalette.WindowText,
    QColor("#FFFFFF")
)
message.setPalette(message_palette)


# ==========================================
# INPUT
# ==========================================

number_input = QLineEdit()

number_input.setPlaceholderText(
    "Enter your guess..."
)

number_input.setAlignment(Qt.AlignCenter)
number_input.setFixedHeight(55)

input_font = QFont()
input_font.setPointSize(18)
input_font.setBold(True)
number_input.setFont(input_font)


# ==========================================
# GUESS BUTTON
# ==========================================

guess_button = QPushButton(
    "⚡  LOCK IN GUESS  ⚡"
)

guess_button.setFixedHeight(70)

button_font = QFont()
button_font.setPointSize(16)
button_font.setBold(True)
guess_button.setFont(button_font)


button_palette = guess_button.palette()

button_palette.setColor(
    QPalette.Button,
    QColor("#FFD21F")
)

button_palette.setColor(
    QPalette.ButtonText,
    QColor("#101010")
)

guess_button.setPalette(button_palette)
guess_button.setAutoFillBackground(True)


# ==========================================
# ATTEMPTS
# ==========================================

attempts_text = QLabel(
    "❤️  ATTEMPTS LEFT"
)

attempts_text.setAlignment(Qt.AlignCenter)

attempts_text_font = QFont()
attempts_text_font.setPointSize(12)
attempts_text_font.setBold(True)
attempts_text.setFont(attempts_text_font)

attempts_text_palette = attempts_text.palette()
attempts_text_palette.setColor(
    QPalette.WindowText,
    QColor("#FF477E")
)
attempts_text.setPalette(attempts_text_palette)


attempts_number = QLabel(
    str(attempts)
)

attempts_number.setAlignment(Qt.AlignCenter)

attempts_number_font = QFont()
attempts_number_font.setPointSize(28)
attempts_number_font.setBold(True)
attempts_number.setFont(attempts_number_font)

attempts_number_palette = attempts_number.palette()
attempts_number_palette.setColor(
    QPalette.WindowText,
    QColor("white")
)
attempts_number.setPalette(
    attempts_number_palette
)


# ==========================================
# FOOTER
# ==========================================

footer = QLabel(
    "🔥 Get closer. Crack the machine. Win."
)

footer.setAlignment(Qt.AlignCenter)

footer_font = QFont()
footer_font.setPointSize(10)
footer_font.setBold(True)
footer.setFont(footer_font)

footer_palette = footer.palette()
footer_palette.setColor(
    QPalette.WindowText,
    QColor("#00D9FF")
)
footer.setPalette(footer_palette)


# ==========================================
# RANGE BOX
# ==========================================

range_box = QVBoxLayout()

range_box.addWidget(range_title)
range_box.addWidget(range_number)


# ==========================================
# ATTEMPTS BOX
# ==========================================

attempts_box = QHBoxLayout()

attempts_box.addWidget(attempts_text)
attempts_box.addWidget(attempts_number)


# ==========================================
# MAIN LAYOUT
# ==========================================

layout = QVBoxLayout()

layout.setContentsMargins(
    35, 30, 35, 25
)

layout.setSpacing(18)

layout.addWidget(title)
layout.addWidget(subtitle)

layout.addSpacing(10)

layout.addLayout(range_box)

layout.addSpacing(10)

layout.addWidget(emoji)
layout.addWidget(message)

layout.addSpacing(5)

layout.addWidget(number_input)
layout.addWidget(guess_button)

layout.addSpacing(10)

layout.addLayout(attempts_box)

layout.addStretch()

layout.addWidget(footer)

window.setLayout(layout)


# ==========================================
# BUTTON
# ==========================================

guess_button.clicked.connect(
    check_guess
)


# ==========================================
# START
# ==========================================

window.show()

app.exec_()