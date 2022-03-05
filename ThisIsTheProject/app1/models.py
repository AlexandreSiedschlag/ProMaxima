from django.db import models

class WebSiteInfo(models.Model):
    Atualizado = models.IntegerField()
    IP = models.GenericIPAddressField(max_length=100)
    Porto = models.IntegerField(blank=True, null=True)
    Pais = models.CharField(max_length=100)
    Velocidade = models.FloatField(max_length=100)
    Conectados = models.CharField(max_length=100)
    Protocolo = models.CharField(max_length=100)
    Anonimato = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Info'
        
    def __str__(self):
        return self.IP
    
    
# Create your models here.
