from view import *
from main import *
from PyQt6.QtWidgets import *
import finnhub
import datetime
import time

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        Initializes the Logic class by connecting the buttons to functions and setting up the API
        """
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.submit())
        self.pushButton_2.clicked.connect(lambda: self.clear())
        self.finnhub_client = finnhub.Client(api_key="clh9ho9r01qgurun15vgclh9ho9r01qgurun1600")
        


    def clear(self) -> None:
        """
        Empties all relevant fields
        """
        self.inputField.clear()
        self.buttonGroup_2.setExclusive(False)
        self.radioButton.setChecked(True)
        self.predictRadioButton.setChecked(False)
        self.historicalRadioButton.setChecked(False)
        self.buttonGroup_2.setExclusive(True)
        self.outputLabel.clear()


    def submit(self) -> None:
        """
        Strips the input from the inputField in the GUI and tests to make sure it is a proper ticker
        """

        ticker = self.inputField.text().strip()
        print(ticker)
        try:
            ticker = str(ticker)
            ticker = ticker.upper()

            #Below will throw an error if the input is not a valid ticker
            self.finnhub_client.company_basic_financials(ticker, 'all')
    



            if self.predictRadioButton.isChecked():

                self.outputLabel.setText(f"The 52-week low for {ticker} this past year\n was {self.finnhub_client.company_basic_financials(ticker, 'all')['metric']['52WeekLow']}")
                # print(self.finnhub_client.company_basic_financials(ticker, 'all')['metric']['52WeekLow'])
            elif self.historicalRadioButton.isChecked():
                self.outputLabel.setText(f"The 52-week high for {ticker} this past year\n was {self.finnhub_client.company_basic_financials(ticker, 'all')['metric']['52WeekHigh']}")
            
            elif not(self.predictRadioButton.isChecked()) and not(self.historicalRadioButton.isChecked()):
                self.outputLabel.setText("Pick an option")
         
        except:
            self.outputLabel.setText("Enter a valid stock ticker")
            return

