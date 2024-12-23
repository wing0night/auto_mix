from PyQt5.Qt import QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
import PyQt5.QtWidgets, PyQt5.QtCore
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from .components.com import mycom

from siui.components import SiPixLabel
from siui.components.option_card import SiOptionCardLinear, SiOptionCardPlane
from siui.components.page import SiPage
from siui.components.slider import SiSliderH
from siui.components.titled_widget_group import SiTitledWidgetGroup
from siui.components.combobox import SiComboBox
from siui.components.widgets import (
    SiDenseHContainer,
    SiDenseVContainer,
    SiLabel,
    SiLineEdit,
    SiLongPressButton,
    SiPushButton,
    SiSimpleButton,
    SiSwitch,
)
from siui.core.color import SiColor
from siui.core.effect import SiQuickEffect
from siui.core.globals import SiGlobal
from siui.core.silicon import Si
from siui.gui import SiFont, GlobalFont

from .components.themed_option_card import ThemedOptionCardPlane

com_port = "com1" # 默认串口号（全局变量）
com_baud = 115200 # 默认波特率（全局变量）
com = mycom() # 创建串口对象


class Homepage(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 滚动区域
        self.scroll_container = SiTitledWidgetGroup(self)
        

        # 整个顶部
        self.head_area = SiLabel(self)
        self.head_area.setFixedHeight(450)

        # 创建背景底图和渐变
        self.background_image = SiPixLabel(self.head_area)
        self.background_image.setFixedSize(1366, 300)
        self.background_image.setBorderRadius(6)
        self.background_image.load("./img/1.png")

        self.background_fading_transition = SiLabel(self.head_area)
        self.background_fading_transition.setGeometry(0, 100, 0, 200)
        self.background_fading_transition.setStyleSheet(
            """
            background-color: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop:0 {}, stop:1 {})
            """.format(SiGlobal.siui.colors["INTERFACE_BG_B"],
                       SiColor.trans(SiGlobal.siui.colors["INTERFACE_BG_B"], 0))
        )

        # 创建大标题和副标题
        self.title = SiLabel(self.head_area)
        self.title.setGeometry(64, 0, 500, 128)
        self.title.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.title.setText("AutoMix")
        self.title.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.title.setFont(SiGlobal.siui.fonts["XL_NORMAL"])

        self.subtitle = SiLabel(self.head_area)
        self.subtitle.setGeometry(64, 72, 500, 48)
        self.subtitle.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.subtitle.setText("A powerful sample pretreatment platform")
        self.subtitle.setStyleSheet("color: {}".format(SiColor.trans(SiGlobal.siui.colors["TEXT_A"], 0.9)))
        self.subtitle.setFont(SiFont.fromToken(GlobalFont.S_DEMI_BOLD))

        # 创建一个水平容器
        self.container_for_cards = SiDenseHContainer(self.head_area)
        self.container_for_cards.move(0, 130)
        self.container_for_cards.setFixedHeight(310)
        self.container_for_cards.setAlignment(Qt.AlignCenter)
        self.container_for_cards.setSpacing(32)
        
        # 用来放switch的容器
        self.container_for_switch = SiDenseHContainer(self.head_area)
        self.container_for_switch.move(1250, 0)
        self.container_for_switch.setFixedHeight(40)
        self.container_for_switch.setAlignment(Qt.AlignCenter)
        self.container_for_switch.setSpacing(32)

        # 添加卡片
        self.option_card_project = ThemedOptionCardPlane(self)
        self.option_card_project.setTitle("Github Repo")
        self.option_card_project.setFixedSize(218, 270)
        self.option_card_project.setThemeColor("#855198")
        self.option_card_project.setDescription(
            "Check Github Repo to know more and reuse code")  # noqa: E501
        self.option_card_project.setURL("https://github.com/wing0night/auto_mix.git")

        # 切换主题的switch
        self.switch = SiSwitch(self)
        self.switch.setFixedHeight(32)
        
        # 添加到水平容器
        self.container_for_cards.addPlaceholder(64 - 32)
        self.container_for_cards.addWidget(self.option_card_project)
        self.container_for_switch.addWidget(self.switch)

        # 添加到滚动区域容器
        self.scroll_container.addWidget(self.head_area)

        SiQuickEffect.applyDropShadowOn(self.container_for_cards, color=(0, 0, 0, 80), blur_radius=48)

        # 下方区域标签
        self.body_area = SiLabel(self)
        self.body_area.setSiliconWidgetFlag(Si.EnableAnimationSignals)
        self.body_area.resized.connect(lambda _: self.scroll_container.adjustSize())

        # 下面的 titledWidgetGroups
        self.titled_widget_group = SiTitledWidgetGroup(self.body_area)
        self.titled_widget_group.setSiliconWidgetFlag(Si.EnableAnimationSignals)
        self.titled_widget_group.resized.connect(lambda size: self.body_area.setFixedHeight(size[1]))
        self.titled_widget_group.move(64, 0)

        # 开始搭建界面
        # 控件的线性选项卡

        self.titled_widget_group.setSpacing(16)
        self.titled_widget_group.addTitle("Check connection")
        self.titled_widget_group.addWidget(WidgetsExamplePanel(self))

        self.titled_widget_group.addTitle("Test Motors")
        self.titled_widget_group.addWidget(WidgetsTestMotor(self))

        self.titled_widget_group.addPlaceholder(64)

        # 添加到滚动区域容器
        self.body_area.setFixedHeight(self.titled_widget_group.height())
        self.scroll_container.addWidget(self.body_area)

        # 添加到页面
        self.setAttachment(self.scroll_container)
        

    def resizeEvent(self, event):
        super().resizeEvent(event)
        w = event.size().width()
        self.body_area.setFixedWidth(w)
        self.background_image.setFixedWidth(w)
        self.titled_widget_group.setFixedWidth(min(w - 128, 900))
        self.background_fading_transition.setFixedWidth(w)

# 带虫子icon和查看源码按钮的容器组件定制
class WidgetsExampleOptionCardPlane(SiOptionCardPlane):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.button_bug = SiSimpleButton(self)
        self.button_bug.attachment().load(SiGlobal.siui.iconpack.get("ic_fluent_bug_regular"))
        self.button_bug.resize(32, 32)
        self.button_bug.setHint("Report bugs")

        self.button_source_code = SiSimpleButton(self)
        self.button_source_code.attachment().load(SiGlobal.siui.iconpack.get("ic_fluent_open_regular"))
        self.button_source_code.resize(32, 32)
        self.button_source_code.setHint("Source code")

        self.header().addWidget(self.button_source_code, "right")
        self.header().addWidget(self.button_bug, "right")


class WidgetsExamplePanel(SiDenseVContainer):
    def __init__(self, *args, **kwargs):
        global com
        
        super().__init__(*args, **kwargs)

        self.setAdjustWidgetsSize(True)
        self.setSpacing(12)

        # 第一个水平容器
        container_h_a = SiDenseHContainer(self)
        container_h_a.setFixedHeight(128)
        container_h_a.setAdjustWidgetsSize(True)

        # 上面的两个选项卡，按钮和开关
        # 按钮
        self.option_card_button = WidgetsExampleOptionCardPlane(self)
        self.option_card_button.setTitle("Check motor connection")

        option_card_button_container_h = SiDenseHContainer(self)
        option_card_button_container_h.setFixedHeight(32)

        
        # 选取com口
        self.package_selection_combobox = SiComboBox(self)
        self.package_selection_combobox.resize(128, 32)
        self.package_selection_combobox.addOption("com1")
        self.package_selection_combobox.addOption("com2")
        self.package_selection_combobox.addOption("com3")
        self.package_selection_combobox.addOption("com4")
        self.package_selection_combobox.addOption("com5")
        self.package_selection_combobox.addOption("com6")
        self.package_selection_combobox.addOption("com7")
        # 设置槽函数
        self.package_selection_combobox.valueChanged.connect(self.com_changed)
        self.package_selection_combobox.menu().setShowIcon(False)
        self.package_selection_combobox.colorGroup().assign(
            SiColor.INTERFACE_BG_B, self.colorGroup().fromToken(SiColor.INTERFACE_BG_A))
        self.package_selection_combobox.colorGroup().assign(
            SiColor.INTERFACE_BG_D, self.colorGroup().fromToken(SiColor.INTERFACE_BG_C))
        
        # 选取波特率
        self.baud_selection_combobox = SiComboBox(self)
        self.baud_selection_combobox.resize(128, 32)
        self.baud_selection_combobox.addOption("9600")
        self.baud_selection_combobox.addOption("19200")
        self.baud_selection_combobox.addOption("38400")
        self.baud_selection_combobox.addOption("115200")
        # 设置槽函数
        self.baud_selection_combobox.valueChanged.connect(self.baud_changed)
        self.baud_selection_combobox.menu().setShowIcon(False)
        self.baud_selection_combobox.colorGroup().assign(
            SiColor.INTERFACE_BG_B, self.colorGroup().fromToken(SiColor.INTERFACE_BG_A))
        self.baud_selection_combobox.colorGroup().assign(
            SiColor.INTERFACE_BG_D, self.colorGroup().fromToken(SiColor.INTERFACE_BG_C))
        
        # 打开com口按钮
        button_opencom = SiPushButton(self)
        button_opencom.resize(128, 32)
        button_opencom.attachment().setText("Open com")
        button_opencom.mouseReleaseEvent = lambda event: self.open_com()
        
        # 关闭com口按钮
        button_closecom = SiPushButton(self)
        button_closecom.resize(128, 32)
        button_closecom.attachment().setText("Close com")
        button_closecom.mouseReleaseEvent = lambda event: self.close_com()
        
        self.show_com_info = SiLabel(self)
        self.show_com_info.setAlignment(Qt.AlignCenter)
        self.show_com_info.setFixedSize(200, 32)
        self.show_com_info.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
        self.show_com_info.setStyleSheet(f"color: {self.colorGroup().fromToken(SiColor.TEXT_D)}")
        
        # 将com口选取添加到布局
        option_card_button_container_h.addWidget(self.package_selection_combobox)
        # 将波特率选取添加到布局
        option_card_button_container_h.addWidget(self.baud_selection_combobox)
        # 打开com口按钮添加到布局
        option_card_button_container_h.addWidget(button_opencom)
        # 关闭com口按钮添加到布局
        option_card_button_container_h.addWidget(button_closecom)
        # 显示com口信息添加到布局
        option_card_button_container_h.addWidget(self.show_com_info)
        # # 将长按退出添加到布局
        # option_card_button_container_h.addWidget(button_c)
        # container_h_a2.addWidget(self.package_selection_combobox)
        self.option_card_button.body().addWidget(option_card_button_container_h)
        
        # 长按确认按钮
        button_c = SiLongPressButton(self)
        button_c.resize(128, 32)
        button_c.attachment().setText("Quit")

        # 添加到第一个水平容器
        container_h_a.addWidget(self.option_card_button)

        # 添加两个水平容器到自己
        self.addWidget(container_h_a)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.option_card_button.setFixedWidth(event.size().width() - 50 - 16)
    
    # menu中被选中的值将会自动被传递为槽函数的参数（com）
    def com_changed(self, com):
        global com_port
        # a = self.package_selection_combobox.menu().option
        com_port = com
    
    def baud_changed(self, baud):
        global com_baud
        com_baud = baud

    def open_com(self):
        global com_port
        global com_baud
        #### com Open Code here ####
        comName = com_port
        comBaud = com_baud
        com.open(comName)
        com.setrate(int(comBaud))
        print(com_port)
        print(com_baud)
        print("com opened")
        self.show_com_info.setText(f"com: {com_port} {com_baud} opened")
    
    def close_com(self):
        #### com Close Code here ####
        com.close()
        print("com closed")
        self.show_com_info.setText(f"com closed")
        
class WidgetsTestMotor(SiDenseVContainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        global com
        global com_port
        global com_baud

        self.setAdjustWidgetsSize(True)
        self.setSpacing(12)
        
        self.motor = "Motor1"

        # 第一个水平容器
        container_h_a = SiDenseHContainer(self)
        container_h_a.setFixedHeight(128)
        container_h_a.setAdjustWidgetsSize(True)

        # 上面的两个选项卡，按钮和开关
        # 按钮
        self.option_card_button = WidgetsExampleOptionCardPlane(self)
        self.option_card_button.setTitle("Check motor connection")

        option_card_button_container_h = SiDenseHContainer(self)
        option_card_button_container_h.setFixedHeight(32)

        self.com_data = ""
        # 选取电机名称
        
        self.package_selection_motor = SiComboBox(self)
        self.package_selection_motor.resize(128, 32)
        self.package_selection_motor.addOption("Motor1")
        self.package_selection_motor.addOption("Motor2")
        # 设置槽函数
        self.package_selection_motor.valueChanged.connect(self.motor_chosen)
        self.package_selection_motor.menu().setShowIcon(False)
        self.package_selection_motor.colorGroup().assign(
            SiColor.INTERFACE_BG_B, self.colorGroup().fromToken(SiColor.INTERFACE_BG_A))
        self.package_selection_motor.colorGroup().assign(
            SiColor.INTERFACE_BG_D, self.colorGroup().fromToken(SiColor.INTERFACE_BG_C))
        
        
        # 电机正向转动
        button_rotate = SiPushButton(self)
        button_rotate.resize(128, 32)
        button_rotate.attachment().setText("forward rotate")
        button_rotate.mouseReleaseEvent = lambda event: self.rotate(self.motor)
        
        # 电机逆向转动
        button_reverse = SiPushButton(self)
        button_reverse.resize(128, 32)
        button_reverse.attachment().setText("back rotate")
        button_reverse.mouseReleaseEvent = lambda event: self.reverse()
        
        # 电机正向加速
        button_speed = SiPushButton(self)
        button_speed.resize(128, 32)
        button_speed.attachment().setText("forward speed")
        button_speed.mouseReleaseEvent = lambda event: self.speed()
        
        # 电机逆向加速
        button_respeed = SiPushButton(self)
        button_respeed.resize(128, 32)
        button_respeed.attachment().setText("back speed")
        button_respeed.mouseReleaseEvent = lambda event: self.respeed()
        
        # 电机转速信息
        self.show_com_info = SiLabel(self)
        self.show_com_info.setAlignment(Qt.AlignCenter)
        self.show_com_info.setFixedSize(200, 32)
        self.show_com_info.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
        self.show_com_info.setStyleSheet(f"color: {self.colorGroup().fromToken(SiColor.TEXT_D)}")
        
        # 将com口选取添加到布局
        option_card_button_container_h.addWidget(self.package_selection_motor)
        # 将波特率选取添加到布局
        option_card_button_container_h.addWidget(button_rotate)
        # 打开com口按钮添加到布局
        option_card_button_container_h.addWidget(button_reverse)
        # 关闭com口按钮添加到布局
        option_card_button_container_h.addWidget(button_speed)
        # 关闭com口按钮添加到布局
        option_card_button_container_h.addWidget(button_respeed)
        # 显示com口信息添加到布局
        option_card_button_container_h.addWidget(self.show_com_info)
        
        self.option_card_button.body().addWidget(option_card_button_container_h)
        

        # 添加到第一个水平容器
        container_h_a.addWidget(self.option_card_button)

        # 添加两个水平容器到自己
        self.addWidget(container_h_a)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.option_card_button.setFixedWidth(event.size().width() - 50 - 16)
    
    # menu中被选中的值将会自动被传递为槽函数的参数（com）
    def motor_chosen(self, motor):
        self.motor = motor
    
    def rotate(self, motor):
        com.com_data = motor+"forward_rotate"
        com.Com_Send_Data()
        self.show_com_info.setText(f"{motor} forward rotate")
    
    def reverse(self):
        self.textEdit_Send.setText("reverse")
        com.Com_Send_Data()
        self.show_com_info.setText(f"reverse")
    
    def speed(self):
        self.textEdit_Send.setText("speed")
        com.Com_Send_Data()
        self.show_com_info.setText("speed")
    
    def respeed(self):
        self.textEdit_Send.setText("respeed")
        com.Com_Send_Data()
        self.show_com_info.setText("respeed")
        
        



