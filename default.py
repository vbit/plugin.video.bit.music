
import util, urllib2
import xbmc

def playVideo(params):
    link = WEB_PAGE_BASE + params['link']
    response = urllib2.urlopen(link)
    if response and response.getcode() == 200:
        content = response.read()
        videoLink = util.extract(content, "source src='", "'")
        util.playMedia(params['title'], params['image'], videoLink, 'Video')
    else:
        util.showError(ADDON_ID, 'Could not open URL %s to get video information' % (params['video']))

def buildCategories():
    url = WEB_PAGE_BASE + '/the-loai/music'
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        links = util.extractAll(content, 'idscroll="', '<ul class="thumn">')
        for link in links:
            params = {'makeCategories':1}
            params['link'] = util.extract(link,'href="','\"')
            params['title'] = util.extract(link,'/1">','</a>')
            link = util.makeLink(params)
            util.addMenuItem(params['title'], link, 'DefaultVideo.png', 'DefaultVideo.png', True)

        util.endListing()
        xbmc.executebuiltin("Container.SetViewMode(506)")
        
        
    else:
        util.showError(ADDON_ID, 'Could not open URL CATEGORIES %s to create menu' %(url))

def buildPlay(inputParams):
    url = WEB_PAGE_BASE + inputParams['link']
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        links = util.extractAll(content, '<div class="col">', '</span>')
        for link in links:
            params = {'makePlay':1}
            params['title'] = util.extract(link,'data-original-title="','\"')
            params['link'] = util.extract(link,'href="','\"')
            params['image'] = util.extract(link,'img src="','"')
            link = util.makeLink(params)
            util.addMenuItem(params['title'], link, params['image'], params['image'], True)
        util.endListing()
        xbmc.executebuiltin("Container.SetViewMode(506)")

    else:
        util.showError(ADDON_ID, 'Could not open URL SHOW %s to create menu' %(url))

WEB_PAGE_BASE = 'http://play.fpt.vn'
ADDON_ID = 'plugin.video.bit.tvshow'

parameters = util.parseParameters()

if 'makePlay' in parameters:
    playVideo(parameters)
elif 'makeCategories' in parameters:
    buildPlay(parameters)
else:
    buildCategories()




    



