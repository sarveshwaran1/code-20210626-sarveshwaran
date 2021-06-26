def BMICalculator(param):
    def BMICategory(BMI):
        if BMI <= 18.4:
            return ("18.4 and below", "Malnutrition risk")
        elif BMI >= 18.5 and BMI <= 24.9:
            return("18.5 - 24.9", "Low risk")
        elif BMI >= 25.0 and BMI <= 29.9:
            return("25 - 29.9", "Enhanced risk")
        elif BMI >= 30.0 and BMI <= 34.9:
            return("30 - 34.9", "Medium risk")
        elif BMI >= 35.0 and BMI <= 39.9:
            return("35 - 39.9", "High risk")
        elif BMI >= 40.0:
            return("40 and above", "Very high risk")
    bmi = param["WeightKg"] / (param["HeightCm"]/100)**2
    BmiCategory = BMICategory(bmi)
    param["BMI"] = round(bmi, 2)
    param["BMICategory"],param["HealthRisk"] = BmiCategory
    return param