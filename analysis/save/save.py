import os
from supabase_py import create_client, Client
url = "https://oijeyquhvtggsqshldnm.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9pamV5cXVodnRnZ3Nxc2hsZG5tIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTE2MDUxMzcsImV4cCI6MjAwNzE4MTEzN30.Pap8ZUU3EWk6ELQ0txIJzlOGJ6RiExI6dUp_z9gfx44"
supabase: Client = create_client(url, key)


# Save Function
def save(table, data: dict):
    supabase.table(table).insert(data).execute()


