import email
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Specialites(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    departement = models.CharField(max_length=50)
    
class Niveau(models.Model):
    id = models.AutoField(primary_key=True)
    idSpecialite =models.ForeignKey(Specialites, on_delete=models.CASCADE)
    numNiveau = models.PositiveIntegerField()
    
class Classe(models.Model):
    id = models.AutoField(primary_key=True)
    idNiveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    capacite = models.PositiveIntegerField()

class Etudiants(models.Model):
    matricule = models.CharField(max_length=15,primary_key=True)
    # nombre = models.PositiveIntegerField()
    nom = models.CharField(max_length=100)
    prenom  = models.CharField(max_length=100)
    dateNaissance = models.DateField()
    lieuNaissance = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    addressParent = models.CharField(max_length=100)
    email = models.EmailField(max_length = 100)
    sexe = models.CharField(max_length=10)

class AnneeAcademique(models.Model):
    id = models.AutoField(primary_key=True)
    dateDebut = models.DateField()
    dateFin = models.DateField()

class Inscriptions(models.Model):
    id = models.AutoField(primary_key=True)
    matriculeEtudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    idSpecialite = models.ForeignKey(Specialites, on_delete=models.CASCADE)
    idNiveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    dateInscription = models.DateField()
    montant = models.PositiveIntegerField()

class Frais(models.Model):
    id = models.AutoField(primary_key=True)
    idAnneAcademique = models.ForeignKey(AnneeAcademique, on_delete=models.CASCADE)
    dateDebut = models.DateField()
    dateFin = models.DateField()
    montant = models.PositiveIntegerField()
    typeFrais = models.CharField(max_length=50)
    
class Payements(models.Model):
    id = models.AutoField(primary_key=True)
    matriculeEtudiant = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    idFrais = models.ForeignKey(Frais, on_delete=models.CASCADE)
    datePayement = models.DateField()
    montant = models.PositiveIntegerField()
    
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    noms = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password =models.Char
    role = models.CharField(max_length=50)
    