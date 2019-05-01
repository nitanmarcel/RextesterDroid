from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.image import Image
from kivymd.list import ILeftBody, OneLineAvatarListItem

Builder.load_string("""
<LanguageButton>:
    text: root.text
    LanguageIcon:
        source: root.icon
""")


class LanguageButton(OneLineAvatarListItem):
    icon = StringProperty('')

    def _set_active(self, active, list):
        pass


class LanguageIcon(ILeftBody, Image):
    pass
