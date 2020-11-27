import requests

def main():
	response = requests.get("https://api.exchangeratesapi.io/latest")
	if response.status_code != 200:
		print("Status Code", response.status_code)
		raise Exception("There was an error")
	print("Status code", response.status_code)
	print("--------------------------------------------------------------")
	print("Headers", response.headers)
	print("--------------------------------------------------------------")
	print("Content-Type", response.headers['Content-Type'])
	print("--------------------------------------------------------------")
	data = response.json()
	print("Data", data)	
if __name__ == "__main__":
	main()

