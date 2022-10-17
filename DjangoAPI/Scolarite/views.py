from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.conf import settings
from Scolarite.models import Etudiants,Users,Payements,Frais,AnneeAcademique,Specialites,Niveau,Classe,Inscriptions
from Scolarite.serializers import EtudiantsSerialiser,UsersSerialiser,PayementsSerialiser,FraisSerialiser,AnneeAcademiqueSerialiser,SpecialiteSerialiser,NiveauSerialiser,ClasseSerialiser,InscriptionsSerialiser
import datetime
thisYear = datetime.datetime.now().year
count = 0
import logging
logger = logging.getLogger("mylogger")
@csrf_exempt

def countEtudiant():
    count = Etudiants.objects.count()
    if count < 9:
        return '0000'+ str(count + 1)
    elif count < 99:
        return '000'+ str(count + 1)
    elif count < 999:
        return '00'+ str(count + 1)
    elif count < 9999:
        return '0'+ str(count + 1)

@csrf_exempt
def findAnnee(list,value):
    for x in list:
        if x.dateDebut.year == value:
            return x.id
        
    
@csrf_exempt
def etudiantsApi(request, matriculeEtudiant=''):
    if request.method =='GET':
        etudiants = Etudiants.objects.all()
        etudiantsSerialiser = EtudiantsSerialiser(etudiants, many=True)
        return JsonResponse(etudiantsSerialiser.data, safe=False)
     
    elif request.method == 'POST':
        etudiantsData = JSONParser().parse(request)
        etudiantsData['matricule'] = "ET" + str(thisYear) + countEtudiant()
        etudiantsSerialiser = EtudiantsSerialiser(data= etudiantsData)
        if etudiantsSerialiser.is_valid():
            etudiantsSerialiser.save()
            return JsonResponse("Etudiant Ajoute avec succes",safe=False)
        return JsonResponse("Échec de l'ajout d'Etudiant",safe=False)

    elif request.method == 'PUT':
            etudiantsData = JSONParser().parse(request)
            etudiant = Etudiants.objects.get(matricule = etudiantsData['matricule'])
            etudiantsSerialiser = EtudiantsSerialiser(etudiant, data= etudiantsData)
            if etudiantsSerialiser.is_valid():
                etudiantsSerialiser.save()
                return JsonResponse("Etudiant Edite avec succes",safe=False)
            return JsonResponse("Échec de l'edition d'Etudiant",safe=False)
    
    elif request.method == 'DELETE':
        etudiant = Etudiants.objects.get(matricule = matriculeEtudiant)
        etudiant.delete()
        return JsonResponse('Suppresion effectuer avec succes', safe=False)

@csrf_exempt
def specialiteApi(request, id=0):
    if request.method =='GET':
        specialites = Specialites.objects.all()
        specialitesSerialiser = SpecialiteSerialiser(specialites, many=True)
        return JsonResponse(specialitesSerialiser.data, safe=False)
     
    elif request.method == 'POST':
        specialitesData = JSONParser().parse(request)
        specialitesSerialiser = SpecialiteSerialiser(data= specialitesData)
        if specialitesSerialiser.is_valid():
            specialitesSerialiser.save()
            return JsonResponse("specialite Ajoute avec succes",safe=False)
        return JsonResponse("Échec de l'ajout de la specialites",safe=False)

    elif request.method == 'PUT':
            specialitesData = JSONParser().parse(request)
            specialite = Specialites.objects.get(id = specialitesData['id'])
            specialitesSerialiser = SpecialiteSerialiser(specialite, data= specialitesData)
            if specialitesSerialiser.is_valid():
                specialitesSerialiser.save()
                return JsonResponse("specialite Edite avec succes",safe=False)
            return JsonResponse("Échec de l'edition de la specialite",safe=False)
    
    elif request.method == 'DELETE':
        specialite = Specialites.objects.get(id = id)
        specialite.delete()
        return JsonResponse('Suppresion effectuer avec succes', safe=False)
 
