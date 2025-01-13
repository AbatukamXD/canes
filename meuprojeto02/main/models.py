from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    mensagem = models.TextField()

class User(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()

    class Meta:
        db_table = 'cursos'

    def __str__(self):
        return self.nome

class Matricula(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} - {self.curso.nome}"