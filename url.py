# url identifier
url = 'https://web.chatgpt.com/yuvaraj'

protocol = url[:url.find(':')]
dot = url.find('.')
domain = url[dot+1 : url.rfind('.')]
slag = url[(url.rfind('/') + 1):]

print('Protocol  : ',protocol)
print('Domain    : ',domain)
print('Slag      : ',slag)