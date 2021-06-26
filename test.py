from calculator import BMICalculator

params = [
    { "Gender": "Male", "HeightCm": 161, "WeightKg":85 }, 
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, 
    { "Gender": "Female", "HeightCm": 166,"WeightKg": 62 }, 
    { "Gender": "Female", "HeightCm": 150, "WeightKg": 70 }, 
    { "Gender": "Female", "HeightCm": 167, "WeightKg": 82 }
]

result = map(BMICalculator, params)
print(list(result))