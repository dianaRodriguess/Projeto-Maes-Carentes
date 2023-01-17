"""projetom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MaesCarentes.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="url_inicio"),
    path('registrar/', createApoiador, name="url_registrar"),
    path('login/', loginApoiador, name="url_login"),
    path('index.html', logout_views, name="url_logout"),
    path('apoiador/', apoiador, name="url_apoiador"),
    path('funcionario/', funcionario, name="url_funcionario"),
    path('cadastrar_evento/<int:id>', forms_evento, name="url_cadastrar_evento"),
    path('ver_maes/', tabela_m, name="url_ver_maes"),
    path('eventos/<int:id>', eventos, name="url_eventos"),
    path('delete_eventodin/<int:id>', delete_eventodin, name="url_delete_eventodin"),
    path('delete_eventoprod/<int:id>', delete_eventoprod, name="url_delete_eventoprod"),
    path('cadastrar_mae/', forms_mae, name="url_cadastrar_mae"),
    path('atualizar_mae/<int:id>', updateforms_mae, name="url_atualizar_mae"),
    path('delete_mae/<int:id>', delete_mae, name="url_delete_mae"),
    path('doar_produto/', forms_pro, name="url_doar_produto"),
    path('doar/', doar, name="url_doar"),
    path('mae/<int:id>', mae, name="url_Mperfil"),
    path('doacoes/', doacoes, name="url_doacoes"),
    path('doacoes_confirmadas/', d_conf, name="url_d_conf"),
    path('produtos_confirmados/<int:id>', d_conf_pro, name="url_d_conf_pro"),
    path('dinheiros_confirmadas/<int:id>', d_conf_din, name="url_d_conf_din"),
    path('produtos_deletar/<int:id>', delete_d_pro, name="url_delete_d_pro"),
    path('dinheiros_deletar/<int:id>', delete_d_din, name="url_delete_d_din"),

]
