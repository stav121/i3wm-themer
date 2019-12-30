from enum import Enum, unique


@unique
class XresourcesAttr(Enum):
    """
    Attributes that should be parsed from the configuration file for Xresources.
    """
    NAME = 'xresources'
    BACKGROUND = 'background'
    FOREGROUND = 'foreground'
    CURSOR = 'cursorcolor'
    COLOR0 = 'color0'
    COLOR1 = 'color1'
    COLOR2 = 'color2'
    COLOR3 = 'color3'
    COLOR4 = 'color4'
    COLOR5 = 'color5'
    COLOR6 = 'color6'
    COLOR7 = 'color7'
    COLOR8 = 'color8'
    COLOR9 = 'color9'
    COLOR10 = 'color10'
    COLOR11 = 'color11'
    COLOR12 = 'color12'
    COLOR13 = 'color13'
    COLOR14 = 'color14'
    COLOR15 = 'color15'
    ROFI_WIND = 'rofi.color-window'
    ROFI_NORM = 'rofi.color-normal'
    ROFI_ACTI = 'rofi.color-active'
    ROFI_URGE = 'rofi.color-urgent'


@unique
class I3Attr(Enum):
    """
    Attributes that should be parsed from the configuration file for i3.
    """
    NAME = 'i3wm'
    BACKGROUND = 'client.background'
    FOCUSED = 'client.focused'
    UNFOCUSED = 'client.unfocused'
    INACTIVE = 'client.focused_inactive'
    URGENT = 'client.urgent'
    PLACEHOLDER = 'client.placeholder'


@unique
class PolybarAttr(Enum):
    """
    Attributes that should be parsed from the configuration file for Polybar.
    """
    NAME = 'polybar'
    BACKGROUND = 'background'
    FOREGROUND = 'foreground'
    MOD_L = 'modules-left'
    MOD_C = 'modules-center'
    MOD_R = 'modules-right'
    LABEL_UN_BACK = 'label-unfocused-background'
    LABEL_UN_FORE = 'label-unfocused-foreground'
    LABEL_MOD_BACK = 'label-mode-background'
    LABEL_MOD_FORE = 'label-mode-foreground'
    LABEL_FOC_BACK = 'label-focused-background'
    LABEL_FOC_FORE = 'label-focused-foreground'
    LABEL_VIS_BACK = 'label-visible-background'
    LABEL_VIS_FORE = 'label-visible-foreground'
    FORMAT_BACK = 'format-background'
    FORMAT_FORE = 'format-foreground'
    LABEL_OPEN_FORE = 'label-open-foreground'
    LABEL_CLOSE_FORE = 'label-close-foreground'
    LABEL_SEP_FOREGROUND = 'label-separator-foreground'
    FORMAT_CON_FORE = 'format-connected-foreground'
    FORMAT_CON_BACK = 'format-connected-background'
    FORMAT_CON_PRE_FORE = 'format-connected-prefix-foreground'
    RAMP_SIG_FOREGROUND = 'ramp-signal-foreground'


@unique
class NitrogenAttr(Enum):
    """
    Attributes that should be parsed from the configuration file for Nitrogen.
    """
    NAME = 'wallpaper'
