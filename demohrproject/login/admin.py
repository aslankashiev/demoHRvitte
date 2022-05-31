from msilib import Table
from tkinter import Entry
from django.contrib import admin
from login.models import Table, Entry

# Register your models here.
admin.site.register(Table)
admin.site.register(Entry)
