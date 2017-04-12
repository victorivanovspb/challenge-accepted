#*.* coding: utf-8 *.*
"""
    Необходимо определить угол в градусах между часовой и
    минутной стрелкой на циферблате часов.
"""
class WatchFace(object):
    @staticmethod
    def get_one_hour_angle():
        return 30.0 # 360 / 12
    
    @staticmethod
    def get_one_minute_angle():
        return 6.0 # 360 / 60

    def __init__(self, hour, minute):
        if type(hour) is not int:
            raise TypeError("type of argument 'hour' is not a integer")
        if hour < 0:
            raise AttributeError("the value of the argument 'hour' can not be less than zero")
        if type(minute) is not int:
            raise TypeError("type of argument 'minute' is not a integer")
        if minute < 0:
            raise AttributeError("the value of the argument 'minute' can not be less than zero")
        
        while hour >= 12: # Нормализация значения часов
            hour -= 12
        while minute >= 60: # Нормализация значения минут
            minute -= 60

        self.hour = hour
        self.minute = minute

    def get_angle(self): # Целевой метод
        """Определение угла между стрелками."""
        minute_ang =  self.minute * self.get_one_minute_angle()
        hour_ang = self.hour * self.get_one_hour_angle()
        hour_ang += (minute_ang / 360.0) * self.get_one_hour_angle() # Продвижение часовой стрелки "внутри часа", определяемое положением минутной стрелки.
        return abs(hour_ang - minute_ang)

if __name__ == "__main__":
    print WatchFace( 3, 15).get_angle()
    print WatchFace( 3, 16).get_angle()
    print WatchFace( 3, 17).get_angle()
    print WatchFace( 3,  0).get_angle()
    print WatchFace(10, 47).get_angle()

