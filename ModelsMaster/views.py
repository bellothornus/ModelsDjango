from django.shortcuts import render, redirect
from django.views import View
from .forms import AmbitoForm, TipoObjetivoForm, SectorForm, NivelAreaGeograficaForm, AreaGeograficaForm, EmpresaForm, ModeloForm, BenchmarkingForm, PuntosCapituloForm, ObjetivoForm, UserForm
from .models import Ambito, TipoObjetivo, Sector, NivelAreaGeografica, AreaGeografica, Empresa, Modelo, Benchmarking, PuntosCapitulo, Objetivo
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
# Create your views here.

class UserView(View):
    
    def index(request):
        all = User.objects.filter(is_active=1)
        args = {
            "querys":all,
            "titulo":"user",
            "titulo_view":"Users"
        }
        return render(request, 'base_index.html', args)

    def show(request,id):
        user = User.objects.get(id=id)
        args = {
            "user":user
        }
        return render(request, 'user/show.html', args)

    def create(request):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                #new_user = User.objects.create_user(**form.cleaned_data)
                #login(new_user)
                return render(request,'user/new.html')
        else:
            form = UserForm()
            arg={
                'form': form
            } 

        return render(request,'user/new.html', arg)

    def update(request,id):
        user = User.objects.get(id=id)
        form = UserForm(request.POST, instance=user)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                arg={
                    'form':form,
                    'user':user,
                }
        else:
            form = UserForm(instance=user)
            arg={
                    'form':form,
                    'user':user,
                }
        return render(request, 'user/update.html', arg)

    def delete(request,id):
        user = User.objects.get(id=id)
        user.is_active = 0
        user.save()
        eliminado = "El usuario se ha eliminado"
        all = User.objects.filter(is_active=1)
        args = {
            "eliminado":eliminado,
            "querys":all,
            "titulo":"user",
            "titulo_view":"User"
        }
        return render(request, 'base_index.html', args)

def index(request):
    return render(request, 'index.html')

def prueba1(request):
    args = {
    }
    return render(request, 'Prueba/index.html', args)

def prueba2(request):
    querys = Ambito.objects.all()
    args = {
        "querys":querys,
        "titulo":"ambito"
    }
    return render(request, 'Prueba/index.html', args)

def prueba3(request):
    querys = Sector.objects.all()
    args = {
        "querys":querys,
        "titulo":"sector"
    }
    return render(request, 'Prueba/index.html', args)

def prueba4(request):
    querys = NivelAreaGeografica.objects.all()
    columns = NivelAreaGeografica._meta.fields
    args = {
        "querys":querys,
        "titulo":"nag"
    }
    return render(request, 'Prueba/index.html', args)

def prueba5(request):
    querys = Ambito.objects.all()
    columns = Ambito._meta.fields
    args = {
        "querys":querys,
        "titulo":"ambito",
        "columns":columns,
        "titulo_view":"Ambito"
    }
    return render(request, 'Prueba/form.html', args)

def prueba6(request):
    relacionados1 = NivelAreaGeografica.objects.filter(Eliminado=False)
    padres = AreaGeografica.objects.filter(Eliminado=False)
    columns = AreaGeografica._meta.fields
    args = {
        "relacionados1":relacionados1,
        "padres":padres,
        "titulo":"area_geografica",
        "columns":columns,
        "titulo_view":"Áreas Geográficas"
    }
    return render(request, 'base_prueba_form.html', args)

def prueba7(request):
    relacionados1 = PuntosCapitulo.objects.all()
    relacionados2 = TipoObjetivo.objects.all()
    columns = Objetivo._meta.fields
    args = {
        "relacionados1":relacionados1,
        "titulo":"objetivo",
        "columns":columns,
        "titulo_view":"Objetivos"
    }
    return render(request, 'base_prueba_form.html', args)

