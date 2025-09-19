#!/usr/bin/env python3
import requests
import json
import sys

def test_api_endpoints():
    """Test all API endpoints to identify the 405 error"""
    
    # Test with local API first, then deployed
    base_urls = [
        "http://localhost:5000",  # Local development
        "https://your-vercel-url.vercel.app"  # Update with your actual Vercel URL
    ]
    
    for base_url in base_urls:
        print(f"\n=== Testing {base_url} ===")
        
        # Test 1: Health check (GET)
        try:
            response = requests.get(f"{base_url}/api/health", timeout=10)
            print(f"Health check: Status {response.status_code}")
            if response.status_code == 200:
                print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Health check failed: {e}")
        
        # Test 2: Test endpoint (GET)
        try:
            response = requests.get(f"{base_url}/api/test", timeout=10)
            print(f"Test GET: Status {response.status_code}")
            if response.status_code == 200:
                print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Test GET failed: {e}")
        
        # Test 3: Test endpoint (POST)
        try:
            response = requests.post(f"{base_url}/api/test", 
                                   json={"test": "data"}, 
                                   timeout=10)
            print(f"Test POST: Status {response.status_code}")
            if response.status_code == 200:
                print(f"Response: {response.json()}")
        except Exception as e:
            print(f"Test POST failed: {e}")
        
        # Test 4: Match skills (POST) - This is the problematic one
        try:
            test_skills = ["Python", "Data Analysis", "Machine Learning"]
            response = requests.post(f"{base_url}/api/match-skills", 
                                   json={"skills": test_skills},
                                   headers={"Content-Type": "application/json"},
                                   timeout=10)
            print(f"Match skills: Status {response.status_code}")
            if response.status_code == 200:
                matches = response.json()
                print(f"Found {len(matches)} matches")
                if matches:
                    print(f"Top match: {matches[0]['title']} - {matches[0]['match_score']:.1f}%")
            else:
                print(f"Error response: {response.text}")
        except Exception as e:
            print(f"Match skills failed: {e}")
        
        # Test 5: Check if OPTIONS is working for match-skills
        try:
            response = requests.options(f"{base_url}/api/match-skills", timeout=10)
            print(f"Match skills OPTIONS: Status {response.status_code}")
            print(f"Allowed methods: {response.headers.get('Allow', 'Not specified')}")
            print(f"CORS headers: {response.headers.get('Access-Control-Allow-Methods', 'Not specified')}")
        except Exception as e:
            print(f"Match skills OPTIONS failed: {e}")

if __name__ == "__main__":
    test_api_endpoints()
