from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'cargar$', 'museos.views.xmlParser', name = "Parser"),
    url(r'^$', 'museos.views.pagina_principal', name = "Página principal de la práctica"),
    url(r'^.*style\.css$', 'museos.views.style'),
    url(r'^museos$', 'museos.views.museos', name = "Página con todos los museos"),
    url(r'^museos/(\d+)$', 'museos.views.museos_id', name = "Página de un museo"),
    url(r'^acceso$', 'museos.views.filtro_accesibilidad'),
    url(r'^distrito$', 'museos.views.distrito'),
    url(r'^distrito/(.*)', 'museos.views.distrito_concreto'),
    url(r'^comentario_nuevo$', 'museos.views.comentar', name = "Nuevos comentarios"),
    url(r'^estilo_nuevo$', 'museos.views.estiloUser', name = "Estilo"),
    url(r'^titulo_nuevo$', 'museos.views.tituloUser', name = "Titulo"),
    url(r'^about$', 'museos.views.about', name = "Página autoría de la práctica y funcionamiento"),
    url(r'^logout$', 'museos.views.mylogout' , name = "Logout de usuarios"),
    url(r'^login$', 'museos.views.mylogin', name = "Login de usuarios"),
    url(r'^(.*)', 'museos.views.user', name = "Página personal de un usuario"),
]
