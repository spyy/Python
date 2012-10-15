import os
from Asunto import Asunto



class Alue:
    def __init__( self, p, n ):
        self.parent = p
        self.nimi = n
        self.hakemisto = os.path.join( self.parent, self.nimi )

    def __alusta( self, mista, mihin ):
        mihin += 1
        for i in range( mista, mihin ):
            numero = str( i )
            if len( numero ) < 2: numero = "0" + numero
            asunto = Asunto( self.hakemisto, str( numero ) )
            asunto.alusta()

    def __lisaa( self, mista, mihin ):    	
        if not os.path.exists( self.hakemisto ): os.mkdir( self.hakemisto )
        self.__alusta( mista, mihin )

    def lisaa( self, mista, mihin ):    	
        if mihin > mista: self.__lisaa( mista, mihin )

    def lue2( self ):
        itemList = os.listdir( self.hakemisto )
        numerot = []
        tiedot = []
        for item in itemList:
            a = Asunto( self.hakemisto, item )
            nimi = a.nimi()
            paivays = a.paivays()
            numero = unicode( item )
            if len( nimi ) < 1: nimi = u""
            tiedot.append( numero + u" " + nimi + u" " + paivays )
            numerot.append( item )
        return numerot, tiedot

    def lue1( self ):
        itemList = os.listdir( self.hakemisto )
        asunnot = []        
        for item in itemList:
            a = Asunto( self.hakemisto, item )
            nimi = a.nimi()
            numero = unicode( item )
            if len( nimi ) < 1: nimi = u""            
            asunnot.append( ( item, numero, nimi ) )
        return asunnot

    def poista( self ):
        itemList = os.listdir( self.hakemisto )
        for item in itemList:
            a = Asunto( self.hakemisto, item )
            a.poista()
        os.rmdir( self.hakemisto )



