# import requests
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json


class Insta_Info_Scraper:
    r_data = {}
    def getinfo(self, url):
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('meta', attrs={'property': 'og:description'})
        text = data[0].get('content').split()
        user = '%s %s %s' % (text[-3], text[-2], text[-1])
        followers = text[0]
        following = text[2]
        posts = text[4]
        self.r_data['posts'] = posts
        self.r_data['user'] = user
        self.r_data['Followers'] = followers
        self.r_data['Following'] = following
        

    def main(self, user_name):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.getinfo('https://www.instagram.com/' + user_name + '/')
        return self.r_data

