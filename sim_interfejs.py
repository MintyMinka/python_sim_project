import PySimpleGUI as sg
from sim_class import Character, Family, House, Furniture, TV, Fridge, Bed, Toilet, Bath, Bookshelf

Fams = []
Houses = []
Choices = []
def make_window(title: str, layout: list) -> sg.Window:
    sg.theme('DarkRed')
    return sg.Window(title, layout)

def title_screen():
    layout = [
        [sg.Text('Wybierz akcję')],
        [sg.Submit(button_text='Nowa gra')]
    ]
    window = make_window('SYMULATOR ŻYCIA', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        if event == 'Nowa gra':
            window.close()
            return make_family() 

def make_family():
    layout = [
        [sg.Text('Stwórz rodzinę')],
        [sg.Text('Nazwisko:', size =(15, 1)), sg.InputText()],
        [sg.Submit(button_text='Stwórz'), sg.CloseButton(button_text='Wyjście')]
    ]

    window = make_window('NOWA RODZINA', layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Wyjście'):
            break
        if event == 'Stwórz':
            Fams.append(Family(values[0]))
            window.close()
            return make_members()
    
def make_members():
    layout = [
        [sg.Text('Stwórz członków rodziny')],
        [sg.Text('Imię:', size =(15, 1)), sg.InputText()],
        [sg.Text('Wiek:', size =(15, 1)), sg.InputText()],
        [sg.Submit(button_text='Dodaj'), sg.Submit(button_text='Gotowe'), sg.CloseButton(button_text='Wyjście')]
    ]

    window = make_window('DODAJ CZŁONKÓW', layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Wyjście'):
            break
        if event == "Gotowe":
            window.close()
            return choose_house()
        if event == 'Dodaj':
            try:
                Character(values[0], Fams[-1], int(values[1]))
                sg.popup("Dodano nowego członka rodziny")
            except Exception as error_message:
                sg.popup(error_message)
    
def choose_house():
    layout = [
        [sg.Text('Wybierz dom')],
        [sg.Submit(button_text='Urocza willa, wielkość: 50, czynsz: 600 PY')],
        [sg.Submit(button_text='Nowoczesny dom parterowy, wielkość: 40, czynsz: 500 PY')],
        [sg.Submit(button_text='Nawiedzony dom, wielkość: 70, czynsz: 400 PY')],
        [sg.CloseButton(button_text='Wyjście')]
    ]

    window = make_window('WYBIERZ DOM', layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Wyjście'):
            break
        if event == 'Urocza willa, wielkość: 50, czynsz: 600 PY':
            Houses.append(House("urocza willa", Fams[-1], 50, 600))
            window.close()
            return choose_furniture()
        if event == 'Nowoczesny dom parterowy, wielkość: 40, czynsz: 500 PY':
            Houses.append(House("nowoczesny parterowy", Fams[-1], 40, 500))
            window.close()
            return choose_furniture()
        if event == 'Nawiedzony dom, wielkość: 70, czynsz: 400 PY':
            Houses.append(House("nawiedzony", Fams[-1], 70, 400))
            window.close()
            return choose_furniture()

def choose_furniture():
    layout = [
        [sg.Text('Wybierz meble')],
        [sg.Submit(button_text='Lodówka, wielkość: 2, cena: 50 PY')],
        [sg.Submit(button_text='Łóżko, wielkość: 4, cena: 20 PY')],
        [sg.Submit(button_text='Toaleta, wielkość: 1, cena: 20 PY')],
        [sg.Submit(button_text='Wanna, wielkość: 4, cena: 30 PY')],
        [sg.Submit(button_text='Biblioteczka, wielkość: 5, cena: 30 PY')],
        [sg.Submit(button_text='Telewior, wielkość: 2, cena: 50 PY')],
        [sg.Submit(button_text='Gotowe'), sg.CloseButton(button_text='Wyjście')]
    ]

    window = make_window('WYBIERZ MEBLE', layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Wyjście'):
            break
        if event == 'Lodówka, wielkość: 2, cena: 50 PY':
            try:
                Fridge(2, 50, Houses[-1])
                sg.popup(f"Dodano nową lodówkę \n {Fams[-1].get_money()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == 'Łóżko, wielkość: 4, cena: 20 PY':
            try:
                Bed(4, 20, Houses[-1])
                sg.popup(f"Dodano nowe łóżko \n {Fams[-1].get_money()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == 'Toaleta, wielkość: 1, cena: 20 PY':
            try:
                Toilet(1, 20, Houses[-1])
                sg.popup(f"Dodano nową toaletę \n {Fams[-1].get_money()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == 'Wanna, wielkość: 4, cena: 30 PY':
            try:
                Bath(4, 30, Houses[-1])
                sg.popup(f"Dodano nową wannę \n {Fams[-1].get_money()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == 'Biblioteczka, wielkość: 5, cena: 30 PY':
            try:
                Bookshelf(5, 30, Houses[-1])
                sg.popup(f"Dodano nową biblioteczkę \n {Fams[-1].get_money()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == 'Telewior, wielkość: 2, cena: 50 PY':
            try:
                TV(2, 50, Houses[-1])
                sg.popup(f"Dodano nowy telewizor \n {Fams[-1].get_money()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == 'Gotowe':
            window.close()
            return menu()

def menu():
    layout = [
        [sg.Text('Wybierz co chcesz zrobić')],
        [sg.Submit(button_text='Wybierz postać')],
        [sg.Submit(button_text='Sprawdź fundusze')],
        [sg.Submit(button_text='Dodaj meble')],
        [sg.Submit(button_text='Sprawdź rachunki do spłacenia')],
        [sg.Submit(button_text='Zapłać rachunki')],
        [sg.Submit(button_text='Nowy rok')],
        [sg.CloseButton(button_text='Wyjście')]
    ]

    window = make_window('MENU', layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Wyjście'):
            break
        if event == 'Wybierz postać':
            window.close()
            return choose_member()
        if event == 'Sprawdź fundusze':
            sg.popup(f"{Fams[-1].get_money()}")
        if event == 'Dodaj meble':
            window.close()
            return choose_furniture()
        if event == 'Sprawdź rachunki do spłacenia':
            sg.popup(f"{Houses[-1].get_bills()}")
        if event == 'Zapłać rachunki':
            try:
                sg.popup(f"{Houses[-1].pay_bills()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == 'Nowy rok':
            try:
                Houses[-1].pay_bills()
                for memb in Fams[-1].members:
                    memb.add_age()
                Houses[-1].add_bills()
                sg.popup("Szczęśliwego Nowego Roku!")
            except Exception as error_message:
                sg.popup(error_message)

def choose_member():
    layout = [
        [sg.Text(f"Wybierz członka rodziny {Fams[-1].surname}")]
    ]
    lst = []
    for memb in Fams[-1].members:
        layout.append([sg.Button(f"{memb.name}")])
        lst.append(memb.name)

    window = make_window('WYBIERZ CZŁONKA RODZINY', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event in lst:
            Choices.append(event)
            window.close()
            return choose_action()

def choose_action():
    name = Choices[-1]
    layout = [
        [sg.Text(f'Wybierz akcję {name}')],
        [sg.Submit(button_text='Pokaż statystyki')],
        [sg.Submit(button_text='Idź poćwiczyć')],
        [sg.Submit(button_text='Użyj...')]
    ]
    
    lst = []
    for memb in Fams[-1].members:
        lst.append(memb.name)
    name = Choices[-1]
    index = lst.index(name)
    char = Fams[-1].members[index]
    if char.is_child():
        layout.append([sg.Submit(button_text='Idź do szkoły')])
    elif char.is_adult():
        layout.append([sg.Submit(button_text='Idź do pracy')])
    elif char.is_elder():
        layout.append([sg.Submit(button_text='Pobierz emeryturę')])

    layout.append([sg.Submit(button_text='Wybierz inną postać')])
    layout.append([sg.Submit(button_text='Menu')])

    window = make_window('WYBIERZ AKCJĘ', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'Pokaż statystyki':
            sg.popup(f"wiek: {char.age} \n {char.get_needs()} \n {char.get_skills()}")

        if event == 'Idź do pracy':
            try:
                sg.popup(f"{char.go_to_work()} \n {char.get_needs()} \n {char.get_skills()} \n {Fams[-1].get_money()}")
            except Exception as error_message:
                sg.popup(error_message)

        if event == 'Idź do szkoły':
            try:
                sg.popup(f"{char.go_to_school()} \n {char.get_needs()} \n {char.get_skills()}")
            except Exception as error_message:
                sg.popup(error_message)
        
        if event == 'Pobierz emeryturę':
            try:
                sg.popup(f"{char.get_pension()} \n {char.get_needs()} \n {char.get_skills()} \n {Fams[-1].get_money()}")
            except Exception as error_message:
                sg.popup(error_message)

        if event == 'Idź poćwiczyć':
            try:   
                sg.popup(f"{char.exercise()} \n {char.get_needs()} \n {char.get_skills()}")
            except Exception as error_message:
                sg.popup(error_message)
            
        if event == 'Użyj...':
            window.close()
            return use_furniture()

        if event == 'Wybierz inną postać':
            window.close()
            return choose_member()
        
        if event == 'Menu':
            window.close()
            return menu()

def use_furniture():
    layout = [
        [sg.Text(f"Wybierz co chcesz użyć")],
    ]
    lst = []
    for furn in Houses[-1].furniture:
        layout.append([sg.Button(f"{str(furn)}")])
        lst.append(str(furn))
    layout.append([sg.Button("Wstecz")])
    window = make_window('WYBIERZ CO CHCESZ UŻYC', layout)
    lst1 = []
    for memb in Fams[-1].members:
        lst1.append(memb.name)
    name = Choices[-1]
    index = lst1.index(name)
    char = Fams[-1].members[index]

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "lodówka":
            fridge = Houses[-1].furniture[lst.index('lodówka')]
            try:
                sg.popup(f"{fridge.eat(char)} \n {char.get_needs()} \n {Fams[-1].get_money()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == "toaleta":
            toilet = Houses[-1].furniture[lst.index('toaleta')]
            try:
                sg.popup(f"{toilet.use_toilet(char)} \n {char.get_needs()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == "wanna":
            bath = Houses[-1].furniture[lst.index('wanna')]
            try:
                sg.popup(f"{bath.take_bath(char)} \n {char.get_needs()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == "biblioteczka":
            bookshelf = Houses[-1].furniture[lst.index('biblioteczka')]
            try:
                sg.popup(f"{bookshelf.read_book(char)} \n {char.get_needs()} \n {char.get_skills()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == "telewizor":
            tv = Houses[-1].furniture[lst.index('telewizor')]
            try:
                sg.popup(f"{tv.watch_tv(char)} \n {char.get_needs()} \n {char.get_skills()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == "łóżko":
            bed = Houses[-1].furniture[lst.index('łóżko')]
            try:
                sg.popup(f"{bed.sleep(char)} \n {char.get_needs()}")
            except Exception as error_message:
                sg.popup(error_message)
        if event == "Wstecz":
            window.close()
            return choose_action()

if __name__ == "__main__":
    title_screen()