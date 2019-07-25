
import urllib.parse

url =r'https://wer.coms/i733/8734.html' 
url, frag = urllib.parse.urldefrag(url)


print(url+'   2222    '+frag)