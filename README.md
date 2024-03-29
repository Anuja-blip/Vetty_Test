# Vetty_Test

This Flask application reads the content of specified text files, allowing optional parameters for line range filtering.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setting Up and Running the Application

### Create a Virtual Environment

```bash
 python -m venv venv
```
## Activate the Virtual Environment

### On Windows:

```bash
.\venv\Scripts\activate
```
### On Unix or MacOS:
```bash
venv/bin/activate
```
### Install Dependencies

```bash
pip install -r requirements.txt
```
### Running the Application
**Run the Flask application:**


```bash
python app.py
```


Open your browser and go to http://127.0.0.1:5000/file_content to view the default file content.

Optionally, specify a file name and line range using URL parameters:

Example: http://127.0.0.1:5000/file_content/file2.txt?start_line=2&end_line=5

### Deactivating the Virtual Environment
When you're done using the application, deactivate the virtual environment:

```bash
deactivate
```

