#!/usr/bin/python
# vim: set fileencoding=UTF-8 :

import urllib
import codecs
from xml.dom import minidom

email = 'bohdan.mandziuvatyi.kb.2019@lpnu.ua'  # your email here..feel free to ommit the '@...' suffix
passwd = '19.11.2001'  # your password here

url = 'https://%s:%s@mail.google.com/mail/feed/atom' % (email, passwd)

dom = minidom.parse(urllib.urlopen(url))

count = dom.getElementsByTagName('fullcount')[0].childNodes[0].nodeValue

names = []
sums = []

for n in dom.getElementsByTagName('name'):
    name = n.childNodes[0].nodeValue.encode("utf-8")
    names.append(name)
    # print name

for s in dom.getElementsByTagName('summary'):
    summary = s.childNodes[0].nodeValue.encode("utf-8")
    sums.append(summary)
    # print summary

print("You got " + count + " new mails  \n ")
mail = dict(zip(names, sums))
for k, v in mail.iteritems():
    print("{:<12} {:<12}".format(k, v))
# for key, value in mail.items():
    # print key, value
