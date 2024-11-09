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
        
        self.com_data = ''
    
    def open(self, port):
        self.com.setPortName(port)
        self.com.open(QSerialPort.ReadWrite)
    
    def setrate(self, rate):
        self.com.setBaudRate(rate)
    
    def close(self):
        self.com.close()
    
    def send(self, data):
        self.com.write(data)
    
    # 串口发送数据
    def Com_Send_Data(self):
        txData = self.com_data
        self.com.write(txData.encode('UTF-8'))
        # if len(txData) == 0 :
        #     return
        # if self.hexSending_checkBox.isChecked() == False:
        #     self.com.write(txData.encode('UTF-8'))
        # else:
        #     Data = txData.replace(' ', '')
        #     # 如果16进制不是偶数个字符, 去掉最后一个, [ ]左闭右开
        #     if len(Data)%2 == 1:
        #         Data = Data[0:len(Data)-1]
        #     # 如果遇到非16进制字符
        #     if Data.isalnum() is False:
        #         QMessageBox.critical(self, '错误', '包含非十六进制数')
        #     try:
        #         hexData = binascii.a2b_hex(Data)
        #     except:
        #         QMessageBox.critical(self, '错误', '转换编码错误')
        #         return
        #     # 发送16进制数据, 发送格式如 ‘31 32 33 41 42 43’, 代表'123ABC'
        #     try:
        #         self.com.write(hexData) 
        #     except:
        #         QMessageBox.critical(self, '异常', '十六进制发送错误')
        #         return
                
                
    
    # 串口接收数据
    def Com_Receive_Data(self):
        
        try:
            rxData = bytes(self.com.readAll())
        except:
            QMessageBox.critical(self, '严重错误', '串口接收数据错误')
        if self.hexShowing_checkBox.isChecked() == False :
            try:
                self.textEdit_Recive.insertPlainText(rxData.decode('UTF-8'))
            except:
                pass
        else :
            Data = binascii.b2a_hex(rxData).decode('ascii')
            # re 正则表达式 (.{2}) 匹配两个字母
            hexStr = ' 0x'.join(re.findall('(.{2})', Data))
            # 补齐第一个 0x
            hexStr = '0x' + hexStr
            self.textEdit_Recive.insertPlainText(hexStr)
            self.textEdit_Recive.insertPlainText(' ')
            
     
    # 串口刷新
    def Com_Refresh_Button_Clicked(self):
        self.Com_Name_Combo.clear()
        com = QSerialPort()
        com_list = QSerialPortInfo.availablePorts()
        for info in com_list:
            com.setPort(info)
            if com.open(QSerialPort.ReadWrite):
                self.Com_Name_Combo.addItem(info.portName())
                com.close()




