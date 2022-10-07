import webbrowser
import urllib.request   #Libreria para comunicarse con el servidor y hacer scrapping
from bs4 import BeautifulSoup   #Libreria para trabajar con el contenido HTML más facil

def run():
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False
    flag5 = False
    flag6 = False
    flag7 = False
    flag8 = False
    flag9 = False
    flag10 = False

    datos = urllib.request.urlopen('https://dropdaz.com/')    #Pedimos el HTML y entrar a la pag de Dropdaz

    soup =  BeautifulSoup(datos, "html.parser")  #Variable para laburar más facil
    tags = soup('a')
    
    for i in range(1):
        
        for tag in tags:
            
            streamer = tag.get('data-name')
            live = tag.get('data-running')
		
    		
            if streamer == 'frydasolebh' and live == True:
                print("si")

                if flag5 == False: 
                    webbrowser.open_new_tab('https://www.twitch.tv/frydasolebh')
                    flag5 = True

                else:
                    flag5 = False
                    webbrowser.close('https://www.twitch.tv/frydasolebh')

            else:
                continue


if __name__ == "__main__":    #access point
    run()