#!/usr/bin/env python3
"""
Flask API blueprint
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from server.api.v1.views.listings import *
