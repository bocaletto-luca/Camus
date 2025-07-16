# examples/chat/app.py
from camus.core import CamusApp

app = CamusApp(name="ChatExample")

@app.register_event("message")
async def handle_message(payload, websocket, app: CamusApp):
    """
    Broadcast incoming chat message to all connected clients.
    payload should be a dict: {"username": "...", "text": "..."}
    """
    for ws in app.clients:
        if ws != websocket:
            await ws.send_json({
                "event": "message",
                "payload": payload
            })

if __name__ == "__main__":
    # This allows running `python examples/chat/app.py` directly
    app.run()
