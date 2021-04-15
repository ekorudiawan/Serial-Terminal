import serial_terminal_ui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSerialPort import *
import os
import sys

class SerialTerminal(serial_terminal_ui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(SerialTerminal, self).__init__()
        self.setupUi(self)
        list_port_name = self.check_serial_device()
        for port in list_port_name:
            self.comboBoxSerialPort.addItem(port)
        list_baudrate = [1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]
        self.list_enum_baudrate = [QSerialPort.Baud1200,
                                   QSerialPort.Baud2400,
                                   QSerialPort.Baud4800,
                                   QSerialPort.Baud9600,
                                   QSerialPort.Baud19200,
                                   QSerialPort.Baud38400,
                                   QSerialPort.Baud57600,
                                   QSerialPort.Baud115200]
        for baudrate in list_baudrate:
            self.comboBoxBaudrate.addItem(str(baudrate))
        self.serial = QSerialPort(readyRead=self.receive_data)
        self.pushButtonConnect.clicked.connect(self.serial_connect)
        self.pushButtonDisconnect.clicked.connect(self.serial_disconnect)
        self.pushButtonSend.clicked.connect(self.send_data)
        self.pushButtonClearText.clicked.connect(self.clear_text)

    def check_serial_device(self):
        list_devices = os.listdir('/dev')
        list_ports = [s for s in list_devices if "ttyACM" in s]
        list_ports_name = []
        for port in list_ports:
            list_ports_name.append("/dev/"+port)
        return list_ports_name

    def serial_connect(self):
        selected_port = self.comboBoxSerialPort.currentText()
        selected_baudrate = self.list_enum_baudrate[self.comboBoxBaudrate.currentIndex()]
        self.serial.setPortName(selected_port)
        self.serial.setBaudRate(selected_baudrate)
        self.serial.open(QIODevice.ReadWrite)
        # self.serial.flush()
        # self.serial.clear(QSerialPort.Direction.AllDirections)

    def serial_disconnect(self):
        self.serial.close()

    def clear_text(self):
        self.textEditSerialIn.clear()

    @pyqtSlot()
    def receive_data(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode('ISO-8859-1')
            text = text.rstrip('\r\n')
            self.textEditSerialIn.append(text)

    @pyqtSlot()
    def send_data(self):
        self.serial.write(self.textEditSerialOut.toPlainText().encode())

def main():
    serial_terminal = QApplication(sys.argv)
    serial_terminal_gui = SerialTerminal()
    serial_terminal_gui.show()
    serial_terminal.exec_()


if __name__ == "__main__":
    main()
