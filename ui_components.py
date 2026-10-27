# ui_components.py
from nicegui import ui
import database
import events

def baue_kopfzeile():
    """Rendert die obere Kopfzeile mitsamt dem automatischen Boot-Loader für aktive Profile."""
    global aktiver_lieferant_id, aktives_reward_profil_id
    
    # PROFI-BOOT-LOADER: Wir prüfen beim Laden der Seite, ob heute ein Profil aktiv ist!
    heute_profil = database.hole_heute_aktives_testprofil()
    
    initialer_text = "Kein Profil aktiv"
    if heute_profil:
        # IDs und Namen direkt aus der DB-Historie ins RAM einrasten lassen!
        aktiver_lieferant_id = heute_profil['l_id']
        aktives_reward_profil_id = heute_profil['r_id']
        initialer_text = f"{heute_profil['l_name']} | {heite_profil['r_name']}"

    with ui.row().classes('w-full items-center justify-between p-3 bg-slate-800 text-white shadow shrink-0'):
        with ui.row().classes('items-center gap-2'):
            ui.icon('inventory').classes('text-xl text-blue-400')
            ui.label('Warenwirtschaft & Produkttest').classes('text-base font-bold tracking-wide')
            
        # DIE COMPAKTE INFO-BOX IM HEADER (Zeigt jetzt ab Sekunde 1 den echten DB-Status an!)
        with ui.row().classes('items-center gap-1.5 bg-slate-700 px-2.5 py-1 rounded-md border border-slate-600 text-xs cursor-pointer hover:bg-slate-600 transition-colors') as reward_badge:
            ui.icon('workspace_premium').classes('text-sm text-amber-400')
            
            # Befüllt das Label reaktiv mit dem ermittelten Start-Zustand
            header_labels['txt_badge'] = ui.label(initialer_text).classes('font-bold text-white')
            
            ui.icon('info').classes('text-[14px] text-slate-400 ml-0.5')
        
        reward_badge.on('click', events.zeige_status_details)

def baue_kpi_leiste():
    """Rendert die KPI-Leiste."""
    # Beispiel-KPIs
    kpis = [
        {'label': 'Artikel', 'value': 100},
        {'label': 'Bewertungen', 'value': 50},
        {'label': 'Lieferanten', 'value': 20},
        {'label': 'Profile', 'value': 15}
    ]

    with ui.row().classes('w-full gap-4 p-3 bg-slate-100 border-b border-slate-200'):
        for kpi in kpis:
            with ui.card().classes('w-1/4 p-2 bg-white border border-slate-200 rounded-md flex flex-col items-center justify-center gap-1'):
                ui.label(kpi['value']).classes('text-xl font-bold text-slate-800')
                ui.label(kpi['label']).classes('text-sm text-slate-600')

def baue_artikel_auswahl():
    """Rendert die Artikel-Auswahl."""
    suchfeld = ui.input(placeholder='Artikel oder Nummer suchen...').props('outlined dense').classes('w-full mb-1 shrink-0')
    
    tabelle = ui.table(
        columns = [
            {'name': 'bdat_anzeige', 'label': 'Best.-Datum', 'field': 'bdat_anzeige', 'sortable': True, 'align': 'left', 'style': 'width: 15%'},
            {'name': 'ldat_anzeige', 'label': 'Lieferdatum', 'field': 'ldat_anzeige', 'sortable': True, 'align': 'left', 'style': 'width: 15%'},
            {'name': 'thumb', 'label': 'Bild', 'field': 'thumb', 'align': 'left', 'style': 'width: 60px'},
            {'name': 'num_anzeige', 'label': 'Artikelnr.', 'field': 'num_anzeige', 'sortable': True, 'align': 'left', 'style': 'width: 20%'},
            {'name': 'name', 'label': 'Bezeichnung', 'field': 'name', 'sortable': True, 'align': 'left', 'style': 'width: 45%'}
        ],
        rows=database.hole_artikel(),
        selection='single',
        row_key='id'
    )

    tabelle.props('''
        hide-selected-banner 
        dense 
        flat 
        wrap-cells=false 
        sort-by="bdat_anzeige" 
        binary-state-sort
        :sort-method="(rows, sortBy, descending) => sortBy === 'bdat_anzeige' ? rows.sort((a, b) => { const pA = (a.bdat_anzeige || '').split('.'); const pB = (b.bdat_anzeige || '').split('.'); const dA = pA[2]+pA[1]+pA[0]; const dB = pB[2]+pB[1]+pB[0]; return descending ? dB.localeCompare(dA) : dA.localeCompare(dB); }) : rows"
    ''')
    
    tabelle.classes('w-full flex-1 border border-slate-100 rounded-md cursor-pointer no-checkbox-table overflow-y-auto')

    tabelle.on('row-click', events.row_click)

    return tabelle

