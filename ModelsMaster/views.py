from django.shortcuts import render, redirect
from django.views import View
from .forms import AmbitoForm, TipoObjetivoForm, EstructuraForm, RiesgoForm, TipoIntervinienteForm, SectorForm, NivelAreaGeograficaForm, AreaGeograficaForm, EmpresaForm, ModeloForm, BenchmarkingForm, PuntosCapituloForm, ObjetivoForm, ObjetivoRelacionadoForm
from .models import Ambito, TipoObjetivo, Estructura, Riesgo, TipoInterviniente,Sector, NivelAreaGeografica, AreaGeografica, Empresa, Modelo, Benchmarking, PuntosCapitulo, Objetivo, ObjetivoRelacionado

# Create your views here.
def index(request):
    return render(request, 'index.html')

class AmbitoView(View):
    def index(request):
        all = Ambito.objects.filter(bool_am_eliminado=False)
        args = {
            "ambitos":all
        }
        return render(request, 'Ambitos/index.html', args)

    def show(request,id):
        ambito = Ambito.objects.get(id_am=id)
        args = {
            "ambito":ambito
        }
        return render(request, 'Ambitos/show.html', args)
    
    def new(request):
        return render(request,'Ambitos/new.html')

    def create(request):
        form = AmbitoForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "El ambito se ha creado con éxito"
            all = Ambito.objects.filter(bool_am_eliminado=False)
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
        ambito = Ambito.objects.get(id_am=id)
        args = {
            "ambito":ambito
            }
        return render(request, 'Ambitos/edit.html', args)

    def update(request,id):
        ambito = Ambito.objects.get(id_am=id)
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
            ambito = Ambito.objects.get(id_am=id)
            args = {
                "form":form,
                "ambito":ambito
            }
            return render(request, 'Ambitos/edit.html',args)

    def delete(request,id):
        ambito = Ambito.objects.get(id_am=id)
        all = Ambito.objects.filter(bool_am_eliminado=False)
        try:
            am_pc = PuntosCapitulo.objects.filter(id_pc_am=ambito.id_am)
        except AttributeError:
            am_pc = "nope"
        if am_pc != "nope":
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "ambitos":all
            }
        else:
            ambito.bool_am_eliminado = True
            ambito.save()
            eliminado = "El ambito se ha eliminado"
            all = Ambito.objects.filter(bool_am_eliminado=False)
            args = {
                "eliminado":eliminado,
                "ambitos":all
            }
        return render(request, 'Ambitos/index.html', args)

class TipoObjetivoView(View):
    def index(request):
        all = TipoObjetivo.objects.filter(bool_to_eliminado=False)
        args = {
            "tipos_objetivos":all
        }
        return render(request, 'TipoObjetivo/index.html', args)

    def show(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_to=id)
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
            aviso = "El tipo objetivo se ha creado con éxito"
            all = TipoObjetivo.objects.filter(bool_to_eliminado=False)
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
        tipo_objetivo = TipoObjetivo.objects.get(id_to=id)
        args = {
            "tipo_objetivo":tipo_objetivo
        }
        return render(request, 'TipoObjetivo/edit.html', args)

    def update(request,id):
        tipo_objetivo = TipoObjetivo.objects.get(id_to=id)
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
        tipo_objetivo = TipoObjetivo.objects.get(id_to=id)
        tipo_objetivo.bool_to_eliminado = True
        tipo_objetivo.save()
        eliminado = "El tipo objetivo se ha eliminado"
        all = TipoObjetivo.objects.filter(bool_to_eliminado=False)
        args = {
            "eliminado":eliminado,
            "tipos_objetivos":all
        }
        return render(request, 'TipoObjetivo/index.html', args)

class EstructuraView(View):
    def index(request):
        all = Estructura.objects.filter(bool_est_eliminado=False)
        args = {
            "estructuras":all
        }
        return render(request, 'Estructura/index.html', args)

    def show(request,id):
        estructura = Estructura.objects.get(id_est=id)
        args = {
            "estructura":estructura
        }
        return render(request, 'Estructura/show.html', args)

    def new(request):
        return render(request, 'Estructura/new.html')

    def create(request):
        form = EstructuraForm(request.POST)
        if form.is_valid():
            form.save()
            aviso = "La estructura se ha creado con éxito"
            all = Estructura.objects.filter(bool_est_eliminado=False)
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
        estructura = Estructura.objects.get(id_est=id)
        args = {
            "estructura": estructura
        }
        return render(request, 'Estructura/edit.html', args)

    def update(request,id):
        estructura = Estructura.objects.get(id_est=id)
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
        estructura = Estructura.objects.get(id_est=id)
        estructura.bool_est_eliminado = True
        estructura.save()
        eliminado = "El tipo objetivo se ha eliminado"
        all = Estructura.objects.filter(bool_est_eliminado=False)
        args = {
            "eliminado":eliminado,
            "estructuras":all
        }
        return render(request, 'Estructura/index.html', args)

