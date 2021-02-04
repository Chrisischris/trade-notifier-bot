import os

REDIRECT_URI = 'http://localhost:8080/'

DIRNAME = os.path.abspath(".")
TOKEN_PATH = os.path.join(DIRNAME, 'userData', '')
BOT_USER_PATH = os.path.join(DIRNAME, 'userData', 'savedconfig')
