import os
from supabase_py import create_client, Client
url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')
supabase: Client = create_client(url, key)


# Save Function
def save(table, data: dict):
    supabase.table(table).insert(data).execute()


