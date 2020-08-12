import urllib

site = urllib.urlopen("http://businesscorp.com.br")
server = site.info()

print "O servidor web esta rodando:"
print server ['Server']
