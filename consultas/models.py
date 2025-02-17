from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=255)
    nome_social = models.CharField(max_length=255, blank=True)
    profissao = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    data = models.DateTimeField()
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    paciente_nome = models.CharField(max_length=255)

    def __str__(self):
        return f"Consulta com {self.profissional.nome} em {self.data}"