class AmbitoView(View):
    def index(request):
        all = Ambito.objects.filter(Eliminado=False)
        args = {
            "querys":all,
            "titulo":"ambito",
            "titulo_view":"Ambito"
        }
        #return render(request, 'Ambitos/index.html', args)
        return render(request, 'base_index.html', args)
    def show(request,id):
        ambito = Ambito.objects.get(Id__name=id)
        args = {
            "ambito":ambito
        }
        return render(request, 'Ambitos/show.html', args)
    
    def new(request):
        columns = Ambito._meta.fields
        args = {
            "titulo":"ambito",
            "columns":columns,
            "titulo_view":"Ambitos"
        }
        #return render(request,'Ambitos/new.html')
        return render(request, 'base_prueba_form.html',args)

    def create(request):
        form = AmbitoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "El ambito se ha creado con éxito"
            all = Ambito.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "ambitos":all
                }
            return render(request, 'Ambitos/index.html', args )
        else:
            args = {
                'form': form
                }
            return render (request, 'Ambitos/new.html', args )

    def edit(request,id):
        ambito = Ambito.objects.get(Id__name=id)
        args = {
            "ambito":ambito
            }
        return render(request, 'Ambitos/edit.html', args)

    def update(request,id):
        ambito = Ambito.objects.get(Id__name=id)
        form = AmbitoForm(request.POST, instance=ambito)
        if form.is_valid():
            form.save()
            aviso = "Se han actualizado los datos"
            args = {
                "aviso":aviso,
                "form":form,
                "ambito":ambito
            }
            return render(request, 'Ambitos/edit.html', args)
        else:
            ambito = Ambito.objects.get(Id__name=id)
            args = {
                "form":form,
                "ambito":ambito
            }
            return render(request, 'Ambitos/edit.html',args)

    def delete(request,id):
        ambito = Ambito.objects.get(Id__name=id)
        all = Ambito.objects.filter(Eliminado=False)
        am_pc = PuntosCapitulo.objects.filter(IdAm=ambito.Id)
        if am_pc:
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "querys":all,
                "titulo":"ambito",
                "titulo_view":"Ambito"
            }
        else:
            ambito.Eliminado = True
            ambito.save()
            eliminado = "El ambito se ha eliminado"
            all = Ambito.objects.filter(Eliminado=False)
            args = {
                "eliminado":eliminado,
                "querys":all,
                "titulo":"ambito",
                "titulo_view":"Ambito"
            }
        return render(request, 'base_index.html', args)

class TipoObjetivoView(View):
    def index(request):
        all = TipoObjetivo.objects.filter(Eliminado=False)
        args = {
            #"tipos_objetivos":all
            "querys":all,
            "titulo":"tipo_objetivo",
            "titulo_view":"Tipo Objetivo"
        }
        #return render(request, 'TipoObjetivo/index.html', args)
        return render(request, 'base_index.html', args)
    def show(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(Id__name=id)
        args = {
            "tipo_objetivo":tipo_objetivo
        }
        return render(request, 'TipoObjetivo/show.html', args)

    def new(request):
        columns = TipoObjetivo._meta.fields
        args = {
            "titulo":"tipo_objetivo",
            "columns":columns,
            "titulo_view":"Tipo Objetivo"
        }
        #return render(request, 'TipoObjetivo/new.html')
        return render(request, 'base_prueba_form.html',args)

    def create(request):
        form = TipoObjetivoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "El tipo objetivo se ha creado con éxito"
            all = TipoObjetivo.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "tipos_objetivos":all
            }
            return render(request, 'TipoObjetivo/index.html', args)
        else:
            args = {
                "form":form
            }
            return render(request, 'TipoObjetivo/new.html', args)

    def edit(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(Id__name=id)
        args = {
            "tipo_objetivo":tipo_objetivo
        }
        return render(request, 'TipoObjetivo/edit.html', args)

    def update(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(Id__name=id)
        form = TipoObjetivoForm(request.POST, instance = tipo_objetivo)
        if form.is_valid():
            form.save()
            aviso = "Los datos se han actualizado!"
            args = {
                "aviso":aviso,
                "form":form,
                "tipo_objetivo":tipo_objetivo
            }
            return render(request, 'TipoObjetivo/edit.html', args)
        else:
            args = {
                "form":form,
                "tipo_objetivo":tipo_objetivo
            }
            return render(request, 'TipoObjetivo/edit.html', args)

    def delete(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(Id__name=id)
        tipo_objetivo.Eliminado = True
        tipo_objetivo.save()
        eliminado = "El tipo objetivo se ha eliminado"
        all = TipoObjetivo.objects.filter(Eliminado=False)
        args = {
            "eliminado":eliminado,
            "querys":all,
            "titulo":"tipo_objetivo",
            "titulo_view":"Tipo Objetivo"
        }
        return render(request, 'base_index.html', args)

class EstructuraView(View):
    def index(request):
        all = Estructura.objects.filter(Eliminado=False)
        args = {
            #"estructuras":all
            "querys":all,
            "titulo":"estructura",
            "titulo_view":"Estructura"
        }
        #return render(request, 'Estructura/index.html', args)
        return render(request, 'base_index.html', args)

    def show(request,id):
        estructura = Estructura.objects.get(Id__name=id)
        args = {
            "estructura":estructura
        }
        return render(request, 'Estructura/show.html', args)

    def new(request):
        columns = Estructura._meta.fields
        args = {
            "titulo":"estructura",
            "columns":columns,
            "titulo_view":"Estructuras"
        }
        #return render(request, 'Estructura/new.html')
        return render(request,'base_prueba_form.html',args)

    def create(request):
        form = EstructuraForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "La estructura se ha creado con éxito"
            all = Estructura.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "estructuras":all
            }
            return render(request, 'Estructura/index.html', args)
        else:
            args = {
                "form":form
            }
            return render(request, 'Estructura/new.html', args)

    def edit(request,id):
        estructura = Estructura.objects.get(Id__name=id)
        args = {
            "estructura": estructura
        }
        return render(request, 'Estructura/edit.html', args)

    def update(request,id):
        estructura = Estructura.objects.get(Id__name=id)
        form = EstructuraForm(request.POST, instance=estructura)
        if form.is_valid():
            form.save()
            aviso = "Los datos se han actualizado!"
            args = {
                "aviso":aviso,
                "estructura":estructura
            }
            return render(request, 'Estructura/edit.html', args)
        else:
            args = {
                "form":form
            }
            return render(request, 'Estructura/edit.html', args)

    def delete(request,id):
        estructura = Estructura.objects.get(Id__name=id)
        estructura.Eliminado = True
        estructura.save()
        eliminado = "El tipo objetivo se ha eliminado"
        all = Estructura.objects.filter(Eliminado=False)
        args = {
            "eliminado":eliminado,
            "querys":all,
            "titulo":"estructura",
            "titulo_view":"Estructura"
        }
        return render(request, 'base_index.html', args)

class RiesgoView(View):
    def index(request):
        all = Riesgo.objects.filter(Eliminado=False)
        args = {
            #"riesgos":all
            "querys":all,
            "titulo":"riesgo",
            "titulo_view":"Riesgo"
        }
        #return render(request, 'Riesgo/index.html', args)
        return render(request, 'base_index.html', args)

    def show(request,id):
        riesgo = Riesgo.objects.get(Id__name=id)
        args = {
            "riesgo":riesgo
        }
        return render(request, 'Riesgo/show.html', args)

    def new(request):
        return render(request, 'Riesgo/new.html')

    def create(request):
        form = RiesgoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "El riesgo se ha creado con éxito"
            all = Riesgo.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "riesgos":all
            }
            return render(request, 'Riesgo/index.html', args)
        else:
            args = {
                "form":form
            }
            return render(request, 'Riesgo/new.html', args)

    def edit(request,id):
        riesgo = Riesgo.objects.get(Id__name=id)
        args = {
            "riesgo":riesgo
        }
        return render(request, 'Riesgo/edit.html', args)

    def update(request,id):
        riesgo = Riesgo.objects.get(Id__name=id)
        form = RiesgoForm(request.POST, instance=riesgo)
        if form.is_valid():
            form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "riesgo":riesgo
            }
            return render(request, 'Riesgo/edit.html', args)
        else:
            args = {
                "riesgo":riesgo,
                "form":form
            }
            return render(request, 'Riesgo/edit.html', args)

    def delete(request,id):
        riesgo = Riesgo.objects.get(Id__name=id)
        riesgo.Eliminado = True
        riesgo.save()
        all = Riesgo.objects.filter(Eliminado=False)
        eliminado = "El riesgo se ha eliminado"
        args = {
            "eliminado":eliminado,
            "querys":all,
            "titulo":"riesgo",
            "titulo_view":"Riesgo"
        }
        return render(request, 'base_indexindex.html', args)

