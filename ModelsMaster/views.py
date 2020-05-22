from django.shortcuts import render, redirect
from django.views import View
from .forms import AmbitoForm, TipoObjetivoForm, TipoIntervinienteForm, SectorForm, NAGForm
from .models import Ambito,TipoObjetivo,Estructura,Riesgo,TipoInterviniente,Sector,Nivel_Area_Geografica
# Create your views here.
def index(request):
    return render(request, 'index.html')

class AmbitoView(View):
    def index(request):
        all = Ambito.objects.filter(bool_eliminado=False)
        args = {"ambitos":all}
        return render(request, 'Ambitos/index.html', args)

    def show(request,id):
        ambito = Ambito.objects.get(id_Ambito=id)
        args = {"ambito":ambito}
        return render(request, 'Ambitos/show.html', args)
    
    def new(request):
        return render(request,'Ambitos/new.html')

    def create(request):
        form = AmbitoForm(request.POST)
        if form.is_valid():
            form.save()
            all = Ambito.objects.filter(bool_eliminado=False)
            args = {
                "ambitos":all
                }
            return render(request, 'Ambitos/index.html', args )
        else:
            args = {
                'form': form
                }
            return render (request, 'Ambitos/new.html', args )

    def edit(request,id):
        ambito = Ambito.objects.get(id_Ambito=id)
        args = {
            "ambito":ambito
            }
        return render(request, 'Ambitos/edit.html', args)

    def update(request,id):
        ambito = Ambito.objects.get(id_Ambito=id)
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
            ambito = Ambito.objects.get(id_Ambito=id)
            args = {
                "form":form,
                "ambito":ambito
            }
            return render(request, 'Ambitos/edit.html',args)

    def delete(request,id):
        ambito = Ambito.objects.get(id_Ambito=id)
        ambito.bool_eliminado = True
        ambito.save()
        eliminado = "El ambito se ha eliminado"
        all = Ambito.objects.filter(bool_eliminado=False)
        args = {
            "eliminado":eliminado,
            "ambitos":all
        }
        return render(request, 'Ambitos/index.html', args)

class TipoObjetivoView(View):
    def index(request):
        all = TipoObjetivo.objects.filter(bool_eliminado=False)
        args = {
            "tipos_objetivos":all
        }
        return render(request, 'TipoObjetivo/index.html', args)

    def show(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo = id)
        args = {
            "tipo_objetivo":tipo_objetivo
        }
        return render(request, 'TipoObjetivo/show.html', args)

    def new(request):
        return render(request, 'TipoObjetivo/new.html')

    def create(request):
        form = TipoObjetivoForm(request.POST)
        if form.is_valid():
            form.save()
            return
            aviso = "El tipo objetivo se ha creado con éxito"
            all = TipoObjetivo.objects.filter(bool_eliminado=False)
            args = {
                "aviso":aviso,
                "tipo_objetivos":all
            }
            return render(request, 'TipoObjetivo/index.html', args)
        else:
            args = {
                "form":form
            }
            return render(request, 'TipoObjetivo/new.html', args)

    def edit(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo=id)
        arg = {
            "tipo_objetivo":tipo_objetivo
        }
        return render(request, 'TipoObjetivo/edit.html', arg)


    def update(request,id):
        nombre = request.POST['nombre']

        tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo=id)
        tipo_objetivo.Str_Nombre = nombre
        tipo_objetivo.save()
        aviso = "Los datos se han actualizado!"
        
        return render(request, 'TipoObjetivo/edit.html', {"aviso":aviso, "tipo_objetivo":tipo_objetivo})

    def delete(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_Tipo_Objetivo=id)
        tipo_objetivo.bool_eliminado = True
        tipo_objetivo.save()
        eliminado = "El tipo objetivo se ha eliminado"

        return render(request, 'TipoObjetivo/index.html', {"eliminado":eliminado,"tipo_objetivo":tipo_objetivo})

def index_estructura(request):
    all = Estructura.objects.filter(bool_eliminado=False)
    return render(request, 'Estructura/index.html', {"estructuras":all})

def show_estructura(request,id):
    estructura = Estructura.objects.get(id_Estructura=id)
    return render(request, 'Estructura/show.html', {"estructura":estructura})

def new_estructura(request):
    return render(request, 'Estructura/new.html')