@csrf_exempt
def classeApi(request, id=0):
    if request.method =='GET':
        classes = Classe.objects.all()
        classesSerialiser = ClasseSerialiser(classes, many=True)
        return JsonResponse(classesSerialiser.data, safe=False)
     
    elif request.method == 'POST':
        classesData = JSONParser().parse(request)
        classesSerialiser = ClasseSerialiser(data= classesData)
        if classesSerialiser.is_valid():
            classesSerialiser.save()
            return JsonResponse("classe Ajoute avec succes",safe=False)
        return JsonResponse("Échec de l'ajout de la classe",safe=False)

    elif request.method == 'PUT':
            classesData = JSONParser().parse(request)
            classe = Classe.objects.get(id = classesData['id'])
            classesSerialiser = ClasseSerialiser(classe, data= classesData)
            if classesSerialiser.is_valid():
                classesSerialiser.save()
                return JsonResponse("classe Edite avec succes",safe=False)
            return JsonResponse("Échec de l'edition de la classe",safe=False)
    
    elif request.method == 'DELETE':
        classe = Classe.objects.get(id = id)
        classe.delete()
        return JsonResponse('Suppresion effectuer avec succes', safe=False)

@csrf_exempt
def niveauApi(request,id=0):
    if request.method =='GET':
        niveaux = Niveau.objects.all()
        niveauxSerialiser = NiveauSerialiser(niveaux, many=True)
        return JsonResponse(niveauxSerialiser.data, safe=False)
    
    elif request.method == 'POST':
        niveauxData = JSONParser().parse(request)
        niveauxSerialiser = NiveauSerialiser(data= niveauxData)
        if niveauxSerialiser.is_valid():
            niveauxSerialiser.save()
            return JsonResponse("niveaux Ajoute avec succes",safe=False)
        return JsonResponse("Échec de l'ajout du niveau",safe=False)

    elif request.method == 'PUT':
            niveauxData = JSONParser().parse(request)
            niveau = Niveau.objects.get(id = niveauxData['id'])
            niveauxSerialiser = NiveauSerialiser(niveau, data= niveauxData)
            if niveauxSerialiser.is_valid():
                niveauxSerialiser.save()
                return JsonResponse("niveau Edite avec succes",safe=False)
            return JsonResponse("Échec de l'edition du niveau",safe=False)
    
    elif request.method == 'DELETE':
        niveau = Niveau.objects.get(id = id)
        niveau.delete()
        return JsonResponse('Suppresion effectuer avec succes', safe=False)

@csrf_exempt
def InscriptionApi(request, id=0):
    if request.method =='GET':
        inscription = Inscriptions.objects.all()
        inscriptionsSerialiser = InscriptionsSerialiser(inscription, many=True)
        logger.warning(inscriptionsSerialiser)
        return JsonResponse(inscriptionsSerialiser.data, safe=False)
    
    elif request.method == 'POST':
        inscriptionData = JSONParser().parse(request)
        inscriptionData['dateInscription'] = datetime.date.today()
        etudiant = Etudiants.objects.filter(matricule = inscriptionData['matriculeEtudiant'])
        send_mail("FELECITATIONS!!!!",
                  "Inscription Effectuer avec Succes" + "matricule : "+etudiant[0].matricule,
                  settings.EMAIL_HOST_USER,
                  [etudiant[0].email])
        inscriptionsSerialiser = InscriptionsSerialiser(data= inscriptionData)
        if inscriptionsSerialiser.is_valid():
            inscriptionsSerialiser.save()
            return JsonResponse("Inscription Ajoute avec succes",safe=False)
        return JsonResponse("Échec de l'ajout du Inscription",safe=False)

    elif request.method == 'PUT':
            inscriptionData = JSONParser().parse(request)
            inscription = Inscriptions.objects.get(id = inscriptionData['id'])
            inscriptionsSerialiser = InscriptionsSerialiser(inscription, data= inscriptionData)
            if inscriptionsSerialiser.is_valid():
                inscriptionsSerialiser.save()
                return JsonResponse("Inscription edite avec succes",safe=False)
            return JsonResponse("Échec de l'edition de l'inscription",safe=False)
    
    elif request.method == 'DELETE':
        inscription = Inscriptions.objects.get(id = id)
        inscription.delete()
        return JsonResponse('Suppresion effectuer avec succes', safe=False)

