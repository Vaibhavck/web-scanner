from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
import os
from .scan import scan_img

BASE_DIR = os.path.abspath('.')
LOCAL_STORAGE_PATH = os.path.join(BASE_DIR, 'samples', 'original'),
FIREBASE_USER_ID = ''

FILES_TO_DELETE = [
    os.path.join(os.path.abspath('.'), 'samples', 'original', 'original.png'),
    os.path.join(os.path.abspath('.'), 'samples', 'scanned', 'scanned.png'),
]

config = {
    "apiKey": "AIzaSyDw1RWsM-6b7ibyIem9bHHlta9MNpQMOSQ",
    "authDomain": "scanner-4f47e.firebaseapp.com",
    "databaseURL": "https://scanner-4f47e.firebaseio.com",
    "projectId": "scanner-4f47e",
    "storageBucket": "scanner-4f47e.appspot.com",
    "messagingSenderId": "10227005215",
    "appId": "1:10227005215:web:f4812c6ccae4b59a50e22a",
    "measurementId": "G-2DDDH9BPZV"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()

# Create your views here.
def scanner(request):
    fbw.download()
    return HttpResponse('<h1>Scanner</h1>')

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def test(request):
    # test = request.GET.get('test')
    # print(test)
    return HttpResponse(os.path.join(os.path.abspath('.'), 'samples', 'scanned', 'scanned.png'))

def upload(FIREBASE_PATH):
    temp = FIREBASE_PATH.split('/')[-1]
    FIREBASE_PATH = FIREBASE_PATH.replace(temp, 'scanned.png')
    # firebase_path = os.path.join(FIREBASE_USER_ID, 'deadpool.png')
    local_path = 'scanned.png'
    storage.child(FIREBASE_PATH).put(local_path)
    return FIREBASE_PATH

def download(request):
    FIREBASE_PATH = request.GET.get('firebasepath')
    img_name = FIREBASE_PATH.split('/')[-1]
    filename = os.path.join(BASE_DIR, 'samples', 'original', 'original.png')
    storage.child(FIREBASE_PATH).download('.', filename)
    ### scanning images
    scanned_img = scan_img(filename)
    ### uploading images
    path = upload(FIREBASE_PATH)
    # print(os.getcwd())
    for file_path in FILES_TO_DELETE:
        os.remove(file_path)

    print('images deleted')
    return HttpResponse(f'<h5>Scanned image saved at : {path}</h5>')

def login(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    user = auth.sign_in_with_email_and_password(email, password)
    # print(user)
    uid = user['localId']
    FIREBASE_USER_ID = uid
    print(uid)
    return HttpResponse('<h1>Logged In Successfully</h1>')

def logout(request):
    pass