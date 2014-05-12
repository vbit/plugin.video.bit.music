
import util, urllib2
'''


def playVideo(params):
    response = urllib2.urlopen(params['video'])
    if response and response.getcode() == 200:
        content = response.read()
        videoLink = util.extract(content, 'src=\'" + "', '\"')
        print videoLink

    else:
        util.showError(ADDON_ID, 'Could not open URL %s to get video information' % (params['video']))

def buildMenu():
    url = 'http://play.fpt.vn/Video/the-amazing-race-us-season-24-cuoc-dua-ky-thu-my-mua-thu-24/1'
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        links = util.extract(content, 'a href="#">&laquo', 'href="#">&raquo')
        extractLinks = util.extractAll(links,'a href="','"')
        for link in extractLinks:
            params = {'play':1}
            params['title'] = util.extractTitle(link)
            params['video'] = WEB_PAGE_BASE + link
            print params['video']
            print params['title']
            
        
            

WEB_PAGE_BASE = 'http://play.fpt.vn'
ADDON_ID = 'plugin.video.fptplay'

parameters = util.parseParameters()
if 'play' in parameters:
    playVideo(parameters)
else:
    buildMenu()

'''
WEB_PAGE_BASE = 'http://play.fpt.vn'

def buildMenu():
    url = WEB_PAGE_BASE
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        makeLinks = util.extract(content, '"nav navbar-nav menu"', '</ul>')
        links = util.extractAll(makeLinks,'a href="','</a>')
        for link in links:
            params = {'makeCategories':1}
            params['link'] = util.extract(link,'href="','\"')
            #params['title'] = util.extract(link,'/1">','</a>')

    print makeLinks


buildMenu()