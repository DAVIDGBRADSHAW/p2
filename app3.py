from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  data = {
        'title': 'Welcome to David\'s Website',
        'heading': 'Welcome to my Flask app!',
        'description': 'This is a simple Flask application using an HTML template and a dictionary.',
        'new_items':['item 1', 'item 2'],
        
  }
  return render_template('index.html', data=data)

if __name__ == '__main__':
  app.run(debug=True)