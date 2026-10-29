import os
from nicegui import ui
import database

def create_left_column(haupt_splitter):
    with haupt_splitter.before:
        with ui.column().classes('w-full h-full p-2 bg-white border border-slate-200 rounded-md flex flex-col overflow-y-auto'):
            with ui.row().classes('w-full items-center gap-2 border-b border-slate-200 pb-1 mb-2 shrink-0 flex-nowrap cursor-pointer hover:bg-slate-50 p-0.5 rounded').on('click', lambda: setattr(haupt_splitter, 'value', 0)):
                ui.icon('chevron_left', color='slate-500').classes('text-base shrink-0')
                ui.icon('list_alt', color='slate-700').classes('text-base shrink-0')
                ui.label('Artikel-Auswahl').classes('custom-title flex-1')
                ui.tooltip('Artikelliste zur Seite ausblenden')
                suchfeld = ui.input(placeholder=' Artikel oder Nummer suchen...').props('outlined dense').classes('w-full mb-1 shrink-0')
                tabelle = ui.table(
                    columns=[
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
                tabelle.add_slot('body-cell-thumb', '''
                    <q-td :props="props">
                    <q-img v-if="props.row.thumb" :src="props.row.thumb" style="width: 35px; height: 26px; border-radius: 3px;" class="border border-slate-200" />
                    <div v-else style="width: 35px; height: 26px;" class="bg-slate-100 rounded border border-dashed border-slate-300"></div>
                    </q-td>
                ''')
    return tabelle, suchfeld  # Returns tabelle and suchfeld

