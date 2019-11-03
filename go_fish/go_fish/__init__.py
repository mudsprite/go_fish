import os
from flask import Flask


app = Flask(__name__)

from go_fish import routes
