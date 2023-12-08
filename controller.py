from view import *

from main import *

from PyQt6.QtWidgets import *
import finnhub
import datetime
import time

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.submit())
        self.pushButton_2.clicked.connect(lambda: self.clear())
        self.finnhub_client = finnhub.Client(api_key="clh9ho9r01qgurun15vgclh9ho9r01qgurun1600")





    def clear(self):
        self.inputField.clear()
        self.predictRadioButton.setChecked(False)
        self.historicalRadioButton.setChecked(False)
        self.outputLabel.clear()


    def submit(self):

        ticker = self.inputField.text().strip()
        print(ticker)
        try:
            ticker = str(ticker)
            ticker = ticker.upper()
            self.finnhub_client.company_basic_financials(ticker, 'all')
    



            if self.predictRadioButton.isChecked():

                self.outputLabel.setText(f"The 52-week low for {ticker} this past year\n was {self.finnhub_client.company_basic_financials(ticker, 'all')['metric']['52WeekLow']}")
                print(self.finnhub_client.company_basic_financials(ticker, 'all')['metric']['52WeekLow'])
            elif self.historicalRadioButton.isChecked():
                self.outputLabel.setText(f"The 52-week high for {ticker} this past year\n was {self.finnhub_client.company_basic_financials(ticker, 'all')['metric']['52WeekHigh']}")
            
            elif not(self.predictRadioButton.isChecked()) and not(self.historicalRadioButton.isChecked()):
                self.outputLabel.setText("Pick an option")
         
        except:
            self.outputLabel.setText("Enter a valid stock ticker")
            return

