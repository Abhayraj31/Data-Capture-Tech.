import firebase_admin
import csv, random
from datetime import datetime
# from firebase_admin import credentials

databaseURL = 'https://feb25-59968-default-rtdb.asia-southeast1.firebasedatabase.app/'
cred_obj = firebase_admin.credentials.Certificate(
    'new.json'
)
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':databaseURL
	})

from firebase_admin import db

# A reference point is always needed to be set
# before any operation is carried out on a database.
# 
ref = db.reference("/")
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# JSON format data (key/value pair)
data = { 
  "Sensor": [ 
    { 
      "Name": "DHT22",
      "Readings": [   { 
    "Time": "2025-02-02 11:26:08",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:09",
    "Distance (cm)": "Distance: 34 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:11",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:11",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:12",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:13",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:14",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:15",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:16",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:17",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:18",
    "Distance (cm)": "Distance: 34 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:19",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:20",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:21",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:22",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:23",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:24",
    "Distance (cm)": "Distance: 34 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:25",
    "Distance (cm)": "Distance: 34 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:26",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:27",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:28",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:29",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:30",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:31",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:32",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:33",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:34",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:35",
    "Distance (cm)": "Distance: 35 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:36",
    "Distance (cm)": "Distance: 34 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:37",
    "Distance (cm)": "Distance: 34 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:38",
    "Distance (cm)": "Distance: 28 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:39",
    "Distance (cm)": "Distance: 4 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:40",
    "Distance (cm)": "Distance: 55 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:41",
    "Distance (cm)": "Distance: 28 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:42",
    "Distance (cm)": "Distance: 796 cm" 
  },
  { 
    "Time": "2025-02-02 11:26:43",
    "Distance (cm)": "Distance: 51 cm" 
  }
        
      ] 
    }
    
  ] 
}

# JSON format data is set (overwritten) to the reference 
# point set at /, which is the root node.
# 
ref.set(data)
