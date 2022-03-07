from django.forms import ModelForm
from .models import WebSiteInfo

class WebSiteInfoForm(ModelForm):
    class Meta:
        model = WebSiteInfo
        fields = '__all__'