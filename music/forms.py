from django import forms
from music.models import PlayList


class PlayListForm(forms.ModelForm):
    class Meta:
        model = PlayList
        fields = ['name', 'user', 'description', 'image']
