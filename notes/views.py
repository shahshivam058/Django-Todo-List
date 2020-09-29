from django.shortcuts import render,get_object_or_404,redirect
from .models import Note
from .forms import NoteForm

# Create your views here
def Notelist(request):
    todo_list =  Note.objects.filter(finished=False)
    finished_list = Note.objects.filter(finished=True)
    context = {
        "todo_list" : todo_list,
        "finished_list" : finished_list
    }
    return render(request,"note_list.html",context)

def finished_item(request,id):
    note = get_object_or_404(Note,id=id)
    note.finished = True
    note.save()
    return redirect("Notes:notelist")

def Recover_item(request,id):
    note = get_object_or_404(Note,id=id)
    note.finished = False
    note.save()
    return redirect("Notes:notelist")


def delete_item(request,id):
    note = get_object_or_404(Note,id=id)
    note.delete()
    return redirect("Notes:notelist")

def noteform(request):
    note_form = NoteForm(request.POST or None)
    if note_form.is_valid():
        note_form.save()
        return redirect("Notes:notelist")
    context = {
        "note_form" : note_form
    }
    return render(request,"forms.html",context)