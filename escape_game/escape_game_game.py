import PySimpleGUI as sg
from escape_game_layouts import Layouts

class Game:
    def __init__(self):
        self.levels = [
            sg.Window('Escape: PIRMAS LYGIS', Layouts.layout_one(), font='Arial 20'),
            sg.Window('Escape: ANTRAS LYGIS', Layouts.layout_two(), font='Arial 20'),
            sg.Window('Escape: III LYGIS', Layouts.layout_three(), font='Arial 20'),
            sg.Window('Escape: KETVIRTAS LYGIS - NEMATOMAS RAŠALAS', Layouts.layout_four(), font='Arial 20'),
            sg.Window('Escape: 5 lygis', Layouts.layout_five(), font='Arial 20', right_click_menu=sg.MENU_RIGHT_CLICK_EXIT),
            sg.Window('Game Over', Layouts.layout_game_over(), font='Arial 20')
        ]

    def level_one_window(self):
        while True:
            event, values = self.levels[0].read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Exit':
                self.levels[0]['OUTPUT_ONE'].update('Nope')
            elif event == 'patvirtinti' and values['INPUT_ONE'] not in ['"Ne" arba "Taip"']:
                self.levels[0]['OUTPUT_ONE'].update('Pasirinkimas neteisingas, bandykite dar karta')
            elif event == 'patvirtinti' and values['INPUT_ONE'] in ['"Ne" arba "Taip"']:
                self.levels[0]['OUTPUT_ONE'].update('Pasirinkimas teisingas!')
                self.levels[0]['CONTINUE_ONE'](visible=True)

            if event == 'CONTINUE_ONE':
                self.levels[0].close()
                self.level_two_window()

    def level_two_window(self):
        while True:
            event, values = self.levels[1].read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Exit':
                self.levels[1]['OUTPUT_TWO'].update('Nope')
            elif event == 'patvirtinti_two' and values['INPUT_TWO'] in ["piaT", "eN"]:
                self.levels[1]['OUTPUT_TWO'].update(f"Pasirinkimas teisingas!")
                self.levels[1]['CONTINUE_TWO'](visible=True)
            elif event == 'patvirtinti_two' and values['INPUT_TWO'] not in ["piaT", "eN"]:
                self.levels[1]['OUTPUT_TWO'].update("Pasirinikinkimas neteisingas, bandykite dar karta")

            if event == 'CONTINUE_TWO':
                self.levels[1].close()
                self.level_three_window()

    def level_three_window(self):
        while True:
            event, values = self.levels[2].read()

            atsakymas = 'III'
            teisingas_skaicius = '3'
            teisingi_stringai = ['trys', 'three', 'tres', 'trois', 'drei', 'tri']
            neteisingi_skaiciai = ['1', '2', '4', '5', '6', '7', '8', '9', '10']

            if event == sg.WINDOW_CLOSED:
                break 
            elif event == 'GUESS' and values['INPUT_THREE'] in neteisingi_skaiciai:
                self.levels[2]['OUTPUT_THREE'].update('Neteisingas skaičiaus formatas, bandykite dar kartą')
            elif event == 'GUESS' and values['INPUT_THREE'] == teisingas_skaicius:
                self.levels[2]['OUTPUT_THREE'].update('Skaičių atspėjote, tačiau neteisingas skaičiaus formatas,\nbandykite dar kartą')
            elif event == 'GUESS' and values['INPUT_THREE'] in teisingi_stringai:
                self.levels[2]['OUTPUT_THREE'].update('Skaičių atspėjote, teisingas skaičiaus formatas,\npabandykite įvesti skaičių senovine garsios imperijos kalba')
            elif event == 'GUESS' and values['INPUT_THREE'] != atsakymas:
                self.levels[2]['OUTPUT_THREE'].update('Teisingas skaičiaus formatas, skaičiaus neatspėjote, bandykite dar kartą')
            elif event == 'GUESS' and values['INPUT_THREE'] == atsakymas:
                self.levels[2]['OUTPUT_THREE'].update('Pasirinkimas teisingas, spauskite mygtuką "Tęsti"')
                self.levels[2]['CONTINUE_THREE'](visible=True)

            if event == 'CONTINUE_THREE':
                self.levels[2].close()
                self.level_four_window()

    def level_four_window(self):
        while True:
            event, values = self.levels[3].read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'MYGTUKAS' and values['INPUT_FOUR'] != '1337':
                self.levels[3]['OUTPUT_FOUR'].update('Užduotis neįvykdyta, bandykite dar kartą')
            elif event == 'MYGTUKAS' and values['INPUT_FOUR'] == '1337':
                self.levels[3]['OUTPUT_FOUR'].update('Užduotis įvykdyta, spauskite mygtuką "Tęsti"')
                self.levels[3]['CONTINUE_FOUR'](visible=True)
                self.levels[3].close()
                self.level_five_window()

    def level_five_window(self):
        while True:
            event, values = self.levels[4].read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Exit?':
                self.levels[4]['OUTPUT_FIVE'].update('Nope')
            elif event == 'Exit':
                self.levels[4]['OUTPUT_FIVE'].update('Game completed')

    def run(self):
        self.level_one_window()