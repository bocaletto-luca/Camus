# camus/core.py
import yaml
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn

class CamusApp:
    def __init__(self, name: str, config_path: str = "config.yaml"):
        # Load configuration
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)
        self.name = name
        self.app = FastAPI(title=name)
        self.clients: list[WebSocket] = []
        self.handlers: dict[str, asyncio.coroutine] = {}
        self._setup_routes()

    def _setup_routes(self):
        @self.app.get("/health")
        async def health():
            return {"status": "ok"}

        @self.app.websocket("/ws")
        async def websocket_endpoint(ws: WebSocket):
            await ws.accept()
            self.clients.append(ws)
            try:
                while True:
                    data = await ws.receive_json()
                    event = data.get("event")
                    payload = data.get("payload")
                    handler = self.handlers.get(event)
                    if handler:
                        # handler(payload, ws, self) may broadcast or reply
                        await handler(payload, ws, self)
            except WebSocketDisconnect:
                self.clients.remove(ws)

    def register_event(self, event_name: str):
        """
        Decorator to register a coroutine as event handler.
        Handler signature: async def(payload, websocket, app)
        """
        def decorator(func):
            self.handlers[event_name] = func
            return func
        return decorator

    def run(self,
            host: str = None,
            port: int = None,
            reload: bool = False):
        host = host or self.config["server"]["host"]
        port = port or self.config["server"]["port"]
        uvicorn.run(
            self.app,
            host=host,
            port=port,
            reload=reload
        )
