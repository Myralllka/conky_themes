#!/usr/bin/env python3

import urllib.request
import blessed
term = blessed.Terminal()

import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))


def get_tag(block, tag):
    b_from = block.index(tag) + len(tag)
    b_to   = block.index(tag[:1] + '/' + tag[1:])
    return block[b_from:b_to]

def normalize(text):
    text = text.replace('&amp;', '&')
    text = text.replace('&#39;', '\'')
    return text


with open(CURR_DIR+'/credentials', 'r') as cred:
    email = cred.readline().strip()
    password = cred.readline().strip()

# Set up authentication for gmail
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='mail.google.com',
                          uri='https://mail.google.com/',
                          user=email,
                          passwd=password)
opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)

gmailurl = 'https://mail.google.com/gmail/feed/atom'
with urllib.request.urlopen(gmailurl) as page:
    contents = page.read().decode('utf-8')

blocks = contents.split('<entry>')[1:6]
mails = []
for block in blocks:
    title = get_tag(block, '<title>')
    issued = get_tag(block, '<issued>')
    author_block = block[block.index('<author>')+8:block.index('</author>')]
    author_name = get_tag(author_block, '<name>')
    mails.append([title, issued, author_name])

ifrom = contents.index('<fullcount>') + 11
ito   = contents.index('</fullcount>')

fullcount = contents[ifrom:ito]

print(f'\t{fullcount} unread  ({email})')


max_authorname = 0
after_author_spaces = []
for mail in mails:
    if len(mail[2]) > max_authorname:
        max_authorname = len(mail[2])


for mail in mails:
    if mail[1] != max_authorname:
        after_author_spaces = ''
        while len(after_author_spaces) + len(mail[2]) != max_authorname:
            after_author_spaces += ' '
    time_date = mail[1].strip('Z').split('-')
    time = time_date[1]+'/'+time_date[2][:2]
    date = time_date[2].split(':')[0][3:]+':'+time_date[2].split(':')[1]
    print(normalize(str(time + ' ' + date + '  ' + term.bold(mail[2].upper())+after_author_spaces + ' - ' + mail[0])))
