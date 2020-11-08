from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances


# Create your models here.
class Liga(models.Model):
    #Model representing a book genre."""
	nombre = models.CharField(max_length=200)
	
	def __str__(self):
		return self.nombre

class Camisetas(models.Model):
    
	país = models.CharField(max_length=200)
	equipo = models.ForeignKey('Liga', on_delete=models.SET_NULL, null=True)
	
    
	def __str__(self):
		return self.equipo
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('camiseta_detalle', args=[str(self.id)])


class CamisetasInstance(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID único para cada camiseta en la tienda')
	camiseta = models.ForeignKey('Camisetas', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	

	LOAN_STATUS = (
		('l', 'La Liga'),
		('pl', 'Premier League'),
		('a', 'Serie A'),
		
	)

	status = models.CharField(
		max_length=100,
		choices=LOAN_STATUS,
		blank=True,
		default='l',
		help_text='Camisetas disponibles',
	)

	class Meta:
		ordering = ['camiseta']

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.book.title})'


class Cliente(models.Model):
	"""Model representing an author."""
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	edad = models.IntegerField(null=True, blank=True)
	Rut = models.IntegerField(null=True, blank=True)

	class Meta:
		ordering = ['apellido', 'nombre']

	def get_absolute_url(self):
		return reverse('cliente_detalle', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.apellido}, {self.nombre}'	