import requests

URL = "https://crumbs.web.actf.co/"
responses = ['61f57d99-6d8e-4e5e-bfc1-995dc358fce7'] #FirstString

for flag in responses:
	r = requests.get(URL + flag).text
	print (str(responses)+flag)

	if "actf" not in r:
		repeat = r.strip("Go to")
		responses.append(repeat)

	else: 
		print("Flag = " + r)
