#!/usr/bin/env python3

import json
from pprint import pprint
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
      # TODO add ordered_dicts=False once python is updated
      pprint( airSensor.getAll() )
      print()

if __name__ == "__main__":
   test_AirSensor()
