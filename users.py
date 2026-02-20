# handle user based queries in the database

from supabase import Client
from sb_client import supabase   # adjust import name if needed

def create_user(email: str, password: str):
    response = supabase.auth.sign_up({
        "email": email,
        "password": password
    })
    return response

def login_user(email: str, password: str):
    response = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
    return response

def get_user_profile(user_id: str):
    response = supabase.table("profiles") \
        .select("*") \
        .eq("id", user_id) \
        .execute()
    return response