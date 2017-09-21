# -*- coding: UTF-8 -*-
from django.db import models

'''
    Modelos Para sistema de gestão de academia
'''


class Matricula(models.Model):
    pass


class Modalidade(models.Model):
    description = models.CharField(u'Descrição', max_length=255)
    value = models.CharField(u'Valor', max_length=255)

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'
        ordering = ['description']

    def __str__(self):
        return self.description


class Pagamento(models.Model):
    pass

class FichaTreino(models.Model):
    pass


class Aluno(models.Model):
    name = models.CharField(u'Nome', max_length=255)
    dt_cadastro = models.DateTimeField(u'Data de criação')
    endereco = models.TextField(u'Endereço', max_length=1000)
    bairro = models.CharField(u'Bairro', max_length=255)
    cep = models.CharField(u'CEP', max_length=255)
    cidade = models.CharField(u'Cidade', max_length=255)
    uf = models.CharField(u'UF', max_length=255)
    fone1 = models.CharField(u'Telefone 1', max_length=255)
    fone2 = models.CharField(u'Telefone 2', max_length=255)
    sexo = models.CharField(u'Sexo', max_length=10)
    cpf = models.CharField(u'CPF', max_length=15)
    rg = models.CharField(u'RG', max_length=10)
    dt_nascimento = models.DateField(u'Data de Nascimento', null=True, blank=True)
    idade = models.IntegerField(u'Idade', null=True, blank=True)
    email =


    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['name']

    def __str__(self):
        return self.name


class Funcionario(models.Model):
    pass

class Funcao(models.Model):
    pass

class AgendaTelefone(models.Model):
    pass

class Antopometrica(models.Model):
    pass

class Circunferencia(models.Model):
    pass


class DobraCultanea(models.Model):
    pass

class Diametro(models.Model):
    pass

class AvaliacaoFisica(models.Model):
    pass

class Frequencia(models.Model):
    pass

class Funcionario(models.Model):
    pass


