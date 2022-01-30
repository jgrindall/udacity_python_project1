#!/bin/sh

py main.py inspect --pdes 1P
echo $'\n'
py main.py inspect --name Halley
echo $'\n'
py main.py inspect --verbose --name Halley
echo $'\n'
py main.py inspect --verbose --name Ganymed
echo $'\n'
py main.py inspect --name fake-comet
echo $'\n'


# Show (the first) two close approaches in the data set.
py main.py query --limit 2
#On 1900-01-01 00:11, '170903' approaches Earth at a distance of 0.09 au and a velocity of 16.75 km/s.
#On 1900-01-01 02:33, '2005 OE3' approaches Earth at a distance of 0.41 au and a velocity of 17.92 km/s.
echo $'\n'

# Show (the first) three close approaches on July 29th, 1969.
py main.py query --date 1969-07-29 --limit 3
#On 1969-07-29 01:47, '408982' approaches Earth at a distance of 0.36 au and a velocity of 24.24 km/s.
#On 1969-07-29 13:33, '2010 MA' approaches Earth at a distance of 0.21 au and a velocity of 8.80 km/s.
#On 1969-07-29 19:56, '464798' approaches Earth at a distance of 0.10 au and a velocity of 8.02 km/s.
echo $'\n'

# Show (the first) three close approaches in 2050.
py main.py query --start-date 2050-01-01 --limit 3
#On 2050-01-01 04:18, '2019 AY9' approaches Earth at a distance of 0.31 au and a velocity of 8.31 km/s.
#On 2050-01-01 06:00, '162361' approaches Earth at a distance of 0.19 au and a velocity of 9.08 km/s.
#On 2050-01-01 09:55, '2009 LW2' approaches Earth at a distance of 0.04 au and a velocity of 19.02 km/s.
echo $'\n'

# Show (the first) four close approaches in March 2020 that passed at least 0.4au of Earth.
py main.py query --start-date 2020-03-01 --end-date 2020-03-31 --min-distance 0.4 --limit 4
#On 2020-03-01 00:28, '152561' approaches Earth at a distance of 0.42 au and a velocity of 11.23 km/s.
#On 2020-03-01 09:28, '462550' approaches Earth at a distance of 0.47 au and a velocity of 17.19 km/s.
#On 2020-03-02 21:41, '2020 QF2' approaches Earth at a distance of 0.45 au and a velocity of 8.79 km/s.
#On 2020-03-03 00:49, '2019 TU' approaches Earth at a distance of 0.49 au and a velocity of 5.92 km/s.
echo $'\n'

# Show (the first) three close approaches that passed at most 0.0025au from Earth with a relative speed of at most 5 km/s.
# That's slightly less than the average distance between the Earth and the moon.
py main.py query --max-distance 0.0025 --max-velocity 5 --limit 3
#On 1949-01-01 02:53, '2003 YS70' approaches Earth at a distance of 0.00 au and a velocity of 3.64 km/s.
#On 1954-03-13 00:00, '2013 RZ53' approaches Earth at a distance of 0.00 au and a velocity of 3.04 km/s.
#On 1979-09-02 00:16, '2014 WX202' approaches Earth at a distance of 0.00 au and a velocity of 1.79 km/s.
echo $'\n'

# Show (the first) three close approaches in the 2000s of NEOs with a known diameter of least 6 kilometers that passed Earth at a relative velocity of at least 15 km/s.
py main.py query --start-date 2000-01-01 --min-velocity 15 --min-diameter 6 --limit 3
#On 2000-05-21 10:08, '7092 (Cadmus)' approaches Earth at a distance of 0.34 au and a velocity of 28.46 km/s.
#On 2004-05-25 03:54, '7092 (Cadmus)' approaches Earth at a distance of 0.41 au and a velocity of 30.52 km/s.
#On 2006-06-10 20:04, '1866 (Sisyphus)' approaches Earth at a distance of 0.49 au and a velocity of 26.81 km/s.
echo $'\n'

# Show (the first) two close approaches in January 2030 of NEOs that are at most 50m in diameter and are marked not potentially hazardous.
py main.py query --start-date 2030-01-01 --end-date 2030-01-31 --max-diameter 0.05 --not-hazardous --limit 2
#On 2030-01-07 20:59, '2010 GH7' approaches Earth at a distance of 0.46 au and a velocity of 18.84 km/s.
#On 2030-01-13 07:29, '2010 AE30' approaches Earth at a distance of 0.06 au and a velocity of 14.00 km/s.
echo $'\n'

# Show (the first) three close approaches in 2021 of potentially hazardous NEOs at least 100m in diameter that pass within 0.1au of Earth at a relative velocity of at least 15 kilometers per second.
py main.py query --start-date 2021-01-01 --max-distance 0.1 --min-velocity 15 --min-diameter 0.1 --hazardous --limit 3
#On 2021-01-21 22:56, '363024' approaches Earth at a distance of 0.07 au and a velocity of 15.31 km/s.
#On 2021-02-01 22:26, '2016 CL136' approaches Earth at a distance of 0.04 au and a velocity of 18.06 km/s.
#On 2021-08-21 15:10, '2016 AJ193' approaches Earth at a distance of 0.02 au and a velocity of 26.17 km/s.
echo $'\n'


py main.py query --date 1969-07-29
echo $'\n'
py main.py query --start-date 2020-01-01 --end-date 2020-01-31 --max-distance 0.025
echo $'\n'
py main.py query --start-date 2050-01-01 --min-distance 0.2 --min-velocity 50
echo $'\n'
py main.py query --date 2020-03-14 --max-velocity 25 --min-diameter 0.5 --hazardous
echo $'\n'
py main.py query --start-date 2000-01-01 --max-diameter 0.1 --not-hazardous
echo $'\n'
py main.py query --hazardous --max-distance 0.05 --min-velocity 30
echo $'\n'

py main.py query --start-date 2020-01-01 --end-date 2020-12-31 --hazardous --min-diameter 0.25 --max-distance 0.1 --limit 5 --outfile results.json
echo $'\n'
py main.py query --start-date 2020-01-01 --end-date 2020-12-31 --hazardous --min-diameter 0.25 --max-distance 0.1 --limit 5 --outfile results.csv
echo $'\n'


py -m unittest --verbose
echo $'\n'


#py main.py interactive

#Explore close approaches of near-Earth objects. Type `help` or `?` to list commands and `exit` to exit.

#(neo) inspect --pdes 433
#NEO 433 (Eros) has a diameter of 16.840 km and is not potentially hazardous.
#(neo) help i
#Shorthand for `inspect`.
#(neo) i --name Halley
#NEO 1P (Halley) has a diameter of 11.000 km and is not potentially hazardous.
#(neo) query --date 2020-12-31 --limit 2
#On 2020-12-31 05:48, '2010 PQ10' approaches Earth at a distance of 0.45 au and a velocity of 21.69 km/s.
#On 2020-12-31 16:00, '2015 YA' approaches Earth at a distance of 0.17 au and a velocity of 5.65 km/s.
#(neo) q --date 2021-3-14 --min-velocity 10
#On 2021-03-14 06:17, '2019 DS1' approaches Earth at a distance of 0.39 au and a velocity of 20.17 km/s.
#On 2021-03-14 20:19, '483656' approaches Earth at a distance of 0.06 au and a velocity of 12.09 km/s.
