class WeatherData:

    def __init__ (self, city_name, description):
        self.city_name = city_name
        self.description = description
        self.temperature = ''
        

    def getTemperature(self, temp):
        self.temperature = str(round(temp * 1.8 + 32,2)) + 'F.'

    def __str__(self):
        return self.city_name + ", " + self.description + ", " + self.temperature