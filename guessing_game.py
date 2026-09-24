import random

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget
)

from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect


# ==========================================
# GAME
# ==========================================

secret_number = 0
attempts = 7


def start_game():
    global secret_number, attempts

    secret_number = random.randint(1, 100)
    attempts = 7

    emoji.setText("🧠")
    message.setText("I'M THINKING OF A NUMBER...")
    attempts_number.setText(str(attempts))

    number_input.clear()
    number_input.setEnabled(True)
    guess_button.setEnabled(True)

    restart_button.hide()

    # Go to game page
    pages.setCurrentWidget(game_page)


def check_guess():
    global attempts

    guess = int(number_input.text())

    if guess == secret_number:

        emoji.setText("🏆")
        message.setText("YOU FOUND IT!")

        guess_button.setEnabled(False)
        number_input.setEnabled(False)

        restart_button.show()

        QApplication.beep()

        result_animation()

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
        number_input.setEnabled(False)

        restart_button.show()

        QApplication.beep()
        QApplication.beep()

        result_animation()


# ==========================================
# ANIMATION
# ==========================================

def result_animation():

    global animation

    start_position = emoji.geometry()

    bigger_position = QRect(
        start_position.x() - 20,
        start_position.y() - 20,
        start_position.width() + 40,
        start_position.height() + 40
    )

    animation = QPropertyAnimation(
        emoji,
        b"geometry"
    )

    animation.setDuration(500)

    animation.setStartValue(
        start_position
    )

    animation.setKeyValueAt(
        0.5,
        bigger_position
    )

    animation.setEndValue(
        start_position
    )

    animation.start()


# ==========================================
# APP
# ==========================================

app = QApplication([])

window = QWidget()

window.setWindowTitle(
    "Mind Reader Arena"
)

window.setFixedSize(
    1200,
    1200
)


# ==========================================
# WINDOW COLORS
# ==========================================

window_palette = window.palette()

window_palette.setColor(
    QPalette.Window,
    QColor("#070b20")
)

window.setPalette(
    window_palette
)

window.setAutoFillBackground(True)


# ==========================================
# PAGES
# ==========================================

pages = QStackedWidget()


# ==========================================
# START PAGE
# ==========================================

start_page = QWidget()

start_palette = start_page.palette()

start_palette.setColor(
    QPalette.Window,
    QColor("#070b20")
)

start_page.setPalette(
    start_palette
)

start_page.setAutoFillBackground(True)


# ==========================================
# START TITLE
# ==========================================

start_emoji = QLabel("🧠")

start_emoji.setAlignment(
    Qt.AlignCenter
)

start_emoji_font = QFont()
start_emoji_font.setPointSize(70)

start_emoji.setFont(
    start_emoji_font
)


start_title = QLabel(
    "MIND READER ARENA"
)

start_title.setAlignment(
    Qt.AlignCenter
)

start_title_font = QFont()

start_title_font.setPointSize(30)
start_title_font.setBold(True)

start_title.setFont(
    start_title_font
)

start_title_palette = start_title.palette()

start_title_palette.setColor(
    QPalette.WindowText,
    QColor("#FFD21F")
)

start_title.setPalette(
    start_title_palette
)


# ==========================================
# START SUBTITLE
# ==========================================

start_subtitle = QLabel(
    "CAN YOU READ THE MACHINE'S MIND?"
)

start_subtitle.setAlignment(
    Qt.AlignCenter
)

start_subtitle_font = QFont()

start_subtitle_font.setPointSize(14)
start_subtitle_font.setBold(True)

start_subtitle.setFont(
    start_subtitle_font
)

start_subtitle_palette = (
    start_subtitle.palette()
)

start_subtitle_palette.setColor(
    QPalette.WindowText,
    QColor("#00D9FF")
)

start_subtitle.setPalette(
    start_subtitle_palette
)


# ==========================================
# START DESCRIPTION
# ==========================================

start_description = QLabel(
    "The machine is hiding a secret number.\n\n"
    "You have 7 attempts to crack it.\n\n"
    "🔥 GO HIGHER\n"
    "🧊 GO LOWER\n"
    "🏆 FIND THE SECRET NUMBER"
)

start_description.setAlignment(
    Qt.AlignCenter
)

description_font = QFont()

description_font.setPointSize(13)
description_font.setBold(True)

start_description.setFont(
    description_font
)

description_palette = (
    start_description.palette()
)

description_palette.setColor(
    QPalette.WindowText,
    QColor("white")
)

start_description.setPalette(
    description_palette
)


# ==========================================
# START BUTTON
# ==========================================

