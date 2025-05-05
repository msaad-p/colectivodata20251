import pandas as pd

asistenciaDataFrame=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#FILTROS

#Estudiantes que asistieron
estdsAsistieron=asistenciaDataFrame.query('estado=="asistio"')
#Estudiantes que faltaron
estdsNoAsistieron=asistenciaDataFrame.query('estado=="inasistencia"')
#Estudiantes que llegaron tarde (justificaron)}
estdsTarde=asistenciaDataFrame.query('estado=="justificado"')
#Estudiantes de estrato 1
estdsEstrato1y2=asistenciaDataFrame.query('estrato==1 or estrato==2')
#Estudiantes de estratos altos (5, 6)
estdsEstrato5y6=asistenciaDataFrame.query('estrato==5 or estrato==6')
#Estudiantes que llegan en metro
estdsLleganEnMetro=asistenciaDataFrame.query('medio_transporte=="metro"')
#Estudiantes que llegan en bici
estdsLleganEnBici=asistenciaDataFrame.query('medio_transporte=="bicicleta"')
#Estudiantes TODOS menos los que llegaron a pie
estdsNoCaminan=asistenciaDataFrame.query('medio_transporte!="a pie"')
#Estudiantes TODOS los registros de asistencia de junio
fechadt=pd.to_datetime(asistenciaDataFrame['fecha'], format='%Y-%m-%d')
registrosJunio=fechadt[fechadt.dt.month==6]
#Estudiantes que usan transportes ecológicos
estdsEcologicos=asistenciaDataFrame.query('medio_transporte=="a pie" or medio_transporte=="bicicleta" or medio_transporte=="metro"')
#Estudiantes que usan bus y son de estrato alto (5,6)
estdsBusEstratoAlto=asistenciaDataFrame.query('medio_transporte=="bus" and (estrato==5 or estrato==6)')
#Estudiantes que usan bus y son de estrato bajo (1,2)
estdsBusEstratoBajo=asistenciaDataFrame.query('medio_transporte=="bus" and (estrato==1 or estrato==2)')
#Estudiantes que caminan para llegar a clase
estdsCaminanAClase=asistenciaDataFrame.query('medio_transporte=="a pie"')

#CONTEOS POR AGRUPACIONES

#Conteo de registros por estado de asistencia (cuantos faltaron de cada cual, cuantos asistieron cuantos no etc)
conteoPorEstadoDeAsistencia=asistenciaDataFrame.groupby('estado').size()
#Numero de regristros por estrato
conteoPorEstrato=asistenciaDataFrame.groupby('estrato').size()
#Cantidad de estudiantes por medio de transporte
conteoEstdsPorMedioTransporte=asistenciaDataFrame.groupby('medio_transporte').size()
#Promedio de estrato por estado de asistencia
promedioAsistenciaPorEstrato=asistenciaDataFrame.groupby('estado')['estrato'].mean()
#Maximo estrato por estado de asistencia
maxEstratoPorEstado=asistenciaDataFrame.groupby('estado')['estrato'].max()
#Minimo estrato por estado de asistencia
minEstratoPorEstado=asistenciaDataFrame.groupby('estado')['estrato'].min()
#Conteo de asistencia por grupo y estado
conteoAsistenciaGrupoYEstado=asistenciaDataFrame.groupby(['id_grupo','estado']).size()