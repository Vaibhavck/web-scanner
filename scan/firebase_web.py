import pyrebase


config = {
    "apiKey": "AIzaSyC2acP5riaygZhGvlSiF6HalXHDTD-3Now",
    "authDomain": "vanced-38fba.firebaseapp.com",
    "databaseURL": "https://vanced-38fba.firebaseio.com",
    "projectId": "vanced-38fba",
    "storageBucket": "vanced-38fba.appspot.com",
    "messagingSenderId": "931988615176",
    "appId": "1:931988615176:web:f0d3fc6847bc1041ce21bd",
    "measurementId": "G-31RZ1CTNB4"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()