class RiesgoView(View):
    def index(request):
        all = Riesgo.objects.filter(bool_rg_eliminado=False)
        args = {
            "riesgos":all
        }
        return render(request, 'Riesgo/index.html', args)

    def show(request,id):
        riesgo = Riesgo.objects.get(id_rg=id)
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
            all = Riesgo.objects.filter(bool_rg_eliminado=False)
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
        riesgo = Riesgo.objects.get(id_rg=id)
        args = {
            "riesgo":riesgo
        }
        return render(request, 'Riesgo/edit.html', args)

    def update(request,id):
        riesgo = Riesgo.objects.get(id_rg=id)
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
        riesgo = Riesgo.objects.get(id_rg=id)
        riesgo.bool_rg_eliminado = True
        riesgo.save()
        all = Riesgo.objects.filter(bool_rg_eliminado=False)
        eliminado = "El riesgo se ha eliminado"
        args = {
            "eliminado":eliminado,
            "riesgos":all
        }
        return render(request, 'Riesgo/index.html', args)

class TipoIntervinienteView(View):

    def index(request):
        all = TipoInterviniente.objects.filter(bool_ti_eliminado=False)
        args = {
            "tipo_intervinientes":all
        }
        return render(request, 'TipoInterviniente/index.html', args)

    def show(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(id_ti=id)
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
            all = TipoInterviniente.objects.filter(bool_ti_eliminado=False)
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
        tipo_interviniente = TipoInterviniente.objects.get(id_ti=id)
        args = {
            "tipo_interviniente":tipo_interviniente
        }
        return render(request, 'TipoInterviniente/edit.html', args)

    def update(request,id):
        tipo_interviniente = TipoInterviniente.objects.get(id_ti=id)
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
        tipo_interviniente = TipoInterviniente.objects.get(id_ti=id)
        tipo_interviniente.bool_ti_eliminado = True
        tipo_interviniente.save()
        eliminado = "El tipo Interviniente se ha eliminado"
        all = TipoInterviniente.objects.filter(bool_ti_eliminado=False)
        args = {
            "eliminado":eliminado,
            "tipo_intervinientes":all
        }
        return render(request, 'TipoInterviniente/index.html', args)

class SectorView(View):

    def index(request):
        all = Sector.objects.filter(bool_sc_eliminado=False)
        args = {
            "sectores":all
        }
        return render(request, 'Sector/index.html', args)

    def show(request,id):
        sector = Sector.objects.get(id_sc=id)
        args = {
            "sector":sector
        }
        return render(request, 'Sector/show.html', args)

    def new(request):
        return render(request, 'Sector/new.html')

    def create(request):
        ModelForm_form = SectorForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El sector se ha creado con éxito!"
            all = Sector.objects.filter(bool_sc_eliminado=False)
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
        sector = Sector.objects.get(id_sc=id)
        args = {
            "sector":sector
        }
        return render(request, 'Sector/edit.html', args)

    def update(request,id):
        sector = Sector.objects.get(id_sc=id)
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
        all = Sector.objects.filter(bool_sc_eliminado=False)
        sector = Sector.objects.get(id_sc=id)
        try:
            sc_emp = Empresa.objects.filter(id_emp_sc=sector.id_sc)
        except AttributeError:
            sc_emp = "nope"
        try:
            sc_bench = Benchmarking.objects.filter(id_bench_sc=sector.id_sc)
        except AttributeError:
            sc_bench = "nope"

        if sc_emp != "nope" or sc_bench != "nope":
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "sectores":all
            }
        else:
            sector.bool_sc_eliminado = True
            sector.save()
            eliminado = "El sector se ha eliminado"
            all = Sector.objects.filter(bool_sc_eliminado=False)
            args = {
                "eliminado":eliminado,
                "sectores":all
            }
        return render(request, 'Sector/index.html', args)

