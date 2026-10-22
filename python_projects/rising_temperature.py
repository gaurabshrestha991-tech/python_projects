from datetime import datetime, timedelta

def rising_temperatre(weather):
    weather_by_date = {
        row["recordDate"]: row for row in weather
    }
    
    result = []
    
    for row in weather:
        previous_date = row["recordDate"] - timedelta(days=1)
        
        if previous_date in weather_by_date:
            if row["temperature"] > weather_by_date[previous_date]["temperature"]:
                result.append(row["id"])
                
    return result
weather = [
    {"id": 1, "recordDate": datetime(2015, 1, 1), "temperature": 10},
    {"id": 2, "recordDate": datetime(2015, 1, 2), "temperature": 25},
    {"id": 3, "recordDate": datetime(2015, 1, 3), "temperature": 20},
    {"id": 4, "recordDate": datetime(2015, 1, 4), "temperature": 30},
]

print(rising_temperatre(weather))