import time
#import redis
from flask import Flask, render_template, url_for

app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)
#
#def get_hit_count():
#    retries = 5
#    while True:
#        try:
#            return cache.incr('hits')
#        except redis.exceptions.ConnectionError as exc:
#            if retries == 0:
#                raise exc
#            retries -= 1
#            time.sleep(0.5)

@app.route('/')

def index():
    print(hello())
    return render_template('index.html')

def hello():
    count = 1 #get_hit_count()
    return f'Hello World! I have been seen {count} times.\n'

if __name__ == "__main__":
    app.run(debug=True)    