class NivelAreaGeograficaView(View):
    def index(request):
        all = NivelAreaGeografica.objects.filter(bool_nag_eliminado=False)
        args = {
            "nags":all
        }
        return render(request, 'Nag/index.html', args)

    def show(request,id):
        nag = NivelAreaGeografica.objects.get(id_nag=id)
        args = {
            "nag":nag
        }
        return render(request, 'Nag/show.html', args)

    def new(request):
        return render(request, 'Nag/new.html')

    def create(request):
        ModelForm_form = NivelAreaGeograficaForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Nivel de Área geográfica se ha creado con éxito!"
            all = NivelAreaGeografica.objects.filter(bool_nag_eliminado=False)
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
        nag = NivelAreaGeografica.objects.get(id_nag=id)
        args = {
            "nag":nag
        }
        return render(request, 'Nag/edit.html', args)

    def update(request,id):
        nag = NivelAreaGeografica.objects.get(id_nag=id)
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
        all = NivelAreaGeografica.objects.filter(bool_nag_eliminado=False)
        nag = NivelAreaGeografica.objects.get(id_nag=id)
        try:
            nag_ag = AreaGeografica.objects.filter(id_ag_nag=nag.id_nag)
        except AttributeError:
            nag_ag = "nope"
        if nag_ag != "nope":
            args = {
                "eliminado":"No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "nags":all
            }
        else:
            nag.bool_nag_eliminado = True
            nag.save()
            eliminado = "El Nivel de Área geográfica se ha eliminado"
            all = NivelAreaGeografica.objects.filter(bool_nag_eliminado=False)
            args = {
                "eliminado":eliminado,
                "nags":all
            }
        return render(request, 'Nag/index.html', args)

class AreaGeograficaView(View):
    def index(request):
        all = AreaGeografica.objects.filter(bool_ag_eliminado=False)
        args = {
            "ags":all
        }
        return render(request, 'AreaGeografica/index.html', args)

    def show(request,id):
        ag = AreaGeografica.objects.get(id_ag=id)
        try:
            ag_parent = AreaGeografica.objects.get(id_ag=ag.id_ag_parent.id_ag)
        except AttributeError:
            ag_parent = "nope"
        args = {
            "ag":ag,
            "ag_parent":ag_parent
        }
        return render(request, 'AreaGeografica/show.html', args)

    def new(request):
        nags = NivelAreaGeografica.objects.filter(bool_nag_eliminado=False)
        ags = AreaGeografica.objects.filter(bool_ag_eliminado=False)
        args ={
            "nags":nags,
            "ags":ags
        }
        return render(request, 'AreaGeografica/new.html', args)

    def create(request):
        ModelForm_form = AreaGeograficaForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Área geográfica se ha creado con éxito!"
            all = AreaGeografica.objects.filter(bool_ag_eliminado=False)
            args = {
                "aviso":aviso,
                "ags":all
            }
            return render(request, 'AreaGeografica/index.html', args)
        else:
            nags = NivelAreaGeografica.objects.filter(bool_nag_eliminado=False)
            ags = AreaGeografica.objects.filter(bool_ag_eliminado=False)
            args = {
                "form":ModelForm_form,
                "nags":nags,
                "ags":ags
            }
            return render(request, 'AreaGeografica/new.html', args)

    def edit(request,id):
        nags = NivelAreaGeografica.objects.filter(bool_nag_eliminado=False)
        ag = AreaGeografica.objects.get(id_ag=id)
        ags = AreaGeografica.objects.filter(bool_ag_eliminado=False)
        args = {
            "ag":ag,
            "nags":nags,
            "ags":ags
        }
        return render(request, 'AreaGeografica/edit.html', args)

    def update(request,id):
        ag = AreaGeografica.objects.get(id_ag=id)
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
        all = AreaGeografica.objects.filter(bool_ag_eliminado=False)
        ag = AreaGeografica.objects.get(id_ag=id)
        try:
            ag_parent = AreaGeografica.objects.filter(id_ag_parent=ag.id_ag)
        except AttributeError:
            ag_parent = "nope"
        try:
            bench_ag = Benchmarking.objects.filter(id_bench_ag=ag.id_ag)
        except AttributeError:
            bench_ag = "nope"
        try:
            emp_ag = Empresa.objects.filter(id_emp_ag=ag.id_ag)
        except AttributeError:
            emp_ag = "nope"
        if ag_parent != "nope" or bench_ag != "nope" or emp_ag != "nope":
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "ags":all
            }
        else:
            ag.bool_ag_eliminado = True
            ag.save()
            eliminado = "El Área geográfica se ha eliminado"
            all = AreaGeografica.objects.filter(bool_ag_eliminado=False)
            args = {
                "eliminado":eliminado,
                "ags":all
            }
        return render(request, 'AreaGeografica/index.html', args)

