#!/usr/bin/env python3

# Provides libraries to contact the the AirGradient sensors and return current data

class airsensor():
   """
   Provides various getData functions for a specific sensor
   """

   def __init__(  *, hwid, name, indoor=True ):
      self.hwid = hwid
      self.name = name
      self.indoor = indoor
