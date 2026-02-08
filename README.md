# OIBSIP_Python_Task1
Oasis Infobyte Python Internship Task 1 - Weather App"


This is a Python-based command-line Weather Application that retrieves real-time weather information for any city using the OpenWeatherMap API. The application allows users to enter a city name and instantly receive current weather details including temperature (in Celsius), humidity percentage, and a brief description of the weather conditions.

The project demonstrates how to work with REST APIs in Python using the requests library, handle JSON responses, manage API parameters, and implement basic error handling for invalid city inputs or failed requests.

This application is lightweight, beginner-friendly, and designed to showcase fundamental concepts such as API integration, HTTP requests, response parsing, and structured data extraction in Python.

It serves as a practical mini-project for learning backend data fetching and can be extended into a GUI application, web app, or enhanced with additional features like multi-day forecasts and unit conversion.


# Weather App

**Description**

Simple weather lookup app using OpenWeatherMap. Includes a command-line script (`weather.py`) and a Tkinter GUI (`weather_gui.py`).

**Features**

- Get current temperature, humidity and condition for a city 
- CLI and GUI frontends

**Prerequisites**

- Python 3.8 or later
- `requests` (install via pip)
- `tkinter` (usually included with Python on Windows)

**Install dependencies**

```bash
python -m pip install --upgrade pip
pip install requests
```

**Obtain API Key**

Create a free account at https://openweathermap.org/ and get an API key.

**How to run (CLI)**

```bash
python weather.py
```

**How to run (GUI)**

```bash
python weather_gui.py
```

**Security note**

The repository currently hardcodes an OpenWeatherMap API key in source. Revoke the exposed key and instead set an environment variable `OPENWEATHER_API_KEY`. Update the code to read it with:

```python
import os
API_KEY = os.getenv("OPENWEATHER_API_KEY")
```

**Suggested improvements**

- Move API key to environment variable; never commit secrets.
- Add error handling for timeouts and malformed API responses.
- Validate and sanitize user input.
- Add a `requirements.txt` and a short contribution section.
- Add license and author details.

**Files**

- `weather.py` — CLI version.
- `weather_gui.py` — Tkinter GUI frontend.
- `README.md` — (this file).

