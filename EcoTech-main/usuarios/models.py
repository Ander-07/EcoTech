from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

class Pecas(models.Model):
    componente = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    peso = models.CharField(max_length=6)


