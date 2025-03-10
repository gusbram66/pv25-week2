import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, 
    QHBoxLayout, QGroupBox, QRadioButton, QComboBox, QFormLayout
)

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 400, 300)
        
        main_layout = QVBoxLayout()
        
        # Identitas
        identitas_group = QGroupBox("Identitas (vertical box layout)")
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel("Nama : Ida Bagus Brahmanta Jayana"))
        identitas_layout.addWidget(QLabel("Nim : F1D022052"))
        identitas_layout.addWidget(QLabel("Kelas : C"))
        identitas_group.setLayout(identitas_layout)
        main_layout.addWidget(identitas_group)
        
        # Navigasi 
        nav_group = QGroupBox("Navigation (horizontal box layout)")
        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_group.setLayout(nav_layout)
        main_layout.addWidget(nav_group)
        
        # Registrasi User
        form_group = QGroupBox("User Registration (form layout)")
        form_layout = QFormLayout()
        self.full_name = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()
        form_layout.addRow("Full Name:", self.full_name)
        form_layout.addRow("Email:", self.email)
        form_layout.addRow("Phone:", self.phone)
        
        # Berjenis kelamin apa 
        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        gender_layout.addWidget(QLabel("Gender:"))
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        form_layout.addRow(gender_layout)
        
        # Pilih Negaramu
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Select", "Jepang", "UK", "Korea", "Meksikano"])
        form_layout.addRow("Country:", self.country_combo)
        
        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)
        
        # Tombol Action 
        action_group = QGroupBox("Actions (horizontal box layout)")
        action_layout = QHBoxLayout()
        submit_btn = QPushButton("Submit")
        cancel_btn = QPushButton("Cancel")
        action_layout.addWidget(submit_btn)
        action_layout.addWidget(cancel_btn)
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)
        
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())
