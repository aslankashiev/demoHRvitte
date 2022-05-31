from tabnanny import verbose
from django import forms
from django.db import models

# Create your models here.

class Table(models.Model):
    text = models.CharField(max_length=200)

    def ___str___(self):
        return self

class Entry(models.Model):

    # Поля для ввода на стартововм экране
    inputFieldOne = forms.CharField
    inputFieldTwo = forms.CharField

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.inputFieldOne, self.inputFieldTwo

