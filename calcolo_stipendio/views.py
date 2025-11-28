from django.shortcuts import render
from .forms import SalaryForm
from .utils import calcola_netto

def salary_view(request):
    result = None
    if request.method == "POST":
        form = SalaryForm(request.POST)
        if form.is_valid():
            ral = form.cleaned_data["ral"]
            regione = form.cleaned_data["regione"]
            result = calcola_netto(ral, regione)
    else:
        form = SalaryForm()
    return render(request, "calcolatore.html", {"form": form, "result": result})
