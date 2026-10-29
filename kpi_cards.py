from nicegui import ui

def build_kpi_cards(kpis):
    with ui.row().classes('w-full gap-2 mb-2 shrink-0 flex-nowrap'):
        
        # KPI CARD 1: GEGENWERT-LOGIK
        with ui.card().classes('flex-1 p-2 bg-slate-50 border border-blue-100 shadow-sm rounded items-center gap-0'):
            ui.label('🏆 Gesamt-Gegenwert (Behalten)').classes('text-[10px] text-slate-500 font-semibold uppercase tracking-wider')
            ui.label(f"{kpis['gesamt_preis']:,} €".replace(',', '.')).classes('text-lg font-bold text-blue-600')
            ui.label(f"Ø {kpis['avg_preis']} € | Min: {kpis['min_preis']} € | Max: {kpis['max_preis']} €").classes('text-[10px] text-slate-400 font-medium')
                
        # KPI CARD 2: BERICHTS-PERFORMANCE
        with ui.card().classes('flex-1 p-2 bg-slate-50 border border-emerald-100 shadow-sm rounded items-center gap-0'):
            ui.label('✍️ Rezensions-Performance').classes('text-[10px] text-slate-500 font-semibold uppercase tracking-wider')
            ui.label(f"{kpis['berichte']} Berichte").classes('text-lg font-bold text-emerald-600')
            ui.label(f"Davon qualifiziert: {kpis['qualifiziert']} Premium-Berichte").classes('text-[10px] text-slate-400 font-medium')
                
        # KPI CARD 3: SCHWUND / DIEBSTAHL-METRIK
        with ui.card().classes('flex-1 p-2 bg-slate-50 border border-red-100 shadow-sm rounded items-center gap-0'):
            ui.label('🚨 Paket-Schwund & Verluste').classes('text-[10px] text-slate-500 font-semibold uppercase tracking-wider')
            ui.label(f"{kpis['verlust_anzahl']} Pakete verloren").classes('text-lg font-bold text-red-600')
            ui.label(f"Finanzieller Schaden: {kpis['verlust_summe']:,} €".replace(',', '.')).classes('text-[10px] text-slate-400 font-medium')