class EmpresaView(View):
    def index(request):
        all = Empresa.objects.filter(bool_emp_eliminado=False)
        args = {
            "emps":all
        }
        return render(request, 'Empresa/index.html', args)
    
    def show(request,id):
        emp = Empresa.objects.get(id_emp=id)
        emp_ag = AreaGeografica.objects.get(id_ag=emp.id_emp_ag.id_ag)
        emp_sc = Sector.objects.get(id_sc=emp.id_emp_sc.id_sc)
        args = {
            "emp":emp,
            "emp_ag":emp_ag,
            "emp_sc":emp_sc
        }
        return render(request, 'Empresa/show.html', args)

    def new(request):
        emp_scs = Sector.objects.filter(bool_sc_eliminado=False)
        emp_ags = AreaGeografica.objects.filter(bool_ag_eliminado=False)
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
            all = Empresa.objects.filter(bool_emp_eliminado=False)
            args = {
                "aviso":aviso,
                "emps":all
            }
            return render(request, 'Empresa/index.html', args)
        else:
            emp_scs = Sector.objects.filter(bool_sc_eliminado=False)
            emp_ags = AreaGeografica.objects.filter(bool_ag_eliminado=False)
            args = {
                "form":ModelForm_form,
                "emp_scs":emp_scs,
                "emp_ags":emp_ags
            }
            return render(request, 'Empresa/new.html', args)
    def edit(request,id):
        emp_scs = Sector.objects.filter(bool_sc_eliminado=False)
        emp = Empresa.objects.get(id_emp=id)
        emp_ags = AreaGeografica.objects.filter(bool_ag_eliminado=False)
        args = {
            "emp":emp,
            "emp_ags":emp_ags,
            "emp_scs":emp_scs
        }
        return render(request, 'Empresa/edit.html', args)
    
    def update(request,id):
        emp = Empresa.objects.get(id_ag=id)
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
        all = Empresa.objects.filter(bool_emp_eliminado=False)
        emp = Empresa.objects.get(id_emp=id)
        try:
            md_emp = Modelo.objects.filter(id_md_emp=emp.id_emp)
        except AttributeError:
            md_emp = "nope"
        if md_emp != "nope":
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "emps":all
            }
        else:
            emp.bool_emp_eliminado = True
            emp.save()
            eliminado = "la empresa se ha eliminado"
            all = Empresa.objects.filter(bool_emp_eliminado=False)
            args = {
                "eliminado":eliminado,
                "emps":all
            }
        return render(request, 'Empresa/index.html', args)

class ModeloView(View):

    def index(request):
        all=Modelo.objects.filter(bool_md_eliminado=False)
        args= {"modelos":all}

        return render(request, 'Modelo/index.html', args)
    
    def show(request,id):
        modelo = Modelo.objects.get(id_md=id)
        modelo_emp = Empresa.objects.get(id_emp=modelo.id_md_emp.id_emp)
        args = {
            "modelo":modelo,
            "modelo_emp":modelo_emp,
        }
        return render(request, 'Modelo/show.html', args)
    
    def new(request):
        modelo_emps = Empresa.objects.filter(bool_emp_eliminado=False)
        args = {
            "modelo_emps":modelo_emps,
        }
        return render(request, 'Modelo/new.html', args)

    def create(request):
        ModelForm_form = ModeloForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Modelo se ha creado con éxito!"
            all = Modelo.objects.filter(bool_md_eliminado=False)
            args = {
                "aviso":aviso,
                "modelos":all
            }
            return render(request, 'Modelo/index.html', args)
        else:
            modelo_emps = Empresa.objects.filter(bool_emp_eliminado=False)
            args = {
                "form":ModelForm_form,
                "modelo_emps":modelo_emps,
            }
            return render(request, 'Modelo/new.html', args)

    def edit(request,id):
        modelo_emps = Empresa.objects.filter(bool_emp_eliminado=False)
        modelo = Modelo.objects.get(id_md=id)
        args = {
            "modelo":modelo,
            "modelo_emps":modelo_emps,
        }
        return render(request, 'Modelo/edit.html', args)
    
    def update(request,id):
        modelo = Modelo.objects.get(id_md=id)
        ModelForm_form = ModeloForm(request.POST, instance=modelo)
        modelo_emps = Empresa.objects.filter(bool_emp_eliminado=False)
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
        all = Modelo.objects.filter(bool_md_eliminado=False)
        modelo = Modelo.objects.get(id_md=id)
        try:
            pc_md = PuntosCapitulo.objects.filter(id_pc_md=modelo.id_md)
        except AttributeError:
            pc_md = "nope"
        if pc_md != "nope":
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "modelos":all
            }
        else:
            modelo.bool_md_eliminado = True
            modelo.save()
            eliminado = "El Modelo se ha eliminado"
            all = Modelo.objects.filter(bool_md_eliminado=False)
            args = {
                "eliminado":eliminado,
                "modelos":all
            }
        return render(request, 'Modelo/index.html', args)
            
