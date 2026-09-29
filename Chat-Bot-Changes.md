### chatbot changes made 0928-2026 ###
python manage.py startapp chatbot <br>
--- creates new app into the project<br>

move agents.py into \chatbot\ <br>
--- existing code ported from UDEMY class with some edits<br>

---
(main) settings.py edit: add chatbot to INSTALLED_APPS<br>
(main) urls.py edit: add ref to 'chatbot.urls'<br>
(chatbot) create urls.py -> /save-location/ -> (chatbot) views.save_location<br>
(chatbot) views.save_location update session with user_location for life of current session<br>

index.html has this javascript call: fetch("/chatbot/save-location/" ....
---

python manage.py shell

from chatbot.agent import agent
config = {"configurable": {"thread_id": "test1"}}
result = agent.invoke({"messages": [{"role": "user", "content": "What's the weather in Paris?"}]}, config)
print(result["messages"][-1].content)

---
from django.test import Client 

**Client** is a fake web browser that lives inside Python.<BR> Django ships it for testing, so you can call your views without starting the server or opening a page.<BR>

The import line just brings that tool into your shell session, the same way import json brings in the json module.

When you write c = Client(), you create one of these pretend browsers. It has three properties that matter here:

It calls your view directly. c.post("/chatbot/chat-reply/", ...) sends a POST to that URL, and Django routes it through urls.py to chat_reply, exactly like a real request.
It remembers cookies. The session cookie from the first call is sent with the second call, so thread_id and messages stick around between calls, like a real browser tab.
It skips the CSRF check. That's why no token is needed from the shell.

### 0929-2026 testing chat-reply###
from django.test import Client
c = Client()
r = c.post(
    "/chatbot/chat-reply/",
    {"message": "what's the weather in here?"},
    content_type="application/json",
    HTTP_HOST="localhost",
)
print(r.status_code)
print(r.json())
>>> print(r.status_code)
200
>>> print(r.json())
{'reply': [{'type': 'text', 'text': 'The weather in Chicago is 76.6°F with scattered clouds.', 'extras': {'signature': 'EmAKXgFpFH0Tl8/N5/MgZRT/W/EpQTB1hwuRHSzb5301sG4aCfPXHCBfXz2b3mXxR3nCV4L3ZWGBGOEYR1+xPG7jDLQWA9uLnNxmY8tQotgdI6gYXnMNb6Sw66pLO6ZDdQo='}}]}

MUST DO
   from django.test import Client
   c = Client()
   s = c.session
   s["user_location"] = {"lat": 41.85, "lon": -87.65}
   s.save()
      r = c.post(
       "/chatbot/chat-reply/",
       {"message": "what's the weather here?"},
       content_type="application/json",
       HTTP_HOST="localhost",
   )
   print(r.json())