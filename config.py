from os import environ 

class Config:
    API_ID = environ.get("API_ID", "27638569")
    API_HASH = environ.get("API_HASH", "b1d91c7cfe1da5c8f925b794b7409026")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "Auto forwarding") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://abhijeetavinash2022_db_user:Rstdqj8QVMMGJGyE@cluster0.gdwf36r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8239003834').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
