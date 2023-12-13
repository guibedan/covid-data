from flask import Flask
from flask_cors import CORS

from routes.brazil import brazil
from routes.world import world


app = Flask(__name__)

CORS(app)

app.register_blueprint(brazil, url_prefix="/v1")
app.register_blueprint(world, url_prefix="/v1")

app.run(debug=True, port=5000)
