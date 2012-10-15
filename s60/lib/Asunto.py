import os
import codecs
from time import localtime, strftime
from Tapahtumat import Tapahtumat



KEncoding = "utf-8"



class Asunto:
    def __init__( self, parent, numero ):
        self.parent = parent
        self.numero = numero
        self.hakemisto = os.path.join( parent, numero )
        self.__nimi = os.path.join( self.hakemisto, "nimi.txt" )
        self.__paivays = os.path.join( self.hakemisto, "paivays.txt" )        

    def alusta( self ):
        os.mkdir( self.hakemisto )
        tapahtumat = Tapahtumat( self.hakemisto )
        tapahtumat.initialize()
        f = open( self.__nimi, "w" )
        f.close()
        f = open( self.__paivays, "w" )
        f.close()

    def poista( self ):
        tapahtumat = Tapahtumat( self.hakemisto )
        tapahtumat.delete()
        os.remove( self.__nimi )
        os.remove( self.__paivays )
        os.rmdir( self.hakemisto )

    def tapahtumat( self ):
        tapahtumat = Tapahtumat( self.hakemisto )
        return tapahtumat.read()

    def __kirjoitaPaivays( self, data ):        
        f = open( self.__paivays, "w" )
        f.write( data )
        f.close()

    def paivays( self ):
        f = open( self.__paivays, "r" )
        data = f.read()
        f.close()
        return unicode( data )

    def lisaaTapahtuma( self, teksti ):
        tapahtumat = Tapahtumat( self.hakemisto )
        tapahtumat.add( teksti )
        self.__kirjoitaPaivays( self.__tamapaiva() )        

    def poistaTapahtumat( self ):
        tapahtumat = Tapahtumat( self.hakemisto )
        tapahtumat.clear()
        self.__kirjoitaPaivays( " " )        

    def __tamapaiva( self ):
        return strftime("%m.%d", localtime())

    def nimi( self ):
        tiedosto = open( self.__nimi, "r" )
        data = tiedosto.read()
        tiedosto.close()
        return unicode( data, KEncoding )

    def kirjoitaNimi( self, nimi ):
        tiedosto = open( self.__nimi, "w" )
        encoded = nimi.encode( KEncoding )
        tiedosto.write( encoded )
        tiedosto.close()

