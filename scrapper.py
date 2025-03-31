import csv
import sys
import time
import random
import requests
import re as reg
import pandas as pd
from stem import Signal
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urlparse
from difflib import SequenceMatcher
from stem.control import Controller
from fake_useragent import UserAgent
from colorama import Fore, Style, init

init(autoreset=True)

def printred(text):
    print(Fore.RED + text + Style.RESET_ALL)

def printyellow(text):
    print(Fore.YELLOW + text + Style.RESET_ALL)

def printgreen(text):
    print(Fore.GREEN + text + Style.RESET_ALL)

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

urls = {
    "Ahmia" : "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion",
    "Torch" : "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion",
    "Haystak" : "http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion",
    "Notevil" : "http://notevilcdlnwra7bbxio2rnrrpxyecw6dvodqeelvujf66ja3ssbdcid.onion",
    "Onionlinks" : "http://jaz45aabn5vkemy4jkg4mi4syheisqn2wn2n4fsuitpccdackjwxplad.onion"
}

# session = requests.session()

def banner():
    banner1 = '''
    
    ___  _   _ ___ ___  _   _   ____  _____    _    ____   ____ _   _ _____ ____  
   / _ \| \ | |_ _/ _ \| \ | | / ___|| ____|  / \  |  _ \ / ___| | | | ____|  _ \ 
  | | | |  \| || | | | |  \| | \___ \|  _|   / _ \ | |_) | |   | |_| |  _| | |_) |
  | |_| | |\  || | |_| | |\  |  ___) | |___ / ___ \|  _ <| |___|  _  | |___|  _ < 
 (_)___/|_| \_|___\___/|_| \_| |____/|_____/_/   \_\_| \_\\____|_| |_|_____|_| \_\ 
_____________________________________________________________________________________                                                                          
    '''

    banner2 = '''
     ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █      ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ ▓█████  ██▀███  
    ▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █    ▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
    ▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒   ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░▒███   ▓██ ░▄█ ▒
    ▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒     ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
    ░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██░   ▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒░██▓ ▒██▒
    ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
      ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░   ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
    ░ ░ ░ ▒     ░   ░ ░  ▒ ░░ ░ ░ ▒     ░   ░ ░    ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░   ░     ░░   ░ 
        ░ ░           ░  ░      ░ ░           ░          ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░   ░  ░   ░     
___________________________________________________________________________________________________________________________                                
    '''
    print(random.choice([banner1, banner2]))

def checkConnection():
    try:
        printyellow("Checking IP to confirm it's via Tor")

        response = requests.get("http://check.torproject.org", proxies=proxies, timeout=10)
        
        if "Congratulations. This browser is configured to use Tor." in response.text:
            printgreen("[SUCCESS:] Tor connection is established.")
            return True
        else:
            printred("[ERROR:] Not connected to Tor.")
            return False
    except requests.RequestException as e:
        printred(f"[ERROR:] Cannot access tor or Connection failed > {e}")
        exit()

def changeMe():
    headers = { 'User-Agent': UserAgent().random }


    try:
        with Controller.from_port(port=9051) as c:
            c.authenticate()
            c.signal(Signal.NEWNYM)
            printyellow("New Tor circuit requested.")
        
        # Confirm IP change
        ip = requests.get('https://ident.me', proxies=proxies, headers=headers).text
        printgreen(f"Your IP is: {ip}  ||  User Agent is: {headers['User-Agent']}")
    except Exception as e:
        printred(f"[ERROR:] In changing profile > {e}")

    return headers, proxies

def get_request_params(url, user_agent=None, extra_headers=None):
    headers, proxies = changeMe()
    
    if extra_headers:
        headers.update(extra_headers)
    
    return {
        'url': url,
        'headers': headers,
        'proxies': proxies
    }

def fetch_data(url, user_agent=None, extra_headers=None, timeout=10):
    session = requests.Session()
    params = get_request_params(url, user_agent, extra_headers)
    params['timeout'] = timeout

    try:
        response = session.get(**params)
        response.raise_for_status()
        return response.content

    except requests.exceptions.Timeout:
        printred(f"[ERROR:] Request timed out >{e}")
        return None
    except requests.exceptions.RequestException as e:
        printred(f"[ERROR:] Request failed >{e}")
        return None

