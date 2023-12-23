from bs4 import BeautifulSoup
import requests
from chessdotcom import get_player_profile, get_player_stats, Client

def USCF_player_lookup(id: str):
    url = f"https://www.uschess.org/msa/thin.php?{id}"
    res = requests.get(url)
    
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        inps = soup.find_all("input")
        data_json = {
            "uscf_id" : inps[0]['value'],
            "suppl_date" : inps[2]['value'],
            "expires" : inps[3]['value'],
            "name" : inps[4]['value'],
            "reg_rating" : inps[5]['value'],
            "quick_rating": inps[6]['value'],
            "blitz_rating": inps[7]['value'],
            "onl_reg_rating": inps[8]['value'],
            "onl_quick_rating": inps[9]['value'],
            "onl_blitz_rating": inps[10]['value'],
            "region": inps[11]['value'],
            "FIDE_country_is": inps[12]['value'],
            "FIDE_rating" : inps[13]['value']
        }
        return data_json
        

def chesscom_player_lookup(username):
    Client.request_config["headers"]["User-Agent"] = (
    "My Python Application. "
    "Contact me at email@example.com"
    )
    profile_res = get_player_profile(username)
    stats_res = get_player_stats(username)
    player_profile = profile_res.json
    player_stats = stats_res.json

    final_data = {
        "profile": player_profile,
        "stats": player_stats,
    }
    return final_data
    

def MA():
    url = "http://www.masschess.org/Events/chess-event-list.aspx"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    event_name = soup.find_all('td', class_="txt_left")
    event_name = [name.text.strip() for name in event_name]
    
    organizer = []
    date = []
    
    for i,data in enumerate(soup.find_all("td", class_="txt_center")):
        if i % 2:
            organizer.append(data.text.strip())
        else:
            date.append(data.text.strip())
            
    event_objs = []
    for i in range(len(date)):
        event_objs.append({
            "event_name":event_name[i],
            "organizer": organizer[i],
            "date": date[i]
        })
        
    return event_objs

print(chesscom_player_lookup("swayam4321"))