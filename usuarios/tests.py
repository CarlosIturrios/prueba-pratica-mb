from django.test import TestCase
from .models import Usuario

class UsuarioTests(TestCase):
    def setUp(self):
        Usuario.objects.create(nombre="Carlos", apellido_paterno="Iturrios", 
                               apellido_materno="Alcaraz", edad=26, 
                               email="c.iturriosalcaraz@gmail.com", telefono="5629696036")

    def test_usuario_creado_correctamente(self):
        usuario = Usuario.objects.get(nombre="Carlos")
        self.assertEqual(usuario.apellido_paterno, "Iturrios")
