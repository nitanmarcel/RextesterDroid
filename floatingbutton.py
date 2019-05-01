from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivymd.button import BaseButton, BaseRaisedButton, CircularElevationBehavior
from kivymd.ripplebehavior import CircularRippleBehavior

Builder.load_string("""

<CustomBaseRoundButton>:
    canvas:
        Clear
        Color:
            rgba: root.theme_cls.primary_color
        Ellipse:
            size: self.size
            pos: self.pos

    size_hint: None, None
    size: dp(56), dp(56)
    x: Window.width - self.width - dp(10)
    y: dp(10)

    CustomFloatingActionButtonImage:
        source: root.icon
""")


class CustomBaseRoundButton(CircularRippleBehavior, BaseButton):
    pass


class CustomFloatingActionButtonImage(Image):
    pass


class CustomFloatingActionButton(CustomBaseRoundButton, CircularElevationBehavior, BaseRaisedButton):
    background_palette = StringProperty('Accent')
    icon = StringProperty('')
    pass
