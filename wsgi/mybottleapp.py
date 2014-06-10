#!/usr/bin/python
# -*- coding : utf-8 -*-

import bottle
from bottle import route, run, template, static_file, get, error, post, request, TEMPLATE_PATH, default_app
import requests
import json
import goslate
import os

@error(500)
def error400(error):
	return template('error')


@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static')
  
@route('/static/<filename>')
def server_static(filename):
	return static_file(filename, root='./static/*css')

@route('/')
def search():
	return template('index')

@get('/corta')
def search_name():
    return template('corta')

@get('/absoluta')
def search_name():
    return template('absoluta')	



@post('/respuesta1')
def busqueda1():
	origin=request.forms.get("origin1")
	destin=request.forms.get("destin1")
	url='http://maps.googleapis.com/maps/api/directions/json'
	obtener=requests.get(url=url,params={'origin':origin,
									   'destination':destin,
									   'region':'ES',
									   'sensor':'false',
									   'avoid':'tolls',
									   'units':'metric',
									   'mode':'BUS'})

	dicc = json.loads(obtener.text.encode("utf-8"))
	
	gs = goslate.Goslate()
	
	listadistancia=['']
	listaduration=['']
	listalatitud=['']
	listalongitud=['']
	listahtml=['']
	contador1=0
	contadores=1
	variable=''
	
	for i in dicc['routes'][0]['legs'][0]['steps']:
		distancia= i['distance']['text']
		duration= i['duration']['text']
		latitud= i['end_location']['lat']
		longitud= i['end_location']['lng']
		html=i['html_instructions']
		html=html.replace('<b>','')
		html=html.replace('</b>','')
		html=html.replace('<div style="font-size:0.9em">','')
		html=html.replace('</div>','')
		html=gs.translate(html, 'es')
		listadistancia.append(distancia)
		listaduration.append(duration)
		listalatitud.append(latitud)
		listalongitud.append(longitud)
		listahtml.append(html)
		contador1=contador1+1
	
	while contadores != contador1:
		variable=variable+'|'+str(listalatitud[contadores])+','+str(listalongitud[contadores])
		contadores=contadores+1
	
	urlmapa='http://maps.googleapis.com/maps/api/staticmap?size=400x400&path=color:0x0000ff|weight:5'
	
	urlfinal=urlmapa+variable
	
	
	return template('result1.tpl', listadistancia=listadistancia,listaduration=listaduration, listahtml=listahtml, origin=origin, destin=destin, contadordor=contador1, urlfinal=urlfinal)
	





@post('/respuesta2')
def busqueda1():
	origin=request.forms.get("origin2")
	destin=request.forms.get("destin2")
	url='http://maps.googleapis.com/maps/api/directions/json'
	obtener=requests.get(url=url,params={'origin':origin,
									   'destination':destin,
									   'region':'ES',
									   'sensor':'false',
									   'avoid':'tolls',
									   'units':'metric',
									   'mode':'BUS'})

	dicc = json.loads(obtener.text.encode("utf-8"))
	
	gs = goslate.Goslate()
	
	listadistancia=['']
	listaduration=['']
	listalatitud=['']
	listalongitud=['']
	listahtml=['']
	contador1=0
	contadores=1
	variable=''
	
	for i in dicc['routes'][0]['legs'][0]['steps']:
		distancia= i['distance']['text']
		duration= i['duration']['text']
		latitud= i['end_location']['lat']
		longitud= i['end_location']['lng']
		html=i['html_instructions']
		html=html.replace('<b>','')
		html=html.replace('</b>','')
		html=html.replace('<div style="font-size:0.9em">','')
		html=html.replace('</div>','')
		html=gs.translate(html, 'es')
		listadistancia.append(distancia)
		listaduration.append(duration)
		listalatitud.append(latitud)
		listalongitud.append(longitud)
		listahtml.append(html)
		contador1=contador1+1
	
	while contadores != contador1:
		variable=variable+'|'+str(listalatitud[contadores])+','+str(listalongitud[contadores])
		contadores=contadores+1
	
	urlmapa='http://maps.googleapis.com/maps/api/staticmap?size=400x400&path=color:0x0000ff|weight:5'
	
	urlfinal=urlmapa+variable
	
	
	return template('result2.tpl', listadistancia=listadistancia,listaduration=listaduration, listahtml=listahtml, origin=origin, destin=destin, contadordor=contador1, urlfinal=urlfinal)




# This must be added in order to do correct path lookups for the views


ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

if ON_OPENSHIFT:
    TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_HOMEDIR'],
                                      'app-root/runtime/repo/wsgi/views/'))
    
    application=default_app()
else:
    run(host='localhost', port=8080)


