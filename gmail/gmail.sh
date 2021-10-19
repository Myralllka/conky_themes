#!/usr/bin/sh

curl -s -u email:passwd https://mail.google.com/mail/feed/atom | grep fullcount | sed 's/<[^0-9]*>//g'
