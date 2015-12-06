def fahrenheit(tempcelsius):
    """Convert temperature in degrees celsius to fahrenheit"""
    return tempcelsius * (9.0/5.0) + 32.0

def celsius(tempfahrenheit):
    """Convert temperature in degrees fahrenheit to celsius"""
    return (tempfahrenheit - 32) * 5.0 / 9.0