class BenchmarkingView(View):
    def index(request):
        all = Benchmarking.objects.filter(bool_bench_eliminado=False)
        args = {
            "benchs":all
        }
        return render(request, 'Benchmarking/index.html', args)
    
    def show(request,id):
        bench = Benchmarking.objects.get(id_bench=id)
        bench_ag = AreaGeografica.objects.get(id_ag=bench.id_bench_ag.id_ag)
        bench_sc = Sector.objects.get(id_sc=bench.id_bench_sc.id_sc)
        args = {
            "bench":bench,
            "bench_ag":bench_ag,
            "bench_sc":bench_sc
        }
        return render(request, 'Benchmarking/show.html', args)

    def new(request):
        bench_scs = Sector.objects.filter(bool_sc_eliminado=False)
        bench_ags = AreaGeografica.objects.filter(bool_ag_eliminado=False)
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
            all = Benchmarking.objects.filter(bool_bench_eliminado=False)
            args = {
                "aviso":aviso,
                "benchs":all
            }
            return render(request, 'Benchmarking/index.html', args)
        else:
            bench_scs = Sector.objects.filter(bool_sc_eliminado=False)
            bench_ags = AreaGeografica.objects.filter(bool_ag_eliminado=False)
            args = {
                "form":ModelForm_form,
                "bench_scs":bench_scs,
                "bench_ags":bench_ags
            }
            return render(request, 'Benchmarking/new.html', args)
    def edit(request,id):
        bench_scs = Sector.objects.filter(bool_sc_eliminado=False)
        bench = Benchmarking.objects.get(id_bench=id)
        bench_ags = AreaGeografica.objects.filter(bool_ag_eliminado=False)
        args = {
            "bench":bench,
            "bench_ags":bench_ags,
            "bench_scs":bench_scs
        }
        return render(request, 'Benchmarking/edit.html', args)
    
    def update(request,id):
        bench = Benchmarking.objects.get(id_bench=id)
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
        bench = Benchmarking.objects.get(id_bench=id)
        bench.bool_bench_eliminado = True
        bench.save()
        eliminado = "El benchmarking se ha eliminado"
        all = Benchmarking.objects.filter(bool_bench_eliminado=False)
        args = {
            "eliminado":eliminado,
            "benchs":all
        }
        return render(request, 'Benchmarking/index.html', args)

