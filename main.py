# AstroPi 2021

# from picamera import Picamera
from pathlib import Path
import csv
from time import sleep
from datetime import timedelta, datetime
import ephem

current_dir = Path(__file__).parent.resolve()
log_file = str(current_dir) + '/log.csv'
print(current_dir)
print(log_file)

line_0 = "ISS (ZARYA)"
line_1 = "1 25544U 98067A   21025.32718219  .00001091  00000-0  28047-4 0  9999"
line_2 = "2 25544  51.6462 329.3197 0002267 288.7769 172.4159 15.48884919266453"

experiment_start = datetime.utcnow()
experiment_end = experiment_start + timedelta(seconds=30)

iss = ephem.readtle(line_0, line_1, line_2)
sun = ephem.Sun()

# camera = Picamera()
# camera.resolution = (2592, 1944)
i = 0

with open(log_file, 'w') as f:
    writer = csv.writer(f)
    header = (
      'datetime',
      'latitude',
      'longitude',
      'sun elevation',
      'filename'
    )
    writer.writerow(header)

while datetime.utcnow() < experiment_end:
    iss.compute()

    iss_observer = ephem.Observer()
    iss_observer.lat = iss.sublat
    iss_observer.lon = iss.sublong
    iss_observer.elevation = iss.elevation

    sun.compute(iss_observer)
    sun_elevation = sun.alt

    # print(iss.sublat, iss.sublong)
    print(sun_elevation)

    # camera.capture(f'image{i:3d}')

    with open(log_file, 'a') as f:
        writer = csv.writer(f)
        row = (
            datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            iss.sublat/ephem.degree,
            iss.sublong/ephem.degree,
            sun.alt/ephem.degree,
            f'image_{i:04}.jpg',

        )
        writer.writerow(row)

    i += 1
    sleep(2)
