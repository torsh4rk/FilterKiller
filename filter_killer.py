import requests
from requests import Session
import json, sys
from concurrent.futures import ThreadPoolExecutor
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from datetime import datetime
from time import sleep
import threading


startTime = datetime.now()

def banner():
    print(""""\033[91m
    

  █████▒██▓ ██▓  ▄▄▄█████▓▓█████  ██▀███      ██ ▄█▀ ██▓ ██▓     ██▓    ▓█████  ██▀███  
▓██   ▒▓██▒▓██▒  ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒    ██▄█▒ ▓██▒▓██▒    ▓██▒    ▓█   ▀ ▓██ ▒ ██▒
▒████ ░▒██▒▒██░  ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒   ▓███▄░ ▒██▒▒██░    ▒██░    ▒███   ▓██ ░▄█ ▒
░▓█▒  ░░██░▒██░  ░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄     ▓██ █▄ ░██░▒██░    ▒██░    ▒▓█  ▄ ▒██▀▀█▄  
░▒█░   ░██░░██████▒▒██▒ ░ ░▒████▒░██▓ ▒██▒   ▒██▒ █▄░██░░██████▒░██████▒░▒████▒░██▓ ▒██▒
 ▒ ░   ░▓  ░ ▒░▓  ░▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░   ▒ ▒▒ ▓▒░▓  ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ░      ▒ ░░ ░ ▒  ░  ░     ░ ░  ░  ░▒ ░ ▒░   ░ ░▒ ▒░ ▒ ░░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░    ▒ ░  ░ ░   ░         ░     ░░   ░    ░ ░░ ░  ▒ ░  ░ ░     ░ ░      ░     ░░   ░ 
        ░      ░  ░          ░  ░   ░        ░  ░    ░      ░  ░    ░  ░   ░  ░   ░     
                                                                                        
Trying bypass domains filters and any Protections in Secures Redirects Bypass      by:@TORSh4rk
                                                                              
""")


def_wordlist = "safe-redirect-bypass.txt"

headers = {'X-Forwarded-For':'127.0.0.1','Origin':'127.0.0.1','Location':'127.0.0.1'}

cookies = dict(ROUTEIDPHP='.node1') #Change this cookie value

#Total amount of payloads that worked on the Bypass
qtd_payloads = []


def get_redirect_bypass(url, wordlist):


    global qtd_payloads

    print("\n\033[93m[+] PAYLOADS LIST: {}".format(wordlist))
    print("\n\033[93mTesting all payloads from Wordlist above in URL {}".format(url))
    sleep(2)
    print("\n\n\033[93m[+] PAYLOADS FOUNDS ON WORDLIST\n\n")

    with open(wordlist) as payloads:

        while True:

            pld_bypass = payloads.readline().strip("\n")
        
            try:

                session = Session()
                r = session.get(url + pld_bypass, headers=headers, cookies=cookies, allow_redirects=True, verify=True)
    
                if r.status_code == 403:
                    pass
                elif r.status_code == 404:
                    pass
                #Erro de retornar falso positivo aqui logo abaixo nesse else.
                else:
                    pld_found = pld_bypass
                    print("\t\033[91m-Payload Used:{} ===> (Status Code:{})\n".format(pld_found,r.status_code))
                    qtd_payloads.append(pld_found)

            except:
                pass

            #When all payloads from Wordlist was read and tested
            if not pld_bypass: 
                if len(qtd_payloads) != 0:
                    print("\033[92m\n\nFound {} payloads to do a Secure Redirect Bypass in target".format(len(qtd_payloads)))
                    print("\n\033[92m\nGood Locky and have nice day!\n")
                else:
                    print("\033[91mDidn't find any payload here...Bye!\n")
                    pass
                break


threads = []

if len(sys.argv) == 3:

    for i in range(len(sys.argv[2])):
        threading.Thread(target=get_redirect_bypass)
        threads.append(i)
else:
    for i in range(len(def_wordlist)):
        threading.Thread(target=get_redirect_bypass)
        threads.append(i)



def main():

    if len(sys.argv) == 3:
        banner()
        with ThreadPoolExecutor() as executor:
            executor.map(get_redirect_bypass(sys.argv[1], sys.argv[2]), timeout=10)

    elif len(sys.argv) == 2:
        banner()
        with ThreadPoolExecutor() as executor:
            executor.map(get_redirect_bypass(sys.argv[1], def_wordlist), timeout=10)

    else:
        banner()
        print("\033[91m[-] Warning: Invalid argument numbers!\n")
        print("""\033[93m[+] USAGE EXEMPLE:\n
        python bypass-secure-redirect.py https://www.exemple.com/path your_wordlist_path.txt\n
        Default Wordlist: safe-redirect-bypass.txt\n""")
        print("\033[91m\nPlease, try again...Bye!\n")
        sys.exit()


    #Calculing the tool execution time total
    endTime = datetime.now()
    totalTime = endTime - startTime
    print("\033[93m\n\nCompleted in {}\n".format(totalTime))


if __name__ == '__main__':
    main()

    