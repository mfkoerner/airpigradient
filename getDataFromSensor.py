#!/usr/bin/env python3

# Provides libraries to contact the the AirGradient sensors and return current data

import requests
import json

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