class TipoIntervinienteView(View):

    def index(request):
        all = TipoInterviniente.objects.filter(Eliminado=False)
        args = {
            #"tipo_intervinientes":all
            "querys":all,
            "titulo":"tipo_interviniente",
            "titulo_view":"Tipo Interviniente"
        }
        #return render(request, 'TipoInterviniente/index.html', args)
        return render(request, 'base_index.html', args)

    def show(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(Id__name=id)
        args = {
            "tipo_interviniente":tipo_interviniente
        }
        return render(request, 'TipoInterviniente/show.html', args)

    def new(request):
        return render(request, 'TipoInterviniente/new.html')

    def create(request):
        ModelForm_form = TipoIntervinienteForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El tipo interviniente se ha creado con éxito!"
            all = TipoInterviniente.objects.filter(Eliminado=False)
            args ={
                "aviso":aviso,
                "tipo_intervinientes":all
            }
            return render(request, 'TipoInterviniente/index.html', args)
        else:
            args = {
                "form":ModelForm_form
            }
            return render(request, 'TipoInterviniente/new.html', args)

    def edit(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(Id__name=id)
        args = {
            "tipo_interviniente":tipo_interviniente
        }
        return render(request, 'TipoInterviniente/edit.html', args)

    def update(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(Id__name=id)
        ModelForm_form = TipoIntervinienteForm(request.POST, instance=tipo_interviniente)
        if ModelForm_form.is_valid():
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "tipo_interviniente":tipo_interviniente
            }
        else:
            args = {
                "form":ModelForm_form,
                "tipo_interviniente":tipo_interviniente
            }
        return render(request, 'TipoInterviniente/edit.html', args)

    def delete(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(Id__name=id)
        tipo_interviniente.Eliminado = True
        tipo_interviniente.save()
        eliminado = "El tipo Interviniente se ha eliminado"
        all = TipoInterviniente.objects.filter(Eliminado=False)
        args = {
            "eliminado":eliminado,
            "querys":all,
            "titulo":"tipo_interviniente",
            "titulo_view":"Tipo Interviniente"
        }
        return render(request, 'base_index.html', args)

class SectorView(View):

    def index(request):
        all = Sector.objects.filter(Eliminado=False)
        args = {
            #"sectores":all
            "querys":all,
            "titulo":"sector",
            "titulo_view":"Sector"
        }
        #return render(request, 'Sector/index.html', args)
        return render(request, 'base_index.html', args)

    def show(request,id):
        sector = Sector.objects.get(Id__name=id)
        args = {
            "sector":sector
        }
        return render(request, 'Sector/show.html', args)

    def new(request):
        columns = Sector._meta.fields
        args = {
            "titulo":"sector",
            "columns":columns,
            "titulo_view":"Sector"
        }
        return render(request, 'base_prueba_form.html',args)

    def create(request):
        ModelForm_form = SectorForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El sector se ha creado con éxito!"
            all = Sector.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "sectores":all
            }
            return render(request, 'Sector/index.html', args)
        else:
            args = {
                "form":ModelForm_form
            }
            return render(request, 'Sector/new.html', args)
    def edit(request,id):
        sector = Sector.objects.get(Id__name=id)
        args = {
            "sector":sector
        }
        return render(request, 'Sector/edit.html', args)

    def update(request,id):
        sector = Sector.objects.get(Id__name=id)
        ModelForm_form = SectorForm(request.POST, instance=sector)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "sector":sector
            }
        else:
            args = {
                "form":ModelForm_form,
                "sector":sector
            }
        return render(request, 'Sector/edit.html', args)

    def delete(request,id):
        all = Sector.objects.filter(Eliminado=False)
        sector = Sector.objects.get(Id__name=id)
        sc_emp = Empresa.objects.filter(Id__name=sector.Id)
        sc_bench = Benchmarking.objects.filter(Id__name=sector.Id)
        if sc_emp or sc_bench:
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "querys":all,
                "titulo":"sector",
                "titulo_view":"Sector"
            }
        else:
            sector.Eliminado = True
            sector.save()
            eliminado = "El sector se ha eliminado"
            all = Sector.objects.filter(Eliminado=False)
            args = {
                "eliminado":eliminado,
                "querys":all,
                "titulo":"sector",
                "titulo_view":"Sector"
            }
        return render(request, 'Sector/index.html', args)

