from flask import Flask, render_template, request
import chardet 

app = Flask(__name__)

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/file_content', defaults={'file_name': 'file1.txt'}, methods=['GET'])
@app.route('/file_content/<file_name>', methods=['GET'])
def get_file_content(file_name='file1.txt'):
    try:
        # Get start and end line numbers from URL query parameters, default to None
        start_line = request.args.get('start_line', None, type=int)
        end_line = request.args.get('end_line', None, type=int)
        
        # Convert start_line and end_line to integers, providing default values if None
        start_line = int(start_line) if start_line is not None else None
        end_line = int(end_line) if end_line is not None else None
        
        #detect the encoding of the files
        encoding = detect_file_encoding(file_name)
        
        # Read content of the specified file
        with open(file_name, 'r', encoding=encoding) as file:
            lines = file.readlines()

        # Filter lines based on start and end line numbers
        if start_line is not None and end_line is not None:
           lines = lines[start_line-1:end_line]

        # Join lines to form the content
        content = ''.join(lines)

        # Render the content in an HTML template
        return render_template('index.html', content=content)

    except Exception as e:
        # Handle exceptions and render an error page with exception details
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
