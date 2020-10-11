import os
import sqlite3
from dotenv import load_dotenv # pip install python-dotenv
conn = sqlite3.connect('secret.db')

# bad way
login = "db_login"
password = "db_password"

print(login, password, "hardcoded")
# good way
# get data from .env file (don't forget to add .env to .gitignore)
load_dotenv()

login = os.environ.get('DB_LOGIN')
password = os.environ.get('DB_PASS')
print(login, password, "from environ")

c = conn.cursor(
    # here could be login and pass
)

# c.execute('''CREATE TABLE users
#              (username text, email text)''')

# c.execute("INSERT INTO users VALUES ('dennis','dennis@example.com')")

# conn.commit()

# c.execute('SELECT * FROM users')

# for row in c:
#     print(row)
conn.close()

