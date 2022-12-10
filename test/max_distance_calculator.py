from lib import Coordinate, Gis
from datetime import datetime


def calc_all(filename: str):
    retval = []
    home = Coordinate(latitude=15.250936, longitude=100.337037, altitude=235.0)
    with open(filename, mode='r', encoding='utf-8') as csv:
        for i, line in enumerate(csv):
            line_list = line.strip().split(',')
            if len(line_list) != 4:
                raise Exception("Line error at line {} with line content: {} but got {}".format(i, line, line_list))
            timestamp, lat, lon, alt = line_list
            target = Coordinate(lat, lon, alt)
            tester = Gis(home, target)

            los = round(tester.getLineOfSight(), 2)
            az = round(tester.getAzimuth(), 2)
            elev = round(tester.getElevationApprox(), 2)
            time_hr = datetime.fromtimestamp(int(timestamp))

            retval.append(
                ['{:02}:{:02}:{:02}'.format(time_hr.hour, time_hr.minute, time_hr.second),
                 float(lat),
                 float(lon),
                 round(float(alt)),
                 los,
                 az,
                 elev
                 ]
            )
    return retval


def main():
    fname = 'out_2022_12_10_18_40_00.csv'
    res = calc_all('flight_path.csv')
    max_dist = 0
    max_time = ''
    with open(fname, mode='w', encoding='utf-8') as f:
        f.write('time,lat,lon,alt,los,azm,elev\n')
        for e in res:
            if e[-3] > max_dist:
                max_dist = e[-3]
                max_time = e[0]
            str_out = ','.join([str(x) for x in e])
            f.write(str_out)
            f.write('\n')
            print(str_out)
    print('Maximum distance =', max_dist, 'at time =', max_time)
    return


if __name__ == '__main__':
    main()
