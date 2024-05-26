from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton,\
    QTextEdit

import sys




class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)


        # Add chat area widget
        self.chat_area = QTextEdit(self)
        


        # Add the input field widget
        self.input_field = QLineEdit(self)


        # Add the send button
        self.button = QPushButton("Send", self)

        self.show()




class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
