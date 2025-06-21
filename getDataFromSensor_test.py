#!/usr/bin/env python3

import json
from getDataFromSensor import (
   AirSensor,
)

with open( "settings.json" ) as f:
   settings = json.load( f )

def test_AirSensor():
   for device in settings[ "devices" ]:
      airSensor = AirSensor( hwid=device[ "hwid" ],
                             name=device[ "name" ] )
      print( airSensor.name )
      print( airSensor.getRaw() )
      print()

if __name__ == "__main__":
   test_AirSensor()
