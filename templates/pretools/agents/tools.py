from cogsol.tools import BaseTool


class CurrentDateTimeTool(BaseTool):
    """Provides the current date and time for Montevideo (UTC-3)."""

    name = "current_datetime"
    description = (
        "Returns the current date, time, day of the week, and period "
        "of the day for Montevideo (UTC-3). Call this tool to provide "
        "temporal context before responding to the user."
    )

    def run(self, chat=None, data=None, secrets=None, log=None):
        try:
            from datetime import datetime, timezone, timedelta

            log.append("Fetching current date and time for Montevideo (UTC-3)")

            tz = timezone(timedelta(hours=-3))
            now = datetime.now(tz)
            hour = now.hour

            if hour < 12:
                period = "morning"
            elif hour < 18:
                period = "afternoon"
            else:
                period = "evening"

            result = {
                "date": now.strftime("%Y-%m-%d"),
                "time": now.strftime("%H:%M"),
                "day_of_week": now.strftime("%A"),
                "period": period,
                "timezone": "UTC-3 (Montevideo)",
            }

            log.append(f"Result: {result['date']} {result['time']} ({period})")

            return result

        except Exception as exc:
            log.append(f"Error: {exc}")
            return {"error": str(exc)}


class WeatherInfoTool(BaseTool):
    """Fetches current weather for Montevideo from the Open-Meteo API."""

    name = "weather_info"
    description = (
        "Returns the current weather conditions for Montevideo including "
        "temperature, sky condition, and wind speed. Uses the free "
        "Open-Meteo API (no API key required)."
    )

    def run(self, chat=None, data=None, secrets=None, log=None):
        try:
            import json
            import urllib.request

            log.append("Fetching weather from Open-Meteo API")

            weather_codes = {
                0: "Clear sky",
                1: "Mainly clear",
                2: "Partly cloudy",
                3: "Overcast",
                45: "Fog",
                48: "Depositing rime fog",
                51: "Light drizzle",
                53: "Moderate drizzle",
                55: "Dense drizzle",
                61: "Slight rain",
                63: "Moderate rain",
                65: "Heavy rain",
                71: "Slight snow fall",
                73: "Moderate snow fall",
                75: "Heavy snow fall",
                77: "Snow grains",
                80: "Slight rain showers",
                81: "Moderate rain showers",
                82: "Violent rain showers",
                85: "Slight snow showers",
                86: "Heavy snow showers",
                95: "Thunderstorm",
                96: "Thunderstorm with slight hail",
                99: "Thunderstorm with heavy hail",
            }

            latitude = -34.9011
            longitude = -56.1645

            url = (
                f"https://api.open-meteo.com/v1/forecast"
                f"?latitude={latitude}&longitude={longitude}"
                f"&current_weather=true"
            )

            with urllib.request.urlopen(url, timeout=5) as response:
                weather_data = json.loads(response.read().decode())

            weather = weather_data["current_weather"]
            code = weather.get("weathercode", -1)
            condition = weather_codes.get(code, "Unknown")

            result = {
                "temperature_celsius": weather["temperature"],
                "condition": condition,
                "wind_speed_kmh": weather["windspeed"],
                "location": "Montevideo, Uruguay",
            }

            log.append(
                f"Result: {result['temperature_celsius']}°C, "
                f"{result['condition']}, wind {result['wind_speed_kmh']} km/h"
            )

            return result

        except Exception as exc:
            log.append(f"Error fetching weather: {exc}")
            return {"error": "Could not fetch weather data."}


class DailyTipTool(BaseTool):
    """Provides a CogSol Framework tip that rotates daily."""

    name = "daily_tip"
    description = (
        "Returns a CogSol Framework tip of the day. The tip rotates "
        "automatically based on the current date."
    )

    def run(self, chat=None, data=None, secrets=None, log=None):
        try:
            from datetime import datetime, timezone, timedelta

            log.append("Selecting tip of the day")

            tips = [
                "Run `makemigrations` before `migrate` to review changes before deploying them.",
                "Use `genconfigs.QA()` for conversational agents and `genconfigs.FastRetrieval()` for search-focused pretools.",
                "Keep system prompts in separate Markdown files under prompts/ for easy editing.",
                "Each tool should do one thing well — split complex logic into multiple tools.",
                "Use `max_consecutive_tool_calls` to prevent infinite tool-call loops.",
                "FAQs are matched by semantic similarity, while fixed responses use exact key matching.",
                "Lessons shape the agent's behavior across all responses — use them for guidelines and best practices.",
                "Store environment variables in `.env` and never commit credentials to version control.",
                "Use `python manage.py chat --agent AgentName` to test your agent interactively after deploying.",
                "Pretools run before the main generation phase — use them to gather context that enriches the agent's response.",
            ]

            tz = timezone(timedelta(hours=-3))
            day_of_year = datetime.now(tz).timetuple().tm_yday
            index = day_of_year % len(tips)
            tip = tips[index]

            log.append(f"Selected tip #{index + 1}: {tip[:50]}...")

            return {"tip": tip}

        except Exception as exc:
            log.append(f"Error: {exc}")
            return {"error": str(exc)}
