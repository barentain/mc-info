import requests, json, logging

minecraft_name = input("[!] Enter a MC username: ")

def converttostr(input_seq, seperator):
   # Join all the strings in list
   final_str = seperator.join(input_seq)
   return final_str

def req(name):
	try:
		resp = requests.get("https://api.ashcon.app/mojang/v2/user/" + name)
		data = json.loads(resp.text)

		print("[*] Username: " + data["username"])
		print("[*] UUID: " + data["uuid"])
		if data["created_at"] == None:
			print("[*] Created: Not Found")
		else:
			print("[*] Created: " + data["created_at"])
		print("\n[*] Name History: ")

		# Checking for username history
		for names in data["username_history"]:
			try:
				print(" - " + names["username"] + f"(Changed {data['changed_at']})")
			except:
				print(" - " + names["username"])
	
	except Exception as x:
		logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
		logging.critical(x)

req(minecraft_name)
