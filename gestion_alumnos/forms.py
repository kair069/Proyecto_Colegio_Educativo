from django import forms
from .models import Nivel
####################################################################################################
from django import forms
from .models import Nivel

from django import forms
from .models import Nivel

class NivelForm(forms.ModelForm):
    class Meta:
        model = Nivel
        fields = ['nombre', 'codigo', 'descripcion', 'estado', 'años_duracion', 'imagen']  # Todos los campos

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nivel (Primaria o Secundaria)',
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Código único para el nivel',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del nivel',
                'rows': 3,
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control',
            }),
            'años_duracion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cantidad de años de duración',
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*',  # Asegura que solo se acepten imágenes
            }),
        }

        labels = {
            'nombre': 'Nombre del Nivel',
            'codigo': 'Código del Nivel',
            'descripcion': 'Descripción del Nivel',
            'estado': 'Estado del Nivel',
            'años_duracion': 'Años de Duración',
            'imagen': 'Imagen del Nivel',
        }


####################################################################################################
from django import forms
from .models import Grado

class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['nivel', 'nombre', 'descripcion', 'imagen']
        widgets = {
            'nivel': forms.Select(attrs={
                'class': 'form-control',
                'title': 'Seleccione el nivel educativo (Primaria o Secundaria)',
            }),
            'nombre': forms.Select(attrs={
                'class': 'form-control',
                'title': 'Seleccione el grado',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese una breve descripción del grado',
                'rows': 3,
                'title': 'Proporcione detalles sobre el grado',
            }),
            'imagen': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://ejemplo.com/imagen.jpg',
                'title': 'Ingrese un enlace válido a una imagen',
            }),
        }
        labels = {
            'nivel': 'Nivel Educativo',
            'nombre': 'Grado',
            'descripcion': 'Descripción',
            'imagen': 'Imagen (URL)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Reemplazamos el campo de nombre con un Select dinámico
        self.fields['nombre'].widget.choices = Grado.GRADOS_CHOICES

####################################################################################################

from django import forms
from .models import Seccion, Grado

class SeccionForm(forms.ModelForm):
    grado = forms.ModelChoiceField(
        queryset=Grado.objects.all(),
        empty_label="Seleccione un grado",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    nombre = forms.CharField(
        max_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: A, B, C'})
    )

    class Meta:
        model = Seccion
        fields = ['grado', 'nombre']
####################################################################################################
from django import forms
from .models import Periodo

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ["nombre", "fecha_inicio", "fecha_fin"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ejemplo: 1er Bimestre"}),
            "fecha_inicio": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }


####################################################################################################
from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni', 'seccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el DNI', 'maxlength': '8'}),
            'seccion': forms.Select(attrs={'class': 'form-select'}),
        }

from django import forms
from .models import AlumnoDetalle

from django import forms
from .models import AlumnoDetalle

class AlumnoDetalleForm(forms.ModelForm):
    class Meta:
        model = AlumnoDetalle
        exclude = ['alumno']  # ❌ Evitar errores al asignar manualmente el alumno

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono del alumno'}),
            'telefono_padre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono del padre'}),
            'telefono_madre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono de la madre'}),
            'telefono_tutor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono del tutor'}),
            'foto_dni': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'partida_nacimiento': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ficha_matricula': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'codigo_estudiante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Código del estudiante'}),
            'promedio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '20'}),
            'estado_academico': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del alumno'}),
            'tipo_sangre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: O+, A-, AB+'}),
            'alergias': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Ejemplo: Maní, polen, mariscos'}),
            'enfermedades': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Ejemplo: Asma, diabetes'}),
            'seguro_medico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: ESSALUD, Pacífico'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Peruano'}),
            'idiomas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Español, Inglés, Francés'}),
            'salida_autorizada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'restricciones_legales': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Ejemplo: Orden judicial'}),
        }


        labels = {
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'direccion': 'Dirección',
            'telefono': 'Teléfono del Alumno',
            'imagen': 'Foto del Alumno',
            'foto_dni': 'Foto del DNI',
            'partida_nacimiento': 'Partida de Nacimiento',
            'ficha_matricula': 'Ficha de Matrícula',
            'codigo_estudiante': 'Código del Estudiante',
            'promedio': 'Promedio Académico',
            'estado_academico': 'Estado Académico',
            'nombre_padre': 'Nombre del Padre',
            'telefono_padre': 'Teléfono del Padre',
            'nombre_madre': 'Nombre de la Madre',
            'telefono_madre': 'Teléfono de la Madre',
            'nombre_tutor': 'Nombre del Tutor',
            'telefono_tutor': 'Teléfono del Tutor',
            'tipo_sangre': 'Tipo de Sangre',
            'alergias': 'Alergias',
            'enfermedades': 'Enfermedades',
            'seguro_medico': 'Seguro Médico',
            'nacionalidad': 'Nacionalidad',
            'idiomas': 'Idiomas',
            'salida_autorizada': '¿Puede salir solo después de clases?',
            'restricciones_legales': 'Restricciones Legales',
        }







