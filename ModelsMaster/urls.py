from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from .views import *
from . import views

urlpatterns = [
    path('index/ambito/', views.AmbitoView.index),
    path('show/ambito/<int:id>', views.AmbitoView.show),
    path('new/ambito', views.AmbitoView.new),
    path('create/ambito', views.AmbitoView.create),
    path('edit/ambito/<int:id>', views.AmbitoView.edit),
    path('update/ambito/<int:id>', views.AmbitoView.update),
    path('delete/ambito/<int:id>', views.AmbitoView.delete),

    path('index/tipo_objetivo', views.TipoObjetivoView.index),
    path('show/tipo_objetivo/<int:id>', views.TipoObjetivoView.show),
    path('new/tipo_objetivo', views.TipoObjetivoView.new),
    path('create/tipo_objetivo', views.TipoObjetivoView.create),
    path('edit/tipo_objetivo/<int:id>', views.TipoObjetivoView.edit),
    path('update/tipo_objetivo/<int:id>', views.TipoObjetivoView.update),
    path('delete/tipo_objetivo/<int:id>', views.TipoObjetivoView.delete),

    path('index/estructura', views.index_estructura),
    path('show/estructura/<int:id>', views.show_estructura),
    path('new/estructura', views.new_estructura),
    path('create/estructura', views.create_estructura),
    path('edit/estructura/<int:id>', views.edit_estructura),
    path('update/estructura/<int:id>', views.update_estructura),
    path('delete/estructura/<int:id>', views.delete_estructura),

    path('index/riesgo', views.index_riesgo), 
    path('show/riesgo/<int:id>', views.show_riesgo),
    path('new/riesgo', views.new_riesgo),
    path('create/riesgo', views.create_riesgo),
    path('edit/riesgo/<int:id>', views.edit_riesgo),
    path('update/riesgo/<int:id>', views.update_riesgo),
    path('delete/riesgo/<int:id>', views.delete_riesgo),

    path('index/tipo_interviniente', views.TipoIntervinienteView.index),
    path('show/tipo_interviniente/<int:id>', views.TipoIntervinienteView.show),
    path('new/tipo_interviniente', views.TipoIntervinienteView.new),
    path('create/tipo_interviniente', views.TipoIntervinienteView.create),
    path('edit/tipo_interviniente/<int:id>', views.TipoIntervinienteView.edit),
    path('update/tipo_interviniente/<int:id>', views.TipoIntervinienteView.update),
    path('delete/tipo_interviniente/<int:id>', views.TipoIntervinienteView.delete),

    path('index/sector', views.SectorView.index),
    path('show/sector/<int:id>', views.SectorView.show),
    path('new/sector', views.SectorView.new),
    path('create/sector', views.SectorView.create),
    path('edit/sector/<int:id>', views.SectorView.edit),
    path('update/sector/<int:id>', views.SectorView.update),
    path('delete/sector/<int:id>', views.SectorView.delete),

    path('index/nag', views.nagView.index),
    path('show/nag/<int:id>', views.nagView.show),
    path('new/nag', views.nagView.new),
    path('create/nag', views.nagView.create),
    path('edit/nag/<int:id>', views.nagView.edit),
    path('update/nag/<int:id>', views.nagView.update),
    path('delete/nag/<int:id>', views.nagView.delete),
]
urlpatterns += staticfiles_urlpatterns()