import os
import sys
import codecs
from Alue import Alue



class Alueet:
    def __init__( self, scriptPath ):
        self.hakemisto = os.path.join( scriptPath, "alueet" )

    def alusta( self ):
        if not os.path.exists( self.hakemisto ):
            os.mkdir( self.hakemisto )
        
    def lisaa( self, nimi, mista, mihin ):
        alue = Alue( self.hakemisto, nimi )
        alue.lisaa( mista, mihin )

    def poista( self, nimi ):
        alue = Alue( self.hakemisto, nimi )
        alue.poista()

    def lue( self ):
        itemList = os.listdir( self.hakemisto )
        alueet = []
        for item in itemList:
            alueet.append( unicode( item ) )
        return alueet

