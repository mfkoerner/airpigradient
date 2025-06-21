#!/usr/bin/env python3

# Provides libraries to contact the the AirGradient sensors and return current data

from datetime import datetime
import json
import requests

class AirSensor():
   """
   Provides various getData functions for a specific sensor

   INPUTS:
   hwid : The serial number of your airgradient device
   name : Exists simply to differentiate devices

   OUTPUTS:
   getRaw : returns a dictionary of the current sensor values. Empty on failure.
   """

   def __init__(  self, *, hwid, name, indoor=True ):
      self.hwid = hwid
      self.name = name

   def getRaw( self ):
      """
      Returns a dict of the current sensor values directly as they come from
      the json request.
      """
      res = requests.get( f'http://airgradient_{self.hwid}.local/measures/current' )
      # check for valid response
      if res.status_code != 200:
         return {}
      else:
         try:
            return json.loads( res.text )
         except:
            return {}

   def getCalculated( self, *, rawData ):
      """
      calculate desired values from raw data
      """
      if not rawData:
         return {}
      calcData = {}
      calcData[ 'TIME' ] = datetime.now().strftime( "%Y-%m-%d %H:%M:%S" )
      calcData[ 'PM2.5' ] = round( rawData[ 'pm02Compensated' ], 0 )
      calcData[ 'CO2' ] = round( rawData[ 'rco2' ], 0 )
      calcData[ 'TEMP_F' ] = round( rawData[ 'atmpCompensated' ]*9/5 + 32, 1 )
      calcData[ 'HUMID' ] = round( rawData[ 'rhumCompensated' ], 0 )
      return calcData

   def getAll( self ):
      """
      return all calculated and raw data together
      """
      rawData = self.getRaw()
      calcData = self.getCalculated( rawData=rawData )
      return { 'raw' : rawData, 'calculated' : calcData }
