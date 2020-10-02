from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    
    class Meta:
        model = Note
        #no need of active field
        fields = ("title","due_date","labels","finished")