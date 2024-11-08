from siui.core.color.color import SiColor

from .color_group import SiColorGroup

class RainyNightColorGroup(SiColorGroup):
    def __init__(self):
        super().__init__()

        # 主题色 - 深蓝色
        self.assign(SiColor.THEME, "#0A246A")  # 深蓝色

        # 过渡色 - 稍微亮一点的深蓝色
        self.assign(SiColor.THEME_TRANSITION_A, "#1A3A77")  # 中深蓝色
        self.assign(SiColor.THEME_TRANSITION_B, "#2A4E8A")  # 浅深蓝色

        # SVG颜色
        self.assign(SiColor.SVG_NORMAL, "#FFFFFF")  # 白色
        self.assign(SiColor.SVG_THEME, "#0A246A")  # 深蓝色

        # 层级颜色
        self.assign(SiColor.LAYER_DIM, "#0A246A80")  # 深蓝色半透明

        # 工具提示背景
        self.assign(SiColor.TOOLTIP_BG, "#0A246A80")  # 深蓝色半透明

        # 界面背景
        self.assign(SiColor.INTERFACE_BG_A, "#0A246A")  # 深蓝色
        self.assign(SiColor.INTERFACE_BG_B, "#0D2D72")  # 深蓝色
        self.assign(SiColor.INTERFACE_BG_C, "#102A7F")  # 深蓝色
        self.assign(SiColor.INTERFACE_BG_D, "#142C8E")  # 深蓝色
        self.assign(SiColor.INTERFACE_BG_E, "#182D9D")  # 深蓝色

        # 文本颜色
        self.assign(SiColor.TEXT_A, "#ADD8E6")  # 浅蓝色
        self.assign(SiColor.TEXT_B, "#FFFFFF")  # 白色
        self.assign(SiColor.TEXT_C, "#82A4C6")  # 中浅蓝色
        self.assign(SiColor.TEXT_D, "#5983A3")  # 中深蓝色
        self.assign(SiColor.TEXT_E, "#2E5A8B")  # 深蓝色
        self.assign(SiColor.TEXT_THEME, "#ADD8E6")  # 浅蓝色

        # 侧边消息颜色
        self.assign(SiColor.SIDE_MSG_FLASH, "#FFFF00")  # 黄色
        self.assign(SiColor.SIDE_MSG_THEME_NORMAL, "#1A3A77")  # 中深蓝色
        self.assign(SiColor.SIDE_MSG_THEME_SUCCESS, "#00FF00")  # 绿色
        self.assign(SiColor.SIDE_MSG_THEME_INFO, "#0A246A")  # 深蓝色
        self.assign(SiColor.SIDE_MSG_THEME_WARNING, "#FFA500")  # 橙色
        self.assign(SiColor.SIDE_MSG_THEME_ERROR, "#FF0000")  # 红色

        # 菜单背景
        self.assign(SiColor.MENU_BG, "#102A7F")  # 深蓝色

        # 标题相关
        self.assign(SiColor.TITLE_INDICATOR, "#ADD8E6")  # 浅蓝色
        self.assign(SiColor.TITLE_HIGHLIGHT, "#FFFFFF")  # 白色

        # 按钮鼠标相关
        self.assign(SiColor.BUTTON_IDLE, "#00000000")
        self.assign(SiColor.BUTTON_HOVER, "#FFFFFF20")
        self.assign(SiColor.BUTTON_FLASH, "#FFFFFF40")

        # 按钮外观
        self.assign(SiColor.BUTTON_PANEL, "#0A246A")  # 深蓝色
        self.assign(SiColor.BUTTON_SHADOW, SiColor.mix(self.fromToken(SiColor.INTERFACE_BG_C), "#000000", 0.5))

        # 按钮主题背景
        self.assign(SiColor.BUTTON_THEMED_BG_A, "#1A3A77")  # 中深蓝色
        self.assign(SiColor.BUTTON_THEMED_BG_B, "#2A4E8A")  # 浅深蓝色
        self.assign(SiColor.BUTTON_THEMED_SHADOW_A, "#000000")  # 黑色
        self.assign(SiColor.BUTTON_THEMED_SHADOW_B, "#0A246A")  # 深蓝色

        # 开关按钮状态
        self.assign(SiColor.BUTTON_ON, "#00FF00")  # 绿色
        self.assign(SiColor.BUTTON_OFF, "#5983A3")  # 中深蓝色

        # 单选按钮
        self.assign(SiColor.RADIO_BUTTON_UNCHECKED, "#1A3A77")  # 中深蓝色
        self.assign(SiColor.RADIO_BUTTON_CHECKED, "#ADD8E6")  # 浅蓝色

        # 复选框
        self.assign(SiColor.CHECKBOX_SVG, "#0A246A")  # 深蓝色
        self.assign(SiColor.CHECKBOX_UNCHECKED, "#5983A3")  # 中深蓝色
        self.assign(SiColor.CHECKBOX_CHECKED, "#ADD8E6")  # 浅蓝色

        # 文本按钮
        self.assign(SiColor.BUTTON_TEXT_BUTTON_IDLE, "#ADD8E6")  # 浅蓝色
        self.assign(SiColor.BUTTON_TEXT_BUTTON_FLASH, "#ADD8E6")  # 浅蓝色
        self.assign(SiColor.BUTTON_TEXT_BUTTON_HOVER, "#FFFFFF")  # 白色

        # 长按按钮
        self.assign(SiColor.BUTTON_LONG_PRESS_PANEL, "#0A246A")  # 深蓝色
        self.assign(SiColor.BUTTON_LONG_PRESS_SHADOW, "#000000")  # 黑色
        self.assign(SiColor.BUTTON_LONG_PRESS_PROGRESS, "#1A3A77")  # 中深蓝色

        # 开关
        self.assign(SiColor.SWITCH_DEACTIVATE, "#5983A3")  # 中深蓝色
        self.assign(SiColor.SWITCH_ACTIVATE, "#00FF00")  # 绿色

        # 滚动条
        self.assign(SiColor.SCROLL_BAR, "#ADD8E699")  # 浅蓝色半透明

        # 进度条
        self.assign(SiColor.PROGRESS_BAR_TRACK, "#1A3A77")  # 中深蓝色
        self.assign(SiColor.PROGRESS_BAR_PROCESSING, "#2A4E8A")  # 浅深蓝色
        self.assign(SiColor.PROGRESS_BAR_COMPLETING, "#00FF00")  # 绿色
        self.assign(SiColor.PROGRESS_BAR_PAUSED, "#FFA500")  # 橙色
        self.assign(SiColor.PROGRESS_BAR_FLASHES, "#FFFFFF")  # 白色