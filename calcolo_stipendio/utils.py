REGIONALI = {
    "lombardia": 0.0158,
    "lazio": 0.0247,
    "piemonte": 0.0185,
    "toscana": 0.0142,
    "veneto": 0.0123,
    "campania": 0.023,
    "sicilia": 0.0123,
    "emilia_romagna": 0.0161,
    "calabria": 0.0173,
    "puglia": 0.0137,
    "umbria": 0.0233,
    "marche": 0.0137,
    "friuli_venezia_giulia": 0.0123,
    "liguria": 0.0209,
    "abruzzo": 0.0220,
    "basilicata": 0.0123,
    "molise": 0.0182,
    "valle_d_aosta": 0.0123,
    "trentino_alto_adige": 0.0123,
    "sardegna": 0.0123,
}

COMUNALE = 0.008
INPS = 0.0919

def calcola_detrazioni_lavoro(imponibile):
    if imponibile <= 15000:
        return 1955
    elif imponibile <= 28000:
        return 1955 + 440 * (28000 - imponibile) / 13000
    elif imponibile <= 50000:
        return 1.910 * (50000 - imponibile) / 22000
    return 0

def calcola_cuneo_fiscale_2025(reddito):
    if reddito <= 8500:
        return reddito * 0.071
    elif reddito <= 15000:
        return reddito * 0.053
    elif reddito <= 20000:
        return reddito * 0.048
    elif reddito <= 32000:
        return 1000
    elif reddito <= 40000:
        return 1000 * (40000 - reddito) / 8000
    return 0

def calcola_netto(ral, regione):
    contributi_inps = ral * INPS
    imponibile_irpef = ral - contributi_inps

    if imponibile_irpef <= 28000:
        irpef_lorda = imponibile_irpef * 0.23
    elif imponibile_irpef <= 50000:
        irpef_lorda = 28000 * 0.23 + (imponibile_irpef - 28000) * 0.35
    else:
        irpef_lorda = (
            28000 * 0.23
            + 22000 * 0.35
            + (imponibile_irpef - 50000) * 0.43
        )

    detrazioni = calcola_detrazioni_lavoro(imponibile_irpef)
    irpef_netta = max(irpef_lorda - detrazioni, 0)
    add_regionale = imponibile_irpef * REGIONALI[regione]
    add_comunale = imponibile_irpef * COMUNALE
    totale_addizionali = add_regionale + add_comunale
    cuneo_2025 = calcola_cuneo_fiscale_2025(ral)
    netto_annuo = imponibile_irpef - irpef_netta - totale_addizionali + cuneo_2025
    netto_mensile = netto_annuo / 14

    return {
        "netto_annuo": round(netto_annuo, 2),
        "netto_mensile": round(netto_mensile, 2),
        "contributi_inps": round(contributi_inps, 2),
        "imponibile_irpef": round(imponibile_irpef, 2),
        "irpef_lorda": round(irpef_lorda, 2),
        "detrazioni": round(detrazioni, 2),
        "irpef_netta": round(irpef_netta, 2),
        "cuneo_2025": round(cuneo_2025, 2),
        "add_regionale": round(add_regionale, 2),
        "add_comunale": round(add_comunale, 2),
        "totale_addizionali": round(totale_addizionali, 2),
    }
