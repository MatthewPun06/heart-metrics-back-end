import os
from supabase import create_client, Client
from dotenv import load_dotenv

# load the environment variables from the .env file
# SUPABASE_URL and SUPABASE_KEY should be defined in the .env file
load_dotenv()

# create a Supabase client using the URL and key from the environment variables
supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_KEY")
)