def create_estructura(request):
    nombre = request.POST['nombre']
    estructura = Estructura(Str_Nombre=nombre)
    estructura.save()
    aviso = "La estructura se ha creado con éxito"
    all = Estructura.objects.filter(bool_eliminado=False)

    return render(request, 'Estructura/index.html', {"aviso":aviso, "estructuras":all})

def edit_estructura(request,id):
    estructura = Estructura.objects.get(id_Estructura=id)
    return render(request, 'Estructura/edit.html', {"estructura":estructura})

def update_estructura(request,id):
    estructura = Estructura.objects.get(id_Estructura=id)
    nombre = request.POST['nombre']
    estructura.Str_Nombre = nombre
    estructura.save()
    aviso = "Los datos se han actualizado!"

    return render(request, 'Estructura/edit.html', {"aviso":aviso, "estructura":estructura})

def delete_estructura(request,id):
    estructura = Estructura.objects.get(id_Estructura=id)
    estructura.bool_eliminado = True
    estructura.save()
    eliminado = "El tipo objetivo se ha eliminado"
    all = Estructura.objects.filter(bool_eliminado=False)

    return render(request, 'Estructura/index.html', {"eliminado":eliminado, "estructuras":all})

def index_riesgo(request):
    all = Riesgo.objects.filter(bool_eliminado=False)
    return render(request, 'Riesgo/index.html', {"riesgos":all})

def show_riesgo(request,id):
    riesgo = Riesgo.objects.get(id_Riesgo=id)
    return render(request, 'Riesgo/show.html', {"riesgo":riesgo})

def new_riesgo(request):
    return render(request, 'Riesgo/new.html')

def create_riesgo(request):
    nombre = request.POST['nombre']

    riesgo = Riesgo(Str_Nombre=nombre)
    riesgo.save()
    aviso = "El riesgo se ha creado con éxito"
    all = Riesgo.objects.filter(bool_eliminado=False)
    return render(request, 'Riesgo/index.html', {"aviso":aviso, "riesgos":all})

def edit_riesgo(request,id):
    riesgo = Riesgo.objects.get(id_Riesgo=id)
    return render(request, 'Riesgo/edit.html', {"riesgo":riesgo})

def update_riesgo(request,id):
    riesgo = Riesgo.objects.get(id_Riesgo=id)
    riesgo.Str_Nombre = request.POST['nombre']
    riesgo.save()
    aviso = "Los datos se han actualizado con éxito"
    return render(request, 'Riesgo/edit.html', {"riesgo":riesgo, "aviso":aviso})

def delete_riesgo(request,id):
    riesgo = Riesgo.objects.get(id_Riesgo=id)
    riesgo.bool_eliminado = True
    riesgo.save()
    all = Riesgo.objects.filter(bool_eliminado=False)
    eliminado = "El riesgo se ha eliminado"
    return render(request, 'Riesgo/index.html', {"eliminado":eliminado, "riesgos":all})