class PuntosCapituloView(View):

    def index(request):
       all=PuntosCapitulo.objects.filter(bool_pc_eliminado=False) 
       args = {
           "pcs":all
       }
       return render(request, 'PuntosCapitulo/index.html', args)

    def show(request,id):
        pc = PuntosCapitulo.objects.get(id_pc=id)
        pc_modelo = Modelo.objects.get(id_md=pc.id_pc_md.id_md)
        pc_ambito = Ambito.objects.get(id_am=pc.id_pc_am.id_am)
        args = {
            "pc":pc,
            "pc_modelo":pc_modelo,
            "pc_ambito":pc_ambito
        }
        return render(request, 'PuntosCapitulo/show.html', args)

    def new(request):
        pc_modelos = Modelo.objects.filter(bool_md_eliminado=False)
        pc_ambitos = Ambito.objects.filter(bool_am_eliminado=False)
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
            all = PuntosCapitulo.objects.filter(bool_pc_eliminado=False)
            args = {
                "aviso":aviso,
                "pcs":all
            }
            return render(request, 'PuntosCapitulo/index.html', args)
        else:
            pc_modelos = Modelo.objects.filter(bool_md_eliminado=False)
            pc_ambitos = Ambito.objects.filter(bool_am_eliminado=False)
            args = {
                "form":ModelForm_form,
                "pc_modelos":pc_modelos,
                "pc_ambitos":pc_ambitos
            }
            return render(request, 'PuntosCapitulo/new.html', args)

    def edit(request,id):
        pc_modelos = Modelo.objects.filter(bool_md_eliminado=False)
        pc = PuntosCapitulo.objects.get(id_pc=id)
        pc_ambitos = Ambito.objects.filter(bool_am_eliminado=False)
        args = {
            "pc":pc,
            "pc_modelos":pc_modelos,
            "pc_ambitos":pc_ambitos
        }
        return render(request, 'PuntosCapitulo/edit.html', args)

    def update(request,id):
        pc = PuntosCapitulo.objects.get(id_pc=id)
        ModelForm_form = PuntosCapituloForm(request.POST, instance=pc)
        pc_ambitos = Ambito.objects.filter(bool_am_eliminado=False)
        pc_modelos = Modelo.objects.filter(bool_md_eliminado=False)
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
        all = PuntosCapitulo.objects.filter(bool_pc_eliminado=False)
        pc = PuntosCapitulo.objects.get(id_pc=id)
        try:
            Ob_pc = Objetivo.objects.filter(id_ob_pc=pc.id_pc)
        except AttributeError:
            ob_pc = "nope"
        if ob_pc != "nope":
            args = {
                "eliminado": "No puedes borrar este elemento porque otros dependen de él, borralos primero",
                "pcs":all
            }
        else:
            pc.bool_pc_eliminado = True
            pc.save()
            eliminado = "El PuntoCapitulo se ha eliminado"
            all = PuntosCapitulo.objects.filter(bool_pc_eliminado=False)
            args = {
                "eliminado":eliminado,
                "pcs":all
            }
        return render(request, 'PuntosCapitulo/index.html', args)
        
class ObjetivoView(View):

    def index(request):
       all=Objetivo.objects.filter(bool_ob_eliminado=False) 
       args = {
           "objs":all
       }
       return render(request, 'Objetivo/index.html', args)

    def show(request,id):
        obj = Objetivo.objects.get(id_ob=id)
        obj_pc = PuntosCapitulo.objects.get(id_pc=obj.id_ob_pc.id_pc)
        obj_to = TipoObjetivo.objects.get(id_to=obj.id_ob_to.id_to)
        args = {
            "obj":obj,
            "obj_pc":obj_pc,
            "obj_to":obj_to
        }
        return render(request, 'Objetivo/show.html', args)

    def new(request):
        obj_pcs = PuntosCapitulo.objects.filter(bool_pc_eliminado=False)
        obj_tos = TipoObjetivo.objects.filter(bool_to_eliminado=False)
        args = {
            "obj_pcs":obj_pcs,
            "obj_tos":obj_tos
        }
        return render(request, 'Objetivo/new.html', args)
    
    def create(request):
        ModelForm_form = ObjetivoForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Objetivo se ha creado con éxito!"
            all = Objetivo.objects.filter(bool_ob_eliminado=False)
            args = {
                "aviso":aviso,
                "objs":all
            }
            return render(request, 'Objetivo/index.html', args)
        else:
            obj_pcs = PuntosCapitulo.objects.filter(bool_pc_eliminado=False)
            obj_tos = TipoObjetivo.objects.filter(bool_to_eliminado=False)
            args = {
                "form":ModelForm_form,
                "obj_pcs":obj_pcs,
                "obj_tos":obj_tos
            }
            return render(request, 'Objetivo/new.html', args)

    def edit(request,id):
        obj_pcs = PuntosCapitulo.objects.filter(bool_pc_eliminado=False)
        obj = Objetivo.objects.get(id_ob=id)
        obj_tos = TipoObjetivo.objects.filter(bool_to_eliminado=False)
        args = {
            "obj":obj,
            "obj_pcs":obj_pcs,
            "obj_tos":obj_tos
        }
        return render(request, 'Objetivo/edit.html', args)

    def update(request,id):
        obj = Objetivo.objects.get(id_ob=id)
        ModelForm_form = ObjetivoForm(request.POST, instance=obj)
        obj_tos = TipoObjetivo.objects.filter(bool_to_eliminado=False)
        obj_pcs = PuntosCapitulo.objects.filter(bool_pc_eliminado=False)
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
        obj = Objetivo.objects.get(id_ob=id)
        obj.bool_ob_eliminado = True
        obj.save()
        eliminado = "El Objetivo se ha eliminado"
        all = Objetivo.objects.filter(bool_ob_eliminado=False)
        args = {
            "eliminado":eliminado,
            "objs":all
        }
        return render(request, 'Objetivo/index.html', args)

