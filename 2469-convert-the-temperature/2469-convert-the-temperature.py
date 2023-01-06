class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15,       # Kelvin
                celsius * 1.80 + 32.00] # Fahrenheit