import couchdb
import pandas as pd
import json

# 🔹 CouchDB Configuration
COUCHDB_URL = "http://abhayraj:abhayraj@localhost:5984/"  # Update with your credentials
DATABASE_NAME = "gyroscope"
CSV_FILENAME = "gyroscopedata.csv"

# ✅ Connect to CouchDB
try:
    couch = couchdb.Server(COUCHDB_URL)
    if DATABASE_NAME in couch:
        db = couch[DATABASE_NAME]
        print(f"✅ Connected to CouchDB. Fetching data from {DATABASE_NAME}...")
    else:
        print(f"❌ Database '{DATABASE_NAME}' not found.")
        exit(1)
except Exception as e:
    print(f"❌ Failed to connect to CouchDB: {e}")
    exit(1)

# 🔹 Fetch all documents from CouchDB
data_list = []
for doc_id in db:
    doc = db[doc_id]
    # Remove CouchDB metadata (_id, _rev) if not needed
    doc.pop('_id', None)
    doc.pop('_rev', None)
    data_list.append(doc)

# 🔹 Convert to DataFrame
if data_list:
    df = pd.DataFrame(data_list)
    # ✅ Save to CSV
    df.to_csv(CSV_FILENAME, index=False)
    print(f"📂 Data exported successfully to {CSV_FILENAME}")
else:
    print("⚠️ No data found in the database.")

