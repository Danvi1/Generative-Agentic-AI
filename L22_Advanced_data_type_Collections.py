import arrow

brewing_time = arrow.utcnow() # gives UTC time now
brewing_europe_time = brewing_time.to('Europe/Rome')
print(f"brewing Time : {brewing_time}")
print(f"brewing Time in Europe standard : {brewing_europe_time}")

from collections import namedtuple as nt

