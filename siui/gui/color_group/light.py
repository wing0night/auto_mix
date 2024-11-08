from siui.core.color.color import SiColor

from .color_group import SiColorGroup

class PastelColorGroup(SiColorGroup):
    def __init__(self):
        super().__init__()

        # 主题色
        self.assign(SiColor.THEME, "#A6AEBF")  # 灰蓝色
        self.assign(SiColor.THEME_TRANSITION_A, "#C5D3E8")  # 浅蓝色
        self.assign(SiColor.THEME_TRANSITION_B, "#D0E8C5")  # 浅绿色

        # SVG颜色
        self.assign(SiColor.SVG_NORMAL, "#000000")  # 黑色
        self.assign(SiColor.SVG_THEME, "#A6AEBF")  # 灰蓝色

        # 层级颜色
        self.assign(SiColor.LAYER_DIM, "#00000080")  # 黑色半透明

        # 工具提示背景
        self.assign(SiColor.TOOLTIP_BG, "#A6AEBF1A")  # 灰蓝色半透明

        # 界面背景
        self.assign(SiColor.INTERFACE_BG_A, "#FFF8DE")  # 浅黄色
        self.assign(SiColor.INTERFACE_BG_B, "#FFFFFF")  # 白色
        self.assign(SiColor.INTERFACE_BG_C, "#F5F5F5")  # 浅灰色
        self.assign(SiColor.INTERFACE_BG_D, "#E0E0E0")  # 更浅的灰色
        self.assign(SiColor.INTERFACE_BG_E, "#D0E8C5")  # 浅绿色

        # 文本颜色
        self.assign(SiColor.TEXT_A, "#000000")  # 黑色
        self.assign(SiColor.TEXT_B, "#333333")  # 深灰色
        self.assign(SiColor.TEXT_C, "#666666")  # 灰色
        self.assign(SiColor.TEXT_D, "#999999")  # 浅灰色
        self.assign(SiColor.TEXT_E, "#A6AEBF")  # 灰蓝色
        self.assign(SiColor.TEXT_THEME, "#000000")  # 黑色

        # 侧边消息颜色
        self.assign(SiColor.SIDE_MSG_FLASH, "#FFD700")  # 金色
        self.assign(SiColor.SIDE_MSG_THEME_NORMAL, "#FFFFFF")  # 白色
        self.assign(SiColor.SIDE_MSG_THEME_SUCCESS, "#008000")  # 绿色
        self.assign(SiColor.SIDE_MSG_THEME_INFO, "#00FFFF")  # 青色
        self.assign(SiColor.SIDE_MSG_THEME_WARNING, "#FFA500")  # 橙色
        self.assign(SiColor.SIDE_MSG_THEME_ERROR, "#FF0000")  # 红色

        # 菜单背景
        self.assign(SiColor.MENU_BG, "#D0E8C5")  # 浅绿色

        # 标题相关
        self.assign(SiColor.TITLE_INDICATOR, "#000000")  # 黑色
        self.assign(SiColor.TITLE_HIGHLIGHT, "#A6AEBF")  # 灰蓝色

        # 按钮鼠标相关
        self.assign(SiColor.BUTTON_IDLE, "#00000000")
        self.assign(SiColor.BUTTON_HOVER, "#00000020")
        self.assign(SiColor.BUTTON_FLASH, "#00000040")

        # 按钮外观
        self.assign(SiColor.BUTTON_PANEL, "#FFFFFF")  # 白色
        self.assign(SiColor.BUTTON_SHADOW, SiColor.mix(self.fromToken(SiColor.INTERFACE_BG_C), "#000000", 0.1))

        # 按钮主题背景
        self.assign(SiColor.BUTTON_THEMED_BG_A, "#A6AEBF")  # 灰蓝色
        self.assign(SiColor.BUTTON_THEMED_BG_B, "#C5D3E8")  # 浅蓝色
        self.assign(SiColor.BUTTON_THEMED_SHADOW_A, "#000000")  # 黑色
        self.assign(SiColor.BUTTON_THEMED_SHADOW_B, "#A6AEBF")  # 灰蓝色

        # 开关按钮状态
        self.assign(SiColor.BUTTON_ON, "#008000")  # 绿色
        self.assign(SiColor.BUTTON_OFF, "#CCCCCC")  # 更浅的灰色

        # 单选按钮
        self.assign(SiColor.RADIO_BUTTON_UNCHECKED, "#FFFFFF")  # 白色
        self.assign(SiColor.RADIO_BUTTON_CHECKED, "#000000")  # 黑色

        # 复选框
        self.assign(SiColor.CHECKBOX_SVG, "#FFFFFF")  # 白色
        self.assign(SiColor.CHECKBOX_UNCHECKED, "#CCCCCC")  # 更浅的灰色
        self.assign(SiColor.CHECKBOX_CHECKED, "#000000")  # 黑色

        # 文本按钮
        self.assign(SiColor.BUTTON_TEXT_BUTTON_IDLE, "#000000")  # 黑色
        self.assign(SiColor.BUTTON_TEXT_BUTTON_FLASH, "#000000")  # 黑色
        self.assign(SiColor.BUTTON_TEXT_BUTTON_HOVER, "#333333")  # 深灰色

        # 长按按钮
        self.assign(SiColor.BUTTON_LONG_PRESS_PANEL, "#A6AEBF")  # 灰蓝色
        self.assign(SiColor.BUTTON_LONG_PRESS_SHADOW, "#000000")  # 黑色
        self.assign(SiColor.BUTTON_LONG_PRESS_PROGRESS, "#C5D3E8")  # 浅蓝色

        # 开关
        self.assign(SiColor.SWITCH_DEACTIVATE, "#CCCCCC")  # 更浅的灰色
        self.assign(SiColor.SWITCH_ACTIVATE, "#008000")  # 绿色

        # 滚动条
        self.assign(SiColor.SCROLL_BAR, "#00000099")  # 黑色半透明

        # 进度条
        self.assign(SiColor.PROGRESS_BAR_TRACK, "#E0E0E0")  # 浅灰色
        self.assign(SiColor.PROGRESS_BAR_PROCESSING, "#A6AEBF")  # 灰蓝色
        self.assign(SiColor.PROGRESS_BAR_COMPLETING, "#008000")  # 绿色
        self.assign(SiColor.PROGRESS_BAR_PAUSED, "#FFA500")  # 橙色
        self.assign(SiColor.PROGRESS_BAR_FLASHES, "#FFFFFF")  # 白色