start_button = QPushButton(
    "⚡  START GAME  ⚡"
)

start_button.setFixedHeight(80)

start_button_font = QFont()

start_button_font.setPointSize(18)
start_button_font.setBold(True)

start_button.setFont(
    start_button_font
)

start_button_palette = (
    start_button.palette()
)

start_button_palette.setColor(
    QPalette.Button,
    QColor("#FFD21F")
)

start_button_palette.setColor(
    QPalette.ButtonText,
    QColor("#101010")
)

start_button.setPalette(
    start_button_palette
)

start_button.setAutoFillBackground(True)


# ==========================================
# START LAYOUT
# ==========================================

start_layout = QVBoxLayout()

start_layout.setContentsMargins(
    100, 100, 100, 100
)

start_layout.setSpacing(30)

start_layout.addStretch()

start_layout.addWidget(
    start_emoji
)

start_layout.addWidget(
    start_title
)

start_layout.addWidget(
    start_subtitle
)

start_layout.addSpacing(20)

start_layout.addWidget(
    start_description
)

start_layout.addSpacing(30)

start_layout.addWidget(
    start_button
)

start_layout.addStretch()

start_page.setLayout(
    start_layout
)


# ==========================================
# GAME PAGE
# ==========================================

game_page = QWidget()

game_palette = game_page.palette()

game_palette.setColor(
    QPalette.Window,
    QColor("#070b20")
)

game_page.setPalette(
    game_palette
)

game_page.setAutoFillBackground(True)


# ==========================================
# TITLE
# ==========================================

title = QLabel(
    "🧠  MIND READER ARENA  ⚡"
)

title.setAlignment(
    Qt.AlignCenter
)

title_font = QFont()

title_font.setPointSize(22)
title_font.setBold(True)

title.setFont(
    title_font
)

title_palette = title.palette()

title_palette.setColor(
    QPalette.WindowText,
    QColor("#FFD21F")
)

title.setPalette(
    title_palette
)


# ==========================================
# SUBTITLE
# ==========================================

subtitle = QLabel(
    "Crack the secret number before "
    "your attempts run out!"
)

subtitle.setAlignment(
    Qt.AlignCenter
)

subtitle_font = QFont()

subtitle_font.setPointSize(10)
subtitle_font.setBold(True)

subtitle.setFont(
    subtitle_font
)

subtitle_palette = subtitle.palette()

subtitle_palette.setColor(
    QPalette.WindowText,
    QColor("white")
)

subtitle.setPalette(
    subtitle_palette
)


# ==========================================
# SECRET RANGE
# ==========================================

range_title = QLabel(
    "🎯  SECRET RANGE"
)

range_title.setAlignment(
    Qt.AlignCenter
)

range_title_font = QFont()

range_title_font.setPointSize(11)
range_title_font.setBold(True)

range_title.setFont(
    range_title_font
)

range_title_palette = (
    range_title.palette()
)

range_title_palette.setColor(
    QPalette.WindowText,
    QColor("#00D9FF")
)

range_title.setPalette(
    range_title_palette
)


range_number = QLabel(
    "1  —  100"
)

range_number.setAlignment(
    Qt.AlignCenter
)

range_font = QFont()

range_font.setPointSize(26)
range_font.setBold(True)

range_number.setFont(
    range_font
)

range_palette = range_number.palette()

range_palette.setColor(
    QPalette.WindowText,
    QColor("white")
)

range_number.setPalette(
    range_palette
)


# ==========================================
# REACTION
# ==========================================

emoji = QLabel("🧠")

emoji.setAlignment(
    Qt.AlignCenter
)

emoji.setFixedHeight(120)

emoji_font = QFont()

emoji_font.setPointSize(40)

emoji.setFont(
    emoji_font
)


message = QLabel(
    "I'M THINKING OF A NUMBER..."
)

message.setAlignment(
    Qt.AlignCenter
)

message_font = QFont()

message_font.setPointSize(15)
message_font.setBold(True)

message.setFont(
    message_font
)

message_palette = message.palette()

message_palette.setColor(
    QPalette.WindowText,
    QColor("#FFFFFF")
)

message.setPalette(
    message_palette
)


# ==========================================
# INPUT
# ==========================================

number_input = QLineEdit()

number_input.setPlaceholderText(
    "Enter your guess..."
)

number_input.setAlignment(
    Qt.AlignCenter
)

number_input.setFixedHeight(55)

input_font = QFont()

input_font.setPointSize(18)
input_font.setBold(True)

number_input.setFont(
    input_font
)


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

guess_button.setFont(
    button_font
)

button_palette = (
    guess_button.palette()
)

