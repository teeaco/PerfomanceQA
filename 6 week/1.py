from datetime import datetime
import json
from api import register_booking


class Booking:
    def __init__(self, room_name: str, start: datetime, end: datetime):
        if end < start:
            raise ValueError("End time must be after start time.")
        
        self.room_name = room_name
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, new_start: datetime):
        if self._end < new_start:
            raise ValueError("End time must be after start time.")
        self._start = new_start

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, new_end: datetime):
        if new_end < self._start:
            raise ValueError("End time must be after start time.")
        self._end = new_end

    @property
    def duration(self):
        return int((self._end - self._start).total_seconds() / 60)

    @property
    def start_date(self):
        return self._start.strftime("%Y-%m-%d")

    @property
    def end_date(self):
        return self._end.strftime("%Y-%m-%d")

    @property
    def start_time(self):
        return self._start.strftime("%H:%M")

    @property
    def end_time(self):
        return self._end.strftime("%H:%M")


def create_booking(room_name: str, start: datetime, end: datetime) -> str:
    print("Начинаем создание бронирования")
    try:
        booking = Booking(room_name, start, end)
        try:
            result = register_booking(booking)
            if result:
                msg = "Бронирование создано"
                created = True
            else:
                msg = "Комната занята"
                created = False
        except KeyError:
            msg = "Комната не найдена"
            created = False
        response = {
            "created": created,
            "msg": msg,
            "booking": {
                "room_name": booking.room_name,
                "start_date": booking.start_date,
                "start_time": booking.start_time,
                "end_date": booking.end_date,
                "end_time": booking.end_time,
                "duration": booking.duration
            }
        }
        return json.dumps(response, ensure_ascii=False)
    
    except ValueError as e:
        response = {
            "created": False,
            "msg": str(e),
            "booking": {
                "room_name": room_name,
                "start_date": start.strftime("%Y-%m-%d"),
                "start_time": start.strftime("%H:%M"),
                "end_date": end.strftime("%Y-%m-%d"),
                "end_time": end.strftime("%H:%M"),
                "duration": int((end - start).total_seconds() / 60)
            }
        }
        return json.dumps(response, ensure_ascii=False)

    finally:
        print("Заканчиваем создание бронирования")
