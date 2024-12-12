from XRPLib.rangefinder import Rangefinder

rangefinder = Rangefinder.get_default_rangefinder()
while ((rangefinder.distance()) > 10):
    print(rangefinder.distance())
