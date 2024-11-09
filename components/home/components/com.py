from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

class mycom:
    def __init__(self):
        self.com = QSerialPort()
        self.com.setPortName('COM1')
        self.com.setBaudRate(9600)
        self.com.setDataBits(QSerialPort.Data8)
        self.com.setParity(QSerialPort.NoParity)
        self.com.setStopBits(QSerialPort.OneStop)
        self.com.setFlowControl(QSerialPort.NoFlowControl)
    
    def open(self, port):
        self.com.setPortName(port)
        self.com.open(QSerialPort.ReadWrite)
    
    def setrate(self, rate):
        self.com.setBaudRate(rate)
    
    def close(self):
        self.com.close()




