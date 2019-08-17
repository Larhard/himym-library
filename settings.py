HOST = "example.com"
PORT = 22
USER = "user"
BASE_URL = "https://public.example.com/secret/"
SFTP_PATH = "/var/secret"
PLAYER = ["mpv"]

try:
    from local_settings import *
except ModuleNotFoundError:
    pass
