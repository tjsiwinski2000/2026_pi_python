import json
import uuid
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .agent import agent

@require_POST
def save_location(request):
    try:
        lat = float(request.POST["lat"])
        lon = float(request.POST["lon"])
    except (KeyError, ValueError):
        return JsonResponse({"ok": False}, status=400)

    request.session["user_location"] = {"lat": lat, "lon": lon}
    print(f"in save_location:{request.session.get('user_location')}")
    return JsonResponse({"ok": True})

def chat_reply(request):
    data = json.loads(request.body)
    message = data.get("message", "")

    if "thread_id" not in request.session:
        # uid4() gens a random unique ID, str() turns it into text 
        request.session["thread_id"] = str(uuid.uuid4())

    loc = request.session.get("user_location")
    agent_input = message
    if loc:
        agent_input = f"{message}\n\n(User's coordinates: lat {loc['lat']}, lon {loc['lon']})"
    response = agent.invoke(
        {"messages": [{"role": "user", "content": agent_input}]},
        {"configurable": {"thread_id": request.session["thread_id"]}},
    )

    ai_response = response["messages"][-1].text
    messages = request.session.get("messages", [])
    messages.append({"sender": "user", "text": message})
    messages.append({"sender": "agent", "text": ai_response})
    request.session["messages"] = messages
    request.session.modified = True

    return JsonResponse({"reply": ai_response})