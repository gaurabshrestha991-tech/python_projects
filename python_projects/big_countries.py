def bigCountries(world):
    result = []
    
    for country in world:
        if country["area"] >= 3000000 or country["population"] >= 25000000:
            result.append([
                country["name"],
                country["population"],
                country["area"]
            ])
            
    return result