####################################################################################################
from django import forms
from .models import Docente

# class DocenteForm(forms.ModelForm):
#     class Meta:
#         model = Docente
#         fields = ['nombre', 'apellido']
#         widgets = {
#             'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
#             'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
#         }

from django import forms
from django.contrib.auth.models import User
from .models import Docente

from django import forms
from django.contrib.auth.models import User
from .models import Docente

class DocenteForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=User.objects.none(),  # Se asigna dinámicamente en __init__
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Docente
        fields = ['usuario', 'nombre', 'apellido']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el apellido'}),
        }

    def __init__(self, *args, **kwargs):
        super(DocenteForm, self).__init__(*args, **kwargs)
        # Asignamos dinámicamente el queryset para evitar errores de base de datos
        self.fields['usuario'].queryset = User.objects.filter(groups__name='Profesor')


####################################################################################################
from django import forms
from .models import CursoAsignado

class CursoAsignadoForm(forms.ModelForm):
    class Meta:
        model = CursoAsignado
        fields = ['docente', 'curso', 'seccion']
        labels = {
            'docente': 'Docente',
            'curso': 'Curso',
            'seccion': 'Sección',
        }
        widgets = {
            'docente': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'seccion': forms.Select(attrs={'class': 'form-control'}),
        }
####################################################################################################

from django import forms
from .models import Curso
from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['grado', 'nombre', 'descripcion']
        widgets = {
            'grado': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del curso'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del curso (opcional)'}),
        }


####################################################################################################

# from django import forms
# from .models import Asistencia

# class AsistenciaForm(forms.ModelForm):
#     class Meta:
#         model = Asistencia
#         fields = ['alumno', 'curso_asignado', 'periodo', 'estado']
#         widgets = {
#             'alumno': forms.HiddenInput(),  # No se muestra, ya que se asigna automáticamente
#             'curso_asignado': forms.HiddenInput(),  # Se asigna según la vista
#             'periodo': forms.HiddenInput(),  # Se asigna automáticamente
#             'estado': forms.Select(
#                 choices=[
#                     ('Presente', '✅ Presente'),
#                     ('Tarde', '⏳ Tarde'),
#                     ('Ausente', '❌ Ausente')
#                 ],
#                 attrs={'class': 'form-control'}
#             ),
#         }