@csrf_exempt
def payementApi(request, id=0):
    if request.method =='GET':
        payement = Payements.objects.all()
        payementSerialiser = PayementsSerialiser(payement, many=True)
        return JsonResponse(payementSerialiser.data, safe=False)
    
    elif request.method == 'POST':
        payementData = JSONParser().parse(request)
        payementData['datePayement'] = datetime.date.today()
        payementSerialiser = PayementsSerialiser(data= payementData)
        logger.warning(payementData)
        if payementSerialiser.is_valid():
            logger.warning("Serialiser is valid-----------")
            payementSerialiser.save()
            return JsonResponse("payement Ajoute avec succes",safe=False)
        return JsonResponse("Échec de l'ajout du payement",safe=False)

    elif request.method == 'PUT':
            payementData = JSONParser().parse(request)
            payement = Payements.objects.get(id = payementData['id'])
            payementSerialiser = PayementsSerialiser(payement, data= payementData)
            if payementSerialiser.is_valid():
                payementSerialiser.save()
                return JsonResponse("payement edite avec succes",safe=False)
            return JsonResponse("Échec de l'edition du payement",safe=False)
    
    elif request.method == 'DELETE':
        payement = Payements.objects.get(id = id)
        payement.delete()
        return JsonResponse('Suppresion effectuer avec succes', safe=False)

@csrf_exempt
def FraisApi(request, id=0):
    if request.method =='GET':
        frais = Frais.objects.all()
        fraisSerialiser = FraisSerialiser(frais, many=True)
        return JsonResponse(fraisSerialiser.data, safe=False)
            
    elif request.method == 'POST':
        annees = AnneeAcademique.objects.all()
        fraisData = JSONParser().parse(request)
        fraisData["idAnneAcademique"] = findAnnee(annees, thisYear)
        fraisSerialiser = FraisSerialiser(data= fraisData)
        if fraisSerialiser.is_valid():
            fraisSerialiser.save()
            return JsonResponse("Frais Ajoute avec succes",safe=False)
        return JsonResponse("Échec de l'ajout de Frais",safe=False)

    elif request.method == 'PUT':
            fraisData = JSONParser().parse(request)
            frais = Frais.objects.get(id = fraisData['id'])
            fraisSerialiser = FraisSerialiser(frais, data= fraisData)
            if fraisSerialiser.is_valid():
                fraisSerialiser.save()
                return JsonResponse("frais edite avec succes",safe=False)
            return JsonResponse("Échec de l'edition de frais",safe=False)
    
    elif request.method == 'DELETE':
        frais = Frais.objects.get(id = id)
        frais.delete()
        return JsonResponse('Suppresion effectuer avec succes', safe=False)

@csrf_exempt
def AnneeApi(request, id=0):
    if request.method =='GET':
        annee = AnneeAcademique.objects.all()
        anneeSerialiser = AnneeAcademiqueSerialiser(annee, many=True)
        return JsonResponse(anneeSerialiser.data, safe=False)
            
    elif request.method == 'POST':
        anneeData = JSONParser().parse(request)
        anneeSerialiser = AnneeAcademiqueSerialiser(data= anneeData)
        if anneeSerialiser.is_valid():
            anneeSerialiser.save()
            return JsonResponse("Annee Academique Ajoute avec succes",safe=False)
        return JsonResponse("Échec de l'ajout de l'annee Academique",safe=False)

    elif request.method == 'PUT':
            anneeData = JSONParser().parse(request)
            annee = AnneeAcademique.objects.get(id = anneeData['id'])
            anneeSerialiser = AnneeAcademiqueSerialiser(annee, data= anneeData)
            if anneeSerialiser.is_valid():
                anneeSerialiser.save()
                return JsonResponse("Annee Academique edite avec succes",safe=False)
            return JsonResponse("Échec de l'edition de l'annee Academique",safe=False)
    
    elif request.method == 'DELETE':
        annee = AnneeAcademique.objects.get(id = id)
        annee.delete()
        return JsonResponse('Suppresion effectuer avec succes', safe=False)

def UsersApi(request, id=0):
    if request.method == 'GET':
        users = Users.objects.all()
        usersSerialiser = UsersSerialiser(users, many=True)
        return JsonResponse(usersSerialiser.data, safe=False)
    elif request.method =='POST':
        userData = JSONParser().parse(request)
        userSerialiser = UsersSerialiser(data = userData)
        if userSerialiser.is_valid():
            return JsonResponse("Utilisateur Ajouter Avec Succes", safe = True)
        return JsonResponse("Echeque de l'ajout de l'utilisateur")
    elif request.method == 'PUT':
        userData = JSONParser().parse(request)
        user = Users.objects.get(id = userData['id'])
        userSerialiser = UsersSerialiser(user, data = userData )
        if userSerialiser.is_valid():
            return JsonResponse("Utilisateur Edite avec succes", safe = False)
        return JsonResponse("Echec de l'edition de l'utilisateur")
    elif request.method =='DELETE':
        user = Users.objects.get(id = id)
        user.delete()
        return JsonResponse('Suppresion Effectuer avec success')