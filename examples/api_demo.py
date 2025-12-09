
import asyncio
import time
import requests
import multiprocessing
import uvicorn
from bee2bee.api import app

def start_api_server():
    """Run the API server in a separate process."""
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

def run_demo():
    print("🚀 Starting Bee2Bee API Demo...")
    
    # Start API in background process
    p = multiprocessing.Process(target=start_api_server)
    p.start()
    
    try:
        # Wait for server startup
        print("⏳ Waiting for server to start...")
        time.sleep(3)
        
        # 1. Check status
        print("\n1️⃣ Checking Node Status:")
        try:
            resp = requests.get("http://127.0.0.1:8000/")
            print(f"   Status: {resp.status_code}")
            print(f"   Response: {resp.json()}")
        except Exception as e:
            print(f"   Error: {e}")
            
        # 2. List Peers (initially empty)
        print("\n2️⃣ Listing Peers:")
        resp = requests.get("http://127.0.0.1:8000/peers")
        print(f"   Peers: {resp.json()}")

        # 3. Simulate Connect (if we had another node)
        # requests.get("http://127.0.0.1:8000/connect?addr=ws://localhost:4002")

        print("\n✅ Demo completed successfully!")
        
    finally:
        print("\n🛑 Stopping server...")
        p.terminate()
        p.join()

if __name__ == "__main__":
    run_demo()
