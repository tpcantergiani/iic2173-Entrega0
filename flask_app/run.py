from bancoin import app
import os

if __name__ == '__main__':
    if os.environ.get('FLASK_ENV') == 'production':
        app.run(host='0.0.0.0')
    else:
        app.run(debug=True,host='0.0.0.0')

