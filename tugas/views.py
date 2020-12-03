from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.


class NewTugasForm(forms.Form):
    tugas = forms.CharField(label='Tambah Tugas', max_length=60)
    prioritas = forms.IntegerField(label='Prioritas', min_value=1, max_value=5 )

def index(request):
    if "alltugas" not in request.session:
        request.session["alltugas"] = []
    return render(request, "tugas/index.html", {
        "alltugas" : request.session["alltugas"]
    })

def tambah(request):
    if request.method == "POST":
        form = NewTugasForm(request.POST)
        if form.is_valid():
            tugas = form.cleaned_data['tugas']
            # alltugas.append(tugas)
            request.session["alltugas"] += [tugas]
            return HttpResponseRedirect("/tugas")
        else:
            return render(request, "tugas/tambah.html",{
                "form" : form
            })
    return render(request, "tugas/tambah.html",{
        "form" : NewTugasForm()
    })