""" class ObjetivoRelacionadoView(View):

    def index(request):
       all=ObjetivoRelacionado.objects.filter(bool_or_eliminado=False) 
       args = {
           "or1s":all
       }
       return render(request, 'ObjetivoRelacionado/index.html', args)

    def show(request,id):
        or1=ObjetivoRelacionado.objects.get(id_or=id)
        or1_ob = Objetivo.objects.get(id_ob=or1.id_or_ob.id_ob)
        or1_oba = Objetivo.objects.get(id_ob=or1.id_or_ob_asociado.id_ob)
        args = {
            "or1":or1,
            "or1_ob":or1_ob,
            "or1_oba":or1_oba
        }
        return render(request, 'ObjetivoRelacionado/show.html', args)

    def new(request):
        or1_obs = Objetivo.objects.filter(bool_ob_eliminado=False)
        or1_obas = Objetivo.objects.filter(bool_ob_eliminado=False)
        args = {
            "or1_obs":or1_obs,
            "or1_obas":or1_obas
        }
        return render(request, 'ObjetivoRelacionado/new.html', args)
    
    def create(request):
        ModelForm_form = ObjetivoRelacionadoForm(request.POST)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "El Objetivo Relacionado se ha creado con éxito!"
            all = ObjetivoRelacionado.objects.filter(bool_or_eliminado=False)
            args = {
                "aviso":aviso,
                "or1s":all
            }
            return render(request, 'ObjetivoRelacionado/index.html', args)
        else:
            or1_obs = Objetivo.objects.filter(bool_ob_eliminado=False)
            or1_obas = Objetivo.objects.filter(bool_ob_eliminado=False)
            args = {
                "form":ModelForm_form,
                "or1_obs":or1_obs,
                "or1_obas":or1_obas
            }
            return render(request, 'ObjetivoRelacionado/new.html', args)

    def edit(request,id):
        or1_obs = Objetivo.objects.filter(bool_ob_eliminado=False)
        or1 = ObjetivoRelacionado.objects.get(id_or=id)
        or1_obas = Objetivo.objects.filter(bool_ob_eliminado=False)
        args = {
            "or1":or1,
            "or1_obs":or1_obs,
            "or1_obas":or1_obas
        }
        return render(request, 'ObjetivoRelacionado/edit.html', args)

    def update(request,id):
        or1 = ObjetivoRelacionado.objects.get(id_or=id)
        ModelForm_form = ObjetivoRelacionadoForm(request.POST, instance=or1)
        or1_obs = Objetivo.objects.filter(bool_ob_eliminado=False)
        or1_obas = Objetivo.objects.filter(bool_ob_eliminado=False)
        if ModelForm_form.is_valid():
            ModelForm_form.save()
            aviso = "Los datos se han actualizado con éxito"
            args = {
                "aviso":aviso,
                "or1":or1,
                "or1_obs":or1_obs,
                "or1_obas":or1_obas
            }
        else:
            args = {
                "form":ModelForm_form,
                "or1":or1,
                "or1_obs":or1_obs,
                "or1_obas":or1_obas
            }
        return render(request, 'ObjetivoRelacionado/edit.html', args)
    
    def delete(request,id):
        or1 = ObjetivoRelacionado.objects.get(id_or=id)
        or1.bool_or_eliminado = True
        or1.save()
        eliminado = "El Objetivo relacionado se ha eliminado"
        all = ObjetivoRelacionado.objects.filter(bool_or_eliminado=False)
        args = {
            "eliminado":eliminado,
            "or1s":all
        }
        return render(request, 'ObjetivoRelacionado/index.html', args)

 """