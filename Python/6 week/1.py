# Исключения
# Напишем часть сервиса, который будет помогать бронировать переговорки в офисе. Для этого опишем класс Booking - его объекты будут содержать информацию о конкретном бронировании, а также вспомогательную функцию create_booking, которая будет создавать новый объект бронирования и записывать информацию о бронировании в базу данных бронирований через предоставляемое API. Возвращать она должна будет статус создания бронирования (получилось или переговорка уже занята) и информацию о брони в формате JSON. Ниже - подробности.
# Класс Booking должен обладать следующим функционалом.
# конструктор должен принимать три аргумента в следующем порядке: название переговорки, datetime начала брони и datetime конца брони
# внутри конструктора, если datetime конца брони оказался раньше, чем datetime начала, нужно вызвать исключение ValueError
# Также у объектов этого класса должны быть следующие поля (рекомендую сделать часть из них в виде проперти):
# room_name - название переговорки, полученное из конструктора
# start - datetime начала брони. Должна быть возможность назначить новое время начала уже созданной брони
# end - datetime конца брони. Должна быть возможность назначить новое время конца уже созданной брони
# duration - длительность бронирования в минутах (гарантируется, что длительность любой встречи кратна одной минуте, поэтому это должно быть целое число)
# start_date - дата начала брони в формате YYYY-MM-DD (строка)
# end_date - дата конца брони в формате YYYY-MM-DD (строка)
# start_time - время начала брони в формате HH:MM (строка)
# end_time - время конца брони в формате HH:MM (строка)
# Функция create_booking должна обладать следующей сигнатурой:
# create_booking(room_name, start, end) -> str,
# где аргументы - это те же аргументы, которые принимает конструктор Booking, а выходная строка - это json определенного формата, который описан чуть ниже по тексту.
# Будем считать, что взаимодействие с базой данных у нас уже описано нашим коллегой в соседнем файле api.py. В нем есть уже готовая функция register_booking, которая:
# принимает на вход объект класса Booking
# возвращает True, если бронирование получилось создать
# возвращает False, если мы пытаемся забронировать уже занятую в это время переговорку
# # если такой переговорки не существует, вызывается KeyError
# Таким образом, в том же файле, что и класс Booking, вам нужно описать фукнцию create_booking, которая:
# обладает сигнатурой create_booking(room_name, start, end) -> str, где аргументы - те же, что и в конструкторе Booking
# в самом начале своей работы выводит на экран текст: Начинаем создание бронирования
# внутри функции создается объект класса Booking, а также вызывается функция register_booking, которая принимает на вход созданный объект. Должны быть обработаны все случаи работы register_booking: True, False и KeyError. Сделать это поможет конструкция try-except
# перед выходом из функции должно выводиться на экран сообщение Заканчиваем создание бронирования. Это должно происходить в любом случае, даже если мы попытались создать бронирование с неверными датами и получили ValueError (см. описание класса Booking). Для этого рекомендую использовать блок finally, в котором описать этот print
# Функция должна возвращать json-строку с ответом, в котором будут содержаться следующие поля:
# created: true/false, получилось ли забронировать комнату. Если возникло KeyError, то нужно здесь записать false
# msg: сообщение с пояснениями. Сообщение должно быть одним из следующих: Бронирование создано, Комната занята, Комната не найдена. Сообщение выбирается на основе того, что вернет функция register_booking
# booking
# это бронирование в виде json-строки. Должны содержаться поля: room_name, duration, start_date, end_date, start_time, end_time.

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
