import requests

site = requests.get("http://businesscorp.com.br/")
status = site.status_code

if (status == 200):
	print "pagina existe"
else:
	print "pagina nao existe"

