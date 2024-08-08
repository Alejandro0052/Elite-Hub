from django.contrib import admin
from .models import Usuario,Deporte,Deportista,Nutricionista, Patrocinador, Marca





class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'edad', 'direccion')


class PatrocinadorAdmin(admin.ModelAdmin):
    list_display = ('get_usuario_nombre', 'get_usuario_apellido', 'get_usuario_correo', 'deportistas_interes')

    def get_usuario_nombre(self, obj):
        return obj.usuario.nombre
    get_usuario_nombre.short_description = 'Nombre del Patrocinador'

    def get_usuario_apellido(self, obj):
        return obj.usuario.apellido
    get_usuario_apellido.short_description = 'Apellido del Patrocinador'

    def get_usuario_correo(self, obj):
        return obj.usuario.correo
    get_usuario_correo.short_description = 'Correo del Patrocinador'


class NutricionistaAdmin(admin.ModelAdmin):
    list_display = ('get_usuario_nombre', 'get_usuario_apellido', 'get_usuario_correo', 'especialidad')

    def get_usuario_nombre(self, obj):
        return obj.usuario.nombre
    get_usuario_nombre.short_description = 'Nombre del Nutricionista'

    def get_usuario_apellido(self, obj):
        return obj.usuario.apellido
    get_usuario_apellido.short_description = 'Apellido del Nutricionista'

    def get_usuario_correo(self, obj):
        return obj.usuario.correo
    get_usuario_correo.short_description = 'Correo del Nutricionista'


class MarcaAdmin(admin.ModelAdmin):
    list_display = ('get_usuario_nombre', 'get_usuario_apellido', 'get_usuario_correo', 'razon_social')

    def get_usuario_nombre(self, obj):
        return obj.usuario.nombre
    get_usuario_nombre.short_description = 'Nombre de la marca'

    def get_usuario_apellido(self, obj):
        return obj.usuario.apellido
    get_usuario_apellido.short_description = 'Apellido de la marca'

    def get_usuario_correo(self, obj):
        return obj.usuario.correo
    get_usuario_correo.short_description = 'Correo de la marca'

    
class DeportistaAdmin(admin.ModelAdmin):
    list_display = ('get_usuario_nombre', 'get_usuario_apellido', 'get_usuario_correo', 'deporte')

    def get_usuario_nombre(self, obj):
        return obj.usuario.nombre
    get_usuario_nombre.short_description = 'Nombre del deportista'

    def get_usuario_apellido(self, obj):
        return obj.usuario.apellido
    get_usuario_apellido.short_description = 'Apellido del deportista'

    def get_usuario_correo(self, obj):
        return obj.usuario.correo
    get_usuario_correo.short_description = 'Correo del deportista'



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Deporte)
admin.site.register(Deportista, DeportistaAdmin)
admin.site.register(Nutricionista, NutricionistaAdmin)
admin.site.register(Patrocinador, PatrocinadorAdmin)
admin.site.register(Marca, MarcaAdmin)