class NivelAreaGeograficaView(View):
    def index(request):
        all = NivelAreaGeografica.objects.filter(Eliminado=False)
        args = {
            #"nags":all
            "querys":all,
            "titulo":"nag",
            "titulo_view":"Nivel Área Geográfica"
        }
        #return render(request, 'Nag/index.html', args)
        return render(request, 'base_index.html', args)

    def show(request,id):
        nag = NivelAreaGeografica.objects.get(Id__name=id)
        args = {
            "nag":nag
        }
        return render(request, 'Nag/show.html', args)

    def new(request):
        columns = NivelAreaGeografica._meta.fields
        args = {
            "titulo":"nag",
            "columns":columns,
            "titulo_view":"Nivel Área Geográfica"
        }
        return render(request, 'base_prueba_form.html',args)

    def create(request):
        ModelForm_form = NivelAreaGeograficaForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Nivel de Área geográfica se ha creado con éxito!"
            all = NivelAreaGeografica.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "nags":all
            }
            return render(request, 'Nag/index.html', args)
        else:
            args = {
                "form":ModelForm_form
            }
            return render (request, 'Nag/new.html', args)

    def edit(request,id):
        nag = NivelAreaGeografica.objects.get(Id__name=id)
        args = {
            "nag":nag
        }
        return render(request, 'Nag/edit.html', args)

    def update(request,id):
        nag = NivelAreaGeografica.objects.get(Id__name=id)
        ModelForm_form = NivelAreaGeograficaForm(request.POST, instance=nag)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "nag":nag
            }
        else:
            args = {
                "form":ModelForm_form,
                "nag":nag
            }
        return render(request, 'Nag/edit.html', args)

    def delete(request,id):
        all = NivelAreaGeografica.objects.filter(Eliminado=False)
        nag = NivelAreaGeografica.objects.get(Id=id)
        nag_ag = AreaGeografica.objects.filter(IdNag=nag.Id)
        if nag_ag:
            args = {
                "eliminado":"No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "querys":all,
                "titulo":"nag",
                "titulo_view":"Nivel Área Geográfica"
            }
        else:
            nag.Eliminado = True
            nag.save()
            eliminado = "El Nivel de Área geográfica se ha eliminado"
            all = NivelAreaGeografica.objects.filter(Eliminado=False)
            args = {
                "eliminado":eliminado,
                "querys":all,
                "titulo":"nag",
                "titulo_view":"Nivel Área Geográfica"
            }
        return render(request, 'base_index.html', args)

