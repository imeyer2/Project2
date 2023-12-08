from controller import *
# export PATH=$PATH:/Library/Frameworks/Python.framework/Versions/3.10/bin
def main() -> None:
    """
    Generates the window for the application by calling classes in the other files
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()



if __name__ == "__main__":
    main()