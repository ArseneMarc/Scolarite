from django.urls import re_path
from Scolarite import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    re_path(r'^etudiant/$', views.etudiantsApi),
    re_path(r'^etudiant/([a-zA-Z0-9]+)$', views.etudiantsApi),

    re_path(r'^specialite/$', views.specialiteApi),
    re_path(r'^specialite/([0-9]+)$', views.specialiteApi),
    
    re_path(r'^classe/$', views.classeApi),
    re_path(r'^classe/([0-9]+)$', views.classeApi),
    
    re_path(r'^niveau/$', views.niveauApi),
    re_path(r'^niveau/([0-9]+)$', views.niveauApi),
    
    re_path(r'^inscription/$', views.InscriptionApi),
    re_path(r'^inscription/([0-9]+)$', views.InscriptionApi),
    
    re_path(r'^payement/$', views.payementApi),
    re_path(r'^payement/([0-9]+)$', views.payementApi),
    
    re_path(r'^frais/$', views.FraisApi),
    re_path(r'^frais/([0-9]+)$', views.FraisApi),
    
    re_path(r'^annee/$', views.AnneeApi),
    re_path(r'^annee/([0-9]+)$', views.AnneeApi),
    # re_path(r'^saveFile', views.saveFile)
] 
# +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
