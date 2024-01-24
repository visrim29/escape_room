import PySimpleGUI as sg


layout_one = [  
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


layout_two = [
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


layout_three = [
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

# Nekeisti esamo sg.Text ir sg.Input formato
layout_four = [
    [sg.Text('KETVIRTAS LYGIS - NEMATOMAS RAŠALAS')],    
    [sg.Text('\n\nUžduotis:\nĮveskite skaičius: 1337\nĮvedę skaičius spauskite mygtuką', justification='center', size=(40, 7), text_color='#fffff1', background_color='#ffffff')],
    [sg.Text('Jūsų įvestis:')],
    [sg.Input(key='INPUT_FOUR', size=(43, 1))],
    [
    sg.Button('', key='MYGTUKAS', size=(20, 2)),
    sg.Button('Tęsti', key='CONTINUE_FOUR', visible=False)
    ],
    [sg.Text(key='OUTPUT_FOUR')]
]

level_one = sg.Window('Escape: PIRMAS LYGIS', layout_one, font='Arial 20')

level_two = sg.Window('Escape: ANTRAS LYGIS', layout_two, font='Arial 20')

level_three = sg.Window('Escape: III LYGIS', layout_three, font='Arial 20')

level_four = sg.Window('Escape: KETVIRTAS LYGIS - NEMATOMAS RAŠALAS', layout_four, font='Arial 20')


if level_one:
    while True:
        event, values = level_one.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'YES' and values['INPUT_ONE'] == 'Taip':
            level_one['OUTPUT_ONE'].update(f'Pasirinkimas "{values["INPUT_ONE"]}" neteisingas!')
        elif event == 'NO' and values['INPUT_ONE'] == 'Ne':
            level_one['OUTPUT_ONE'].update(f'Pasirinkimas "{values["INPUT_ONE"]}" neteisingas')
        elif event == 'YES' and values['INPUT_ONE'] == 'Ne':
            level_one['OUTPUT_ONE'].update('Pasirinkimas teisingas, spauskite mygtuką "Tęsti"')
            level_one['CONTINUE_ONE'](visible=True)
        elif event == 'NO' and values['INPUT_ONE'] == 'Taip':
            level_one['OUTPUT_ONE'].update('Pasirinkimas teisingas, spauskite mygtuką "Tęsti"')
            level_one['CONTINUE_ONE'](visible=True)
        if event == 'CONTINUE_ONE':
            level_one.close()
            level_two()

if level_two:
    while True:
        event_2, values_2 = level_two.read()        
        if event_2 == sg.WIN_CLOSED:
            break
        elif event_2 == 'YES' and values_2['INPUT_TWO'] == 'eN':
            level_two['OUTPUT_TWO'].update(f'sagnisieten "{values_2["INPUT_TWO"]}" samiknirisaP')
        elif event_2 == 'NO' and values_2['INPUT_TWO'] == 'piaT':
            level_two['OUTPUT_TWO'].update(f'sagnisieten "{values_2["INPUT_TWO"]}" samiknirisaP')
        elif event_2 == 'YES' and values_2['INPUT_TWO'] == 'piaT':
            level_two['OUTPUT_TWO'].update('"itsęT" ąkutgym etiksuaps, sagnisiet samiknirisaP')
            level_two['CONTINUE_TWO'](visible=True)
        elif event_2 == 'NO' and values_2['INPUT_TWO'] == 'eN':
            level_two['OUTPUT_TWO'].update('"itsęT" ąkutgym etiksuaps, sagnisiet samiknirisaP')
            level_two['CONTINUE_TWO'](visible=True)
        if event_2 == 'CONTINUE_TWO':
            level_two.close()

# Padaryti ne case sensitive, išskyrus atsakymą
if level_three:
    while True:
        event_3, values_3 = level_three.read()
        atsakymas = 'III'
        teisingas_skaicius = '3'
        teisingi_stringai =  ['trys', 'three', 'tres', 'trois', 'drei', 'tri']
        neteisingi_skaiciai = ['1', '2', '4', '5', '6', '7', '8', '9', '10']
        if event_3 == sg.WIN_CLOSED:
            break        
        elif event_3 == 'GUESS' and values_3['INPUT_THREE'] in neteisingi_skaiciai:
            level_three['OUTPUT_THREE'].update('Neteisingas skaičiaus formatas, bandykite dar kartą')
        elif event_3 == 'GUESS' and values_3['INPUT_THREE'] == teisingas_skaicius:
            level_three['OUTPUT_THREE'].update('Skaičių atspėjote, tačiau neteisingas skaičiaus formatas,\nbandykite dar kartą')
        elif event_3 == 'GUESS' and values_3['INPUT_THREE'] in teisingi_stringai:
            level_three['OUTPUT_THREE'].update('Skaičių atspėjote, teisingas skaičiaus formatas,\npabandykite įvesti skaičių senovine garsios imperijos kalba')
        elif event_3 == 'GUESS' and values_3['INPUT_THREE'] != atsakymas:
            level_three['OUTPUT_THREE'].update('Teisingas skaičiaus formatas, skaičiaus neatspėjote, bandykite dar kartą')
        elif event_3 == 'GUESS' and values_3['INPUT_THREE'] == atsakymas:
            level_three['OUTPUT_THREE'].update('Pasirinkimas teisingas, spauskite mygtuką "Tęsti"')
            level_three['CONTINUE_THREE'](visible=True)
            level_three.close()            
            level_four.read()


if level_four:
    while True:
        event_4, values_4 = level_four.read()
        if event_4 == sg.WIN_CLOSED:
            break
        elif event_4 == 'MYGTUKAS' and values_4['INPUT_FOUR'] != '1337':
            level_four['OUTPUT_FOUR'].update('Užduotis neįvykdyta, bandykite dar kartą')
        elif event_4 == 'MYGTUKAS' and values_4['INPUT_FOUR'] == '1337':
            level_four['OUTPUT_FOUR'].update('Užduotis įvykdyta, spauskite mygtuką "Tęsti"')
            level_four['CONTINUE_FOUR'](visible=True)
#             level_four.close()


# level_one.close()
# level_two.close()
# level_three.close()