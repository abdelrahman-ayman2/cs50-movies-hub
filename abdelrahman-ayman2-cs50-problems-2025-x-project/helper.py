import difflib
import requests

from flask import redirect, render_template, session
from functools import wraps

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function



def lookup(title):
    # رابط الـ API
    url = "https://streaming-availability.p.rapidapi.com/shows/search/title"

    # المدخلات (query parameters)
    querystring = {
        "title": title,
        "series_granularity": "show",
        "show_type": "movie",
        "output_language": "en",
        "country" : "us"
    }

    # الهيدر (رأس الطلب) يحتوي على المفاتيح الخاصة بـ API
    headers = {
        "x-rapidapi-host": "streaming-availability.p.rapidapi.com",
        "x-rapidapi-key": "a67b323726msh877ee1141695560p142688jsncb4a17ab9560"
    }

    try:
        # إرسال الطلب
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        # استخراج النتائج
        if not data or not isinstance(data, list):
            print(f"No results found for: {title}")
            return None
        
        # أول نتيجة
        result = data[0]

        poster_url = result.get("imageSet", {}).get("verticalPoster", {}).get("w480")

        # تجهيز البيانات المستخرجة
        return {
            "title": result.get("title"),
            "year": result.get("releaseYear"),
            "poster": result["imageSet"]["verticalPoster"]["w480"],
            "cast": result.get("cast", []),
            "genres": [g["name"] for g in result.get("genres", [])],
            "directors": result.get("directors", []),
            "streaming": [
                {
                    "name": option["service"]["name"],
                    "type": option["type"],
                    "link": option["link"]
                }
                for option in result.get("streamingOptions", {}).get("us", [])
            ]
        }

    except Exception as e:
        # Error occurred while fetching movie data: e
        return None
