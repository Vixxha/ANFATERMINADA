from django.db import models

# Create your models here.

class Equipos(models.Model):
    imagen = models.ImageField(upload_to="fotos", null=True)
    info = models.TextField(null=True)
    nombre_equipo = models.CharField(max_length=30)
    cantidad_partidos  = models.IntegerField()
    puntos = models.IntegerField()
    partidos_ganados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    goles_a_favor = models.IntegerField(default=0)
    goles_en_contra = models.IntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)




    def __str__(self):
        return str(self.imagen) + ' ' + str(self.nombre_equipo)  + ' ' + str(self.cantidad_partidos) + ' ' + str(self.puntos)
    
    class Meta:
        verbose_name_plural = "Equipos"

class Noticia(models.Model):
    imagen = models.ImageField(upload_to="noticias", null=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    contenido = models.TextField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Noticias"
        ordering = ['-id']

class Partido(models.Model):
    equipo_local = models.ForeignKey(Equipos, related_name='partidos_local', on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey(Equipos, related_name='partidos_visitante', on_delete=models.CASCADE)
    fecha = models.DateField()
    resultado = models.CharField(max_length=10)
    fechas = models.CharField(max_length=10, default='Fecha')
    zona = models.CharField(max_length=20, default='Escoger', choices=(
        ('Tercera A', 'Tercera A'),
        ('Norte', 'Zona Norte'),
        ('Centro', 'Zona Centro'),
        ('Sur', 'Zona Sur'),
    ))

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha} - {self.resultado} - {self.fechas}"
    
    class Meta:
        verbose_name_plural = "Calendario Partidos"


class TerceraA(models.Model):
    imagen = models.ImageField(upload_to="fotos", null=True)
    nombre_equipo = models.CharField(max_length=30)
    cantidad_partidos = models.IntegerField()
    puntos = models.IntegerField()
    partidos_ganados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    goles_a_favor = models.IntegerField(default=0)
    goles_en_contra = models.IntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_equipo
    
    class Meta:
        verbose_name_plural = "Tabla Tercera A"
    
class Norte(models.Model):
    imagen = models.ImageField(upload_to="fotos", null=True)
    nombre_equipo = models.CharField(max_length=30)
    cantidad_partidos = models.IntegerField()
    puntos = models.IntegerField()
    partidos_ganados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    goles_a_favor = models.IntegerField(default=0)
    goles_en_contra = models.IntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_equipo
    
    class Meta:
        verbose_name_plural = "Tabla zona norte"
    
class Centro(models.Model):
    imagen = models.ImageField(upload_to="fotos", null=True)
    nombre_equipo = models.CharField(max_length=30)
    cantidad_partidos = models.IntegerField()
    puntos = models.IntegerField()
    partidos_ganados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    goles_a_favor = models.IntegerField(default=0)
    goles_en_contra = models.IntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_equipo    
    
    class Meta:
        verbose_name_plural = "Tabla zona centro"
    
class Sur(models.Model):
    imagen = models.ImageField(upload_to="fotos", null=True)
    nombre_equipo = models.CharField(max_length=30)
    cantidad_partidos = models.IntegerField()
    puntos = models.IntegerField()
    partidos_ganados = models.IntegerField(default=0)
    partidos_perdidos = models.IntegerField(default=0)
    partidos_empatados = models.IntegerField(default=0)
    goles_a_favor = models.IntegerField(default=0)
    goles_en_contra = models.IntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_equipo    
    
    class Meta:
        verbose_name_plural = "Tabla zona sur"

class Programados(models.Model):
    equipo_local = models.ForeignKey('Equipos', related_name='partidos_programados_local', on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey('Equipos', related_name='partidos_programados_visitante', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.equipo_local.nombre_equipo} vs {self.equipo_visitante.nombre_equipo} - {self.fecha} - {self.hora}"

    class Meta:
        verbose_name = "Partido Programado"