class AreaGeograficaView(View):
    def index(request):
        all = AreaGeografica.objects.filter(Eliminado=False)
        args = {
            #"ags":all
            "querys":all,
            "titulo":"area_geografica",
            "titulo_view":"Área Geográfica"
        }
        #return render(request, 'AreaGeografica/index.html', args)
        return render(request, 'base_index.html', args)

    def show(request,id):
        ag = AreaGeografica.objects.get(Id__name=id)
        try:
            ag_parent = AreaGeografica.objects.get(Id__name=ag.IdParent.Id)
        except AttributeError:
            ag_parent = "nope"
        ag_childs = AreaGeografica.objects.filter(IdParent=ag.Id)
        args = {
            "ag":ag,
            "ag_parent":ag_parent,
            "ag_childs":ag_childs
        }
        return render(request, 'AreaGeografica/show.html', args)

    def new(request):
        nags = NivelAreaGeografica.objects.filter(Eliminado=False)
        ags = AreaGeografica.objects.filter(Eliminado=False)
        columns = AreaGeografica._meta.fields
        args = {
            "relacionados1":nags,
            "padres":ags,
            "titulo":"area_geografica",
            "titulo_view":"Área Geográfica",
            "columns":columns
        }
        #return render(request, 'AreaGeografica/new.html', args)
        return render(request,'base_prueba_form.html',args)

    def create(request):
        ModelForm_form = AreaGeograficaForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Área geográfica se ha creado con éxito!"
            all = AreaGeografica.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "ags":all
            }
            return render(request, 'AreaGeografica/index.html', args)
        else:
            nags = NivelAreaGeografica.objects.filter(Eliminadoo=False)
            ags = AreaGeografica.objects.filter(Eliminado=False)
            args = {
                "form":ModelForm_form,
                "nags":nags,
                "ags":ags
            }
            return render(request, 'AreaGeografica/new.html', args)

    def edit(request,id):
        nags = NivelAreaGeografica.objects.filter(Eliminado=False)
        ag = AreaGeografica.objects.get(Id__name=id)
        ags = AreaGeografica.objects.filter(Eliminado=False)
        args = {
            "ag":ag,
            "nags":nags,
            "ags":ags
        }
        return render(request, 'AreaGeografica/edit.html', args)

    def update(request,id):
        ag = AreaGeografica.objects.get(Id__name=id)
        ModelForm_form = AreaGeograficaForm(request.POST, instance=ag)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "ag":ag
            }
        else:
            args = {
                "form":ModelForm_form,
                "ag":ag
            }
        return render(request, 'AreaGeografica/edit.html', args)

    def delete(request,id):
        all = AreaGeografica.objects.filter(Eliminado=False)
        ag = AreaGeografica.objects.get(Id__name=id)
        ag_parent = AreaGeografica.objects.filter(IdParent=ag.Id)
        bench_ag = Benchmarking.objects.filter(IdAg=ag.Id)
        emp_ag = Empresa.objects.filter(IdAg=ag.Id)
        if ag_parent or bench_ag or emp_ag:
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "querys":all,
                "titulo":"area_geografica",
                "titulo_view":"Área Geográfica"
            }
        else:
            ag.Eliminado = True
            ag.save()
            eliminado = "El Área geográfica se ha eliminado"
            all = AreaGeografica.objects.filter(Eliminado=False)
            args = {
                "eliminado":eliminado,
                "querys":all,
                "titulo":"area_geografica",
                "titulo_view":"Área Geográfica"
            }
        return render(request, 'base_index.html', args)

