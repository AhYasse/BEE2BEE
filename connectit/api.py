
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import List, Optional
import asyncio
from contextlib import asynccontextmanager

from .p2p_runtime import P2PNode

# Global node instance
node: Optional[P2PNode] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global node
    # Initialize node on startup with random port or configured port
    import os
    port = int(os.getenv("CONNECTIT_PORT", "4001"))
    host = os.getenv("CONNECTIT_HOST", "0.0.0.0")
    
    node = P2PNode(host=host, port=port)
    await node.start()
    
    # Auto-bootstrap if env var is set
    bootstrap = os.getenv("CONNECTIT_BOOTSTRAP")
    if bootstrap:
        await node.connect_bootstrap(bootstrap)

    # Enable Supervisor Monitoring
    await node.enable_monitoring(interval_seconds=60) # Default to 60s for demo, can be longer
    
    # --- PRINT INSTRUCTIONS FOR USER ---
    from rich.console import Console
    from .utils import get_lan_ip
    console = Console()
    
    # Determine accessible address
    real_ip = get_lan_ip()
    # If the node is bound to 0.0.0.0, we use the LAN IP. 
    # If it was specific, we use that.
    if node.host == "0.0.0.0":
        display_host = real_ip
    else:
        display_host = node.host
        
    bootstrap_addr = f"ws://{display_host}:{node.port}"
    
    console.print("\n[bold yellow]✨ Main Point Started Successfully![/bold yellow]")
    console.print("[dim]To connect other nodes to this network, run this command on them:[/dim]")
    console.print(f"\n   [bold cyan]python -m connectit config bootstrap_url {bootstrap_addr}[/bold cyan]\n")
    # -----------------------------------
        
    yield
    
    # Cleanup
    if node:
        await node.stop()

app = FastAPI(title="ConnectIT Node API", lifespan=lifespan)

class PeerInfo(BaseModel):
    peer_id: str
    addr: str
    latency_ms: Optional[float]

class ProviderInfo(BaseModel):
    peer_id: str
    addr: Optional[str]
    latency_ms: Optional[float]
    models: List[str]
    price_per_token: Optional[float]

@app.get("/")
def home():
    return {"status": "ok", "node_id": node.peer_id if node else "not_started"}

@app.get("/peers")
def get_peers():
    if not node:
        return []
    res = []
    for pid, info in node.peers.items():
        res.append({
            "peer_id": pid,
            "addr": info.get("addr", ""),
            "latency_ms": info.get("last_pong_ms"),
            "health_status": info.get("health_status", "unknown"),
            "last_audit": info.get("last_audit", 0)
        })
    return res

@app.get("/providers", response_model=List[ProviderInfo])
def list_providers():
    if not node:
        return []
    return node.list_providers()

@app.get("/connect")
async def connect_peer(addr: str):
    if not node:
        return {"error": "Node not running"}
    try:
        if addr.startswith("p2pnet"):
            await node.connect_bootstrap(addr)
        else:
            await node._connect_peer(addr)
        return {"status": "connected", "addr": addr}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
