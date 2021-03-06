#-*- coding: utf-8 -*-
import urllib,re,sys,os,urllib2
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import main
import urlresolver
from BeautifulSoup import MinimalSoup as BeautifulSoup
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net
net = Net()
reload(sys)
sys.setdefaultencoding( "UTF-8" )


#Megabox - by Kasik 2013.

addon_id = 'plugin.video.megabox'
selfAddon = xbmcaddon.Addon(id=addon_id)
art = main.art
base_url='http://megabox.li/'
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

######################################################################################################################
######################################################################################################################
def MOVIES(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.findall('<a href="([^"]*)"><img alt="[^"]*" src="([^"]*)" /></a><div class="title"><a title="[^"]*" href="[^"]*">([^"]*)</a></div><ul class=\'star-rating\'><li class="current-rating" style="[^"]*"></li></ul><div class="item-genres"><a href="[^"]*">([^"]*)</a>',link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name,genre in match:
                main.addInfo(name+'[COLOR blue] Genre: '+genre+'[/COLOR]',base_url+url,8,thumb,genre,'')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        
        
        
        nextpage=re.compile('<a href="([^"]*)" class="next">Next &#187;</a>').findall(link)
        for url in nextpage:
                main.addDir('Next Page >>',base_url+url,1,art+'/next.png')
                
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()

     
def YOUTUBE(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.findall('<a href="([^"]*)"><img alt="[^"]*" src="([^"]*)" /></a><div class="title"><a title="[^"]*" href="[^"]*">([^"]*)</a></div><ul class=\'star-rating\'><li class="current-rating" style="[^"]*"></li></ul><div class="item-genres"><a href="[^"]*">([^"]*)</a>',link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name,genre in match:
                main.addDir(name+'[COLOR blue] Genre: '+genre+'[/COLOR]',base_url+url,8,thumb,'')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        
        
        
        nextpage=re.compile('<a href="([^"]*)" class="next">Next &#187;</a>').findall(link)
        for url in nextpage:
                main.addDir('Next Page >>',base_url+url,50,art+'/next.png')
                
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()        


def TV(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.findall('<a href="([^"]*)"><img alt="[^"]*" src="([^"]*)" /></a><div class="title"><a title="[^"]*" href="[^"]*">([^"]*)</a></div><ul class=\'star-rating\'><li class="current-rating" style="[^"]*"></li></ul><div class="item-genres"><a href="[^"]*">([^"]*)</a>',link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Shows list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Shows loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name,genre in match:
                main.addDirTE('[COLOR green]'+name+'[/COLOR]'+'[COLOR blue] Genre: '+genre+'[/COLOR]',base_url+url,12,thumb,'','','','','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Shows loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False   
        dialogWait.close()
        del dialogWait
        
        nextpage=re.compile('<a href="([^"]*)" class="next">Next &#187;</a>').findall(link)
        for url in nextpage:
                main.addDir('[COLOR aqua]'+'Next Page >>'+'[/COLOR]',base_url+url,11,art+'/next.png')
                
        xbmcplugin.setContent(int(sys.argv[1]), 'TV')
        main.VIEWS()


def ADULTGENRE(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        site_url = 'http://megabox.li/?genre=adult&accept=1'
        url='http://megabox.li/accept_terms.php'
        post_url = net.http_GET(url).get_url()
        html = net.http_GET(post_url).content
        html = html.encode("utf-8")
        match=re.findall('<a href="([^"]*)"><img alt="[^"]*" src="([^"]*)" /></a><div class="title"><a title="[^"]*" href="[^"]*">([^"]*)</a>', html)
        for url,thumb,name in match:
         main.addDir(name,url,16,thumb,'')
          
        
        nextpage=re.findall('<a href="([^"]*)" class="next">Next &#187;</a>', html)
        for url in nextpage:
          url='http://megabox.li/accept_terms.php'
          post_url = net.http_GET(url).get_url()
          html = net.http_GET(post_url).content
          main.addDir('Next Page >>',base_url+url,17,art+'/next.png')
                










        

################################################################################################################################################
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]


def Seasons(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', USER_AGENT)
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        match=re.compile('<h2>Season ([^"]*)</h2>').findall(link)
        #match.sort() # sort list so it shows season one first
        #match = f7(match)
        for season in match:
                print 'SeAsOn:'+season
                #main.addDir("Season "+season,url,13,'','')
                main.addDirG('[COLOR blue]'+'SEASON '+season+'[/COLOR]',url,13,'',season=season)
        
def Episodes(url,season):
        req = urllib2.Request(url)
        req.add_header('User-Agent', USER_AGENT)
        response = urllib2.urlopen(req)
        link=response.read().replace('&#039;',"'")
        response.close()
        season = str(season)
        print 'SeaSon:'+season
        match=re.compile('<a href="info.php[?]id=([^"]*)&season='+season+'&episode=([^"]*)&tv">[^"]*<span class="ep_title">([^"]*)</span> <span class="total">([^"]*)</span>').findall(link)
        #match.sort() # sort list so it shows first episode first
     
        for linkid,episode,title,links in match:
                url = base_url + 'info.php?id='+linkid+'&season='+season+'&episode='+episode+'&tv'
                name = '[COLOR green]'+"Episode "+episode + '[/COLOR] ' + '[COLOR aqua]'+title + '[/COLOR]  ' + '[COLOR red]' +links+'[/COLOR]'
                main.addDir(name,url,14,'','')
                
def Season2(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=2&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season3(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=3&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season4(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=4&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season5(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=5&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season6(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=6&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season7(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=7&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season8(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=8&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season9(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=9&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season10(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=10&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season11(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=11&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season12(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=12&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season13(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=13&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season14(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=14&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season15(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=15&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season16(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=16&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season17(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=17&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season18(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=18&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season19(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=19&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season20(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=20&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season21(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=21&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season22(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=22&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season23(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=23&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season24(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=24&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season25(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=25&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')
def Season65(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=65&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=1&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')

def Season2013(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=2013&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=2013&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')

def Season2012(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match=re.compile('<div class=".*?"><a href="info.php[?]id=([^"]*)&season=2012&episode=([^"]*)&tv">Episode .*?<span class="ep_title">([^"]*)</span> <span').findall(link)
        for showid,episode,name in match:
                name = '[COLOR green]'+"Episode "+ episode + "[/COLOR]" + '[COLOR teal]'+name+'[/COLOR]'
                url = base_url+'info.php?id='+showid+'&season=2012&episode='+episode+'&tv'
                main.addDir(name,url,14,'','')                












#################################################################################################################################################################################################
def Searchhistory():
    seapath=os.path.join(main.datapath,'Search')
    SeaFile=os.path.join(seapath,'SearchHistoryMB')
    if not os.path.exists(SeaFile):
        SEARCH()
    else:
        main.addDir('Search Movies','###',120,art+'/search.png')
        main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
        for seahis in reversed(searchis):
            url=seahis
            seahis=seahis.replace('%20',' ')
            main.addDir(seahis,url,120,thumb)

def Searchhistorytv():
    seapath=os.path.join(main.datapath,'Search')
    SeaFile=os.path.join(seapath,'SearchHistoryTv')
    if not os.path.exists(SeaFile):
        SEARCHTV()
    else:
        main.addDir('Search Tv Shows','###',135,art+'/search.png')
        main.addDir('Clear History',SeaFile,128,art+'/cleahis.png')
        thumb=art+'/link.png'
        searchis=re.compile('search="(.+?)",').findall(open(SeaFile,'r').read())
        for seahis in reversed(searchis):
            url=seahis
            seahis=seahis.replace('%20',' ')
            main.addDir(seahis,url,135,thumb)            

def SEARCH(url = ''):
        encode = main.updateSearchFile(url,'Movies')
        if not encode: return False   
        surl=base_url + 'index.php?search=' + encode + '&movie=&x=0&y=0'
        link=main.OPENURL(surl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.findall('<a href="([^"]*)"><img alt="[^"]*" src="([^"]*)" /></a><div class="title"><a title="[^"]*" href="[^"]*">([^"]*)</a></div><ul class=\'star-rating\'><li class="current-rating" style="[^"]*"></li></ul><div class="item-genres"><a href="[^"]*">([^"]*)</a>',link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name,genre in match:
                name=name.replace('-','').replace('&','').replace('acute;','').strip()
                main.addInfo(name+'[COLOR blue] Genre: '+genre+'[/COLOR]',base_url+url,8,thumb,genre,'')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False 
        dialogWait.close()
        del dialogWait
        
        nextpage=re.compile('<a href="([^"]*)" class="next">Next &#187;</a>').findall(link)
        for url in nextpage:
                main.addDir('Next Page >>',base_url+url,1,art+'/next.png')
                
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()

def SEARCHTV(url = ''):
        encode = main.updateSearchFile(url,'TV')
        if not encode: return False   
        surl=base_url + 'index.php?search=' + encode + '&tv=&x=0&y=0'
        link=main.OPENURL(surl)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','')
        match = re.findall('<a href="([^"]*)"><img alt="[^"]*" src="([^"]*)" /></a><div class="title"><a title="[^"]*" href="[^"]*">([^"]*)</a></div><ul class=\'star-rating\'><li class="current-rating" style="[^"]*"></li></ul><div class="item-genres"><a href="[^"]*">([^"]*)</a>',link)
        dialogWait = xbmcgui.DialogProgress()
        ret = dialogWait.create('Please wait until Movie list is cached.')
        totalLinks = len(match)
        loadedLinks = 0
        remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
        dialogWait.update(0, '[B]Will load instantly from now on[/B]',remaining_display)
        for url,thumb,name,genre in match:
                name=name.replace('-','').replace('&','').replace('acute;','').strip()
                main.addDir(name+'[COLOR blue] Genre: '+genre+'[/COLOR]',base_url+url,12,'','')
                loadedLinks = loadedLinks + 1
                percent = (loadedLinks * 100)/totalLinks
                remaining_display = 'Movies loaded :: [B]'+str(loadedLinks)+' / '+str(totalLinks)+'[/B].'
                dialogWait.update(percent,'[B]Will load instantly from now on[/B]',remaining_display)
                if (dialogWait.iscanceled()):
                        return False 
        dialogWait.close()
        del dialogWait
        
        nextpage=re.compile('<a href="([^"]*)" class="next">Next &#187;</a>').findall(link)
        for url in nextpage:
                main.addDir('Next Page >>',base_url+url,1,art+'/next.png')
                
        xbmcplugin.setContent(int(sys.argv[1]), 'Movies')
        main.VIEWS()        


     

                
#################################################################################################################################################################################################
















     
################################################################################################################################################


def GRABTVLINKS(url):
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('<img src=images/star.gif>','')
        matchname=re.compile('div align="left"><strong>Watch ([^"]*) on:</strong>').findall(link)
        for name in matchname:
         match = re.findall('<a id="link-[^"]*" href="info.php[?]id=([^"]*)&season=[^"]*&episode=[^"]*&tv&link=([^"]*)&host=([^"]*)">',link)
         for link1,link2,host in match:
                url = base_url + 'player.php?authid=&id='+link1+'&link='+link2+'&type=tv2'
                main.addDown2(name.strip()+" [COLOR blue]"+host.upper()+"[/COLOR]",url,6,'.png','.png')
                xbmcplugin.setContent(int(sys.argv[1]), 'Shows')




          
               
                           

def GRABLINKS(url):
    link=main.OPENURL(url)
    link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('<img src=images/star.gif>','').replace('player=2','') 
    matchname=re.compile('<div align="left"><strong>Watch ([^"]*) on:</strong></div>').findall(link)
    for name in matchname:
     match=re.compile('<a id="link-[^"]*" href="info.php[?]id=([^"]*)&([^"]*)&link=([^"]*)&host=[^"]*"><div class="[^"]*"><span class="([^"]*)"></span></div><div class="[^"]*">([^"]*)</div>').findall(link)
     for link,age,link1,quality,host in match:
      if 'older' in age:    
       url = base_url+ 'player.php?authid=&id='+link+'&link='+link1+'&type=older_v2&part=&site=inactive&ref=1'
       main.addDown2(name.strip()+" [COLOR blue]"+host.upper()+"[/COLOR]",url,6,'.png','.png')
    else:
       match=re.compile('href="info.php[?]id=([^"]*)&link=([^"]*)&host=[^"]*"><div class="[^"]*"><span class="([^"]*)"></span></div><div class="[^"]*">([^"]*)</div>').findall(link)
       for link,link1,quality,host in match:
        url = base_url + 'player.php?authid=&id='+link+'&link='+link1+'&type=new&part=&site=inactive&ref=1'
        main.addDown2(name.strip()+" [COLOR blue]"+host.upper()+"[/COLOR]",url,6,'.png','.png')
      
     
        
###############################################################
def GRABMORE(name,url):
     link=main.OPENURL(url)
     link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\\','')
     match=re.compile('<strong>Watch ([^"]*) on ([^"]*) </strong></span><div class="clear"></div></div><div class="player"><a href="([^"]*)" target').findall(link)
     for name,host,url in match:
      url = base_url + url
      main.addDown2(name + ' ' +host,url,6,'','')
################################################################         
    








def resolveMBurl(url):
    html=main.OPENURL(url)
    match = re.search('<p> Source: <a href="([^>]*)" target',html)
    if match: return match.group(1)
    return        
    match2 = re.search('location.href = \'([^>]*)\';',html)
    if match2: return match.group(2)
    return    
    match3 = re.search('action=\'([^>]*)\'>',html)
    if match3: return match.group(3)
    return        
    match4 = re.search('src="([^>]*)" frameborder="0" allowfullscreen=""></iframe></textarea></p>',html)
    if match4: return match.group(4)
    return        
    match5 = re.search('src=\'([^>]*)\' scrolling=\'no\'></iframe></textarea>',html)
    if match5: return match.group(5)
    return        
        



def PLAY(name,url):
        sources = []
        link=main.OPENURL(url)
        link=link.replace('\r','').replace('\n','').replace('\t','').replace('&nbsp;','').replace('\\','')
        xbmc.executebuiltin("XBMC.Notification(Please Wait!,Opening Link,2000)")
        match=re.compile('<p> Source: <a href="([^>]*)" target').findall(link)
        for url in match:
                hosted_media = urlresolver.HostedMediaFile(url=url)
                sources.append(hosted_media)
        match=re.compile('location.href = \'([^>]*)\';').findall(link)
        for url in match:
                hosted_media = urlresolver.HostedMediaFile(url=url)
                sources.append(hosted_media)
        match=re.compile('action=\'([^>]*)\'>').findall(link)
        for url in match:
                hosted_media = urlresolver.HostedMediaFile(url=url)
                sources.append(hosted_media)
        match=re.compile('src="([^>]*)" frameborder="0" allowfullscreen=""></iframe></textarea></p>').findall(link)
        for url in match:
                hosted_media = urlresolver.HostedMediaFile(url=url)
                sources.append(hosted_media)        
        match=re.compile('src=\'([^>]*)\' scrolling=\'no\'></iframe></textarea>').findall(link)
        for url in match:
                hosted_media = urlresolver.HostedMediaFile(url=url)
                sources.append(hosted_media)
        if (len(sources)==0):
                xbmc.executebuiltin("XBMC.Notification(Sorry!,Show doesn't have playable links,5000)")
      
        else:
                source = urlresolver.choose_source(sources)
                if source:
                        stream_url = source.resolve()
                        if source.resolve()==False:
                                xbmc.executebuiltin("XBMC.Notification(Sorry!,Link Cannot Be Resolved,5000)")
                                return
                else:
                      stream_url = False
                      return
                listitem = xbmcgui.ListItem(name, iconImage="DefaultVideo.png")
                listitem.setInfo('video', {'Title': name, 'Year': ''} )       
                xbmc.Player().play(str(stream_url), listitem)
                main.addDir('','','','')      

       