class EmpresaView(View):
    def index(request):
        all = Empresa.objects.filter(Eliminado=False)
        args = {
            #"emps":all
            "querys":all,
            "titulo":"empresa",
            "titulo_view":"Empresa"
        }
        #return render(request, 'Empresa/index.html', args)
        return render(request, 'base_index.html', args)
    
    def show(request,id):
        emp = Empresa.objects.get(Id__name=id)
        emp_ag = AreaGeografica.objects.get(Id__name=emp.IdAg.Id)
        emp_sc = Sector.objects.get(Id__name=emp.IdSc.Id)
        args = {
            "emp":emp,
            "emp_ag":emp_ag,
            "emp_sc":emp_sc
        }
        return render(request, 'Empresa/show.html', args)

    def new(request):
        emp_scs = Sector.objects.filter(Eliminado=False)
        emp_ags = AreaGeografica.objects.filter(Eliminado=False)
        args = {
            "emp_scs":emp_scs,
            "emp_ags":emp_ags
        }
        return render(request, 'Empresa/new.html', args)
    
    def create(request):
        ModelForm_form = EmpresaForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "La empresa se ha creado con éxito!"
            all = Empresa.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "emps":all
            }
            return render(request, 'Empresa/index.html', args)
        else:
            emp_scs = Sector.objects.filter(Eliminado=False)
            emp_ags = AreaGeografica.objects.filter(Eliminado=False)
            args = {
                "form":ModelForm_form,
                "emp_scs":emp_scs,
                "emp_ags":emp_ags
            }
            return render(request, 'Empresa/new.html', args)
    def edit(request,id):
        emp_scs = Sector.objects.filter(Eliminado=False)
        emp = Empresa.objects.get(Id__name=id)
        emp_ags = AreaGeografica.objects.filter(Eliminado=False)
        args = {
            "emp":emp,
            "emp_ags":emp_ags,
            "emp_scs":emp_scs
        }
        return render(request, 'Empresa/edit.html', args)
    
    def update(request,id):
        emp = Empresa.objects.get(Id__name=id)
        ModelForm_form = EmpresaForm(request.POST, instance=emp)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "emp":emp
            }
        else:
            args = {
                "form":ModelForm_form,
                "emp":emp
            }
        return render(request, 'Empresa/edit.html', args)

    def delete(request,id):
        all = Empresa.objects.filter(Eliminado=False)
        emp = Empresa.objects.get(Id__name=id)
        md_emp = Modelo.objects.filter(IdEmp=emp.Id)
        if md_emp:
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "querys":all,
                "titulo":"empresa",
                "titulo_view":"Empresa"
            }
        else:
            emp.Eliminado = True
            emp.save()
            eliminado = "la empresa se ha eliminado"
            all = Empresa.objects.filter(Eliminado=False)
            args = {
                "eliminado":eliminado,
                "querys":all,
                "titulo":"empresa",
                "titulo_view":"Empresa"
            }
        return render(request, 'base_index.html', args)

class ModeloView(View):

    def index(request):
        all=Modelo.objects.filter(Eliminado=False)
        args= {
            #"modelos":all
            "querys":all,
            "titulo":"modelo",
            "titulo_view":"Modelo"
        }
        #return render(request, 'Modelo/index.html', args)
        return render(request, 'base_index.html', args)
    
    def show(request,id):
        modelo = Modelo.objects.get(Id__name=id)
        modelo_emp = Empresa.objects.get(Id__name=modelo.IdEmp.Id)
        args = {
            "modelo":modelo,
            "modelo_emp":modelo_emp,
        }
        return render(request, 'Modelo/show.html', args)
    
    def new(request):
        modelo_emps = Empresa.objects.filter(Eliminado=False)
        args = {
            "modelo_emps":modelo_emps,
        }
        return render(request, 'Modelo/new.html', args)

    def create(request):
        ModelForm_form = ModeloForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Modelo se ha creado con éxito!"
            all = Modelo.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "modelos":all
            }
            return render(request, 'Modelo/index.html', args)
        else:
            modelo_emps = Empresa.objects.filter(Eliminado=False)
            args = {
                "form":ModelForm_form,
                "modelo_emps":modelo_emps,
            }
            return render(request, 'Modelo/new.html', args)

    def edit(request,id):
        modelo_emps = Empresa.objects.filter(Eliminado=False)
        modelo = Modelo.objects.get(Id__name=id)
        args = {
            "modelo":modelo,
            "modelo_emps":modelo_emps,
        }
        return render(request, 'Modelo/edit.html', args)
    
    def update(request,id):
        modelo = Modelo.objects.get(Id__name=id)
        ModelForm_form = ModeloForm(request.POST, instance=modelo)
        modelo_emps = Empresa.objects.filter(Eliminado=False)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "modelo":modelo,
                "modelo_emps":modelo_emps
            }
        else:
            args = {
                "form":ModelForm_form,
                "modelo":modelo,
                "modelo_emps":modelo_emps
            }
        return render(request, 'Modelo/edit.html', args)

    def delete(request,id):
        all = Modelo.objects.filter(Eliminado=False)
        modelo = Modelo.objects.get(Id__name=id)
        pc_md = PuntosCapitulo.objects.filter(IdMd=modelo.Id)
        if pc_md:
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "querys":all,
                "titulo":"modelo",
                "titulo_view":"Modelo"
            }
        else:
            modelo.Eliminado = True
            modelo.save()
            eliminado = "El Modelo se ha eliminado"
            all = Modelo.objects.filter(Eliminado=False)
            args = {
                "eliminado":eliminado,
                "querys":all,
                "titulo":"modelo",
                "titulo_view":"Modelo"
            }
        return render(request, 'base_index.html', args)
            
