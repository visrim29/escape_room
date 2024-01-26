import PySimpleGUI as sg

class Layouts():

    def layout_one():
        return[  
        [sg.Text('PIRMAS LYGIS')],
        [sg.Text('Pabandykite išeiti iš programos')],
        [sg.Text('Turėkite omenyje: programa apgaulinga')],
        [sg.Text('Ar nenorite išeiti iš programos?')],
        [sg.Text('Įveskite "Ne" arba "Taip"')],
        [sg.Text('Įvedę pasirinkimą paspauskite patvirtinimo mygtuką')],
        [sg.Input(key='INPUT_ONE')],
        [
        sg.Button('Patvirtinti teigiamą pasirinkimą', key='YES'),
        sg.Button('Patvirtinti neigiamą pasirinkimą', key='NO'),
        sg.Button('Tęsti', key='CONTINUE_ONE', visible=False)
        ],
        [sg.Text(key='OUTPUT_ONE')]
            ]

    def layout_two():
        return[
        [sg.Text('ANTRAS LYGIS')],
        [sg.Text('?somargorp ši itieši etiron radsiv rA')],
        [sg.Text('"eN" abra "piaT" etiksevĮ')],
        [sg.Text('ąkutgym ominitrivtap etiksuapsap ąmiknirisap ędevĮ')],
        [sg.Input(key='INPUT_TWO')],
        [
        sg.Button('"piaT" ąmiknirisap itnitrivtaP', key='YES'),
        sg.Button('"eN" ąmiknirisap itnitrivtaP', key='NO'),
        sg.Button('itsęT', key='CONTINUE_TWO', visible=False)
        ],
        [sg.Text(key='OUTPUT_TWO')]
            ]
    
    def layout_three():
        return[
        [sg.Text('III LYGIS')],
        [sg.Text('Sveikiname, pasiekėte III-ią lygį!')],
        [sg.Text('Atspėkite skaičių nuo vieno iki dešimt!')],
        [sg.Text('Įvedę spėjimą paspauskite mygtuką "Spėti"')],
        [sg.Input(key='INPUT_THREE')],
        [
        sg.Button('Spėti', key='GUESS'),
        sg.Button('Tęsti', key='CONTINUE_THREE', visible=False)
        ],
        [sg.Text(key='OUTPUT_THREE')]
            ]
    
    # Nekeisti esamo sg.Text ir sg.Input formato (formatą galima papildyti neikeičiant jau nurodytų atributų)
    def layout_four():
        return [
        [sg.Text('KETVIRTAS LYGIS - NEMATOMAS RAŠALAS')],    
        [sg.Text('\n\nUžduotis:\nĮveskite skaičius: 1337\nĮvedę skaičius spauskite mygtuką', justification='center', size=(40, 7), text_color='#fffff1', background_color='#ffffff')],
        [sg.Text('Jūsų įvestis:')],
        [sg.Input(key='INPUT_FOUR', size=(43, 1))],
        [
        sg.Button('', key='MYGTUKAS', size=(20, 2)),
        sg.Button('Tęsti', key='CONTINUE_FOUR', visible=False),
        ],
        [sg.Text(key='OUTPUT_FOUR')]
                ]
    
    def layout_five():
        return [
        
            ]