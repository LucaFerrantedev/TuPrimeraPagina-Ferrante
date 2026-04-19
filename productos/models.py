from django.db import models

class MarcaProductos(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"Marca: {self.nombre}"

class CategoriaProductos(models.Model):
    tipo_prod = models.CharField(max_length=50)

    def __str__(self):
        return f"Tipo de producto: {self.tipo_prod}"

class ComponenteProductos(models.Model):
    modelo = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    descripcion = models.CharField(max_length=200, null=True)

    marca = models.ForeignKey(MarcaProductos, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaProductos, on_delete=models.CASCADE)

    def __str__(self):
        return f"Marca: {self.marca.nombre} / Modelo: {self.modelo} / Precio: {self.precio} / Descripción: {self.descripcion}"