class BenchmarkingView(View):
    def index(request):
        all = Benchmarking.objects.filter(Eliminado=False)
        args = {
            #"benchs":all
            "querys":all,
            "titulo":"benchmarking",
            "titulo_view":"Benchmarking"
        }
        #return render(request, 'Benchmarking/index.html', args)
        return render(request, 'base_index.html', args)
    
    def show(request,id):
        bench = Benchmarking.objects.get(Id__name=id)
        bench_ag = AreaGeografica.objects.get(Id__name=bench.IdAg.Id)
        bench_sc = Sector.objects.get(Id__name=bench.IdSc.Id)
        args = {
            "bench":bench,
            "bench_ag":bench_ag,
            "bench_sc":bench_sc
        }
        return render(request, 'Benchmarking/show.html', args)

    def new(request):
        bench_scs = Sector.objects.filter(Eliminado=False)
        bench_ags = AreaGeografica.objects.filter(Eliminado=False)
        args = {
            "bench_scs":bench_scs,
            "bench_ags":bench_ags
        }
        return render(request, 'Benchmarking/new.html', args)
    
    def create(request):
        ModelForm_form = BenchmarkingForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Benchmarking se ha creado con éxito!"
            all = Benchmarking.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "benchs":all
            }
            return render(request, 'Benchmarking/index.html', args)
        else:
            bench_scs = Sector.objects.filter(Eliminado=False)
            bench_ags = AreaGeografica.objects.filter(Eliminado=False)
            args = {
                "form":ModelForm_form,
                "bench_scs":bench_scs,
                "bench_ags":bench_ags
            }
            return render(request, 'Benchmarking/new.html', args)
    def edit(request,id):
        bench_scs = Sector.objects.filter(Eliminado=False)
        bench = Benchmarking.objects.get(Id__name=id)
        bench_ags = AreaGeografica.objects.filter(Eliminado=False)
        args = {
            "bench":bench,
            "bench_ags":bench_ags,
            "bench_scs":bench_scs
        }
        return render(request, 'Benchmarking/edit.html', args)
    
    def update(request,id):
        bench = Benchmarking.objects.get(Id__name=id)
        ModelForm_form = BenchmarkingForm(request.POST, instance=bench)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "bench":bench
            }
        else:
            args = {
                "form":ModelForm_form,
                "bench":bench
            }
        return render(request, 'Benchmarking/edit.html', args)

    def delete(request,id):
        bench = Benchmarking.objects.get(Id__name=id)
        bench.Eliminado = True
        bench.save()
        eliminado = "El benchmarking se ha eliminado"
        all = Benchmarking.objects.filter(Eliminado=False)
        args = {
            "eliminado":eliminado,
            "querys":all,
            "titulo":"benchmarking",
            "titulo_view":"Benchmarking"
        }
        return render(request, 'base_index.html', args)

class PuntosCapituloView(View):

    def index(request):
       all=PuntosCapitulo.objects.filter(Eliminado=False) 
       args = {
           #"pcs":all
           "querys":all,
           "titulo":"puntoscap",
           "titulo_view":"Puntos Capitulo"
       }
       #return render(request, 'PuntosCapitulo/index.html', args)
       return render(request, 'base_index.html', args)

    def show(request,id):
        pc = PuntosCapitulo.objects.get(Id__name=id)
        pc_modelo = Modelo.objects.get(Id__name=pc.IdMd.Id)
        pc_ambito = Ambito.objects.get(Id__name=pc.IdAm.Id)
        args = {
            "pc":pc,
            "pc_modelo":pc_modelo,
            "pc_ambito":pc_ambito
        }
        return render(request, 'PuntosCapitulo/show.html', args)

    def new(request):
        pc_modelos = Modelo.objects.filter(Eliminado=False)
        pc_ambitos = Ambito.objects.filter(Eliminado=False)
        args = {
            "pc_modelos":pc_modelos,
            "pc_ambitos":pc_ambitos
        }
        return render(request, 'PuntosCapitulo/new.html', args)
    
    def create(request):
        ModelForm_form = PuntosCapituloForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El PuntoCapitulo se ha creado con éxito!"
            all = PuntosCapitulo.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "pcs":all
            }
            return render(request, 'PuntosCapitulo/index.html', args)
        else:
            pc_modelos = Modelo.objects.filter(Eliminado=False)
            pc_ambitos = Ambito.objects.filter(Eliminado=False)
            args = {
                "form":ModelForm_form,
                "pc_modelos":pc_modelos,
                "pc_ambitos":pc_ambitos
            }
            return render(request, 'PuntosCapitulo/new.html', args)

    def edit(request,id):
        pc_modelos = Modelo.objects.filter(Eliminado=False)
        pc = PuntosCapitulo.objects.get(Id__name=id)
        pc_ambitos = Ambito.objects.filter(Eliminado=False)
        args = {
            "pc":pc,
            "pc_modelos":pc_modelos,
            "pc_ambitos":pc_ambitos
        }
        return render(request, 'PuntosCapitulo/edit.html', args)

    def update(request,id):
        pc = PuntosCapitulo.objects.get(Id__name=id)
        ModelForm_form = PuntosCapituloForm(request.POST, instance=pc)
        pc_ambitos = Ambito.objects.filter(Eliminado=False)
        pc_modelos = Modelo.objects.filter(Eliminado=False)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "pc":pc,
                "pc_modelos":pc_modelos,
                "pc_ambitos":pc_ambitos
            }
        else:
            args = {
                "form":ModelForm_form,
                "pc":pc,
                "pc_modelos":pc_modelos,
                "pc_ambitos":pc_ambitos
            }
        return render(request, 'PuntosCapitulo/edit.html', args)
    
    def delete(request,id):
        all = PuntosCapitulo.objects.filter(Eliminado=False)
        pc = PuntosCapitulo.objects.get(Id__name=id)
        ob_pc = Objetivo.objects.filter(IdPc=pc.Id)
        if ob_pc:
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "pcs":all,
                "titulo":"puntoscap",
            "titulo_view":"Puntos Capitulo"
            }
        else:
            pc.Eliminado = True
            pc.save()
            eliminado = "El PuntoCapitulo se ha eliminado"
            all = PuntosCapitulo.objects.filter(Eliminado=False)
            args = {
                "eliminado":eliminado,
                "pcs":all,
                "titulo":"puntoscap",
                "titulo_view":"Puntos Capitulo"
            }
        return render(request, 'PuntosCapitulo/index.html', args)
        
