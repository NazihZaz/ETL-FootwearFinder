from flask import Flask, render_template

# Import our psycopg2 library, which lets us connect our Flask app to our Postgres database.
import sqlalchemy

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'postgresql://postgres:Payrol662!@localhost:5433/FootwearFinderDB'

# Pass connection url to the sqlalchemy create_engine method
engine = sqlalchemy.create_engine(conn)

# Connection to a database was done during the instantiation of the 
# engine above and database MUST exist.

# Drops collection if available to remove duplicates
# engine.execute("DROP TABLE IF EXISTS team;")

# # Create the table "team" within team_db 
# engine.execute('''
# CREATE TABLE team (
#   id SERIAL PRIMARY KEY,
#   player VARCHAR(30) NOT NULL,
#   position VARCHAR(30)
# )''')

# # Insert two rows into the table
# engine.execute('''
# INSERT INTO team (player, position)
# VALUES ('Jessica', 'Point Guard'),
#   ('Mark', 'Center')''')


# Set route
@app.route('/')
def index():
    # Store the entire footwear collection in a list
    shoes = engine.execute("SELECT * FROM shoes")

    # Return the template with the footwear list passed in
    return render_template('index.html', shoes=shoes)


if __name__ == "__main__":
    app.run(debug=True)
