from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Add Task", max_length=60)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        # membuat variable bernama form yang berisi/membuat form kosong dan 
        # kemudian diisi dengan nilai yang diambil dari request.post
        form = NewTaskForm(request.POST)
        # jika data pada variable form valid(dicek di server)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # tasks.append(task)
            request.session["tasks"] += [task]
            # apabila berhasil kita redirect ke halaman tasks list
            return HttpResponseRedirect("/tasks")
            # return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
            "form" : form
        })

    return render(request, "tasks/add.html", {
        "form" : NewTaskForm()
    })
    
