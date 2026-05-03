from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random

class AlarmApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Alarm will start...")
        self.input = TextInput(hint_text="Solve to stop", multiline=False)
        self.button = Button(text="Submit")

        self.button.bind(on_press=self.check_answer)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.button)

        Clock.schedule_once(self.start_alarm, 5)

        return self.layout

    def start_alarm(self, dt):
        self.generate_question()
        self.sound = SoundLoader.load("noman.mp3")
        if self.sound:
            self.sound.loop = True
            self.sound.play()

    def generate_question(self):
        self.a = random.randint(10, 50)
        self.b = random.randint(10, 50)
        self.answer = self.a + self.b
        self.label.text = f"Solve: {self.a} + {self.b}"

    def check_answer(self, instance):
        try:
            if int(self.input.text) == self.answer:
                self.sound.stop()
                self.label.text = "Alarm Stopped ✅"
            else:
                self.label.text = "Wrong! Try again"
                self.generate_question()
        except:
            self.label.text = "Enter number"

AlarmApp().run()
