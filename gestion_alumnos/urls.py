from django.urls import path

from .views import home, salida
from .views import NivelListView, NivelCreateView, NivelUpdateView, NivelDeleteView
from .views import GradoListView, GradoCreateView, GradoUpdateView, GradoDeleteView 
from .views import SeccionListView, SeccionCreateView, SeccionUpdateView, SeccionDeleteView
from .views import (
    PeriodoListView, PeriodoCreateView, 
    PeriodoUpdateView, PeriodoDeleteView
)
from . import views
from .views import (
    AlumnoListView,
    AlumnoCreateView,
    AlumnoUpdateView,
    AlumnoDeleteView,
)
from .views import UnidadListView, UnidadCreateView, UnidadUpdateView, UnidadDeleteView
from .views import (
    DocenteListView,
    DocenteCreateView,
    DocenteUpdateView,
    DocenteDeleteView
)
from .views import exportar_calificaciones_excel

from .views import (
    CursoAsignadoListView, 
    CursoAsignadoCreateView, 
    CursoAsignadoUpdateView, 
    CursoAsignadoDeleteView
)
#iMPORTACION DE REGISTROS
from django.contrib.auth import views as auth_views
from .views import registro_usuario

from .views import (
    TemaListView, TemaDetailView, TemaCreateView,
    TemaUpdateView, TemaDeleteView
)
from .views import exportar_asistencias
# from .views import (
#     AsistenciaListView, AsistenciaCreateView, 
#     AsistenciaUpdateView, AsistenciaDeleteView
# )
from .views import pasar_asistencia
from .views import listar_asistencias  # Asegúrate de tener esta vista

from .views import CursoListView, CursoCreateView, CursoUpdateView, CursoDeleteView
# from .views import asistencia_rapida
from .views import seleccionar_curso_asistencia, pasar_asistencia
from .views import TrabajoListView, TrabajoCreateView, TrabajoUpdateView, TrabajoDeleteView

from .views import (
    CalificacionListView,
    CalificacionCreateView,
    CalificacionUpdateView,
    CalificacionDeleteView,
)
from .views import agregar_horarioo
from .views import ExportarTrabajosExcel
from .views import UnidadListView, UnidadCreateView, UnidadUpdateView, UnidadDeleteView, UnidadDetailView,exportar_unidad_word,exportar_unidad_pdf
from .views import  actualizar_asistencia, eliminar_asistencia

from .views import calendario_academico
from .views import calendario_academico, agregar_evento, editar_evento, eliminar_evento
from .views import reproductor_mp3

from .views import listar_horarios, agregar_horario, editar_horario, eliminar_horario

