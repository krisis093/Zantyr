import requests
import re
def bubs(client, message):
	if message.content == "Zantyr, pokaż cycki":
		r = requests.get('http://oboobs.ru/a/')
		s = re.search('<div class="dimage"><img src="(.*?)"', r.text)
		return r.text[s.start()+30:s.end()-1]

EXPORT = [bubs]