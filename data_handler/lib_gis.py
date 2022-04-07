import math as _math
import dataclasses as _dataclasses
from typing import Union as _Union


@_dataclasses.dataclass(order=True, eq=True)
class Coordinate:
    '''
    A class of coordinate consisting of latitude, longitude, altitude
    '''
    latitude: _Union[int, float, str]
    longitude: _Union[int, float, str]
    altitude: _Union[int, float, str]

    def __post_init__(self):
        '''
        Convert to float

        :return:
        '''
        self.latitude = float(self.latitude)
        self.longitude = float(self.longitude)
        self.altitude = float(self.altitude)

    def __bool__(self):
        return self.__len__() > 0

    def __len__(self):
        return len([x for x in [self.latitude, self.longitude, self.altitude] if x])


class Gis:
    def __init__(self, coord_0: Coordinate, coord_: Coordinate, /,
                 gx: _Union[int, float, str]=0,
                 gy: _Union[int, float, str]=0,
                 gz: _Union[int, float, str]=0) -> None:
        '''
        A Gis object consisting of coordinates and physical variables

        :param coord_0: Coordinate of home location
        :param coord_: Coordinate of target location
        :param gx: Orientation X (Roll)
        :param gy: Orientation Y (Pitch)
        :param gz: Orientation Z (Yaw)
        '''

        self.lat1 = _math.radians(coord_0.latitude)
        self.lat2 = _math.radians(coord_.latitude)
        self.lon1 = _math.radians(coord_0.longitude)
        self.lon2 = _math.radians(coord_.longitude)
        self.dlon = self.lon2 - self.lon1
        self.dlat = self.lat2 - self.lat1

        self.a1 = coord_0.altitude
        self.a2 = coord_.altitude
        self.alt = self.a2 - self.a1

        self.gx = float(gx)
        self.gy = float(gy)
        self.gz = float(gz)

    def getArcRadians(self) -> float:
        '''
        Calculate arc angle in unit system: radians

        :return: Arc angle in radians
        '''
        a = (_math.sin(self.dlat / 2) ** 2)
        a += (_math.cos(self.lat1) * _math.cos(self.lat2) * ((_math.sin(self.dlon / 2)) ** 2))
        y = _math.sqrt(a)
        x = _math.sqrt(1 - a)
        c = 2 * _math.atan2(y, x)
        return c

    def getArcLength(self, R0=6371000) -> float:
        '''
        Calculate arc length in default: meters respect to earth radius

        :param R0: Radius
        :return: Arc length
        '''
        d = R0 * self.getArcRadians()
        return d

    def getLineOfSight(self, R0=6371000) -> float:
        '''
        Calculate line of sight in default: meters respect to earth radius

        :param R0: Radius
        :return: Line of sight distance
        '''
        R = R0 + self.a1
        baselength = 2 * R * _math.cos((_math.pi - self.getArcRadians()) / 2)
        heightlength = self.alt

        los = baselength ** 2 + heightlength ** 2 - \
              2 * baselength * heightlength * _math.cos((_math.pi + self.getArcRadians()) / 2)
        los = _math.fabs(los)
        los = _math.sqrt(los)

        return los

    def getAzimuth(self) -> float:
        '''
        Calculate azimuth angle in degrees

        :return: Azimuth angle in degrees
        '''
        a = _math.sin(self.dlon) * _math.cos(self.lat2)
        b = _math.cos(self.lat1) * _math.sin(self.lat2) - \
            _math.sin(self.lat1) * _math.cos(self.lat2) * _math.cos(self.dlon)
        theta = _math.atan2(a, b)
        theta = _math.degrees(theta)
        return theta

    def getHeading(self) -> int:
        '''
        Calculate heading angle in degrees

        :return: Heading angle in degrees
        '''
        ht = self.getAzimuth() - self.gz
        ht = ht % 360
        return round(ht)

    def getElevationApprox(self, delta: bool=False) -> float:
        '''
        Get elevation angle in degrees

        :param delta: Delta pitch in degrees
        :return: Elevation angle in degrees
        '''
        elev = _math.atan2(self.alt, self.getArcLength())
        elev = _math.degrees(elev)
        if delta:
            elev = elev - self.gx
            elev = elev % 360
        return elev

    def getRoll(self) -> float:
        '''
        Get roll angle in degrees

        :return: Roll angle in degrees
        '''
        ty = self.gy
        ty = ty % 360
        return ty

    def getHalf(self) -> None:
        '''

        :return:
        '''
        return

    def getArcAngleTotalApprox(self) -> float:
        '''
        Approximate arc angle from Pythagorean equivalence in radians

        :return: Approximated arc angle in radians
        '''
        pyx = _math.atan2((self.lon2 - self.lon1), (self.lat2-self.lat1))
        return pyx * 180/_math.pi


if __name__ == '__main__':
    c1 = Coordinate(latitude='15.0', longitude='100.11', altitude='20.1')
    c2 = Coordinate(latitude='15.0', longitude='101.41', altitude='25600.2')
    c3 = Coordinate(latitude='0', longitude='0', altitude='0')
    test = Gis(c1, c2, gx='1.0', gy='-3.0', gz='8.0')
    print(test.getArcLength())
    print(test.getLineOfSight())
    print(test.getAzimuth())
    print(test.getArcAngleTotalApprox())

    print(bool(c3))
