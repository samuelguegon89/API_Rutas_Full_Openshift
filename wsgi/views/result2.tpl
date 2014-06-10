<html lang="es">
<html>
	<head>
		<link rel="stylesheet" href="/static/result.css">
		<meta charset="utf-8">
		<title>RutaCortaCalculada</title>
	</head>
	
	<body>
		<h1>Ruta Corta</h1>
		<h2>La ruta a calcular va desde {{ origin }} hasta {{ destin }}:</h2>
			%contador=0
			<div id="cuadro1">
			<p><b>Ruta Gráfica:</b></p>
			<p><img width="300" height="300" src="{{ urlfinal }}" alt="{{ urlfinal }}"/></p>
			</div>
			</br>
			</br>
			<div id="cuadro2">
			%while contador != contadordor:
				%contador=contador+1
				<ul>
					<li><b>Paso: {{ contador }}</b></li>
					<li><b>La distancia es de: {{ listadistancia[contador] }}</b></li>
					<li><b>Duración: {{ listaduration[contador] }}</b></li>
					<li><b>Instrucción: {{ listahtml[contador] }}</b></li>	
				</ul>
				</br>
			%end
				<ul>
					<li><b>Paso: {{ contador+1 }}</b></li>
					<li><b>Instrucción: Llegamos al destino {{ destin }}</b></li>
				</ul>
				</br>
				<ul>
					<li><a href="/">Iniciar otra busqueda</a></li>
				</ul>
			</div>
	</body>
</html>