#     def __init__(self, *args, **kwargs):
#         super(AsistenciaForm, self).__init__(*args, **kwargs)
#         self.fields['estado'].label = "Estado de asistencia"
from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['alumno', 'fecha', 'periodo', 'estado']  # Se incluye 'fecha' para mayor control
        widgets = {
            'alumno': forms.HiddenInput(),  # Se asigna automáticamente en la vista
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Permite seleccionar la fecha
            'periodo': forms.HiddenInput(),  # Se asigna automáticamente
            'estado': forms.Select(
                choices=[
                    ('Presente', '✅ Presente'),
                    ('Tarde', '⏳ Tarde'),
                    ('Ausente', '❌ Ausente')
                ],
                attrs={'class': 'form-control'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(AsistenciaForm, self).__init__(*args, **kwargs)
        self.fields['estado'].label = "Estado de asistencia"
        self.fields['fecha'].label = "Fecha de asistencia"  # Etiqueta para el campo fecha



####################################################################################################
from django import forms
from .models import Trabajo
from django.utils.translation import gettext_lazy as _

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['curso_asignado', 'titulo', 'descripcion', 'fecha_entrega', 'hora_entrega', 'periodo', 'tipo_trabajo', 'es_obligatorio']
        widgets = {
            'curso_asignado': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del trabajo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del trabajo'}),
            'fecha_entrega': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_entrega': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'periodo': forms.Select(attrs={'class': 'form-control'}),
            'tipo_trabajo': forms.Select(attrs={'class': 'form-control'}),
            'es_obligatorio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'curso_asignado': _('Curso Asignado'),
            'titulo': _('Título'),
            'descripcion': _('Descripción'),
            'fecha_entrega': _('Fecha de Entrega'),
            'hora_entrega': _('Hora de Entrega'),
            'periodo': _('Periodo Académico'),
            'tipo_trabajo': _('Tipo de Trabajo'),
            'es_obligatorio': _('Trabajo Obligatorio'),
        }

####################################################################################################
from django import forms
from .models import Calificacion
from django.utils.translation import gettext_lazy as _

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['trabajo', 'alumno', 'curso_asignado', 'nota', 'comentarios', 'estado']  # ⚠️ Eliminado 'fecha_registro'
        widgets = {
            'trabajo': forms.Select(attrs={'class': 'form-control select2'}),
            'alumno': forms.Select(attrs={'class': 'form-control select2'}),
            'curso_asignado': forms.Select(attrs={'class': 'form-control select2'}),
            'nota': forms.NumberInput(attrs={
                'class': 'form-range', 
                'min': 0, 
                'max': 20, 
                'step': 0.1,
                'oninput': "notaOutput.value = this.value"
            }),
            'comentarios': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Comentarios del docente...'}),
            'estado': forms.RadioSelect(choices=[
                ('Pendiente', 'Pendiente'),
                ('Revisado', 'Revisado'),
                ('Aprobado', 'Aprobado'),
            ]),
        }
        labels = {
            'trabajo': _('Trabajo Asignado'),
            'alumno': _('Alumno'),
            'curso_asignado': _('Curso Asignado'),
            'nota': _('Calificación (0-20)'),
            'comentarios': _('Comentarios'),
            'estado': _('Estado de la Calificación'),
        }

####################################################################################################
from django import forms
from .models import EventoCalendario

class EventoCalendarioForm(forms.ModelForm):
    class Meta:
        model = EventoCalendario
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_fin', 'tipo_evento']
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

####################################################################################################
from django import forms
from .models import Unidad
from ckeditor.widgets import CKEditorWidget

from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Unidad

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = ['curso', 'nombre', 'descripcion', 'numero', 'material_pdf', 'video_url']
        
        widgets = {
            'curso': forms.Select(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%;',
                'data-placeholder': 'Seleccione un curso...',
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: Introducción a la suma y resta',
                'autocomplete': 'off',
                'list': 'sugerencias_unidad',
            }),
            'descripcion': CKEditorWidget(config_name='default', attrs={
                'class': 'form-control',
                'style': 'min-height: 150px;',
            }),
            'numero': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'placeholder': 'Ejemplo: 1 (Primera unidad)',
            }),
            'material_pdf': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'application/pdf',
            }),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.youtube.com/watch?v=...',
            }),
        }

        labels = {
            'curso': 'Curso asociado',
            'nombre': 'Nombre de la Unidad',
            'descripcion': 'Descripción Detallada',
            'numero': 'Número de Unidad',
            'material_pdf': 'Material PDF (Opcional)',
            'video_url': 'Video de YouTube (Opcional)',
        }

        help_texts = {
            'curso': 'Seleccione el curso al que pertenece esta unidad.',
            'nombre': 'Nombre representativo de la unidad.',
            'descripcion': 'Puede incluir imágenes, videos y texto enriquecido.',
            'numero': 'Orden dentro del curso (Ejemplo: 1, 2, 3...).',
            'material_pdf': 'Suba un archivo PDF relacionado con la unidad.',
            'video_url': 'Ingrese un enlace de YouTube válido.',
        }

    def clean_video_url(self):
        """Valida que el enlace ingresado sea un video de YouTube"""
        video_url = self.cleaned_data.get('video_url')
        if video_url and "youtube.com/watch?v=" not in video_url and "youtu.be/" not in video_url:
            raise forms.ValidationError("Ingrese un enlace válido de YouTube.")
        return video_url


####################################################################################################

from django import forms
from .models import Tema
from django_summernote.widgets import SummernoteWidget  # Editor de texto enriquecido

