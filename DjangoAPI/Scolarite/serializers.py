from dataclasses import fields
from rest_framework import serializers
from Scolarite.models import Users,Etudiants,Payements,Frais,AnneeAcademique,Specialites,Niveau,Classe,Inscriptions

class SpecialiteSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Specialites
        fields = ('id',
                  'nom',
                  'departement')
        
class NiveauSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = ('id',
                  'idSpecialite',
                  'numNiveau')

class ClasseSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = ('id',
                  'idNiveau',
                  'nom',
                  'capacite')
        
class EtudiantsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Etudiants
        fields = ('matricule',
                  #'nombre',
                  'nom',
                  'prenom',
                  'dateNaissance',
                  'lieuNaissance',
                  'adresse',
                  'addressParent',
                  'email',
                  'sexe')

class AnneeAcademiqueSerialiser(serializers.ModelSerializer):
    class Meta:
        model = AnneeAcademique
        fields = ('id',
                  'dateDebut',
                  'dateFin')

class InscriptionsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Inscriptions
        fields = ('id',
                  'matriculeEtudiant',
                  'idSpecialite',
                  'idNiveau',
                  'dateInscription',
                  'montant')

class FraisSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Frais
        fields = ('id',
                  'idAnneAcademique',
                  'dateDebut',
                  'dateFin',
                  'montant',
                  'typeFrais')
        
class PayementsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Payements
        fields = ('id',
                  'matriculeEtudiant',
                  'idFrais',
                  'datePayement',
                  'montant',)
        
class UsersSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id',
                  'noms',
                  'email',
                  'role')