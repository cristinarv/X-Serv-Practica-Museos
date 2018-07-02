from django.contrib import admin
from museos.models import Museo
from museos.models import Content_User
from museos.models import Comentario
from museos.models import Configuracion
# Register your models here.

admin.site.register(Museo)
admin.site.register(Content_User)
admin.site.register(Comentario)
admin.site.register(Configuracion)
