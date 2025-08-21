from django.db import models

class Therapist(models.Model):
    # Opciones de documentos
    DOCUMENT_TYPES = [
        ('DNI', 'DNI'),
        ('CE', 'Carné de Extranjería'),
        ('PTP', 'PTP'),
        ('CR', 'Carné de Refugiado'),
        ('PAS', 'Pasaporte'),
    ]

    GENDERS = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    STATUS = [
        (True, 'Activo'),
        (False, 'Inactivo'),
    ]

    # Datos personales
    document_type = models.CharField(max_length=10, choices=DOCUMENT_TYPES)  
    document_number = models.CharField(max_length=20, unique=True)  
    last_name_paternal = models.CharField(max_length=100)  
    last_name_maternal = models.CharField(max_length=100, blank=True, null=True)  
    first_name = models.CharField(max_length=100)  
    birth_date = models.DateField()  
    gender = models.CharField(max_length=1, choices=GENDERS)  
    personal_reference = models.CharField(max_length=255, blank=True, null=True)  
    is_active = models.BooleanField(choices=STATUS, default=True)

    # Información de contacto
    phone = models.CharField(max_length=15)  
    email = models.EmailField(blank=True, null=True)  
    country = models.CharField(max_length=100, blank=True, null=True)  
    department = models.CharField(max_length=100, blank=True, null=True)  
    province = models.CharField(max_length=100, blank=True, null=True)  
    district = models.CharField(max_length=100, blank=True, null=True)  
    address = models.TextField(blank=True, null=True)  
    profile_picture = models.ImageField(
        upload_to='profile_pictures/', 
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name_paternal} {self.last_name_maternal or ''}"
