import os
from PyQt5 import QtWidgets, QtGui

import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

class FileRenamer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.folderLabel = QtWidgets.QLabel('Folder:')
        self.folderEdit = QtWidgets.QLineEdit()
        self.folderButton = QtWidgets.QPushButton('Browse...')
        self.searchLabel = QtWidgets.QLabel('Search:')
        self.searchEdit = QtWidgets.QLineEdit()
        self.replaceLabel = QtWidgets.QLabel('Replacement:')
        self.replaceEdit = QtWidgets.QLineEdit()

        self.renameButton = QtWidgets.QPushButton('Rename')

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.folderLabel, 0, 0)
        layout.addWidget(self.folderEdit, 0, 1)
        layout.addWidget(self.folderButton, 0, 2)
        layout.addWidget(self.searchLabel, 1, 0)
        layout.addWidget(self.searchEdit, 1, 1)
        layout.addWidget(self.replaceLabel, 2, 0)
        layout.addWidget(self.replaceEdit, 2, 1)
        layout.addWidget(self.renameButton, 3, 1)
        self.setLayout(layout)
        self.setWindowTitle('Bulk File Rename Tool')
        self.folderButton.clicked.connect(self.folderSelection)
        self.renameButton.clicked.connect(self.renameFiles)


    def folderSelection(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.folderEdit.setText(folder)


    def renameFiles(self):
        folder = self.folderEdit.text()
        search = self.searchEdit.text()
        replace = self.replaceEdit.text()
        print(folder)
        print(search)
        print(replace)

        for filename in os.listdir(folder):
            if search in filename:
                new_filename = filename.replace(search, replace)
                old_path = os.path.join(folder, filename)
                new_path = os.path.join(folder, new_filename)
                os.rename(old_path, new_path)

        QtWidgets.QMessageBox.information(self, 'File Renamer', 'File renaming complete!')

renamer = FileRenamer()
renamer.show()

sys.exit(app.exec_())
