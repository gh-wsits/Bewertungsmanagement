from nicegui import ui
from artikel_liste import artikel_auswahl_kachel
from artikel_medien import artikel_medien_kachel
from artikel_stamm import artikel_stamm_kachel
from test_ergebnis import test_ergebnis_kachel
from test_medien import test_medien_kachel

def main_page():
    with ui.row():
        with ui.card():
            ui.label('Header')
            # Hier können Sie den Inhalt des Headers hinzufügen

    with ui.row():
        artikel_auswahl_kachel()

    with ui.row().classes('grid grid-cols-2 gap-4'):
        with ui.card():
            artikel_stamm_kachel()
        with ui.card():
            artikel_medien_kachel()

    with ui.row().classes('grid grid-cols-2 gap-4'):
        with ui.card():
            test_ergebnis_kachel()
        with ui.card():
            test_medien_kachel()

ui.run()