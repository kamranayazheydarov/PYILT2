import sys
import csv
import pyilt2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Search and Save Results'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        
        layout = QVBoxLayout()
        
        self.label_comp = QLabel('Enter compound:')
        layout.addWidget(self.label_comp)
        
        self.textbox_comp = QLineEdit(self)
        layout.addWidget(self.textbox_comp)
        
        self.label_year = QLabel('Enter year (optional):')
        layout.addWidget(self.label_year)
        
        self.textbox_year = QLineEdit(self)
        layout.addWidget(self.textbox_year)
        
        self.label_author = QLabel('Enter author (optional):')
        layout.addWidget(self.label_author)
        
        self.textbox_author = QLineEdit(self)
        layout.addWidget(self.textbox_author)
        
        self.button = QPushButton('Search', self)
        self.button.clicked.connect(self.on_click)
        layout.addWidget(self.button)
        
        self.result_area = QTextEdit(self)
        layout.addWidget(self.result_area)
        
        self.setLayout(layout)
        self.show()
        
    def on_click(self):
        comp = self.textbox_comp.text()
        year = self.textbox_year.text()
        author = self.textbox_author.text()
        
        query_params = {'comp': comp}
        if year:
            query_params['year'] = int(year)
        if author:
            query_params['author'] = author
        
        results = pyilt2.query(**query_params)
        
        with open('results.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for i in range(len(results)):
                result = results[i]
                writer.writerow([str(result)])
        
        with open('results.csv', mode='r') as file:
            reader = csv.reader(file)
            data = list(reader)
        
        cleaned_data = [''.join(row).replace(',', '') for row in data]
        
        self.result_area.clear()
        for row in cleaned_data:
            self.result_area.append(row)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())



