import COVID19Py
import requests
from datetime import datetime


class Covid19:
    def __init__(self):
        self.covid19 = COVID19Py.COVID19()

    def check_in_the_world(self):
        now = datetime.now()
        confirmed = self.covid19.getLatest()["confirmed"]
        deaths = self.covid19.getLatest()["deaths"]

        return "Данные по всему миру на {}.{}.{}\nЗараженные: {}\nУмерли: {}".format(
            now.day, now.month, now.year, confirmed,  deaths)

    def check_in_the_russia(self):
        location = self.covid19.getLocationByCountryCode("RU")
        deaths = location[0]["latest"]["deaths"]
        confirmed = int(location[0]["latest"]["confirmed"])
        update = location[0]["last_updated"]
        date = update.split('T')[0]
        time = update.split('T')[1].split('.')[0]
        population = int(location[0]["country_population"])
        procent = int((confirmed / population * 100) * 100000) / 100000

        return "Данные по стране Россия:\nПоследнее обновление: {}, {}\nЗаражённых: {}" \
               "\nУмерло: {}\n%зараженных: {}%".format(date.replace("-", "."), time, confirmed, deaths,
                                                       procent)

    def check_in_the_usa(self):
        location = self.covid19.getLocationByCountryCode("US")
        deaths = location[0]["latest"]["deaths"]
        confirmed = int(location[0]["latest"]["confirmed"])
        update = location[0]["last_updated"]
        date = update.split('T')[0]
        time = update.split('T')[1].split('.')[0]
        population = int(location[0]["country_population"])
        procent = int((confirmed / population * 100) * 100000) / 100000

        return "Данные по стране США:\nПоследнее обновление: {}, {}\nЗаражённых: {}" \
               "\nУмерло: {}\n%зараженных: {}%".format(date.replace("-", "."), time, confirmed, deaths,
                                                       procent)

    def covid_in_different_country(self, kod):
        country_cod = kod[1:].upper()

        location = self.covid19.getLocationByCountryCode(country_cod)
        deaths = location[0]["latest"]["deaths"]
        confirmed = int(location[0]["latest"]["confirmed"])
        update = location[0]["last_updated"]
        date = update.split('T')[0]
        time = update.split('T')[1].split('.')[0]
        population = int(location[0]["country_population"])
        country = location[0]["country"]
        procent = int((confirmed / population * 100) * 100000) / 100000

        return "Данные по стране {}:\nПоследнее обновление: {}, {}\nЗаражённых: {}" \
               "\nУмерло: {}\n% зараженных: \n{}%".format(country, date.replace("-", "."), time, confirmed, deaths,
                                                       procent)


