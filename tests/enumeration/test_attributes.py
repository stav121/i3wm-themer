import logging
import unittest

from i3wmthemer.enumeration.attributes import XresourcesAttr, I3Attr, PolybarAttr, NitrogenAttr

logging.disable(logging.ERROR)


class TestAttributes(unittest.TestCase):
    """
    Tests for enumeration.
    """

    def test_xresources_attributes(self):
        """
        Test for XresourcesAttr.
        """
        self.assertEqual(XresourcesAttr.NAME.value, 'xresources')
        self.assertEqual(XresourcesAttr.BACKGROUND.value, 'background')
        self.assertEqual(XresourcesAttr.FOREGROUND.value, 'foreground')
        self.assertEqual(XresourcesAttr.CURSOR.value, 'cursorcolor')
        self.assertEqual(XresourcesAttr.COLOR0.value, 'color0')
        self.assertEqual(XresourcesAttr.COLOR1.value, 'color1')
        self.assertEqual(XresourcesAttr.COLOR2.value, 'color2')
        self.assertEqual(XresourcesAttr.COLOR3.value, 'color3')
        self.assertEqual(XresourcesAttr.COLOR4.value, 'color4')
        self.assertEqual(XresourcesAttr.COLOR5.value, 'color5')
        self.assertEqual(XresourcesAttr.COLOR6.value, 'color6')
        self.assertEqual(XresourcesAttr.COLOR7.value, 'color7')
        self.assertEqual(XresourcesAttr.COLOR8.value, 'color8')
        self.assertEqual(XresourcesAttr.COLOR9.value, 'color9')
        self.assertEqual(XresourcesAttr.COLOR10.value, 'color10')
        self.assertEqual(XresourcesAttr.COLOR11.value, 'color11')
        self.assertEqual(XresourcesAttr.COLOR12.value, 'color12')
        self.assertEqual(XresourcesAttr.COLOR13.value, 'color13')
        self.assertEqual(XresourcesAttr.COLOR14.value, 'color14')
        self.assertEqual(XresourcesAttr.COLOR15.value, 'color15')
        self.assertEqual(XresourcesAttr.ROFI_WIND.value, 'rofi.color-window')
        self.assertEqual(XresourcesAttr.ROFI_NORM.value, 'rofi.color-normal')
        self.assertEqual(XresourcesAttr.ROFI_ACTI.value, 'rofi.color-active')
        self.assertEqual(XresourcesAttr.ROFI_URGE.value, 'rofi.color-urgent')

    def test_i3_attributes(self):
        """
        Test for I3Attr.
        """
        self.assertEqual(I3Attr.NAME.value, 'i3wm')
        self.assertEqual(I3Attr.BACKGROUND.value, 'client.background')
        self.assertEqual(I3Attr.FOCUSED.value, 'client.focused')
        self.assertEqual(I3Attr.UNFOCUSED.value, 'client.unfocused')
        self.assertEqual(I3Attr.INACTIVE.value, 'client.focused_inactive')
        self.assertEqual(I3Attr.URGENT.value, 'client.urgent')
        self.assertEqual(I3Attr.PLACEHOLDER.value, 'client.placeholder')

    def test_polybar_attributes(self):
        """
        Test for PolybarAttri.
        """
        self.assertEqual(PolybarAttr.NAME.value, 'polybar')
        self.assertEqual(PolybarAttr.BACKGROUND.value, 'background')
        self.assertEqual(PolybarAttr.FOREGROUND.value, 'foreground')
        self.assertEqual(PolybarAttr.MOD_L.value, 'modules-left')
        self.assertEqual(PolybarAttr.MOD_C.value, 'modules-center')
        self.assertEqual(PolybarAttr.MOD_R.value, 'modules-right')
        self.assertEqual(PolybarAttr.LABEL_UN_BACK.value, 'label-unfocused-background')
        self.assertEqual(PolybarAttr.LABEL_UN_FORE.value, 'label-unfocused-foreground')
        self.assertEqual(PolybarAttr.LABEL_MOD_BACK.value, 'label-mode-background')
        self.assertEqual(PolybarAttr.LABEL_MOD_FORE.value, 'label-mode-foreground')
        self.assertEqual(PolybarAttr.LABEL_FOC_BACK.value, 'label-focused-background')
        self.assertEqual(PolybarAttr.LABEL_FOC_FORE.value, 'label-focused-foreground')
        self.assertEqual(PolybarAttr.LABEL_VIS_BACK.value, 'label-visible-background')
        self.assertEqual(PolybarAttr.LABEL_VIS_FORE.value, 'label-visible-foreground')
        self.assertEqual(PolybarAttr.FORMAT_BACK.value, 'format-background')
        self.assertEqual(PolybarAttr.FORMAT_FORE.value, 'format-foreground')
        self.assertEqual(PolybarAttr.LABEL_OPEN_FORE.value, 'label-open-foreground')
        self.assertEqual(PolybarAttr.LABEL_CLOSE_FORE.value, 'label-close-foreground')
        self.assertEqual(PolybarAttr.LABEL_SEP_FOREGROUND.value, 'label-separator-foreground')
        self.assertEqual(PolybarAttr.FORMAT_CON_FORE.value, 'format-connected-foreground')
        self.assertEqual(PolybarAttr.FORMAT_CON_BACK.value, 'format-connected-background')
        self.assertEqual(PolybarAttr.FORMAT_CON_PRE_FORE.value, 'format-connected-prefix-foreground')
        self.assertEqual(PolybarAttr.RAMP_SIG_FOREGROUND.value, 'ramp-signal-foreground')

    def test_nitrogen_attributes(self):
        """
        Test for NitrogenAttr.
        """
        self.assertEqual(NitrogenAttr.NAME.value, 'wallpaper')


if __name__ == '__main__':
    unittest.main()