def queryAhmia(query, isLimited = 0):
    output = []
    try:
        url = f"{urls['Ahmia']}/search/?q={query}"
        response = fetch_data(url)
        print(f'Searching Ahmia for : {query} : {url}')
        soup = BeautifulSoup(response, 'html.parser')
        result = soup.find_all("li", attrs={"class" : "result"})

        for item in result:
            try:
                title = item.find("a").contents[0].text
                title = ' '.join(title.split())

                description = item.find("p").text
                category = checkCategory(description)
                category.extend(x for x in checkCategory(title) if x not in category)
                if len(category) > 1 and 'Uncategorised' in category:
                    category.remove('Uncategorised')
                onionURL = item.find("cite").text
                lastSeen = item.find("span", attrs={"class":"lastSeen"})['data-timestamp']
                timestamp = datetime.now()
                temp = {
                    "timestamp" : timestamp,
                    "sourceName" : "Ahmia.fi",
                    "searchTerm" : query,
                    "sourceURL" : url,
                    "title" : title,
                    "description" : description,
                    "originalURL" : onionURL,
                    "onionURL" : onionURL,
                    "category" : category,
                    "lastSeen" : lastSeen
                }
                output.append(temp)
            except Exception as e:
                printred(f'[ERROR:] saving from ahmia > {e}')
        
        return output
    except Exception as m:
        printred(f'[ERROR:] reaching ahmia > {m}')
        return output

def queryTorch(query, isLimited = 20):
    output = []
    try:
        url = f"{urls['Torch']}/cgi-bin/omega/omega?P={query}"
        print(f'Searching Torch for : {query} : {url}')
        for i in range (1, isLimited): 
            urli = f"{url}&[={str(i)}"

            response = fetch_data(urli) 
            soup = BeautifulSoup(response, 'html.parser')
            result = soup.find_all("tr")
            
            for item in result:
                try:
                    title = item.find("a").contents[0].text
                    title = ' '.join(title.split())

                    description = item.find("small").text
                    category = checkCategory(description)
                    category.extend(x for x in checkCategory(title) if x not in category)
                    if len(category) > 1 and 'Uncategorised' in category:
                        category.remove('Uncategorised')
                    originalURL = item.find("a")["href"]
                    parsed_url = urlparse(originalURL)
                    onionURL = parsed_url.scheme+ "://" + parsed_url.netloc

                    timestamp = datetime.now()
                    lastSeen = '0'
                    temp = {
                        "timestamp" : timestamp,
                        "sourceName" : "Torch",
                        "searchTerm" : query,
                        "sourceURL" : url,
                        "title" : title,
                        "description" : description,
                        "originalURL" : originalURL,
                        "onionURL" : onionURL,
                        "category" : category,
                        "lastSeen" : lastSeen
                    }
                    output.append(temp)
                except Exception as n:
                    return output
                    printred(f'[ERROR:] Saving From Torch > {n}')
        return output
    except Exception as m:
        printred(f'[ERROR:] Reaching Torch > {m}')
        return output

def queryNotevil(query, isLimited = 30):
    output = []
    try:
        url = f"{urls['Notevil']}/search?search={query}"
        print(f'Searching "Not Evil" for : {query} : {url}')
        
        for i in range (1, isLimited): 
            urli = f"{url}&page={str(i)}"

            response = fetch_data(urli) 
            soup = BeautifulSoup(response, 'html.parser')
            page_number = soup.find("span", attrs={"class": "page-numbers"}).text 
            match = reg.search(r"/\s*(\d+)", page_number)
            
            if match:
                printyellow(f"Match :  {match.group(1)}")
                isLimited = match.group(1)
            else:
                printred("No Match For Page Number")

            result = soup.find_all("div", attrs={"class": "custom-result-item"})            
            for item in result:
                try:
                    title = item.find("h2", attrs={"class": "custom-result-title"})
                    title = title.find("a").contents[0].text
                    title = ' '.join(title.split())

                    description = item.find("p", attrs={"class":"custom-result-description"}).text
                    category = checkCategory(description)
                    category.extend(x for x in checkCategory(title) if x not in category)
                    if len(category) > 1 and 'Uncategorised' in category:
                        category.remove('Uncategorised')
                    originalURL = item.find("p", attrs={"class":"custom-result-url"}).text
                    parsed_url = urlparse(originalURL)
                    onionURL = parsed_url.scheme+ "://" + parsed_url.netloc

                    timestamp = datetime.now()
                    lastSeen = '0'
                    temp = {
                        "timestamp" : timestamp,
                        "sourceName" : "Not Evil",
                        "searchTerm" : query,
                        "sourceURL" : url,
                        "title" : title,
                        "description" : description,
                        "originalURL" : originalURL,
                        "onionURL" : onionURL,
                        "category" : category,
                        "lastSeen" : lastSeen
                    }
                    output.append(temp)
                except Exception as e:
                    printred(f'[ERROR:] Saving From Not Evil > {e}')
        return output
    except Exception as m:
        printred(f'[ERROR:] reaching not evil > {m}')
        return output

