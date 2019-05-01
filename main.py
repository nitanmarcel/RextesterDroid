import threading
from functools import wraps

import requests
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.snackbars import Snackbar
from kivymd.theming import ThemeManager


def run_async(f):
    @wraps(f)
    def async_func(*args, **kwargs):
        func_hl = threading.Thread(target=f, args=args, kwargs=kwargs)
        func_hl.start()
        return func_hl

    return async_func


class ScreenManagement(ScreenManager):
    stop = threading.Event()
    LANGUAGE = NumericProperty(None)
    COMPILER_ARGS = StringProperty("")


class HomeScreen(Screen):
    pass


class LanguageScreen(Screen):
    pass


class RextesterApp(App):
    theme_cls = ThemeManager()
    theme_cls.primary_palette = "BlueGray"
    theme_cls.accent_palette = "Gray"
    title = "Rextester Droid"
    root = None

    def go_home(self, *args):
        self.root.current = "home"

    def build(self):
        self.root = Builder.load_file("main.kv")
        #  register_font()
        return self.root

    def on_stop(self):
        self.root.stop.set()

    @run_async
    def execute(self, *args):
        code_field = self.root.screens[0].ids.code_field
        result_field = self.root.screens[0].ids.result_field
        stdin_field = self.root.screens[0].ids.stdin_field
        language = self.root.LANGUAGE
        compiler_args = self.root.COMPILER_ARGS

        if not language:
            Snackbar(text="Please select a language using the Floating Button", font_size=Window.width // 50).show()
            return

        if not code_field.text:
            Snackbar(text="Please type something in the code textfield!", font_size=Window.width // 50).show()
            return

        url = "https://rextester.com/rundotnet/api"
        data = {"LanguageChoice": language, "Program": code_field.text, "Input": stdin_field.text,
                "CompilerArgs": compiler_args}

        r = requests.post(url, data=data)
        status_code = r.status_code
        if status_code != 200:
            Snackbar(text="ERROR: Status Code: " + status_code, font_size=Window.width // 50).show()
            return

        response = r.json()

        result = response.get("Result")
        warnings = response.get("Warnings")
        errors = response.get("Errors")
        stats = response.get("Stats")
        files = response.get("Files")

        if not (result, warnings, errors, files):
            Snackbar("Did you forget to output anything?", font_size=Window.width // 50, font_name="NotoSans").show()
            return

        if result:
            result_field.disabled_foreground_color = (0, 1, 0, 1)
            result_field.text = result

        elif warnings:
            result_field.disabled_foreground_color = (240, 255, 0, 1)
            result_field.text = warnings

        elif errors:
            result_field.disabled_foreground_color = (255, 0, 0, 1)
            result_field.text = errors

        if stats:
            Snackbar(text=stats, font_size=Window.width // 50).show()


if __name__ == "__main__":
    RextesterApp().run()
