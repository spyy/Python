import os
import codecs
#from datetime import date
from time import localtime, strftime


KEncoding = "utf-8"



class Tapahtumat:
    def __init__( self, parent ):
        self.parent = parent
        self.hakemisto = os.path.join( self.parent, "tapahtumat" )

    def initialize( self ):
        os.mkdir( self.hakemisto )

    def delete( self ):
        self.clear()
        os.rmdir( self.hakemisto )

    def read( self ):
        lista = []
        itemList = os.listdir( self.hakemisto )
        for item in itemList:
            tiedosto = os.path.join( self.hakemisto, item )
            f = open( tiedosto, "r" )
            data = f.read()            
            f.close()
            udata = unicode( item ) + u" " + unicode( data, KEncoding )
            lista.append( udata )            
        return lista

    def add( self, teksti ):
        tiedosto = os.path.join( self.hakemisto, self.__tamapaiva() )
        encoded = teksti.encode( KEncoding )
        f = open( tiedosto, "w" )        
        f.write( encoded )
        f.close()

    def remove( self, nimi ):
        tiedosto = os.path.join( self.hakemisto, nimi )
        os.remove( tiedosto )

    def clear( self ):
        itemList = os.listdir( self.hakemisto )
        for item in itemList:
            tiedosto = os.path.join( self.hakemisto, item )
            os.remove( tiedosto )
            
    def __tamapaiva( self ):
        return strftime("%m.%d", localtime())




