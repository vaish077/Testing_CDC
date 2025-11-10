  # Harmless test file to validate UpGuard GitHub monitoring

SERVICE_URL = "https://api.tredence.com/v1/status"
api_key = "testingUGThreatMonitoring"  # mock key for signal detection

def ping_service():
   print(f"Checking {SERVICE_URL} with key {api_key[:8]}...")

if __name__ == "__main__":

ping_service()
