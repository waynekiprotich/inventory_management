# Inventory Management System

This project is a Python-based Inventory Management . It features a Flask RESTful API backend, 
a command-line interface (CLI) frontend, and integration with the external Open Food Facts API 
to automatically retrieve product details via barcode.

## Features
**Flask Routing:** API routes built for `GET`, `POST`, `PATCH`, and `DELETE` requests.
**CRUD Operations:** Full ability to view, add, update, and remove inventory items.
**External API Integration:** Connects to Open Food Facts to fetch product names and brands automatically when a barcode is entered.


## Setup Instructions

# Setup Instructions
1. Clone the repository
2. Create a virtual environment

# Mac/Linux:

Bash
python3 -m venv venv
source venv/bin/activate
# Windows:

Bash
python -m venv venv
venv\Scripts\activate

# Install Dependencies

Bash
pip install flask requests pytest
How to Run the Application
This application requires two separate terminal windows to run simultaneously: one for the Flask server and one for the CLI interface.

Terminal 1: Start the Server
Make sure your virtual environment is activated, then start the Flask API:

Bash
python app.py
The server will start running locally on http://127.0.0.1:5000

Terminal 2: Run the CLI
Open a second terminal window, navigate to the project folder, activate the virtual environment again, and run the CLI:

Bash
python cli.py
Follow the on-screen menu prompts to interact with the database.