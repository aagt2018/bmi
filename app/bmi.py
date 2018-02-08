

class Bmi:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height / 100

    def calculate(self):
        bmi = self.weight / (self.height * self.height)
        bmi = round(bmi, 1)

        return bmi, self.__get_category(bmi)

    def __get_category(self, bmi):
        if bmi <= 15:
            return "Very severely underweight"
        elif bmi <= 16:
            return "Severely underweight"
        elif bmi <= 18.5:
            return "Underweight"
        elif bmi <= 25:
            return "Normal"
        elif bmi <= 30:
            return "Overweight"
        elif bmi <= 35:
            return "Moderately obese"
        elif bmi <= 40:
            return "Severely obese"
        else:
            return "Very severely obese"