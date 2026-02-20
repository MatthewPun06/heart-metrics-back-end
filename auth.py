from flask import request
from supabase import create_client

supabase = create_client()

def get_user_from_request():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None
    
    token = auth_header.split(" ")[1]
    
    # Verify token with Supabase
    user = supabase.auth.get_user(token)
    
    return user