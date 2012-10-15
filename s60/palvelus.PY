
import e32
import sys
import appuifw
import codecs
import Alue
import Alueet
import Asunto


from key_codes import EScancode5
from Alue import Alue
from Alueet import Alueet
from Asunto import Asunto


KMenuAlueet = ( [(u"Lisaa alue", lambda:lisaaAlue()), (u"Poista alue", lambda:poistaAlue()), (u"Exit", lambda:APP_LOCK.signal())] )
KMenuAlue = ( [(u"Nimi", lambda:nimi()), (u"Lisaa tapahtuma", lambda:lisaaTapahtuma()), (u"Tyhjenna tapahtumat", lambda:tyhjennaTapahtumat()), (u"Alueet", lambda:goToAlueet())] )
KMenuAsunto = ( [(u"Alueet", lambda:goToAlueet()), (u"Alue", lambda:goToAlue())] )



numeroLista = []
asuntoLista = [unicode( "Empty" )]
alueLista = [unicode( "Empty" )]
tapahtumaLista = [unicode( "Empty" )]


def goToAlue():
    global asunnotListbox
    alue = currentAlue()
    appuifw.app.title = unicode( alue.nimi )
    appuifw.app.body = asunnotListbox
    appuifw.app.menu = KMenuAlue

def goToAlueet():
    global alueetListbox
    appuifw.app.title = unicode("Alueet")
    appuifw.app.body = alueetListbox
    appuifw.app.menu = KMenuAlueet

def tyhjennaTapahtumat():
    asunto = currentAsunto()
    asunto.poistaTapahtumat()
    paivitaAsuntoLista()
    
def lisaaTapahtuma():
    asunto = currentAsunto()
    tapahtuma = appuifw.query( u"Lisaa tapahtuma", "text" )
    asunto.lisaaTapahtuma( tapahtuma )
    paivitaAsuntoLista()

def nimi():
    asunto = currentAsunto()
    nimi = appuifw.query( unicode("Nimi"), "text" )
    asunto.kirjoitaNimi( nimi )
    paivitaAsuntoLista()

def currentAsunto():
    global alueLista, numeroLista
    currentAlue = alueetListbox.current()
    currentAsunto = asunnotListbox.current()
    alue = Alue( alueet.hakemisto, alueLista[currentAlue] )
    numero = numeroLista[currentAsunto]
    return Asunto( alue.hakemisto, numero )

def currentAlue():
    global alueLista
    currentAlue = alueetListbox.current()
    return Alue( alueet.hakemisto, alueLista[currentAlue] )

def lisaaAlue():
    uusiAlue()
    paivitaAlueLista()

def uusiAlue():
    nimi = appuifw.query( u"Nimi", "text" )
    if nimi:
        numerosta = appuifw.query( u"Numerosta", "number" )
        if numerosta:
            numeroon = appuifw.query( u"Numeroon", "number" )
            if numeroon:
                alueet.lisaa( nimi, numerosta, numeroon )


def poistaAlue():
    global alueLista
    nimi = alueLista[alueetListbox.current()]
    alueet.poista( nimi )
    paivitaAlueLista()

def paivitaAlueLista():
    global alueLista
    alueLista = alueet.lue()
    if len( alueLista ) < 1: alueLista.append( unicode( "Empty" ) )
    alueetListbox.set_list( alueLista )

def paivitaAsuntoLista():
    global asuntoLista, numeroLista
    alue = currentAlue()
    numeroLista, asuntoLista = alue.lue2()
    current = asunnotListbox.current()
    asunnotListbox.set_list( asuntoLista, current )

def paivitaTapahtumaLista():
    global tapahtumaLista    
    asunto = currentAsunto()
    tapahtumaLista = asunto.tapahtumat()
    if len( tapahtumaLista ) < 1: tapahtumaLista.append( unicode( "Empty" ) )
    tapahtumatListbox.set_list( tapahtumaLista )    
    
def alueObserver():
    paivitaAsuntoLista()
    alue = currentAlue()
    appuifw.app.title = alue.nimi
    appuifw.app.body = asunnotListbox
    appuifw.app.menu = KMenuAlue

def asuntoObserver():
    asunto = currentAsunto()
    otsikko = unicode( asunto.numero ) + u" " + asunto.nimi()
    paivitaTapahtumaLista()
    appuifw.app.title = otsikko
    appuifw.app.body = tapahtumatListbox
    appuifw.app.menu = KMenuAsunto



APP_LOCK = e32.Ao_lock()
appuifw.app.title = unicode("Alueet")
appuifw.app.exit_key_handler = APP_LOCK.signal
appuifw.app.menu = KMenuAlueet

alueet = Alueet( sys.path[0] )
alueet.alusta()
alueLista = alueet.lue()
if len( alueLista ) < 1: alueLista.append( unicode( "Empty" ) )

tapahtumaEditori = appuifw.Text()
asunnotListbox = appuifw.Listbox( asuntoLista, asuntoObserver )
alueetListbox = appuifw.Listbox( alueLista, alueObserver )
tapahtumatListbox = appuifw.Listbox( tapahtumaLista )
#alueetListbox.bind( EScancode5, lambda:appuifw.note(u"Key 5", "info", 1) )
appuifw.app.body = alueetListbox

APP_LOCK.wait()






