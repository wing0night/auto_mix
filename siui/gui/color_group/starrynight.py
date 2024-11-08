from siui.core.color.color import SiColor

from .color_group import SiColorGroup

class VanGoghStarryNightColorGroup(SiColorGroup):
    def __init__(self):
        super().__init__()

        # 主题色 - 夜空深蓝色
        self.assign(SiColor.THEME, "#1E4877")  # 深蓝色[^3^]

        # 过渡色 - 夜空中的星星和月亮的黄色
        self.assign(SiColor.THEME_TRANSITION_A, "#FFD700")  # 金色[^3^]
        self.assign(SiColor.THEME_TRANSITION_B, "#FDEE00")  # 淡黄色[^3^]

        # SVG颜色
        self.assign(SiColor.SVG_NORMAL, "#FFFFFF")  # 白色
        self.assign(SiColor.SVG_THEME, "#FFD700")  # 金色[^3^]

        # 层级颜色
        self.assign(SiColor.LAYER_DIM, "#80000000")  # 黑色半透明

        # 工具提示背景
        self.assign(SiColor.TOOLTIP_BG, "#1E4877BF")  # 深蓝色半透明[^3^]

        # 界面背景
        self.assign(SiColor.INTERFACE_BG_A, "#1C1C1C")  # 黑色
        self.assign(SiColor.INTERFACE_BG_B, "#2A2A2A")  # 深灰色
        self.assign(SiColor.INTERFACE_BG_C, "#E0E0E0")  # 更浅的灰色
        self.assign(SiColor.INTERFACE_BG_D, "#D0D0D0")  # 浅灰色
        self.assign(SiColor.INTERFACE_BG_E, "#B0B0B0")  # 灰色

        # 文本颜色
        self.assign(SiColor.TEXT_A, "#000000")  # 黑色
        self.assign(SiColor.TEXT_B, "#000000")  # 黑色
        self.assign(SiColor.TEXT_C, "#979797")  # 灰色
        self.assign(SiColor.TEXT_D, "#AFAFAF")  # 深灰色
        self.assign(SiColor.TEXT_E, "#979797")  # 更深的灰色
        self.assign(SiColor.TEXT_THEME, "#FFD700")  # 金色[^3^]

        # 侧边消息颜色
        self.assign(SiColor.SIDE_MSG_FLASH, "#FFD700")  # 金色[^3^]
        self.assign(SiColor.SIDE_MSG_THEME_NORMAL, "#2A2A2A")  # 深灰色
        self.assign(SiColor.SIDE_MSG_THEME_SUCCESS, "#008000")  # 绿色
        self.assign(SiColor.SIDE_MSG_THEME_INFO, "#00FFFF")  # 青色
        self.assign(SiColor.SIDE_MSG_THEME_WARNING, "#FFA500")  # 橙色
        self.assign(SiColor.SIDE_MSG_THEME_ERROR, "#FF0000")  # 红色

        # 菜单背景
        self.assign(SiColor.MENU_BG, "#2A2A2A")  # 深灰色

        # 标题相关
        self.assign(SiColor.TITLE_INDICATOR, "#FFD700")  # 金色[^3^]
        self.assign(SiColor.TITLE_HIGHLIGHT, "#1E4877")  # 深蓝色[^3^]

        # 按钮鼠标相关
        self.assign(SiColor.BUTTON_IDLE, "#00000000")
        self.assign(SiColor.BUTTON_HOVER, "#1E487740")
        self.assign(SiColor.BUTTON_FLASH, "#FFD700")  # 金色[^3^]

        # 按钮外观
        self.assign(SiColor.BUTTON_PANEL, "#1C1C1C")  # 黑色
        self.assign(SiColor.BUTTON_SHADOW, SiColor.mix(self.fromToken(SiColor.INTERFACE_BG_C), "#000000", 0.9))

        # 按钮主题背景
        self.assign(SiColor.BUTTON_THEMED_BG_A, "#1E4877")  # 深蓝色[^3^]
        self.assign(SiColor.BUTTON_THEMED_BG_B, "#FFD700")  # 金色[^3^]
        self.assign(SiColor.BUTTON_THEMED_SHADOW_A, "#000000")  # 黑色
        self.assign(SiColor.BUTTON_THEMED_SHADOW_B, "#FFD700")  # 金色[^3^]

        # 开关按钮状态
        self.assign(SiColor.BUTTON_ON, "#008000")  # 绿色
        self.assign(SiColor.BUTTON_OFF, "#CCCCCC")  # 更浅的灰色

        # 单选按钮
        self.assign(SiColor.RADIO_BUTTON_UNCHECKED, "#2A2A2A")  # 深灰色
        self.assign(SiColor.RADIO_BUTTON_CHECKED, "#FFD700")  # 金色[^3^]

        # 复选框
        self.assign(SiColor.CHECKBOX_SVG, "#1C1C1C")  # 黑色
        self.assign(SiColor.CHECKBOX_UNCHECKED, "#CCCCCC")  # 更浅的灰色
        self.assign(SiColor.CHECKBOX_CHECKED, "#FFD700")  # 金色[^3^]

        # 文本按钮
        self.assign(SiColor.BUTTON_TEXT_BUTTON_IDLE, "#FFD700")  # 金色[^3^]
        self.assign(SiColor.BUTTON_TEXT_BUTTON_FLASH, "#FFD700")  # 金色[^3^]
        self.assign(SiColor.BUTTON_TEXT_BUTTON_HOVER, "#FFFFFF")  # 白色

        # 长按按钮
        self.assign(SiColor.BUTTON_LONG_PRESS_PANEL, "#FF0080")  # 红色
        self.assign(SiColor.BUTTON_LONG_PRESS_SHADOW, "#A52A2A")  # 棕色
        self.assign(SiColor.BUTTON_LONG_PRESS_PROGRESS, "#FFD700")  # 金色[^3^]

        # 开关
        self.assign(SiColor.SWITCH_DEACTIVATE, "#CCCCCC")  # 更浅的灰色
        self.assign(SiColor.SWITCH_ACTIVATE, "#008000")  # 绿色

        # 滚动条
        self.assign(SiColor.SCROLL_BAR, "#FFD70099")  # 金色半透明[^3^]

        # 进度条
        self.assign(SiColor.PROGRESS_BAR_TRACK, "#2A2A2A")  # 深灰色
        self.assign(SiColor.PROGRESS_BAR_PROCESSING, "#FFD700")  # 金色[^3^]
        self.assign(SiColor.PROGRESS_BAR_COMPLETING, "#008000")  # 绿色
        self.assign(SiColor.PROGRESS_BAR_PAUSED, "#FFA500")  # 橙色
        self.assign(SiColor.PROGRESS_BAR_FLASHES, "#FFFFFF")  # 白色



