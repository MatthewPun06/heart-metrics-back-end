from sb_client import supabase
import pandas as pd

response = supabase.table("users").select("*").execute()

data = response.data

df = pd.DataFrame(data)

print(df.head())