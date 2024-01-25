import PySimpleGUI as sg
from escape_game_layouts import Layouts

level_one = sg.Window('Escape: PIRMAS LYGIS', Layouts.layout_one(), font='Arial 20')

level_two = sg.Window('Escape: ANTRAS LYGIS', Layouts.layout_two(), font='Arial 20')

level_three = sg.Window('Escape: III LYGIS', Layouts.layout_three(), font='Arial 20')

level_four = sg.Window('Escape: KETVIRTAS LYGIS - NEMATOMAS RAŠALAS', Layouts.layout_four(), font='Arial 20')

level_five = sg.Window('Escape: 5 lygis', Layouts.layout_five(), font ='Arial 20', right_click_menu=sg.MENU_RIGHT_CLICK_EXIT)

game_over = sg.Window('Game Over', Layouts.layout_game_over(), font = 'Arial 20')

if level_one:
    while True:
        event, values = level_one.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Exit' :
            level_one['OUTPUT_ONE'].update('Nope')
        elif event == 'patvirtinti' and not values['INPUT_ONE'] == '"Ne" arba "Taip"':
            level_one['OUTPUT_ONE'].update('Pasirinkimas neteisingas, bandykite dar karta')
        elif event == 'patvirtinti' and values['INPUT_ONE'] == '"Ne" arba "Taip"':
            level_one['OUTPUT_ONE'].update(f'Pasirinkimas teisingas!')
            level_one['CONTINUE_ONE'](visible=True)
        if event == 'CONTINUE_ONE':
            level_one.close()
            level_two.read()

if level_two:
    while True:
        event_two, values_two = level_two.read()    
        if event_two == sg.WINDOW_CLOSED:
            break
        elif event_two == 'Exit':
            level_two['OUTPUT_TWO'].update('Nope')
        elif event_two == 'patvirtinti_two' and values_two['INPUT_TWO'] == "piaT" or values_two['INPUT_TWO'] == "eN":
            level_two['OUTPUT_TWO'].update(f"Pasirinkimas teisingas!")
            level_two['CONTINUE_TWO'](visible=True)
        elif event_two == 'patvirtinti_two' and not values_two['INPUT_TWO'] == "piaT" or not values_two['INPUT_TWO'] == "eN":
            level_two['OUTPUT_TWO'].update("Pasirinikinkimas neteisingas, bandykite dar karta")
        if event_two == 'CONTINUE_TWO':
            level_three.read()
            level_two.close()

if level_three:

    while True:
        event_3, values_3 = level_three.read()
        atsakymas = 'III'
        teisingas_skaicius = '3'
        teisingi_stringai =  ['trys', 'three', 'tres', 'trois', 'drei', 'tri']
        neteisingi_skaiciai = ['1', '2', '4', '5', '6', '7', '8', '9', '10']
        if event_3 == sg.WINDOW_CLOSED:
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
        if event_3 == 'CONTINUE_THREE':
            level_four.read()
            level_three.close()
    

if level_four:
    while True:
        event_4, values_4 = level_four.read()
        if event_4 == sg.WINDOW_CLOSED:
            break
        elif event_4 == 'MYGTUKAS' and values_4['INPUT_FOUR'] != '1337':
            level_four['OUTPUT_FOUR'].update('Užduotis neįvykdyta, bandykite dar kartą')
        elif event_4 == 'MYGTUKAS' and values_4['INPUT_FOUR'] == '1337':
            level_four['OUTPUT_FOUR'].update('Užduotis įvykdyta, spauskite mygtuką "Tęsti"')
            level_four['CONTINUE_FOUR'](visible=True)
            level_four.close()
            level_five()


if level_five:

    while True:
        event_5, values_5 = level_five.read()
        if event_5 == sg.WINDOW_CLOSED:
            break
        elif event_5 == 'Exit?':
            level_five['OUTPUT_FIVE'].update('Nope')
        elif event_5 == 'Exit':
            level_five['OUTPUT_FIVE'].update('Game completed')

if game_over:
    
    while True:
        event, value = game_over.read()
        if event_5 == sg.WINDOW_CLOSED:
            break



