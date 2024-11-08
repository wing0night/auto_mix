from siui.core.color.color import SiColor

from .color_group import SiColorGroup

class HalloweenColorGroup(SiColorGroup):
    def __init__(self):
        super().__init__()

        # 主题色
        self.assign(SiColor.THEME, "#FFA500")  # 橙色
        self.assign(SiColor.THEME_TRANSITION_A, "#800080")  # 深紫色
        self.assign(SiColor.THEME_TRANSITION_B, "#9932CC")  # 淡紫色

        # SVG颜色
        self.assign(SiColor.SVG_NORMAL, "#FFFFFF")  # 白色
        self.assign(SiColor.SVG_THEME, "#FFA500")  # 橙色

        # 层级颜色
        self.assign(SiColor.LAYER_DIM, "#80000080")  # 黑色半透明

        # 工具提示背景
        self.assign(SiColor.TOOLTIP_BG, "#FFA500CC")  # 橙色半透明

        # 界面背景
        self.assign(SiColor.INTERFACE_BG_A, "#1C1C1C")  # 深灰色
        self.assign(SiColor.INTERFACE_BG_B, "#2A2A2A")  # 灰色
        self.assign(SiColor.INTERFACE_BG_C, "#383838")  # 浅灰色
        self.assign(SiColor.INTERFACE_BG_D, "#464646")  # 更浅的灰色
        self.assign(SiColor.INTERFACE_BG_E, "#545454")  # 最浅的灰色

        # 文本颜色
        self.assign(SiColor.TEXT_A, "#FFFFFF")  # 白色
        self.assign(SiColor.TEXT_B, "#E5E5E5")  # 浅灰色
        self.assign(SiColor.TEXT_C, "#C7C7C7")  # 更浅的灰色
        self.assign(SiColor.TEXT_D, "#AFAFAF")  # 灰色
        self.assign(SiColor.TEXT_E, "#979797")  # 深灰色
        self.assign(SiColor.TEXT_THEME, "#FF69B4")  # 浅紫色

        # 侧边消息颜色
        self.assign(SiColor.SIDE_MSG_FLASH, "#FFFF99")  # 亮黄色
        self.assign(SiColor.SIDE_MSG_THEME_NORMAL, "#2A2A2A")  # 灰色
        self.assign(SiColor.SIDE_MSG_THEME_SUCCESS, "#32CD32")  # 绿色
        self.assign(SiColor.SIDE_MSG_THEME_INFO, "#20B2AA")  # 青色
        self.assign(SiColor.SIDE_MSG_THEME_WARNING, "#FFA500")  # 橙色
        self.assign(SiColor.SIDE_MSG_THEME_ERROR, "#FF4500")  # 红色

        # 菜单背景
        self.assign(SiColor.MENU_BG, "#383838")  # 浅灰色

        # 标题相关
        self.assign(SiColor.TITLE_INDICATOR, "#FF69B4")  # 浅紫色
        self.assign(SiColor.TITLE_HIGHLIGHT, "#FF4500")  # 红色

        # 按钮鼠标相关
        self.assign(SiColor.BUTTON_IDLE, "#00FFFFFF")
        self.assign(SiColor.BUTTON_HOVER, "#10FFFFFF")
        self.assign(SiColor.BUTTON_FLASH, "#20FFFFFF")

        # 按钮外观
        self.assign(SiColor.BUTTON_PANEL, "#545454")  # 最浅的灰色
        self.assign(SiColor.BUTTON_SHADOW, SiColor.mix(self.fromToken(SiColor.INTERFACE_BG_C), "#000000", 0.9))

        # 按钮主题背景
        self.assign(SiColor.BUTTON_THEMED_BG_A, "#800080")  # 深紫色
        self.assign(SiColor.BUTTON_THEMED_BG_B, "#9932CC")  # 淡紫色
        self.assign(SiColor.BUTTON_THEMED_SHADOW_A, "#4B0082")  # 深紫色阴影
        self.assign(SiColor.BUTTON_THEMED_SHADOW_B, "#6A0DAD")  # 淡紫色阴影

        # 开关按钮状态
        self.assign(SiColor.BUTTON_ON, "#4B0082")  # 深紫色
        self.assign(SiColor.BUTTON_OFF, "#6A0DAD")  # 淡紫色

        # 单选按钮
        self.assign(SiColor.RADIO_BUTTON_UNCHECKED, "#2A2A2A")  # 灰色
        self.assign(SiColor.RADIO_BUTTON_CHECKED, "#FF69B4")  # 浅紫色

        # 复选框
        self.assign(SiColor.CHECKBOX_SVG, "#1C1C1C")  # 深灰色
        self.assign(SiColor.CHECKBOX_UNCHECKED, "#AFAFAF")  # 灰色
        self.assign(SiColor.CHECKBOX_CHECKED, "#FF69B4")  # 浅紫色

        # 文本按钮
        self.assign(SiColor.BUTTON_TEXT_BUTTON_IDLE, "#FF69B4")  # 浅紫色
        self.assign(SiColor.BUTTON_TEXT_BUTTON_FLASH, "#FF69B4")  # 浅紫色
        self.assign(SiColor.BUTTON_TEXT_BUTTON_HOVER, "#FFFFFF")  # 白色

        # 长按按钮
        self.assign(SiColor.BUTTON_LONG_PRESS_PANEL, "#FF4500")  # 红色
        self.assign(SiColor.BUTTON_LONG_PRESS_SHADOW, "#A52A2A")  # 棕色
        self.assign(SiColor.BUTTON_LONG_PRESS_PROGRESS, "#FF6347")  # 番茄色

        # 开关
        self.assign(SiColor.SWITCH_DEACTIVATE, "#D2D2D2")  # 灰色
        self.assign(SiColor.SWITCH_ACTIVATE, "#FF6347")  # 番茄色

        # 滚动条
        self.assign(SiColor.SCROLL_BAR, "#FFA50099")  # 橙色半透明

        # 进度条
        self.assign(SiColor.PROGRESS_BAR_TRACK, "#252229")  # 深灰色
        self.assign(SiColor.PROGRESS_BAR_PROCESSING, "#32CD32")  # 绿色
        self.assign(SiColor.PROGRESS_BAR_COMPLETING, "#FFD700")  # 金色
        self.assign(SiColor.PROGRESS_BAR_PAUSED, "#7F7F7F")  # 灰色
        self.assign(SiColor.PROGRESS_BAR_FLASHES, "#FFFFFF")  # 白色

