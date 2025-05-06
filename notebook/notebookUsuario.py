import pandas as pd

usuariosDataFrame=pd.read_excel("./data/usuarios_sistema_completo.xlsx")

#FILTROS

#Tabla con estudiantes
tablaEstds=usuariosDataFrame.query('tipo_usuario=="estudiante"')
#Tabla con docentes
tablaDocentes=usuariosDataFrame.query('tipo_usuario=="docente"')
#Listado de especialistas en desarrollo web o sistemas
especialistasWeb=usuariosDataFrame.query('especialidad=="Ingenieria de Sistemas" or especialidad=="Desarrollo Web"')
#Usuarios que vivan en Medellín
usuariosMedellin=usuariosDataFrame.query('direccion.str.contains(", Medellín,")')
#Usuarios cuyas direcciones terminen en Sur
usuariosSur=usuariosDataFrame.query('direccion.str.contains(" Sur,")')
#Listado de profes que tengan la palabra "datos" en su rol
profesDatos=usuariosDataFrame.query('especialidad.str.contains("datos", case=False)')
#Docentes de Itagüí
docentesItagui=usuariosDataFrame.query('tipo_usuario=="docente" and direccion.str.contains(", Itagüí,")')
#Nacidos en los 90 o antes (del 90 o antes)
nacidosAntesDel90=usuariosDataFrame.query('fecha_nacimiento <= "1990-12-31"')
#Instructores o profesores mayores
fechadtu=pd.to_datetime(usuariosDataFrame['fecha_nacimiento'], format='%Y-%m-%d')
mayoresDe50=usuariosDataFrame.query('(2025-fechadtu.dt.year)>50')
#Usuarios nacidos del 2000 o después
nacidosDespuesDel2000=usuariosDataFrame.query('fecha_nacimiento >= "2000-01-01"')