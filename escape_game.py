import PySimpleGUI as sg
from layouts import Layouts



def level_one():
    level_one = sg.Window('Escape: PIRMAS LYGIS', layout=Layouts.layout_one(), font='Arial 20')   
    while True:
        event, values = level_one.read()
        if event == sg.WINDOW_CLOSED:
            level_one.close()
            return False
        if event == 'YES' and values['INPUT_ONE'] == 'Taip':
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
            return True

def level_two():
    level_two = sg.Window('Escape: ANTRAS LYGIS', Layouts.layout_two(), font='Arial 20')    
    while True:
        event_2, values_2 = level_two.read()
        if event_2 == sg.WINDOW_CLOSED:
            level_two.close()
            return False
        if event_2 == 'YES' and values_2['INPUT_TWO'] == 'eN':
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
            return True

def level_three():
    level_three = sg.Window('Escape: ANTRAS LYGIS', Layouts.layout_two(), font='Arial 20')
    while True:
        event_3, values_3 = level_three.read()
        atsakymas = 'III'
        teisingas_skaicius = '3'
        teisingi_stringai =  ['trys', 'three', 'tres', 'trois', 'drei', 'tri']
        neteisingi_skaiciai = ['1', '2', '4', '5', '6', '7', '8', '9', '10']
        if event_3 == sg.WINDOW_CLOSED:
            level_three.close()
            return False        
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
            return True

def level_four():
    level_four = sg.Window('Escape: KETVIRTAS LYGIS - NEMATOMAS RAŠALAS', Layouts.layout_four(), font='Arial 20')
    while True:
        event_4, values_4 = level_four.read()
        if event_4 == sg.WINDOW_CLOSED:
            level_four.close()
            return False
        elif event_4 == 'MYGTUKAS' and values_4['INPUT_FOUR'] != '1337':
            level_four['OUTPUT_FOUR'].update('Užduotis neįvykdyta, bandykite dar kartą')
        elif event_4 == 'MYGTUKAS' and values_4['INPUT_FOUR'] == '1337':
            level_four['OUTPUT_FOUR'].update('Užduotis įvykdyta, spauskite mygtuką "Tęsti"')
            level_four['CONTINUE_FOUR'](visible=True)
            level_four.close()
            return True

def level_five():
    pass    

def main():
    current_level = 1
    while True:
        if current_level == 1 and level_one():
            current_level = 2, level_one() == False
        elif current_level == 2 and level_two():
            current_level = 3
        elif current_level == 3 and level_three():
            current_level = 4
        elif current_level == 4 and level_four():
            current_level = 5
        elif current_level == 5 and level_five():
            break                    

main()