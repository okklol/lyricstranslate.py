# this program will fail sometimes, sorry :')

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import dbus

def get_song_name():
    try:
        session_bus = dbus.SessionBus()
        spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                            "/org/mpris/MediaPlayer2")
        spotify_properties = dbus.Interface(spotify_bus,
                                            "org.freedesktop.DBus.Properties")
        metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    except:
        print('no track currently playing')
        quit()
    try:
        return(metadata['xesam:title'])
    except:
        print('error')
        quit()

def get_soup_0 ():
    options = webdriver.FirefoxOptions() # define webdriver options
    options.add_argument('--headless') # add arfguments to webdriver options
    browser = webdriver.Firefox(options=options, service=Service(executable_path='/bin/geckodriver')) # define webdriver
    browser.get('https://lyricstranslate.com/en/site-search?query=' + get_song_name()) # open url
    html = browser.page_source # get html
    soup0 = BeautifulSoup(html, 'lxml').find('a', class_="gs-title")['href'] # get soup0
    browser.quit() # quit broweser
    return soup0 # return soup0

def main ():
    soup = BeautifulSoup(requests.get(get_soup_0()).content, 'html.parser') # get soup using soup0
    a = soup.find('div', {'class': 'translate-node-text'}) # find lyrics
    print(a.text) # print lyrics

if __name__ == "__main__":
   main()