class ObjetivoView(View):

    def index(request):
       all=Objetivo.objects.filter(Eliminado=False) 
       args = {
           #"objs":all
           "querys":all,
           "titulo":"objetivo",
           "titulo_view":"Objetivo"
       }
       #return render(request, 'Objetivo/index.html', args)
       return render(request, 'base_index.html', args)

    def show(request,id):
        obj = Objetivo.objects.get(Id__name=id)
        obj_pc = PuntosCapitulo.objects.get(Id__name=obj.id_ob_pc.Id)
        obj_to = TipoObjetivo.objects.get(Id__name=obj.id_ob_to.Id)
        try:
            obj_parent = Objetivo.objects.get(Id__name=obj.IdParent.Id)
        except:
            obj_parent={}
        obj_childs = Objetivo.objects.filter(IdParent=obj.Id)
        args = {
            "obj":obj,
            "obj_pc":obj_pc,
            "obj_to":obj_to,
            "obj_parent":obj_parent,
            "obj_childs":obj_childs
        }
        return render(request, 'Objetivo/show.html', args)

    def new(request):
        all = Objetivo.objects.filter(Eliminado=False)
        obj_pcs = PuntosCapitulo.objects.filter(Eliminado=False)
        obj_tos = TipoObjetivo.objects.filter(Eliminado=False)
        args = {
            "obj_pcs":obj_pcs,
            "obj_tos":obj_tos,
            "objs":all
        }
        return render(request, 'Objetivo/new.html', args)
    
    def create(request):
        ModelForm_form = ObjetivoForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Objetivo se ha creado con éxito!"
            all = Objetivo.objects.filter(Eliminado=False)
            args = {
                "aviso":aviso,
                "objs":all
            }
            return render(request, 'Objetivo/index.html', args)
        else:
            obj_pcs = PuntosCapitulo.objects.filter(Eliminado=False)
            obj_tos = TipoObjetivo.objects.filter(Eliminado=False)
            args = {
                "form":ModelForm_form,
                "obj_pcs":obj_pcs,
                "obj_tos":obj_tos
            }
            return render(request, 'Objetivo/new.html', args)

    def edit(request,id):
        obj_pcs = PuntosCapitulo.objects.filter(Eliminado=False)
        obj = Objetivo.objects.get(Id__name=id)
        obj_tos = TipoObjetivo.objects.filter(Eliminado=False)
        all = Objetivo.objects.filter(Eliminado=False)
        args = {
            "obj":obj,
            "obj_pcs":obj_pcs,
            "obj_tos":obj_tos,
            "objs":all
        }
        return render(request, 'Objetivo/edit.html', args)

    def update(request,id):
        obj = Objetivo.objects.get(Id__name=id)
        ModelForm_form = ObjetivoForm(request.POST, instance=obj)
        obj_tos = TipoObjetivo.objects.filter(Eliminado=False)
        obj_pcs = PuntosCapitulo.objects.filter(Eliminado=False)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "obj":obj,
                "obj_pcs":obj_pcs,
                "obj_tos":obj_tos
            }
        else:
            args = {
                "form":ModelForm_form,
                "obj":obj,
                "obj_pcs":obj_pcs,
                "obj_tos":obj_tos
            }
        return render(request, 'Objetivo/edit.html', args)
    
    def delete(request,id):
        obj = Objetivo.objects.get(Id__name=id)
        obj.Eliminado = True
        obj.save()
        eliminado = "El Objetivo se ha eliminado"
        all = Objetivo.objects.filter(Eliminado=False)
        args = {
            "eliminado":eliminado,
            "querys":all,
            "titulo":"objetivo",
            "titulo_view":"Objetivo"
        }
        return render(request, 'base_index.html', args)
