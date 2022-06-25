USE_ROUNDED_COORDS = True
OPENWEATHER_API = "94d1bc1bccef5201e5bad6627af7b07b"
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=ru&"
    "units=metric"
)