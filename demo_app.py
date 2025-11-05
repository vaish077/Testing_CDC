# file: demo_app.py
# -----------------
# Dummy example showing a username, password, and API key in code.
# DO NOT USE IN PRODUCTION.

DUMMY_USERNAME = "demo_user_42"
DUMMY_PASSWORD = "P@ssw0rd!NotReal123"
DUMMY_API_KEY  = "api_test_1234567890abcdefFEDCBA9876543210"

def login(username: str, password: str) -> dict:
    """Pretend to authenticate with hard-coded credentials."""
    if username == DUMMY_USERNAME and password == DUMMY_PASSWORD:
        return {"token": "session_token_abcdef123456"}
    raise ValueError("Invalid credentials (dummy).")

def call_service(api_key: str) -> dict:
    """Pretend to call a protected API."""
    if api_key != DUMMY_API_KEY:
        raise PermissionError("Invalid API key (dummy).")
    return {"status": "ok", "data": {"message": "Hello, world!"}}

if __name__ == "__main__":
    try:
        # Using the dummy values directly
        auth = login(DUMMY_USERNAME, DUMMY_PASSWORD)
        print("Authenticated with token:", auth["token"])

        res = call_service(DUMMY_API_KEY)
        print("API call result:", res)
    except Exception as e:
        print("Error:", e)
