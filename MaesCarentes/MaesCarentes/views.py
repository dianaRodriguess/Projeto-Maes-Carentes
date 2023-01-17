from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from datetime import datetime
from MaesCarentes.forms import *
from MaesCarentes.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def inicio(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("/funcionario")
        else:
            return redirect("/apoiador")
    
    return render(request, "maec/index.html")

def createApoiador(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect("/funcionario")
            else:
                return redirect("/apoiador")
        return render(request, "maec/registrar.html")
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        nome = request.POST.get('nome')

        user = Usuarios.objects.filter(email=email).first()

        if user :
            messages.warning(request, 'Email inválido, tente outro')
            return redirect("/registrar")

        user = Usuarios.objects.create_user(username=email, email=email, password=senha, first_name=nome)

        return redirect("/login")
    
def loginApoiador(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect("/funcionario")
            else:
                return redirect("/apoiador")
        return render(request, "maec/login.html")
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(username=email, password=senha)

        if user :
            login(request, user)
            return redirect('/funcionario')
        else:
            messages.warning(request, 'Email ou senha inválidos, tente novamente')
            return redirect("/login")

def logout_views(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(inicio)
    
    return render(request, "maec/index.html")

def apoiador(request):
    if request.user.is_authenticated:
        return render(request, "maec/apoiador.html")
    return redirect(inicio)

def forms_pro(request):
    if request.user.is_authenticated:
        formProduto = ProdutoForm(request.POST or None)
        if formProduto.is_valid() :
            new_produto = DoacaoItem.objects.create(
                apoiador_id = Usuarios.objects.get(pk=request.user.id),
                nome = formProduto.cleaned_data["nome"],
                estado = formProduto.cleaned_data["estado"],
                quantidade = formProduto.cleaned_data["quantidade"],
                confirmacao = False,
            )
            new_produto.save()
            return redirect("/doar_produto/")

        pacote = {"formProduto": formProduto}
        return render(request, "maec/forms_pro.html", pacote)

    return redirect(inicio)

def doar(request):
    if request.user.is_authenticated:
        formDinheiro = DinheiroForm(request.POST or None)
        if formDinheiro.is_valid() :
            new_produto = DoacaoDinheiro.objects.create(
                apoiador_id = Usuarios.objects.get(pk=request.user.id),
                valor = formDinheiro.cleaned_data["valor"],
                forma = formDinheiro.cleaned_data["forma"],
                confirmacao = False,
            )
            new_produto.save()
            return redirect("/doar/")

        pacote = {"formDinheiro": formDinheiro}
        return render(request, "maec/doar.html", pacote)

def doacoes(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            produto = DoacaoItem.objects.all()
            dinheiro = DoacaoDinheiro.objects.all()
            pacote = {"produtos": produto, "dinheiro": dinheiro}
            return render(request, "maec/doacoes.html", pacote)
        
        return redirect(inicio)
    
def d_conf_pro(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            formProduto = DoacaoItem.objects.get(pk=id)
            formProduto.confirmacao = True
            formProduto.data = datetime.now()
            formProduto.save()

            return redirect("/doacoes_confirmadas")

        return render(request, "maec/doacoes_confirmadas")

def d_conf_din(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            formDinheiro = DoacaoDinheiro.objects.get(pk=id)
            formDinheiro.confirmacao = True
            formDinheiro.data = datetime.now()
            formDinheiro.save()

            return redirect("/doacoes_confirmadas")
            
        return render(inicio)

def d_conf(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            produto = DoacaoItem.objects.all()
            dinheiro = DoacaoDinheiro.objects.all()
            pacote = {"produtos": produto, "dinheiro": dinheiro}
            return render(request, "maec/d_confirmadas.html", pacote)

        return redirect(inicio)   

def delete_d_pro(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            produto = DoacaoItem.objects.get(pk=id)
            produto.delete()
            return redirect("/doacoes")

def delete_d_din(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            dinheiro = DoacaoDinheiro.objects.get(pk=id)
            dinheiro.delete()
            return redirect("/doacoes")
    
def funcionario(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return render(request, "maec/funcionario.html")
    return redirect(inicio)


#------------ Eventos -----------

def forms_evento(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            formEvento = EventoForm(request.POST or None)
            if formEvento.is_valid() :
                new_evento = Evento.objects.create(
                    mae = Mae.objects.get(pk=id),
                    dinheiro = formEvento.cleaned_data["dinheiro"],
                    produto = formEvento.cleaned_data["produto"],
                    descricao = formEvento.cleaned_data["descricao"],
                )
                new_evento.save()
                if new_evento.dinheiro != None:
                    formDinheiro = DoacaoDinheiro.objects.get(pk=new_evento.dinheiro.id)
                    formDinheiro.doado = True
                    formDinheiro.save()
                if new_evento.produto != None:
                    formProduto = DoacaoItem.objects.get(pk=new_evento.produto.id)
                    formProduto.doado = True
                    formProduto.save()
                    
                return redirect("/ver_maes")

            pacote = {"formEvento": formEvento}
            return render(request, "maec/forms_evento.html", pacote)

def eventos(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            mae = Mae.objects.get(pk=id)
            evento = Evento.objects.filter(mae=mae)
            pacote = {"eventos": evento, "maes": mae}
            return render(request, "maec/eventos.html", pacote)

def delete_eventoprod(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            evento = Evento.objects.get(pk=id)
            if evento.produto != None :
                formProduto = DoacaoItem.objects.get(pk=evento.produto.id)
                formProduto.doado = False
                evento.produto = None
                formProduto.save()

            evento.save()
            return redirect('/ver_maes') 

def delete_eventodin(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            evento = Evento.objects.get(pk=id)
            if evento.dinheiro != None :
                formDinheiro = DoacaoDinheiro.objects.get(pk=evento.dinheiro.id)
                formDinheiro.doado = False
                evento.dinheiro = None
                formDinheiro.save()

            evento.save()
            return redirect('/ver_maes') 


#------------- Maes -----------------

def tabela_m(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            mae = Mae.objects.all()
            pacote = {"maes": mae}
            return render(request, "maec/tabela_maes.html", pacote)

def forms_mae(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            formMae = MaeForm(request.POST or None)
            if formMae.is_valid() :
                formMae.save()
                return redirect("/ver_maes/")

            pacote = {"formMae": formMae}
            return render(request, "maec/forms_mae.html", pacote)

def updateforms_mae(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            mae = Mae.objects.get(pk=id)
            formMae = MaeForm(request.POST or None, instance=mae)
            if formMae.is_valid() :
                formMae.save()
                return redirect("/ver_maes/")    

            pacote = {"formMae": formMae}
            return render(request, "maec/forms_mae.html/", pacote)

def delete_mae(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            mae = Mae.objects.get(pk=id)
            mae.delete()
            return redirect("/ver_maes/")

def mae(request, id):
    if request.user.is_authenticated:
        if request.user.is_staff:
            mae = Mae.objects.get(pk=id)
            pacote = {"maes": mae}
            return render(request, "maec/mae_perfil.html", pacote)