def checkCategory(description):
    categories = {
        'Carding' : ['cvv', 'carding', 'dump', 'skimmer', 'skimming', 'cc', 'carded', 'paypal'],
        'Hacking' : ['ransomware', 'ddos', 'hacking', 'hack', 'phishing', 'dos', 'exploit', 'zero day', 'rat', 'malware', 'stealer', 'leaked'],
        'Market' : ['sell', 'vendor', 'market', 'shop', 'store', 'marketplace'],
        'Drugs' : ['meth', 'cocain', 'drugs', 'heroin'],
        'Fraud' : ['scam', 'fraud', 'counterfiet', 'theft', 'license'],
        'Forums' : ['forum', 'chat', 'room', 'commmunity', 'discussion', 'Форум'],
        'Killing' : ['hitman', 'killer'],
        'Links' : ['wiki', 'links'],
        'Hosting' : ['hosting', 'server', 'domain'],
        'NSFW' : ['nsfw', 'porn', 'cp'],
    }
    description_lower = description.lower()
    matched_categories = []
    for category, keywords in categories.items():
        if any(keyword in description_lower for keyword in keywords):
            matched_categories.append(category)

    if matched_categories:
        return matched_categories
    else:
        return ['Uncategorised']

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def drop_similar_titles(re, threshold=0.6):
    mask = pd.Series([True] * len(re))
    for i in range(len(re)):
        if not mask[i]:
            continue
        for j in range(i+1, len(re)):
            if re.iloc[i]['onionURL'] == re.iloc[j]['onionURL'] and similar(re.iloc[i]['title'], re.iloc[j]['title']) >= threshold:
                mask[j] = False
    return re[mask]

def createData(input):

    try:
        re = pd.DataFrame(input)
        re = re.sort_values("onionURL", ascending=True).reset_index()
        # re.to_csv(f"RAW_{datetime.now()}.csv", quoting=csv.QUOTE_ALL)
        # re = re.drop_duplicates(subset=['title', 'onionURL'], keep='first').reset_index()
        # re = drop_similar_titles(re)
        file_name = f'FILTERED_{datetime.now()}.csv'
        try:
            re.to_csv(file_name, quoting=csv.QUOTE_ALL)
            printgreen(f"[SUCCESS:] Filtered Results saved as {file_name}")
        except Exception as e:
            print(e)
            printred(f'[ERROR:] While saving to as csv >{e}')
            return
    except Exception as e:
        print(e)
        printred(f'[ERROR:] While creating dataframe >{e}')


def main():

    if len(sys.argv) < 2:
        print("Usage: python script.py <search_query>")
        return
    
    if not checkConnection():
        exit()
    
    search_query = ' '.join(sys.argv[1:])
    print(f"Searching for: {search_query}")
    

    results = []
    try: 
        results += queryAhmia(search_query)
        printgreen(f'[SUCCESS:] Results From Ahmia Returned')
    except Exception as e:
        printred(f"[ERROR:] While Appending Results From Ahmia > {e}")

    try: 
        results += queryTorch(search_query)
        printgreen(f'[SUCCESS:] Results From Torch Returned')
    except Exception as n:
        printred(f"[ERROR:] While Appending Results From Torch > {n}")

    try: 
        results += queryNotevil(search_query)
        printgreen(f'[SUCCESS:] Results From Not Evil Returned')
    except Exception as e:
        printred(f"[ERROR:] While Appending Results From Not Evil > {e}")
    
    createData(results)

if __name__ == "__main__":
    banner()
    main()