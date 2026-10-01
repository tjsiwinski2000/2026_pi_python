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

## python manage.py shell [test working] ##
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


### next items 5:00 pm 0929-2026 ###

**Where things stand**
- `chat_reply` view is done and tested from the shell
- `chat-reply/` path is in `chatbot/urls.py`
- Location fix works: the saved lat/lon is added to the agent's input, and the same question now gives Chicago every time

**Cleanup**
1. Remove the temporary `print("agent_input:", agent_input)` line from `chat_reply` (and the `print` in `save_location` if you no longer need it).

**Browser side (`index.html`)**
2. Look at the existing chat markup: the input box, the send button or `<form>`, and the area where messages show up.
3. If the old Flask form (posting to `/send`) is still there, change it so it doesn't reload the page, or have the button call JavaScript instead.
4. Write a `sendMessage()` function in the same `<script>` block as the `save-location` fetch. It should:
   - read the text from the input box
   - `fetch("/chatbot/chat-reply/", ...)` with:
     - `method: "POST"`
     - `"X-CSRFToken": "{{ csrf_token }}"` in the headers
     - `"Content-Type": "application/json"` in the headers
     - `body: JSON.stringify({ message: <the text> })`
   - read the JSON response and show `reply` on the page
5. Make the send button (or form submit) call `sendMessage()`.

**Test in the browser**
6. Ask about a named city, then ask "what's the weather here?" and check that the location comes through.
7. Reload the page and check what happens to the chat history (`session["messages"]` is saved, but the page has to display it).

**Later**
8. Deployment to PythonAnywhere, including the Python version (the nested-quote f-strings need 3.12+) and setting the API keys as environment variables.

When you're back, paste the chat section of `index.html` and we'll start at step 2.