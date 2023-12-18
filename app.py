import time
from threading import Thread

from flask import Flask
from flask_cors import CORS

from routes.brazil import brazil
from routes.world import world
from data.loadData import load, update

app = Flask(__name__)
CORS(app)

load()

app.register_blueprint(brazil, url_prefix="/v1")
app.register_blueprint(world, url_prefix="/v1")


def wait_and_update():
    while True:
        time.sleep(10)
        update()


if __name__ == '__main__':
    update_thread = Thread(target=wait_and_update)
    update_thread.start()

    app.run(debug=True, port=5000)
