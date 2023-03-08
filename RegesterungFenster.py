import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout


class RegistrierungWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        email_label = QLabel('E-mail:')
        self.email_input = QLineEdit()

        Passwort_label = QLabel('Passwort:')
        self.Passwort_input = QLineEdit()
        self.Passwort_input.setEchoMode(QLineEdit.Password)

        Passwort_confirm_label = QLabel('Passwort wiederholen:')
        self.Passwort_confirm_input = QLineEdit()
        self.Passwort_confirm_input.setEchoMode(QLineEdit.Password)

        submit_button = QPushButton('Registriren')
        submit_button.clicked.connect(self.submit_clicked)

        cancel_button = QPushButton('Abbrechen')
        cancel_button.clicked.connect(self.close)

        vbox = QVBoxLayout()
        vbox.addWidget(email_label)
        vbox.addWidget(self.email_input)
        vbox.addWidget(Passwort_label)
        vbox.addWidget(self.Passwort_input)
        vbox.addWidget(Passwort_confirm_label)
        vbox.addWidget(self.Passwort_confirm_input)
        vbox.addWidget(submit_button)
        vbox.addWidget(cancel_button)

        self.setLayout(vbox)
        self.setWindowTitle('Registrierungsfenster')
        self.show()

    def submit_clicked(self):
        email = self.email_input.text()
        password = self.Passwort_input.text()
        Passwort_confirm = self.Passwort_confirm_input.text()

        if '@' not in email or '.' not in email:
            QMessageBox.critical(self, 'Fehler', 'Ungültige E-mail-adresse.')
        elif not password.isalnum() or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
            QMessageBox.critical(self, 'Fehler', 'Das Passwort muss Großbuchstaben, Kleinbuchstaben und Zahlen enthalten.')
        elif password != Passwort_confirm:
            QMessageBox.critical(self, 'Fehler', 'Die Passwörter stimmen nicht überein.')
        else:
            QMessageBox.information(self, 'Bestätigung', 'Registrierung erfolgreich.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrierungWindow()
    sys.exit(app.exec_())
