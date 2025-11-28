from django import forms

REGIONI = [
    ("lombardia", "Lombardia"),
    ("lazio", "Lazio"),
    ("piemonte", "Piemonte"),
    ("toscana", "Toscana"),
    ("veneto", "Veneto"),
    ("campania", "Campania"),
    ("sicilia", "Sicilia"),
    ("emilia_romagna", "Emilia-Romagna"),
    ("calabria", "Calabria"),
    ("puglia", "Puglia"),
    ("sicilia", "Sicilia"),
    ("umbria", "Umbria"),
    ("marche", "Marche"),
    ("friuli_venezia_giulia", "Friuli Venezia Giulia"),
    ("liguria", "Liguria"),
    ("abruzzo", "Abruzzo"),
    ("basilicata", "Basilicata"),
    ("molise", "Molise"),
    ("valle_d_aosta", "Valle d'Aosta"),
    ("trentino_alto_adige", "Trentino-Alto Adige"),
    ("sardegna", "Sardegna"),
]

class SalaryForm(forms.Form):
    ral = forms.IntegerField(label="RAL annua (lordo)", min_value=1)
    regione = forms.ChoiceField(label="Regione", choices=REGIONI)
