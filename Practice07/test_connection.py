from connect import get_connection

conn = get_connection()
if conn:
    print("✅ Connection OK")
else:
    print("❌ Failed to connect")