from django.db import models
#from .formatChecker  import ContentTypeRestrictedFileField#usado para especifica o tipo de arquivo para upload
import os
# Create your models here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class Informativos(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField('nome',max_length=128)
    info = models.TextField('Informativos')
    #arquivo = ContentTypeRestrictedFileField(upload_to='Documentos', content_types=['application/pdf'],max_upload_size=5242880,blank=False, null=False)
    arquivo = models.FileField(upload_to='Documentos/%Y/%m/%d/')
    class Meta:
        #Ordena os itens "-" Busca itens mais recentes
        ordering = ['-data']
        verbose_name = 'Informativo'
        verbose_name_plural = 'Informativos'

    def __str__(self):
        return self.nome
    