from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Tema

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ["unidad", "nombre", "descripcion", "numero"]
        widgets = {
            "unidad": forms.Select(
                attrs={
                    "class": "form-select select2",
                    "data-placeholder": "Selecciona una unidad..."
                }
            ),
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Escribe el nombre del tema..."
                }
            ),
            "descripcion": CKEditorWidget(),  # Reemplazamos Summernote con CKEditor
            "numero": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejemplo: 1",
                    "min": 1,
                    "max": 100
                }
            ),
        }


####################################################################################################

# from django import forms
# from .models import HorarioDocente

# class HorarioDocenteForm(forms.ModelForm):
#     class Meta:
#         model = HorarioDocente
#         fields = ['docente', 'curso_asignado', 'dia', 'hora_inicio', 'hora_fin', 'aula']
#         widgets = {
#             'dia': forms.Select(attrs={'class': 'form-control'}),
#             'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
#             'hora_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
#             'aula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de aula'}),
#         }
####################################################################################################

# from django import forms
# from .models import HorarioDocente, Docente, CursoAsignado

# class HorarioDocenteForm(forms.ModelForm):
#     docente = forms.ModelChoiceField(
#         queryset=Docente.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-control select2'}),
#         label="👨‍🏫 Docente"
#     )
#     curso_asignado = forms.ModelChoiceField(
#         queryset=CursoAsignado.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-control select2'}),
#         label="📚 Curso Asignado"
#     )

#     class Meta:
#         model = HorarioDocente
#         fields = ['docente', 'curso_asignado', 'dia', 'hora_inicio', 'hora_fin', 'aula']
#         widgets = {
#             'dia': forms.Select(attrs={'class': 'form-control'}),
#             'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
#             'hora_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
#             'aula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Aula 101'}),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         hora_inicio = cleaned_data.get("hora_inicio")
#         hora_fin = cleaned_data.get("hora_fin")
#         docente = cleaned_data.get("docente")
#         dia = cleaned_data.get("dia")

#         if hora_inicio and hora_fin and hora_inicio >= hora_fin:
#             raise forms.ValidationError("⚠️ La hora de inicio no puede ser mayor o igual a la hora de fin.")

#         # Verificar si hay cruces de horarios
#         if HorarioDocente.objects.filter(docente=docente, dia=dia, hora_inicio__lt=hora_fin, hora_fin__gt=hora_inicio).exists():
#             raise forms.ValidationError("⚠️ Este docente ya tiene una clase en este horario.")

#         return cleaned_data

from django import forms
from .models import HorarioDocente, Docente, CursoAsignado

class HorarioDocenteForm(forms.ModelForm):
    docente = forms.ModelChoiceField(
        queryset=Docente.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control select2'}),
        label="👨‍🏫 Docente"
    )
    curso_asignado = forms.ModelChoiceField(
        queryset=CursoAsignado.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control select2'}),
        label="📚 Curso Asignado"
    )

    class Meta:
        model = HorarioDocente
        fields = ['docente', 'curso_asignado', 'dia', 'hora_inicio', 'hora_fin', 'aula']
        widgets = {
            'dia': forms.Select(attrs={'class': 'form-control select2'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'aula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Aula 101'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get("hora_inicio")
        hora_fin = cleaned_data.get("hora_fin")
        docente = cleaned_data.get("docente")
        dia = cleaned_data.get("dia")

        if hora_inicio and hora_fin:
            if hora_inicio >= hora_fin:
                raise forms.ValidationError("⚠️ La hora de inicio debe ser menor que la hora de fin.")

        # Verificar si ya existe un horario con el mismo docente, día y cruce de horas
        if docente and dia and hora_inicio and hora_fin:
            conflicto = HorarioDocente.objects.filter(
                docente=docente,
                dia=dia,
                hora_inicio__lt=hora_fin,  # Se cruza con otra clase que termina después de que esta empieza
                hora_fin__gt=hora_inicio    # Se cruza con otra clase que empieza antes de que esta termine
            )

            # Si estamos editando, excluir el horario actual de la validación
            if self.instance.pk:
                conflicto = conflicto.exclude(pk=self.instance.pk)

            if conflicto.exists():
                raise forms.ValidationError("⚠️ Este docente ya tiene una clase en este horario.")

        return cleaned_data


#3♣3♣####################################################################################################
from django import forms
from django.contrib.auth.models import User

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


####################################################################################################USUARIOS
# Formulario para editar usuario
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }        