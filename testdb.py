from database import Database
from config import DB_CONFIG

# Initialize the database
db = Database(**DB_CONFIG)

# Fetch some data
query = "SELECT * FROM Student WHERE studentID = ?"
params = ("3",)
results = db.execute_query(query, params)
print(results)

# if results:
#     for row in results:
#         print(row)

# Close the database connection
db.close()
