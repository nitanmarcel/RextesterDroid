from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.snackbars import Snackbar

Builder.load_string("""
#:import MDLabel kivymd.label.MDLabel
#:import Snackbar kivymd.snackbars.Snackbar

<CustomSnackbar@Snackbar>:
    BoxLayout:
        id: box
        size_hint_y: None
        height: dp(58)
        spacing: dp(5)
        padding: dp(10)
        y: -self.height
        canvas:
            Color:
                rgba: get_color_from_hex('323232')
            Rectangle:
                pos: self.pos
                size: self.size
        MDLabel:
            id: text_bar
            size_hint_y: None
            height: self.texture_size[1]
            text: root.text
            font_size: Window.width // 30
            font_name: root.font_name
            theme_text_color: 'Custom'
            text_color: get_color_from_hex('ffffff')
            shorten: True
            shorten_from: 'right'
            pos_hint: {'center_y': .5}
""")


class CustomSnackbar(Snackbar):
    font_size = NumericProperty('10dp')
