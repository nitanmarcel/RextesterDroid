##MIT License

#Copyright (c) 2019 Nitan Alexandru Marcel

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import requests
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class DropDownMenu(DropDown):
    pass

class Rextester(GridLayout):
    def __init__(self, **kwargs):
        super(Rextester, self).__init__(**kwargs)
        self.cols = 1
        self.language = None
        self.url = "https://rextester.com/rundotnet/api"

        self.dropdown = DropDownMenu()
        for k, _ in langs.items():
            self.btn = Button(text=k, size_hint=(1, None))
            self.btn.bind(on_release=lambda btn: self.on_btn_press(btn))
            self.dropdown.add_widget(self.btn)

        self.main_btn = Button(text="Select Language", size_hint=(1, None))
        self.main_btn.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda inst, x: setattr(self.main_btn, "text", x))
        self.add_widget(self.main_btn)

        self.code_input = TextInput(multiline=True)
        self.code_input.hint_text = "Enter your code here!"
        self.comp_btn = Button(text="Compile!", size_hint=(1, None))
        self.comp_btn.bind(on_release=lambda x: self.execute(x))
        self.add_widget(self.code_input, index=0, canvas=None)
        self.add_widget(self.comp_btn, index=0, canvas=None)
        self.lbl = Label(text="Waiting for response!")
        self.add_widget(self.lbl)
        self.result_input = TextInput(multiline=True)
        self.add_widget(self.result_input)

    def execute(self, btn):
        self.code = self.code_input.text

        if not self.language:
            self.result_input.text = "Please select a language!"
            return

        if not self.code:
            self.result_input.text = "Please type something in the textfield above!"
            return

        self.data = {"LanguageChoice": self.language, "Program": self.code, "Input": None}
        self.r = requests.post(self.url, data=self.data)
        self.response = self.r.json()

        if self.r.status_code != 200:
            self.result_input.text = "There has been a problem while connecting to the API!"
            return

        self.result = self.response.get("Result")
        self.warnings = self.response.get("Warnings")
        self.errors = self.response.get("Errors")
        self.stats = self.response.get("Stats")

        if not (self.result, self.warnings, self.errors):
            self.result_input.text = "Did you forget to output anything?"
            return

        if self.stats:
            self.lbl.text = self.stats

        self.result_input.text = self.result or self.warnings or self.errors

    def on_btn_press(self, btn):
        self.language = langs.get(btn.text)
        self.dropdown.select(btn.text)


class RextesterApp(App):
    def build(self):
        return Rextester()
    def on_pause(self):
        return True




langs = {
  'C#': '1',
  'VB.NET': '2',
  'F#': '3',
  'Java': '4',
  'Python': '5',
  'C (gcc)': '6',
  'C++ (gcc)': '7',
  'Php': '8',
  'Pascal': '9',
  'Objective-C': '10',
  'Haskell': '11',
  'Ruby': '12',
  'Perl': '13',
  'Lua': '14',
  'Nasm': '15',
  'Sql Server': '16',
  'Javascript': '17',
  'Lisp': '18',
  'Prolog': '19',
  'Go': '20',
  'Scala': '21',
  'Scheme': '22',
  'Node.js': '23',
  'Python 3': '24',
  'Octave': '25',
  'C (clang)': '26',
  'C++ (clang)': '27',
  'C++ (vc++)': '28',
  'C (vc)': '29',
  'D': '30',
  'R': '31',
  'Tcl': '32',
  'MySQL': '33',
  'PostgreSQL': '34',
  'Oracle': '35',
  'Swift': '37',
  'Bash': '38',
  'Ada': '39',
  'Erlang': '40',
  'Elixir': '41',
  'Ocaml': '42',
  'Kotlin': '43',
  'Brainf***': '44',
  'Fortran': '45'
}


if __name__ == "__main__":
    RextesterApp().run()