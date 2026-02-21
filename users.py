# handle user based queries in the database

from urllib import response

from supabase import Client
from sb_client import supabase   # adjust import name if needed

def create_user(name: str, email: str, password: str):
    # Use admin API to bypass rate limits in development
    try:
        response = supabase.auth.admin.create_user({
            "email": email,
            "password": password,
            "email_confirm": True  # Auto-confirm email in dev
        })
        # adds the user to the "users" table with the same id as the auth user
        user_id = response.user.id
        print(f"Created user with ID: {user_id}")
        supabase.table("users").insert({
            "id": user_id,
            "name": name,
            "email": email
        }).execute()
        return response
    except Exception as e:
        return {"error": str(e)}
    
def get_user_id(email: str):
    response = supabase.auth.get_user(email).execute()
    if response.data:
        return response.data.id
    return None

def delete_user(user_id: str):
    # deletes the user from the "users" table
    supabase.table("users").delete().eq("id", user_id).execute()
    # deletes the user from Supabase Auth
    response = supabase.auth.admin.delete_user(user_id)
    return response

def login_user(email: str, password: str):
    response = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })
    return response

def get_user_profile(user_id: str):
    response = supabase.table("users") \
        .select("*") \
        .eq("id", user_id) \
        .execute()
    return response