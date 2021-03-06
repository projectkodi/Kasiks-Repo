import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urllib,urllib2,re,cookielib,string,urlparse,os,time,datetime,threading
from BeautifulSoup import BeautifulSoup
try:
    import urlresolver
    from t0mm0.common.net import Net as net
    from t0mm0.common.addon import Addon
    from metahandler import metahandlers

    
except Exception, e:
    elogo = xbmc.translatePath('special://home/addons/plugin.video.vdeobull/resources/art/sadface.png')
    dialog = xbmcgui.Dialog()
    ok=dialog.ok('[B][COLOR=FF67cc33]VideoBull Import Error[/COLOR][/B]','Failed To Import Needed Modules',str(e),'Report missing Module at [COLOR=FF67cc33]Xbmchub.com[/COLOR] to Fix')
    xbmc.log('VideoBull ERROR - Importing Modules: '+str(e))

    
from resources.src import main
from resources.src.scripts import settings


#VideoBull.com - by Kasik 2013.


base_url ='http://videobull.com/'
addon_id = 'plugin.video.vdeobull'
selfAddon = xbmcaddon.Addon(id=addon_id)
grab = metahandlers.MetaData(preparezip = False)
addon = Addon(addon_id)
art = main.art

AddonPath = addon.get_path()
IconPath = AddonPath + "/resources/art/"




UpdatePath=os.path.join(main.datapath,'Update')
try:
    os.makedirs(UpdatePath)
except: pass
ListsPath=os.path.join(main.datapath,'Lists')
try:
    os.makedirs(ListsPath)
except: pass

############################# Main ###########################################################################################
      
def MAIN():
        main.addDirHome('Search TV Shows',base_url,10,art+'/search.png')
        main.addDirHome('Latest TV Shows',base_url,1,art+'latest.png')
        main.addDirHome('Popular Shows',base_url,2,art+'popular.png')
        main.addDirHome('All Tv Shows',base_url+'tv-shows/',3,art+'AZ.png')

#############################################################################################################################                


def getListFile(url, path, excepturl = None ):
        link = ''
        t = threading.Thread(target=setListFile,args=(url,path,excepturl))
        t.start()
        if not os.path.exists(path):
            t.join()
        if os.path.exists(path):
            try: link = open(path).read()
            except: pass
        return link       
def setListFile(url, path, excepturl = None):
        content = None
        try:
            content=main.OPENURL(url, verbose=False)
        except:
            if excepturl:
                content=main.OPENURL(excepturl, verbose=False)
        if content:
            try:
                open(path,'w+').write(content)
            except: pass
        return

################################################################################ Message Box ##########################################################################################################

def Message():
    help = SHOWMessage()
    help.doModal()
    del help


class SHOWMessage(xbmcgui.Window):
    def __init__(self):
        self.addControl(xbmcgui.ControlImage(0,0,1280,720,art+'/infoposter.png'))
    def onAction(self, action):
        if action == 92 or action == 10:
            xbmc.Player().stop()
            self.close()

def TextBoxes(heading,anounce):
        class TextBox():
            """Thanks to BSTRDMKR for this code:)"""
                # constants
            WINDOW = 10147
            CONTROL_LABEL = 1
            CONTROL_TEXTBOX = 5

            def __init__( self, *args, **kwargs):
                # activate the text viewer window
                xbmc.executebuiltin( "ActivateWindow(%d)" % ( self.WINDOW, ) )
                # get window
                self.win = xbmcgui.Window( self.WINDOW )
                # give window time to initialize
                xbmc.sleep( 500 )
                self.setControls()


            def setControls( self ):
                # set heading
                self.win.getControl( self.CONTROL_LABEL ).setLabel(heading)
                try:
                        f = open(anounce)
                        text = f.read()
                except:
                        text=anounce
                self.win.getControl( self.CONTROL_TEXTBOX ).setText(text)
                return
        TextBox()
################################################################################ Modes ##########################################################################################################


def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param
              
params=get_params()

url=None
name=None
mode=None
iconimage=None
fanart=None
plot=None
genre=None
title=None
season=None
episode=None
location=None
path=None


try:
        name=urllib.unquote_plus(params["name"])
except:
        pass

try:
        
        url=urllib.unquote_plus(params["url"])
        
except:
        pass

try:
        mode=int(params["mode"])
except:
        pass

try:
        iconimage=urllib.unquote_plus(params["iconimage"])
        iconimage = iconimage.replace(' ','%20')
except:
        pass
try:
        plot=urllib.unquote_plus(params["plot"])
except:
        pass
try:
        fanart=urllib.unquote_plus(params["fanart"])
        fanart = fanart.replace(' ','%20')
except:
        pass

try:
        genre=urllib.unquote_plus(params["genre"])
except:
        pass

try:
        title=urllib.unquote_plus(params["title"])
except:
        pass
try:
        episode=int(params["episode"])
except:
        pass
try:
        season=int(params["season"])
except:
        pass
try:
        location=urllib.unquote_plus(params["location"])
except:
        pass
try:
        path=urllib.unquote_plus(params["path"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "Thumb: "+str(iconimage)

if mode==None or url==None or len(url)<1:
        MAIN()
               
       
elif mode==1:
        from resources.src import vdeobull
        print ""+url
        vdeobull.Index(url)
               
elif mode==2:
        from resources.src import vdeobull
        print ""+url
        vdeobull.Popular(url)

elif mode==3:
        from resources.src import vdeobull
        print ""+url
        vdeobull.AtoZ(url,name)

elif mode==4:
        from resources.src import vdeobull
        print ""+url
        vdeobull.Search(url)
        
elif mode==5:
        from resources.src import vdeobull
        print ""+url
        vdeobull.Searchhistory()

elif mode==6:
        from resources.src import vdeobull
        print ""+url
        vdeobull.ALPHA(url,name)

elif mode==7:
        from resources.src import vdeobull
        print ""+url
        vdeobull.Popular2(url)

elif mode==10:
        from resources.src import vdeobull
        print ""+url
        vdeobull.SEARCHS(url)

elif mode==11:
        from resources.src import vdeobull
        print ""+url
        vdeobull.SearchResults(url)        

        

elif mode==20:
        main.Clearhistory(url)


elif mode==75:
       from resources.src import vdeobull
       print ""+url
       vdeobull.VIDEOLINKS(name,url)

elif mode==100:
       from resources.src import vdeobull
       print ""+url
       vdeobull.Play(url,name)

elif mode==150:
       from resources.src import vdeobull
       print ""+url
       vdeobull.PlayB(name,url)
       
    





















































elif mode == 1999:
    settings.openSettings()

elif mode == 2000:
    xbmc.executebuiltin("XBMC.Container.Update(path,replace)")
    xbmc.executebuiltin("XBMC.ActivateWindow(Home)")        
xbmcplugin.endOfDirectory(int(sys.argv[1]))
