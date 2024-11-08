from siui.core.color.color import SiColor

from .color_group import SiColorGroup

class StarryNightTheme(SiColorGroup):
    def __init__(self):
        super().__init__()

        # 主题色
        self.assign(SiColor.THEME, "#0A0E21")  # 深蓝黑色
        self.assign(SiColor.THEME_TRANSITION_A, "#1C2A4C")  # 深蓝色
        self.assign(SiColor.THEME_TRANSITION_B, "#283A6A")  # 暗蓝色

        # SVG颜色
        self.assign(SiColor.SVG_NORMAL, "#FFFFFF")  # 白色
        self.assign(SiColor.SVG_THEME, "#FDEE00")  # 浅黄色

        # 层级颜色
        self.assign(SiColor.LAYER_DIM, "#0A0E2150")  # 深蓝黑色半透明

        # 工具提示背景
        self.assign(SiColor.TOOLTIP_BG, "#0A0E2140")  # 深蓝黑色半透明

        # 界面背景
        self.assign(SiColor.INTERFACE_BG_A, "#0A0E21")  # 深蓝黑色
        self.assign(SiColor.INTERFACE_BG_B, "#1C2A4C")  # 深蓝色
        self.assign(SiColor.INTERFACE_BG_C, "#283A6A")  # 暗蓝色
        self.assign(SiColor.INTERFACE_BG_D, "#1C2A4C")  # 深蓝色
        self.assign(SiColor.INTERFACE_BG_E, "#283A6A")  # 暗蓝色

        # 文本颜色
        self.assign(SiColor.TEXT_A, "#FDEE00")  # 浅黄色
        self.assign(SiColor.TEXT_B, "#FFFFFF")  # 白色
        self.assign(SiColor.TEXT_C, "#E6E6E6")  # 浅灰色
        self.assign(SiColor.TEXT_D, "#C0C0C0")  # 灰色
        self.assign(SiColor.TEXT_E, "#999999")  # 深灰色
        self.assign(SiColor.TEXT_THEME, "#FDEE00")  # 浅黄色

        # 侧边消息颜色
        self.assign(SiColor.SIDE_MSG_FLASH, "#FDEE00")  # 浅黄色
        self.assign(SiColor.SIDE_MSG_THEME_NORMAL, "#1C2A4C")  # 深蓝色
        self.assign(SiColor.SIDE_MSG_THEME_SUCCESS, "#00FF00")  # 绿色
        self.assign(SiColor.SIDE_MSG_THEME_INFO, "#00FFFF")  # 青色
        self.assign(SiColor.SIDE_MSG_THEME_WARNING, "#FFA500")  # 橙色
        self.assign(SiColor.SIDE_MSG_THEME_ERROR, "#FF0000")  # 红色

        # 菜单背景
        self.assign(SiColor.MENU_BG, "#283A6A")  # 暗蓝色

        # 标题相关
        self.assign(SiColor.TITLE_INDICATOR, "#FDEE00")  # 浅黄色
        self.assign(SiColor.TITLE_HIGHLIGHT, "#FFFFFF")  # 白色

        # 按钮鼠标相关
        self.assign(SiColor.BUTTON_IDLE, "#00000000")
        self.assign(SiColor.BUTTON_HOVER, "#FFFFFF20")
        self.assign(SiColor.BUTTON_FLASH, "#FFFFFF40")

        # 按钮外观
        self.assign(SiColor.BUTTON_PANEL, "#283A6A")  # 暗蓝色
        self.assign(SiColor.BUTTON_SHADOW, SiColor.mix(self.fromToken(SiColor.INTERFACE_BG_C), "#000000", 0.1))

        # 按钮主题背景
        self.assign(SiColor.BUTTON_THEMED_BG_A, "#0A0E21")  # 深蓝黑色
        self.assign(SiColor.BUTTON_THEMED_BG_B, "#1C2A4C")  # 深蓝色
        self.assign(SiColor.BUTTON_THEMED_SHADOW_A, "#000000")  # 黑色
        self.assign(SiColor.BUTTON_THEMED_SHADOW_B, "#0A0E21")  # 深蓝黑色

        # 开关按钮状态
        self.assign(SiColor.BUTTON_ON, "#00FF00")  # 绿色
        self.assign(SiColor.BUTTON_OFF, "#999999")  # 深灰色

        # 单选按钮
        self.assign(SiColor.RADIO_BUTTON_UNCHECKED, "#1C2A4C")  # 深蓝色
        self.assign(SiColor.RADIO_BUTTON_CHECKED, "#FDEE00")  # 浅黄色

        # 复选框
        self.assign(SiColor.CHECKBOX_SVG, "#FFFFFF")  # 白色
        self.assign(SiColor.CHECKBOX_UNCHECKED, "#999999")  # 深灰色
        self.assign(SiColor.CHECKBOX_CHECKED, "#FDEE00")  # 浅黄色

        # 文本按钮
        self.assign(SiColor.BUTTON_TEXT_BUTTON_IDLE, "#FDEE00")  # 浅黄色
        self.assign(SiColor.BUTTON_TEXT_BUTTON_FLASH, "#FDEE00")  # 浅黄色
        self.assign(SiColor.BUTTON_TEXT_BUTTON_HOVER, "#FFFFFF")  # 白色

        # 长按按钮
        self.assign(SiColor.BUTTON_LONG_PRESS_PANEL, "#0A0E21")  # 深蓝黑色
        self.assign(SiColor.BUTTON_LONG_PRESS_SHADOW, "#1C2A4C")  # 深蓝色
        self.assign(SiColor.BUTTON_LONG_PRESS_PROGRESS, "#FDEE00")  # 浅黄色

        # 开关
        self.assign(SiColor.SWITCH_DEACTIVATE, "#999999")  # 深灰色
        self.assign(SiColor.SWITCH_ACTIVATE, "#00FF00")  # 绿色

        # 滚动条
        self.assign(SiColor.SCROLL_BAR, "#0A0E2180")  # 深蓝黑色半透明

        # 进度条
        self.assign(SiColor.PROGRESS_BAR_TRACK, "#283A6A")  # 暗蓝色
        self.assign(SiColor.PROGRESS_BAR_PROCESSING, "#FDEE00")  # 浅黄色
        self.assign(SiColor.PROGRESS_BAR_COMPLETING, "#00FF00")  # 绿色
        self.assign(SiColor.PROGRESS_BAR_PAUSED, "#FFA500")  # 橙色
        self.assign(SiColor.PROGRESS_BAR_FLASHES, "#FFFFFF")  # 白色