class TipoIntervinienteView(View):
    def index(request):
        all = TipoInterviniente.objects.filter(bool_eliminado=False)
        arg = {"tipo_intervinientes":all}
        return render(request, 'TipoInterviniente/index.html', arg)

    def show(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(id_Tipo_Interviniente=id)
        arg = {"tipo_interviniente":tipo_interviniente} 
        return render(request, 'TipoInterviniente/show.html', arg)

    def new(request):
        return render(request, 'TipoInterviniente/new.html')

    def create(request):
        form = TipoIntervinienteForm(request.POST)
        if form.is_valid():
            form.save()
            all = TipoInterviniente.objects.filter(bool_eliminado=False)
            args = {
                "tipo_intervinientes":all
                }
            return render(request, 'TipoInterviniente/index.html', args )
        else:
            args = {
                'form': form
                }
            return render (request, 'TipoInterviniente/new.html', args )

    def edit(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(id_Tipo_Interviniente=id)
        arg = {"tipo_interviniente":tipo_interviniente}
        return render(request, 'TipoInterviniente/edit.html', arg)

    def update(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(id_Tipo_Interviniente=id)
        form = TipoIntervinienteForm(request.POST, instance=tipo_interviniente)
        if form.is_valid():
            form.save()
            aviso = "Se han actualizado los datos"
            args = {
                "aviso":aviso,
                "form":form,
                "tipo_interviniente":tipo_interviniente
            }
            return render(request, 'TipoInterviniente/edit.html', args)
        else:
            tipo_interviniente = TipoInterviniente.objects.get(id_Tipo_Interviniente=id)
            args = {
                "form":form,
                "tipo_interviniente":tipo_interviniente
            }
            return render(request, 'TipoInterviniente/edit.html',args)

    def delete(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(id_Tipo_Interviniente=id)
        tipo_interviniente.bool_eliminado = True
        tipo_interviniente.save()
        eliminado = "El tipo Interviniente se ha eliminado"
        all = TipoInterviniente.objects.filter(bool_eliminado=False)
        arg = {"eliminado":eliminado, "tipo_intervinientes":all}
        return render(request, 'TipoInterviniente/index.html', arg)

class SectorView(View):
    def index(request):
        all = Sector.objects.filter(bool_Sc_eliminado=False)
        arg = {"sectores":all}
        return render(request, 'Sector/index.html', arg)

    def show(request,id):
        sector = Sector.objects.get(id_Sector=id)
        arg = {"sector":sector}
        return render(request, 'Sector/show.html', arg)

    def new(request):
        return render(request, 'Sector/new.html')

    def create(request):
        form = SectorForm(request.POST)
        if form.is_valid():
            form.save()
            all = Sector.objects.filter(bool_Sc_eliminado=False)
            args = {
                "sectores":all
                }
            return render(request, 'Sector/index.html', args )
        else:
            args = {
                'form': form
                }
            return render (request, 'Sector/new.html', args )

    def edit(request,id):
        sector = Sector.objects.get(id_Sector=id)
        arg = {"sector":sector}
        return render(request, 'Sector/edit.html', arg)

    def update(request,id):
        sector = Sector.objects.get(id_Sector=id)
        form = SectorForm(request.POST, instance=sector)
        if form.is_valid():
            form.save()
            aviso = "Se han actualizado los datos"
            args = {
                "aviso":aviso,
                "form":form,
                "sector":sector
            }
            return render(request, 'Sector/edit.html', args)
        else:
            sector = Sector.objects.get(id_Sector=id)
            args = {
                "form":form,
                "sector":sector
            }
            return render(request, 'Sector/edit.html',args)

    def delete(request,id):
            sector = Sector.objects.get(id_Sector=id)
            sector.bool_Sc_eliminado = True
            sector.save()
            eliminado = "El sector se ha eliminado"
            all = Sector.objects.filter(bool_Sc_eliminado=False)
            arg = {"eliminado":eliminado, "sectores":all}

            return render(request, 'Sector/index.html', arg)

class nagView(View):

    def index(request):
        all = Nivel_Area_Geografica.objects.filter(bool_NG_Eliminado=False)
        arg = {"nags":all}
        return render(request, 'Nag/index.html', arg)

    def show(request,id):
        nag = Nivel_Area_Geografica.objects.get(id_Nivel_Area=id)
        arg = {"nag":nag}
        return render(request, 'Nag/show.html', arg)

    def new(request):
        return render(request, 'Nag/new.html')

    def create(request):
        form = NAGForm(request.POST)
        if form.is_valid():
            form.save()
            all = Nivel_Area_Geografica.objects.filter(bool_NG_Eliminado=False)
            args = {
                "nags":all
                }
            return render(request, 'Nag/index.html', args )
        else:
            args = {
                'form': form
                }
            return render (request, 'Nag/new.html', args )

    def edit(request,id):
        nag = Nivel_Area_Geografica.objects.get(id_Nivel_Area=id)
        arg = {"nag":nag}
        return render(request, 'Nag/edit.html', arg)

    def update(request,id):
        nag = Nivel_Area_Geografica.objects.get(id_Nivel_Area=id)
        form = NAGForm(request.POST, instance=nag)
        if form.is_valid():
            form.save()
            aviso = "Se han actualizado los datos"
            args = {
                "aviso":aviso,
                "form":form,
                "nag":nag
            }
            return render(request, 'Nag/edit.html', args)
        else:
            nag = Nivel_Area_Geografica.objects.get(id_Nivel_Area=id)
            args = {
                "form":form,
                "nag":nag
            }
            return render(request, 'Nag/edit.html',args).objects.get(id_Nivel_Area=id)
        
    def delete(request,id):
        nag = Nivel_Area_Geografica.objects.get(id_Nivel_Area=id)
        nag.bool_NG_Eliminado = True
        nag.save()
        eliminado = "El Nivel de Área geográfica se ha eliminado"
        all = Nivel_Area_Geografica.objects.filter(bool_NG_Eliminado=False)

        return render(request, 'Nag/index.html', {"eliminado":eliminado, "nags":all})