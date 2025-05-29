

import requests, os
req = requests.Session()
from pystyle import Colorate, Colors, Add, Center, Write, Anime, Box

def getBanner():
	bannerText = """

"""
	
	bannerLogo = """
               ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░  
               ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
               ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
               ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓███████▓▒░  
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
         ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 

                                                                                    
"""

	banner = Colorate.Vertical(Colors.red_to_yellow, Center.Center(Add.Add(bannerLogo, bannerText, 0)), 1)
	return banner
def masscheck():
    cookiefilefolder = os.path.dirname(__file__)
    cookiefile = (cookiefilefolder + "\cookies.txt")
    cookie = open(cookiefile).read().splitlines()
    print(getBanner())
    Printing = Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(f"[Total Rap]: 0 | [Total robux]: 0 | [Total pending]: 0 | [Total stipends]: 0 | [Total credits]: 0 | [Total followers]: 0\n"))
    print(Printing)
    validcount = 0
    invalidcount = 0
    robux = 0
    credit = 0
    rap = 0 
    pending = 0
    followers = 0
    stipends = 0
    i = 0
    if len(cookie) > 0:
        print(str(len(cookie)) + " Cookie(s) Found")
        print(" ")
        pathnameforvalid = os.path.join(os.path.dirname(__file__), "validcookies.txt")
        newfileforvalid = open(pathnameforvalid, "w")
        newfileforvalid.truncate(0)
        pathnameforinvalid = os.path.join(os.path.dirname(__file__), "invalidcookies.txt")
        newfileforinvalid = open(pathnameforinvalid, "w")
        newfileforinvalid.truncate(0)
        
        for line in cookie:
            
            
            check = requests.get('https://accountsettings.roblox.com/v1/email', cookies={'.ROBLOSECURITY': str(line)})
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            print(getBanner())
            Printing = Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(f"[Total Rap]: {rap} | [Total robux]: {robux} | [Total pending]: {pending} | [Total stipends]: {stipends} | [Total credits]: {credit} | [Total followers]: {followers}\n"))
            print(Printing)
            if check.status_code == 200:
                newfileforvalid.write(str(line) + "\n")
                validcount += 1
                i+=1
                userdata = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":line}).json() #get user data
                userid = userdata['id'] #user id
                transactions = requests.get(f"https://economy.roblox.com/v2/users/{userid}/transaction-totals?timeFrame=Month&transactionType=summary", cookies={'.ROBLOSECURITY': str(line)}, data={'timeFrame':'Month', 'transactionType': 'summary'}).json()
                pending += transactions['pendingRobuxTotal']
                credit += requests.get("https://billing.roblox.com/v1/credit", cookies={'.ROBLOSECURITY': str(line)}).json()['balance']
                stipends += transactions['premiumStipendsTotal']
                groups = requests.get(f"https://groups.roblox.com/v1/users/{userid}/groups/roles", cookies={'.ROBLOSECURITY': str(line)})
                groupIds = [i['group']['id'] for i in groups.json()['data'] if i['group']['owner']['userId'] == userid]
                groupFunds = 0
                followers += requests.get(f"https://friends.roblox.com/v1/users/{userid}/followers/count", cookies={'.ROBLOSECURITY': str(line)}).json()['count']
                for i in groupIds:
                    groupFunds += int(requests.get(f"https://economy.roblox.com/v1/groups/{i}/currency", cookies={'.ROBLOSECURITY': str(line)}).json()['robux'])
                robuxdata = requests.get(f'https://economy.roblox.com/v1/users/{userid}/currency',cookies={".ROBLOSECURITY":line}).json() 
                robux += robuxdata['robux'] #get robux balance
                rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":line}).json()
                while rap_dict['nextPageCursor'] != None:
                    rap_dict = requests.get(f'https://inventory.roblox.com/v1/users/{userid}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100',cookies={".ROBLOSECURITY":line}).json()
                rap += sum(i['recentAveragePrice'] for i in rap_dict['data'])
                if os.name == "nt":
                    os.system("cls")
                else:
                    os.system("clear")
                print(getBanner())
                Printing = Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(f"[Total Rap]: {rap} | [Total robux]: {robux} | [Total pending]: {pending} | [Total stipends]: {stipends} | [Total credits]: {credit} | [Total followers]: {followers}\n"))
                print(Printing)
            else:
                newfileforinvalid.write(str(i) + "\n")
                invalidcount += 1
                i+=1
        Total = Colorate.Vertical(Colors.red_to_yellow, Center.XCenter(f"Valid Cookie(s): " + str(validcount) + "\nInvalid Cookie(s): " + str(invalidcount)))
        print(Total)

        Write.Input("Press any key to exit", Colors.orange, interval=0.0025)
    else:
        print("No cookies found.")


masscheck()


    
