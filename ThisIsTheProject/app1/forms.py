from django.forms import ModelForm
from .models import WebSiteInfo

class WebSiteInfoForm(ModelForm):
    class Meta:
        model = WebSiteInfo
        # fields = ['Atualizado', 'IP', 'Porto', 
        #           'Pais', 'Velocidade', 'Conectados',
        #           'Protocolo', 'Anonimato']
        fields = '__all__'