button_palette.setColor(
    QPalette.Button,
    QColor("#FFD21F")
)

button_palette.setColor(
    QPalette.ButtonText,
    QColor("#101010")
)

guess_button.setPalette(
    button_palette
)

guess_button.setAutoFillBackground(
    True
)


# ==========================================
# ATTEMPTS
# ==========================================

attempts_text = QLabel(
    "❤️  ATTEMPTS LEFT"
)

attempts_text.setAlignment(
    Qt.AlignCenter
)

attempts_text_font = QFont()

attempts_text_font.setPointSize(12)
attempts_text_font.setBold(True)

attempts_text.setFont(
    attempts_text_font
)

attempts_text_palette = (
    attempts_text.palette()
)

attempts_text_palette.setColor(
    QPalette.WindowText,
    QColor("#FF477E")
)

attempts_text.setPalette(
    attempts_text_palette
)


attempts_number = QLabel(
    str(attempts)
)

attempts_number.setAlignment(
    Qt.AlignCenter
)

attempts_number_font = QFont()

attempts_number_font.setPointSize(28)
attempts_number_font.setBold(True)

attempts_number.setFont(
    attempts_number_font
)

attempts_number_palette = (
    attempts_number.palette()
)

attempts_number_palette.setColor(
    QPalette.WindowText,
    QColor("white")
)

attempts_number.setPalette(
    attempts_number_palette
)


# ==========================================
# RESTART BUTTON
# ==========================================

restart_button = QPushButton(
    "🔄  PLAY AGAIN  🔄"
)

restart_button.setFixedHeight(65)

restart_font = QFont()

restart_font.setPointSize(15)
restart_font.setBold(True)

restart_button.setFont(
    restart_font
)

restart_palette = (
    restart_button.palette()
)

restart_palette.setColor(
    QPalette.Button,
    QColor("#00D9FF")
)

restart_palette.setColor(
    QPalette.ButtonText,
    QColor("#101010")
)

restart_button.setPalette(
    restart_palette
)

restart_button.setAutoFillBackground(
    True
)

restart_button.hide()


# ==========================================
# FOOTER
# ==========================================

footer = QLabel(
    "🔥 Get closer. Crack the machine. Win."
)

footer.setAlignment(
    Qt.AlignCenter
)

footer_font = QFont()

footer_font.setPointSize(10)
footer_font.setBold(True)

footer.setFont(
    footer_font
)

footer_palette = footer.palette()

footer_palette.setColor(
    QPalette.WindowText,
    QColor("#00D9FF")
)

footer.setPalette(
    footer_palette
)


# ==========================================
# RANGE BOX
# ==========================================

range_box = QVBoxLayout()

range_box.addWidget(
    range_title
)

range_box.addWidget(
    range_number
)


# ==========================================
# ATTEMPTS BOX
# ==========================================

attempts_box = QHBoxLayout()

attempts_box.addWidget(
    attempts_text
)

attempts_box.addWidget(
    attempts_number
)


# ==========================================
# GAME LAYOUT
# ==========================================

game_layout = QVBoxLayout()

game_layout.setContentsMargins(
    35, 30, 35, 25
)

game_layout.setSpacing(18)

game_layout.addWidget(
    title
)

game_layout.addWidget(
    subtitle
)

game_layout.addSpacing(10)

game_layout.addLayout(
    range_box
)

game_layout.addSpacing(10)

game_layout.addWidget(
    emoji
)

game_layout.addWidget(
    message
)

game_layout.addSpacing(5)

game_layout.addWidget(
    number_input
)

game_layout.addWidget(
    guess_button
)

game_layout.addWidget(
    restart_button
)

game_layout.addSpacing(10)

game_layout.addLayout(
    attempts_box
)

game_layout.addStretch()

game_layout.addWidget(
    footer
)

game_page.setLayout(
    game_layout
)


# ==========================================
# ADD PAGES
# ==========================================

pages.addWidget(
    start_page
)

pages.addWidget(
    game_page
)


# ==========================================
# MAIN WINDOW LAYOUT
# ==========================================

window_layout = QVBoxLayout()

window_layout.setContentsMargins(
    0, 0, 0, 0
)

window_layout.addWidget(
    pages
)

window.setLayout(
    window_layout
)


# ==========================================
# BUTTONS
# ==========================================

start_button.clicked.connect(
    start_game
)

guess_button.clicked.connect(
    check_guess
)

restart_button.clicked.connect(
    start_game
)


# ==========================================
# START
# ==========================================

pages.setCurrentWidget(
    start_page
)

window.show()

app.exec_()