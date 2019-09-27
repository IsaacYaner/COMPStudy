from flask import Flask

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy

# Loads data
orders = {}
