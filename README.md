# Inventory Management System

This project is a Python-based Inventory Management System. It features a Flask RESTful API backend, a command-line interface (CLI) frontend, and integration with the external Open Food Facts API to automatically retrieve product details via barcode.

## Features
* **Flask Routing:** API routes built for `GET`, `POST`, `PATCH`, and `DELETE` requests.
* **CRUD Operations:** Full ability to view, add, update, and remove inventory items.
* **External API Integration:** Connects to Open Food Facts to fetch product names and brands automatically.

---

## Setup Instructions

**1. Clone the repository**
```bash
git clone <git@github.com:waynekiprotich/inventory_management.git>
cd inventory_management
```

Create and activate a virtual environment

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install flask requests pytest
```
How to Run the Application
This application requires two separate terminal windows to run simultaneously.

Terminal 1: Start the Server
In the first terminal, ensure your virtual environment is active and start the Flask API:

```bash
python app.py
```
The server will run locally on http://127.0.0.1:5000

Terminal 2: Run the CLI
In a second terminal, navigate to the project folder, activate the virtual environment, and run the interface:

```bash
python cli.py
```
Follow the on-screen menu prompts to interact with the application.