def baue_artikel_stammdaten():
    """Rendert die Artikel-Stammdaten."""
    # Beispiel-Artikel-Daten
    artikel_daten = {
        'nummer': '12345',
        'bezeichnung': 'Artikelbezeichnung',
        'bestelldatum': '2023-10-01',
        'lieferdatum': '2023-10-10',
        'hersteller': 'Herstellername',
        'beschreibung': 'Artikelbeschreibung'
    }

    with ui.card().classes('w-full p-2 bg-white border border-slate-200 rounded-md flex flex-col gap-2'):
        ui.label('Artikel-Daten').classes('font-bold text-slate-800')
        ui.label(f'Artikelnr.: {artikel_daten["nummer"]}').classes('text-sm text-slate-600')
        ui.label(f'Bezeichnung: {artikel_daten["bezeichnung"]}').classes('text-sm text-slate-600')
        ui.label(f'Bestelldatum: {de_datum_format(artikel_daten["bestelldatum"])}').classes('text-sm text-slate-600')
        ui.label(f'Lieferdatum: {de_datum_format(artikel_daten["lieferdatum"])}').classes('text-sm text-slate-600')
        ui.label(f'Hersteller: {artikel_daten["hersteller"]}').classes('text-sm text-slate-600')
        ui.label('Beschreibung:').classes('text-sm text-slate-800 mt-2')
        ui.label(artikel_daten['beschreibung']).classes('text-sm text-slate-600')

def baue_produkt_medien_galerie():
    """Rendert die Produkt-Medien & Galerie."""
    # Beispiel-Medien
    medien = [
        {'type': 'image', 'url': '/images/product1.jpg'},
        {'type': 'video', 'url': '/videos/product1.mp4'}
    ]

    with ui.card().classes('w-full p-2 bg-white border border-slate-200 rounded-md flex flex-col gap-2'):
        ui.label('Produkt-Medien & Galerie').classes('font-bold text-slate-800')
        for medium in medien:
            if medium['type'] == 'image':
                ui.image(medium['url']).classes('w-full h-auto rounded')
            elif medium['type'] == 'video':
                ui.video(medium['url']).classes('w-full rounded')

def baue_produkt_bewertung_rezension():
    """Rendert die Produkt-Bewertung & Rezension."""
    # Beispiel-Bewertungen
    bewertungen = [
        {'rating': 5, 'text': 'Sehr gut!'},
        {'rating': 4, 'text': 'Gut, aber Raum für Verbesserungen.'},
        {'rating': 3, 'text': 'Okay, aber nicht unbedingt empfehlenswert.'},
        {'rating': 2, 'text': 'Nah dran, aber noch nicht zufrieden.'},
        {'rating': 1, 'text': 'Ungewöhnlich schlecht.'}
    ]

    with ui.card().classes('w-full p-2 bg-white border border-slate-200 rounded-md flex flex-col gap-2'):
        ui.label('Produkt-Bewertung & Rezension').classes('font-bold text-slate-800')
        for bewertung in bewertungen:
            with ui.row().classes('items-center gap-2'):
                ui.icon('star').classes('text-yellow-500').repeat(bewertung['rating'])
                ui.label(bewertung['text']).classes('text-sm text-slate-600')

def baue_test_medien_galerie():
    """Rendert die Test-Medien & Galerie."""
    # Beispiel-Medien
    medien = [
        {'type': 'image', 'url': '/images/test1.jpg'},
        {'type': 'video', 'url': '/videos/test1.mp4'}
    ]

    with ui.card().classes('w-full p-2 bg-white border border-slate-200 rounded-md flex flex-col gap-2'):
        ui.label('Test-Medien & Galerie').classes('font-bold text-slate-800')
        for medium in medien:
            if medium['type'] == 'image':
                ui.image(medium['url']).classes('w-full h-auto rounded')
            elif medium['type'] == 'video':
                ui.video(medium['url']).classes('w-full rounded')
                