from django import forms
from .models import Informativos
class InsereForm(forms.Form):
    nome = forms.CharField(max_length=128, min_length=1,widget=forms.TextInput(
        attrs={'class':'form-control mr-sm-2','placeholder':'Nome do informativo','style':'length:200px'
        }))
    info = forms.CharField(widget=forms.Textarea(
        attrs={'class':'form-control mr-sm-2','placeholder':'Descrição'
        }))
    #arq = forms.CharField(widget=forms.TextInput(attrs={"type":"file"}))
    arq = forms.FileField()
class PesqForm(forms.Form):
    busca = forms.CharField(max_length=128, min_length=1,widget=forms.TextInput(
        attrs={'class':'form-control mr-sm-2','placeholder':'Pesquisar'
        }))
class InforForm(forms.ModelForm):
    class Meta:
        model = Informativos
        fields = ('nome', 'info','arquivo', )
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control mr-sm-2','placeholder':'Nome do informativo','style':'length:200px'}),
      
            'info': forms.Textarea(attrs={'class':'form-control mr-sm-2','placeholder':'Descrição'}),
        } 