import requests

def main():
	response = requests.get("https://thesocialtalks.com")
	#response = requests.get("https://thesocialtalks.com/amit-aps")
	print("Status code", response.status_code)
	print("Headers", response.headers)
	print("--------------------------------------------------------------")
	print("Content-Type", response.headers['Content-Type'])
	print("--------------------------------------------------------------")
	print("Content", response.text) 
if __name__ == "__main__":
	main()

