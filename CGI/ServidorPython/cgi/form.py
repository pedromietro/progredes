#!/usr/bin/env python
#coding: utf8
import os, cgi
form = cgi.FieldStorage()
print "Content-type: text/html; charset=utf-8"
print
print "<html><head><title>Post Example</title></head><body>"
print "Nome: "+ form["nome"].value + "<br>"
print "Endereço: "+ form["end"].value + "<br>"
print "Sexo: "+ form["sexo"].value + "<br>"
print "</body></html>"