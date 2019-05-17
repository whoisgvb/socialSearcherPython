import sys, requests
global nickname
import webbrowser
argument = sys.argv
print("""
      ___           ___     
     /  /\         /  /\    
    /  /:/_       /  /:/_   
   /  /:/ /\     /  /:/ /\  
  /  /:/ /::\   /  /:/ /::\ 
 /__/:/ /:/\:| /__/:/ /:/\:|
 \  \:\/:/~/:/ \  \:\/:/~/:/
  \  \::/ /:/   \  \::/ /:/ 
   \__\/ /:/     \__\/ /:/  
     /__/:/        /__/:/   
     \__\/         \__\/    
  Social Searcher v1.0 by GVB
# EM BREVE NOVAS FUNCIONALIDES #
""")

def open(url):
  	webbrowser.open_new_tab(url)

def facebook():
			url = "https://m.facebook.com/"+nickname
			r = requests.get(url) # request na URL
			check = r.status_code # checka status (200 OK)
			if check == 200:
				print(f"[ + ] FACEBOOK > {url}")
				open(url)
			else: # caso nao, retorna erro e nao abre nada
				print(f"[ - ] NOT FOUND FACEBOOK OF THIS PERSON {url}")

def twitter():
			url = "https://twitter.com/"+nickname
			r = requests.get(url) 
			check = r.status_code 
			if check == 200: # se status 200 retorna BOM e abre a URL
				print(f"[ + ] TWITTER > {url}")
				open(url)
			else: # caso nao, retorna erro e nao abre nada
				print(f"[ - ] NOT FOUND TWITTER OF THIS PERSON {url}")

def instagram():
			url = "https://www.instagram.com/"+nickname
			r = requests.get(url)
			check = r.status_code
			if check == 200: 
				print(f"[ + ] INSTAGRAM > {url}")
				open(url)
			else: 
				print(f"[ - ] NOT FOUND INSTAGRAM OF THIS PERSON {url} ")

if argument[1] == "--help":
  			print("""
> --facebook for facebook page
> --instagram for instagram page
> --twitter for twitter page
> --all for all =)
Example: python3 socialSearcher.py whoisgvb --all
				""")
else:
			if len(argument) == 3: 
					nickname = argument[1]   
					if argument[2] == "--all": 
						facebook()
						twitter()
						instagram()
					elif argument[2] == "--facebook": 
						facebook()
					elif argument[2] == "--twitter":
						twitter()
					elif argument[2] == "--instagram":
						instagram()
					elif argument[2] != "--all" or argument[2] != "--facebook" or argument[2] != "--twitter" or argument[2] != "--instagram":
  						print("[ ! ] INVALID")
