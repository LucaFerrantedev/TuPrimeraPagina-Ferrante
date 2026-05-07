from django.db import models

def imagen_upload_to(instance, filename):
    return f"productos/{instance.modelo}/{filename}"

class MarcaProductos(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"Marca: {self.nombre}"

class CategoriaProductos(models.Model):
    tipo_prod = models.CharField(max_length=50)

    def __str__(self):
        return f"Tipo de producto: {self.tipo_prod}"

class ComponenteProductos(models.Model):
    imagen = models.ImageField(
        upload_to=imagen_upload_to,
        default="default/imagen.png",
        blank=True,
        null=True,
        verbose_name="Imagen"
    )

    modelo = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    descripcion = models.CharField(max_length=200, null=True)
    marca = models.ForeignKey(MarcaProductos, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaProductos, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(auto_now_add=True)
    sku = models.IntegerField(unique=True, null=True)

    def __str__(self):
        return f"Marca: {self.marca.nombre} / Modelo: {self.modelo} / Precio: {self.precio} / Descripción: {self.descripcion}"