from io import BytesIO
# Librerias django y rest framework
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.core.paginator import Paginator
# Librerias pdf
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# Modelos 
from .models import Usuario
# Serializers
from .serializers import UsuarioSerializer


class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        queryset = Usuario.objects.all()
        edad = self.request.query_params.get('edad')
        if edad:
            queryset = queryset.filter(edad=edad)
        ordenar_por_edad = self.request.query_params.get('ordenar_por_edad')
        if ordenar_por_edad:
            queryset = self.ordenar_por_edad(queryset)
        ordenar_por_apellido_paterno = self.request.query_params.get('ordenar_por_apellido_paterno')
        if ordenar_por_apellido_paterno:
            queryset = self.ordenar_por_apellido(queryset)
        return queryset
    
    def ordenar_por_edad(self, queryset):
        usuarios = list(queryset) 
        n = len(usuarios)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if usuarios[j].edad > usuarios[j + 1].edad:
                    usuarios[j], usuarios[j + 1] = usuarios[j + 1], usuarios[j]
        return usuarios

    def ordenar_por_apellido(self, queryset):
        usuarios = list(queryset) 
        n = len(usuarios)
        for i in range(1, n):
            key = usuarios[i]
            j = i - 1
            while j >= 0 and usuarios[j].apellido_paterno > key.apellido_paterno:
                usuarios[j + 1] = usuarios[j]
                j -= 1
            usuarios[j + 1] = key
        return usuarios
    
    def get(self, request, *args, **kwargs):
        if 'pdf' in request.path:
            return self.usuarios_pdf(request)
        return super().get(request, *args, **kwargs)
    
    def usuarios_pdf(self, request):
        queryset = self.get_queryset()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="usuarios.pdf"'

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        data = []

        headers = ["Nombre", "Apellido Paterno", "Apellido Materno", "Email", "Teléfono", "Edad"]
        data.append(headers)

        paginator = Paginator(queryset, 100)
        for page_num in range(1, paginator.num_pages + 1):
            page_queryset = paginator.page(page_num)
            for usuario in page_queryset:
                data.append([
                    usuario.nombre,
                    usuario.apellido_paterno,
                    usuario.apellido_materno,
                    usuario.email,
                    usuario.telefono,
                    usuario.edad
                ])

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ])

        tabla = Table(data)
        tabla.setStyle(style)

        elements = [tabla]
        doc.build(elements)

        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response

class UsuarioRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
