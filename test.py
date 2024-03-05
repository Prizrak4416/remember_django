from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
print(SECRET_KEY)


def new(**kwargs):
    print(kwargs)


print(new(**{'a': 1, 'b': 2}))
