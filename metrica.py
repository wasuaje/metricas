# -*- coding: utf-8 -*-
import re
import urllib2

sites={"Ultimas Noticias":"www.ultimasnoticias.com.ve",
	"El Universal":"eluniversal.com",
	"El Nacional":"www.el-nacional.com",
	"Gobovision":"www.globovision.com",
	"Noticias 24":"www.noticias24.com",
	"La Patilla":"www.lapatilla.com",
	"La iguana":"www.laiguana.tv"
}



strings={"Chavez":"(Chávez|chávez|Chavez|chavez)","Capriles":"(Radonski|radonski|randosky|Radonsky)"}


total=0
for site in sites.keys():
	print "Site: %s"%site
	req = urllib2.urlopen('http://'+sites[site])
	data =req.read()
	subtotal=0
	for cadena in strings.keys():
		result = len(re.findall(strings[cadena], data))
		subtotal=subtotal+result
		
		print "Total candidato %s: %s"%(cadena,subtotal)
#total=total+subtotal
#print "Total General%s: %s"%(strings.cadena,total)

	

