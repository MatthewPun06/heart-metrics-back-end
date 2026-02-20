import os
from flask import Flask
from sb_client import supabase

app = Flask(__name__)

# define a route to display the todos from the "todos" table in Supabase
@app.route('/')
def index():
    response = supabase.table('users').select("*").execute()
    users = response.data
    # generate basic/temporary HTML to display the users
    # RETURN NORMAL JSON INSTEAD OF HTML LATER ON
    html = '<h1>Users</h1><ul>'
    for user in users:
        html += f'<li>{user["name"]}</li>'
    html += '</ul>'

    return html

if __name__ == '__main__':
    app.run(debug=True)
