<html>
	<head>
		<title>Ruta Absoluta</title>
		<link rel="stylesheet" href="/static/menu1.css">
	</head>
	<body>
		<h1>Ruta Absoluta</h1>
		<div id="cuadro">
		<form action="/respuesta1" method="POST">
			<div id="cuadro1">
			<b>Lugar Origen:</b>  <input name="origin1" type="text"/>
			</div>
			<div id="cuadro2">
			<b>Lugar Destino:</b> <input name="destin1" type="text"/>
			</div>
			<div id="cuadro3">
			<input value="Iniciar" type="submit"/>
			</div> 
		</form>
		<div id="cuadro4">
		<form action="/" method="GET">
			<input type="submit" value="Volver">
		</div>
		</form>
		</div>
	</body>
</html>
