from siui.core.color.color import SiColor

from .color_group import SiColorGroup

class RainbowCandyColorGroup(SiColorGroup):
    def __init__(self):
        super().__init__()

        # 主题色
        self.assign(SiColor.THEME, "#FF0080")  # 红色
        self.assign(SiColor.THEME_TRANSITION_A, "#FFA500")  # 橙色
        self.assign(SiColor.THEME_TRANSITION_B, "#FFFF00")  # 黄色

        # SVG颜色
        self.assign(SiColor.SVG_NORMAL, "#FFFFFF")  # 白色
        self.assign(SiColor.SVG_THEME, "#FF0080")  # 红色

        # 层级颜色
        self.assign(SiColor.LAYER_DIM, "#80FFFFFF")  # 白色半透明

        # 工具提示背景
        self.assign(SiColor.TOOLTIP_BG, "#FF008040")  # 红色半透明

        # 界面背景
        self.assign(SiColor.INTERFACE_BG_A, "#FFFFFF")  # 白色
        self.assign(SiColor.INTERFACE_BG_B, "#F0F8FF")  # 浅蓝色
        self.assign(SiColor.INTERFACE_BG_C, "#E0FFFF")  # 浅绿色
        self.assign(SiColor.INTERFACE_BG_D, "#F5F5F5")  # 浅灰色
        self.assign(SiColor.INTERFACE_BG_E, "#D0E0E3")  # 浅紫色

        # 文本颜色
        self.assign(SiColor.TEXT_A, "#000000")  # 黑色
        self.assign(SiColor.TEXT_B, "#333333")  # 深灰色
        self.assign(SiColor.TEXT_C, "#666666")  # 灰色
        self.assign(SiColor.TEXT_D, "#999999")  # 浅灰色
        self.assign(SiColor.TEXT_E, "#CCCCCC")  # 更浅的灰色
        self.assign(SiColor.TEXT_THEME, "#8A2BE2")  # 紫色

        # 侧边消息颜色
        self.assign(SiColor.SIDE_MSG_FLASH, "#FFD700")  # 金色
        self.assign(SiColor.SIDE_MSG_THEME_NORMAL, "#F0F8FF")  # 浅蓝色
        self.assign(SiColor.SIDE_MSG_THEME_SUCCESS, "#008000")  # 绿色
        self.assign(SiColor.SIDE_MSG_THEME_INFO, "#00FFFF")  # 青色
        self.assign(SiColor.SIDE_MSG_THEME_WARNING, "#FFA500")  # 橙色
        self.assign(SiColor.SIDE_MSG_THEME_ERROR, "#FF0000")  # 红色

        # 菜单背景
        self.assign(SiColor.MENU_BG, "#E0FFFF")  # 浅绿色

        # 标题相关
        self.assign(SiColor.TITLE_INDICATOR, "#8A2BE2")  # 紫色
        self.assign(SiColor.TITLE_HIGHLIGHT, "#000000")  # 黑色

        # 按钮鼠标相关
        self.assign(SiColor.BUTTON_IDLE, "#00000000")
        self.assign(SiColor.BUTTON_HOVER, "#00000020")
        self.assign(SiColor.BUTTON_FLASH, "#00000040")

        # 按钮外观
        self.assign(SiColor.BUTTON_PANEL, "#FFFFFF")  # 白色
        self.assign(SiColor.BUTTON_SHADOW, SiColor.mix(self.fromToken(SiColor.INTERFACE_BG_C), "#000000", 0.1))

        # 按钮主题背景
        self.assign(SiColor.BUTTON_THEMED_BG_A, "#FF0080")  # 红色
        self.assign(SiColor.BUTTON_THEMED_BG_B, "#FFA500")  # 橙色
        self.assign(SiColor.BUTTON_THEMED_SHADOW_A, "#800000")  # 深红色
        self.assign(SiColor.BUTTON_THEMED_SHADOW_B, "#FF4500")  # 深橙色

        # 开关按钮状态
        self.assign(SiColor.BUTTON_ON, "#008000")  # 绿色
        self.assign(SiColor.BUTTON_OFF, "#CCCCCC")  # 更浅的灰色

        # 单选按钮
        self.assign(SiColor.RADIO_BUTTON_UNCHECKED, "#F0F8FF")  # 浅蓝色
        self.assign(SiColor.RADIO_BUTTON_CHECKED, "#8A2BE2")  # 紫色

        # 复选框
        self.assign(SiColor.CHECKBOX_SVG, "#FFFFFF")  # 白色
        self.assign(SiColor.CHECKBOX_UNCHECKED, "#CCCCCC")  # 更浅的灰色
        self.assign(SiColor.CHECKBOX_CHECKED, "#8A2BE2")  # 紫色

        # 文本按钮
        self.assign(SiColor.BUTTON_TEXT_BUTTON_IDLE, "#8A2BE2")  # 紫色
        self.assign(SiColor.BUTTON_TEXT_BUTTON_FLASH, "#8A2BE2")  # 紫色
        self.assign(SiColor.BUTTON_TEXT_BUTTON_HOVER, "#000000")  # 黑色

        # 长按按钮
        self.assign(SiColor.BUTTON_LONG_PRESS_PANEL, "#FF0080")  # 红色
        self.assign(SiColor.BUTTON_LONG_PRESS_SHADOW, "#FF4500")  # 深橙色
        self.assign(SiColor.BUTTON_LONG_PRESS_PROGRESS, "#FFD700")  # 金色

        # 开关
        self.assign(SiColor.SWITCH_DEACTIVATE, "#CCCCCC")  # 更浅的灰色
        self.assign(SiColor.SWITCH_ACTIVATE, "#008000")  # 绿色

        # 滚动条
        self.assign(SiColor.SCROLL_BAR, "#FF008099")  # 红色半透明

        # 进度条
        self.assign(SiColor.PROGRESS_BAR_TRACK, "#E0E0E0")  # 浅灰色
        self.assign(SiColor.PROGRESS_BAR_PROCESSING, "#FF0080")  # 红色
        self.assign(SiColor.PROGRESS_BAR_COMPLETING, "#008000")  # 绿色
        self.assign(SiColor.PROGRESS_BAR_PAUSED, "#FFA500")  # 橙色
        self.assign(SiColor.PROGRESS_BAR_FLASHES, "#FFFFFF")  # 白色