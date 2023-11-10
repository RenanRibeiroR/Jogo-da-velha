import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("sv-account-key.json")
firebase_admin.initialize_app(cred)


db = firestore.client()


# cred = db.collection("teste").document("teste").get()
# print(cred.to_dict())