from .views import calificar_trabajo
urlpatterns = [
    path('niveles/', NivelListView.as_view(), name='nivel_list'),
    path('niveles/nuevo/', NivelCreateView.as_view(), name='nivel_create'),
    path('niveles/editar/<int:pk>/', NivelUpdateView.as_view(), name='nivel_update'),
    path('niveles/eliminar/<int:pk>/', NivelDeleteView.as_view(), name='nivel_delete'),


    path('grados/', GradoListView.as_view(), name='grado_list'),
    path('grados/nuevo/', GradoCreateView.as_view(), name='grado_create'),
    path('grados/editar/<int:pk>/', GradoUpdateView.as_view(), name='grado_update'),
    path('grados/eliminar/<int:pk>/', GradoDeleteView.as_view(), name='grado_delete'),



    
    path('secciones/', SeccionListView.as_view(), name='seccion_list'),
    path('secciones/nueva/', SeccionCreateView.as_view(), name='seccion_create'),
    path('secciones/editar/<int:pk>/', SeccionUpdateView.as_view(), name='seccion_update'),
    path('secciones/eliminar/<int:pk>/', SeccionDeleteView.as_view(), name='seccion_delete'),


    path("periodos/", PeriodoListView.as_view(), name="periodo_list"),
    path("periodos/nuevo/", PeriodoCreateView.as_view(), name="periodo_create"),
    path("periodos/editar/<int:pk>/", PeriodoUpdateView.as_view(), name="periodo_update"),
    path("periodos/eliminar/<int:pk>/", PeriodoDeleteView.as_view(), name="periodo_delete"),


    path("alumnos/", AlumnoListView.as_view(), name="alumno_list"),
    path("alumnos/nuevo/", AlumnoCreateView.as_view(), name="alumno_create"),
    path("alumnos/editar/<int:pk>/", AlumnoUpdateView.as_view(), name="alumno_update"),
    path("alumnos/eliminar/<int:pk>/", AlumnoDeleteView.as_view(), name="alumno_delete"),



    path("docentes/", DocenteListView.as_view(), name="docente_list"),
    path("docentes/nuevo/", DocenteCreateView.as_view(), name="docente_create"),
    path("docentes/editar/<int:pk>/", DocenteUpdateView.as_view(), name="docente_update"),
    path("docentes/eliminar/<int:pk>/", DocenteDeleteView.as_view(), name="docente_delete"),

    path('cursos_asignados/', CursoAsignadoListView.as_view(), name='curso_asignado_list'),
    path('cursos_asignados/nuevo/', CursoAsignadoCreateView.as_view(), name='curso_asignado_create'),
    path('cursos_asignados/editar/<int:pk>/', CursoAsignadoUpdateView.as_view(), name='curso_asignado_update'),
    path('cursos_asignados/eliminar/<int:pk>/', CursoAsignadoDeleteView.as_view(), name='curso_asignado_delete'),



    path("cursos/", CursoListView.as_view(), name="curso_list"),
    path("cursos/nuevo/", CursoCreateView.as_view(), name="curso_create"),
    path("cursos/editar/<int:pk>/", CursoUpdateView.as_view(), name="curso_update"),
    path("cursos/eliminar/<int:pk>/", CursoDeleteView.as_view(), name="curso_delete"),



    # path('asistencias/', AsistenciaListView.as_view(), name='asistencia_list'),  # 📌 Listar asistencias
    # path('asistencias/nueva/', AsistenciaCreateView.as_view(), name='asistencia_create'),  # 📌 Crear asistencia
    # path('asistencias/editar/<int:pk>/', AsistenciaUpdateView.as_view(), name='asistencia_update'),  # 📌 Editar asistencia
    # path('asistencias/eliminar/<int:pk>/', AsistenciaDeleteView.as_view(), name='asistencia_delete'),  # 📌 Eliminar asistencia
    # path('asistencia_rapida/<int:curso_id>/<int:periodo_id>/', asistencia_rapida, name='asistencia_rapida'),
     path('asistencia/seleccionar/', seleccionar_curso_asistencia, name='seleccionar_curso_asistencia'),
    path('asistencia/pasar/<int:curso_asignado_id>/', pasar_asistencia, name='pasar_asistencia'),
    path('asistencia/listar/', listar_asistencias, name='pasar_asistencia_list'),
    path("asistencia/listar/", listar_asistencias, name="listar_asistencias"),  # <--- Asegúrate de que esta línea exista
    path('exportar-asistencias/', exportar_asistencias, name='exportar_asistencias'),
    
        path('actualizar/<int:asistencia_id>/', actualizar_asistencia, name='actualizar_asistencia'),
    path('eliminar/<int:asistencia_id>/', eliminar_asistencia, name='eliminar_asistencia'),




    path('trabajos/', TrabajoListView.as_view(), name='trabajo_list'),
    path('trabajos/nuevo/', TrabajoCreateView.as_view(), name='trabajo_create'),
    path('trabajos/editar/<int:pk>/', TrabajoUpdateView.as_view(), name='trabajo_update'),
    path('trabajos/eliminar/<int:pk>/', TrabajoDeleteView.as_view(), name='trabajo_delete'),
    path('exportar-excel/', ExportarTrabajosExcel.as_view(), name='exportar_trabajos_excel'),


    path("calificaciones/", CalificacionListView.as_view(), name="calificacion_list"),
    path("calificaciones/nueva/", CalificacionCreateView.as_view(), name="calificacion_create"),
    path("calificaciones/editar/<int:pk>/", CalificacionUpdateView.as_view(), name="calificacion_update"),
    path("calificaciones/eliminar/<int:pk>/", CalificacionDeleteView.as_view(), name="calificacion_delete"),


        path('seleccionar-trabajo/', views.seleccionar_trabajo, name='seleccionar_trabajo'),
        path('calificar-trabajo/<int:trabajo_id>/', views.calificar_trabajo, name='calificar_trabajo'),


    path('calendario/', calendario_academico, name='calendario'),
    path('calendario/agregar/', agregar_evento, name='agregar_evento'),
    path('calendario/editar/<int:evento_id>/', editar_evento, name='editar_evento'),
    path('calendario/eliminar/<int:evento_id>/', eliminar_evento, name='eliminar_evento'),


    path("reproductor/", reproductor_mp3, name="reproductor_mp3"),
  path('calificaciones/exportar_excel/', exportar_calificaciones_excel, name='exportar_calificaciones_excel'),


 
    path('unidades/', UnidadListView.as_view(), name='unidad_list'),
    path('unidades/nueva/', UnidadCreateView.as_view(), name='unidad_create'),
    path('unidades/editar/<int:pk>/', UnidadUpdateView.as_view(), name='unidad_update'),
    path('unidades/eliminar/<int:pk>/', UnidadDeleteView.as_view(), name='unidad_delete'),
    path('unidades/detalle/<int:pk>/', UnidadDetailView.as_view(), name='unidad_detail'),  # ✅ 
    path('unidades/exportar-word/<int:pk>/', exportar_unidad_word, name='unidad_exportar_word'),  # ✅

     path('unidades/exportar_pdf/<int:pk>/', exportar_unidad_pdf, name='exportar_unidad_pdf'),




    path("temas/", TemaListView.as_view(), name="tema_list"),
    path("temas/<int:pk>/", TemaDetailView.as_view(), name="tema_detail"),
    path("temas/nuevo/", TemaCreateView.as_view(), name="tema_create"),
    path("temas/<int:pk>/editar/", TemaUpdateView.as_view(), name="tema_update"),
    path("temas/<int:pk>/eliminar/", TemaDeleteView.as_view(), name="tema_delete"),


    path('horarios/', listar_horarios, name='listar_horarios'),
    path('horarios/agregar/', agregar_horario, name='agregar_horario'),
    path('horarios/editar/<int:horario_id>/', editar_horario, name='editar_horario'),
    path('horarios/eliminar/<int:horario_id>/', eliminar_horario, name='eliminar_horario'),



    path('ver_horarios/', views.ver_horarios, name='ver_horarios'),
    path('agregar-horario/', agregar_horarioo, name='agregar_horario_profesor'),


    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),




    #path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    
    path('registro/', registro_usuario, name='registro'),

    path('', home, name='home'), 
    path('salida/', salida, name='salida'),









    path('alumnos/detalles/', views.listar_detalles_alumnos, name='listar_detalles_alumnos'),
    path('alumnos/detalles/<int:alumno_id>/', views.ver_detalle_alumno, name='ver_detalle_alumno'),
    path('alumnos/detalles/crear/<int:alumno_id>/', views.crear_detalle_alumno, name='crear_detalle_alumno'),
    path('alumnos/detalles/editar/<int:alumno_id>/', views.editar_detalle_alumno, name='editar_detalle_alumno'),
    path('alumnos/detalles/eliminar/<int:alumno_id>/', views.eliminar_detalle_alumno, name='eliminar_detalle_alumno'),

]


