import PySimpleGUI as sg


layout_one = [  
    [sg.Text('PIRMAS LYGIS')],
    [sg.Text('Pabandykite išeiti iš programos')],
    [sg.Text('Turėkite omenyje: programa apgaulinga')],
    [sg.Text('Ar tikrai norite išeiti iš programos?')],
    [sg.Text('Įveskite "Ne" arba "Taip"')],
    [sg.Text('Įvedę pasirinkimą paspauskite patvirtinimo mygtuką')],
    [sg.Input(key='INPUT_ONE')],
    [
    sg.Button('Patvirtinti pasirinkimą "Taip"', key='YES'),
    sg.Button('Patvirtinti pasirinkimą "Ne"', key='NO'),
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
    [sg.Text('Sveikiname, pasiekėte III lygį!')],
    [sg.Text('Atspėkite skaičių nuo 1 iki 10!')],
    [sg.Text('Įvedę spėjimą paspauskite spėjimo mygtuką')],
    [sg.Input(key='INPUT_THREE')],
    [
    sg.Button('Spėti', key='GUESS')
    ],
    [sg.Text(key='OUTPUT_THREE')]
]

level_one = sg.Window('Escape: PIRMAS LYGIS', layout_one, font='Arial 20')

level_two = sg.Window('Escape: ANTRAS LYGIS', layout_two, font='Arial 20')

level_three = sg.Window('Escape: III LYGIS', layout_three, font='Arial 20')


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
            level_two.read()          
            

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
            level_three.read()

level_one.close()
level_two.close()
level_three.close()