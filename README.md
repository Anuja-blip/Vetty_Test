# Vetty_Test

This Flask application reads the content of specified text files, allowing optional parameters for line range filtering.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup

1. Clone the repository:

   git clone https://github.com/your-username/VETTY_TEST.git
   cd VETTY_TEST

   ## Setting Up and Running the Application

### Create a Virtual Environment


python -m venv venv
## Activate the Virtual Environment

### On Windows:


.\venv\Scripts\activate

On Unix or MacOS:

source venv/bin/activate

### Install Dependencies


pip install -r requirements.txt

### Running the Application
###Run the Flask application:



python app.py

Open your browser and go to http://127.0.0.1:5000/file_content to view the default file content.

Optionally, specify a file name and line range using URL parameters:

Example: http://127.0.0.1:5000/file_content/file2.txt?start_line=2&end_line=5
