from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='DATA DO EVENTO')
    data_criacao = models.DateTimeField(verbose_name='DATA DE CRIAÇÃO', auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # chave estrangeira

    # Especificando o nome da tabela
    class Meta:
        db_table = 'evento'

    def get_data_evento(self):
        return self.data_evento.srtftime("%d/%m/%Y %H:%M")

    def get_data_criacao(self):
        return self.data_criacao.srtftime("%d/%m/%Y %H:%M")

    def get_usuario(self):
        return self.usuario.upper()