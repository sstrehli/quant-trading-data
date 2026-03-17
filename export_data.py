#!/usr/bin/env python3
"""
Export Enhanced V2 API data to JSON files for GitHub Pages
"""

import json
import requests
from datetime import datetime
import os

# GitHub Pages data directory
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

# Enhanced V2 API endpoints (via ngrok tunnel)
API_BASE = "https://verna-unsicker-gorgedly.ngrok-free.dev/api"

def fetch_endpoint(endpoint):
    """Fetch data from Enhanced V2 API"""
    try:
        url = f"{API_BASE}/{endpoint}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching {endpoint}: {e}")
        return {"status": "error", "message": str(e), "timestamp": datetime.now().isoformat()}

def export_to_json(data, filename):
    """Export data to JSON file"""
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Exported {filename} ({len(json.dumps(data))} bytes)")

def create_health_status():
    """Create health status file"""
    health_data = {
        "status": "healthy",
        "service": "quant-trading-data-github-pages",
        "version": "1.0.0",
        "endpoints": [
            "trades.json",
            "signals.json", 
            "sessions.json",
            "positions.json",
            "health.json"
        ],
        "last_updated": datetime.now().isoformat(),
        "update_frequency": "5 minutes",
        "data_source": "Enhanced V2 API via ngrok",
        "features": [
            "enhanced_closed_positions",
            "enhanced_session_performance", 
            "enhanced_signals",
            "model_attribution",
            "reason_codes",
            "session_tracking"
        ]
    }
    return health_data

def main():
    """Main export function"""
    print(f"Exporting Enhanced V2 API data to GitHub Pages format")
    print(f"Data directory: {DATA_DIR}")
    print(f"API base: {API_BASE}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print("-" * 60)
    
    # Fetch and export all endpoints
    endpoints = {
        "positions/open": "positions.json",
        "trades/closed": "trades.json",
        "sessions/performance": "sessions.json",
        "signals/current": "signals.json",
        "dashboard/summary": "summary.json"
    }
    
    for endpoint, filename in endpoints.items():
        print(f"Fetching {endpoint}...")
        data = fetch_endpoint(endpoint)
        export_to_json(data, filename)
    
    # Create health status
    print("Creating health status...")
    health_data = create_health_status()
    export_to_json(health_data, "health.json")
    
    print("-" * 60)
    print("Export complete!")
    print(f"Files created in {DATA_DIR}:")
    for f in os.listdir(DATA_DIR):
        if f.endswith('.json'):
            size = os.path.getsize(os.path.join(DATA_DIR, f))
            print(f"  - {f} ({size} bytes)")

if __name__ == "__main__":
    main()