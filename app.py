from flask import *;
from vortex_bot import get_vortex_response
app = Flask(__name__)
app.config['USE_STAT_RELOADER'] = False

@app.route('/')
def index():
    return render_template('vortex-bot.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input')
    return get_vortex_response(user_input);
    
if __name__ == '__main__':
    app.run(debug=True)