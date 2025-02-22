import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock


class ArtQuizApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time_left = 30
        self.index = 0
        self.score = 0
        self.clock_id = None
        self.mode = "Normal"
        self.questions = [
            {"question": "Qual é o maior oceano do mundo?", "options" : ["Atlântico", "Pacífico", "Índico"], "correct": "Pacífico"},
            {"question": "Quem pintou a Mona Lisa?", "options" : ["Michelangelo", "Leonardo da Vinci", "Raphael"], "correct": "Leonardo da Vinci"},
            {"question": "Qual é o elemento químico representado pelo símbolo 'O'?", "options" : ["Ouro", "Oxigênio", "Ósmio"], "correct": "Oxigênio"},
            {"question": "Em que ano o homem pisou na Lua pela primeira vez?", "options" : ["1965", "1969", "1971"], "correct": "1969"},
            {"question": "Qual é o maior planeta do Sistema Solar?", "options" : ["Terra", "Júpiter", "Saturno"], "correct": "Júpiter"},
            {"question": "Quem é conhecido como o 'Pai da Física'?", "options" : ["Isaac Newton", "Albert Einstein", "Galileu Galilei"], "correct": "Isaac Newton"},
            {"question": "Qual foi a primeira capital do Brasil?", "options" : ["Rio de Janeiro", "Salvador", "São Paulo"], "correct": "Salvador"},
            {"question": "Qual país é conhecido como 'a terra do sol nascente'?", "options" : ["China", "Japão", "Coreia do Sul"], "correct": "Japão"},
            {"question": "Qual é o maior animal terrestre?", "options" : ["Elefante africano", "Girafa", "Baleia-azul"], "correct": "Elefante africano"},
            {"question": "Em que continente fica o Egito?", "options" : ["europa", "Ásia", "África"], "correct" : "África"},
            {"question": "Quem escreveu 'Dom Quixote'?", "options" : ["Miguel de Cervantes", "William Shakespeare", "Gabriel García Márquez"], "correct": "Miguel de Cervantes"},
            {"question": "Qual é o nome do primeiro livro da Bíblia?", "options" : ["Gênesis", "Êxodo", "Levítico"], "correct" : "Gênesis"},        
            {"question": "Qual ano foi fundado o Santa Cruz futebol clube?","options" : ["1914", "1902", "1910"], "correct" : "1914"},
            {"question": "Que animal amamentou os gemeos Rômulo e Remo?", "options" : ["uma loba", "uma vaca", "uma ovelha"], "correct" : "uma loba"},
            {"question": "Qual a ciência que estuda a atmosfera da Terra e a climatologia?", "options" : ["Metereologia","Astrologia", "Horologia"],"correct" : "Metereologia"},
            {"question": "Qual destas, apesar do seu nome, não é considerada um tipo de força?", "options" : ["Força de atrito", "Força centrípeta", "Força eletromotriz"], "correct" : "Força eletromotriz"},
            {"question": "Qual é o maior deserto do mundo?", "options" : ["Deserto do Saara", "Deserto da Antártida", "Deserto de Gobi"], "correct": "Deserto da Antártida"},
            {"question": "Quem foi o primeiro presidente do Brasil?", "options" : ["Deodoro da Fonseca", "Getúlio Vargas", "Juscelino Kubitschek"], "correct": "Deodoro da Fonseca"},
            {"question": "Qual é o símbolo químico do ouro?", "options" : ["Ag", "Au", "Pb"], "correct": "Au"},
            {"question": "Qual é o nome da maior floresta tropical do mundo?", "options" : ["Floresta Amazônica", "Floresta do Congo", "Floresta Negra"], "correct": "Floresta Amazônica"},
            {"question": "Qual é o continente mais populoso?", "options" : ["África", "América", "Ásia"], "correct": "Ásia"},
            {"question": "Quem inventou a lâmpada elétrica?", "options" : ["Nikola Tesla", "Thomas Edison", "Alexander Graham Bell"], "correct": "Thomas Edison"},
            {"question": "Qual é o menor país do mundo?", "options" : ["Mônaco", "Vaticano", "San Marino"], "correct": "Vaticano"},
            {"question": "Qual é a capital da França?", "options" : ["Paris", "Londres", "Berlim"], "correct": "Paris"},
            {"question": "Qual é o maior órgão do corpo humano?", "options" : ["Coração", "Fígado", "Pele"], "correct": "Pele"},
            {"question": "Em qual país nasceu a pizza?", "options" : ["França", "Itália", "Grécia"], "correct": "Itália"},
            {"question": "Quem descobriu a penicilina?", "options" : ["Louis Pasteur", "Alexander Fleming", "Marie Curie"], "correct": "Alexander Fleming"},
            {"question": "Em qual cidade aconteceu o primeiro voo dos irmãos Wright?", "options" : ["Washington", "Paris", "Kitty Hawk"], "correct": "Kitty Hawk"},
            {"question": "Qual é o nome da principal lua de Saturno?", "options" : ["Europa", "Titã", "Ío"], "correct": "Titã"},
            {"question": "Qual é a montanha mais alta do mundo?", "options" : ["Monte Kilimanjaro", "Monte Fuji", "Monte Everest"], "correct": "Monte Everest"},
            ]
        self.shuffled_questions = self.questions[:] #Cria uma cópia para embaralhar
        random.shuffle(self.shuffled_questions)

    def update_timer(self, dt):
        self.time_left -= 1
        self.timer_label.text = f"Tempo restante: {self.time_left}"
        if self.time_left <= 0:
            Clock.unschedule(self.clock_id)
            self.time_up()

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=20, padding=30)

        title = Label(
            text="[b]Bem-vindo ao Quiz de Conhecimentos Gerais![/b]",
            font_size=24,
            markup=True,
            halign="center",  # Centralizando horizontalmente
            valign="middle",  # Centralizando verticalmente
        )
        layout.add_widget(title)

        normal_button = Button(
            text="Modo Normal",
            on_press=self.start_normal_mode,
            size_hint=(1, None),
            height=60,
            background_color=(0.2, 0.6, 0.8, 1),
            color=(1, 1, 1, 1),
        )
        timer_button = Button( 
            text="Modo Contra o Tempo",
            on_press=self.start_timer_mode,
            size_hint=(1, None),
            height=60,
            background_color=(0.8, 0.3, 0.3, 1),
            color=(1, 1, 1, 1),
        )

        layout.add_widget(normal_button)
        layout.add_widget(timer_button)

        return layout

    def start_normal_mode(self, instance):
        self.mode = "Normal"
        self.start_quiz()

    def start_timer_mode(self, instance): #inicia o cronometro
        self.mode = "Contra o Tempo"
        self.time_left = 60
        self.start_quiz()

    def start_quiz(self):
        self.index = 0
        self.score = 0

        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.question_label = Label(
            text=self.shuffled_questions[self.index]["question"], #usa as perguntas embaralhadas
            font_size=20,
            markup=True
        )
        self.layout.add_widget(self.question_label)

        self.timer_label = Label(text="", font_size=16)
        if self.mode == "Contra o Tempo":
            self.timer_label.text = f"Tempo restante: {self.time_left}"
            self.clock_id = Clock.schedule_interval(self.update_timer, 1)
        self.layout.add_widget(self.timer_label)

        self.buttons = []
        for option in self.shuffled_questions[self.index]["options"]: #usa as perguntas embaralhadas
            btn = Button(
                text=option,
                size_hint=(1, None),
                height=50,
                background_color=(0.5, 0.5, 0.5, 1),
                color=(1, 1, 1, 1),
                on_press=self.check_answer
            )
            self.buttons.append(btn)
            self.layout.add_widget(btn)

        self.root.clear_widgets()
        self.root.add_widget(self.layout)

    def check_answer(self, instance):
        if instance.text == self.shuffled_questions[self.index]["correct"]: #usa as perguntas embaralhadas
            instance.background_color = (0.2, 0.8, 0.2, 1)
            self.score += 1
        else:
            instance.background_color = (0.8, 0.2, 0.2, 1)

        self.index += 1
        if self.index < len(self.shuffled_questions): #usa as perguntas embaralhadas
            Clock.schedule_once(self.update_question, 0.5)
        else:
            if self.mode == "Contra o Tempo":
                Clock.unschedule(self.clock_id)
            Clock.schedule_once(self.show_score, 0.5)

    def update_question(self, dt):
        self.question_label.text = self.shuffled_questions[self.index]["question"] #peguntas
        for btn in self.buttons:
            self.layout.remove_widget(btn)

        self.buttons.clear()
        for option in self.shuffled_questions[self.index]["options"]: #usa as perguntas embaralhadas
            btn = Button(
                text=option,
                size_hint=(1, None),
                height=50,
                background_color=(0.5, 0.5, 0.5, 1),
                color=(1, 1, 1, 1),
                on_press=self.check_answer
            )
            self.buttons.append(btn)
            self.layout.add_widget(btn)

    def time_up(self):
        popup = Popup(
            title="Tempo Esgotado :(",
            content=Label(text="O tempo acabou! Tente novamente!"),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()
        if self.index < len(self.shuffled_questions):
            self.index = len(self.shuffled_questions)
        Clock.schedule_once(self.show_score, 0.5)

    def show_score(self, dt):
        popup = Popup(
            title="Quiz Concluído",
            content=Label(text=f"Sua pontuação: {self.score}/{len(self.questions)}"),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()
        self.index = 0
        self.score = 0
        self.shuffled_questions = self.questions[:]
        random.shuffle(self.shuffled_questions)
        if self.mode == "Contra o Tempo":
            self.time_left = 60
            Clock.unschedule(self.clock_id)
            self.clock_id = None


if __name__ == "__main__":
    ArtQuizApp().run() #
