from django.db import models

class Atendimentos(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.CharField(max_length=100, null=False, blank=False)
    
    
    
class Especialidades(models.Model):
    
def __str__(self):
    return f"Atendimento [nome={self.nome}]"

