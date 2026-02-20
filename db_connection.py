# handle connection to the database
from supabase import create_client
from sb_client import supabase   # adjust import name if needed
supabase = create_client()