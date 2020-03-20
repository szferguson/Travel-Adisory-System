import pymongo 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import os

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Travel-Advisory-User-Data-Base"]
mycollection = mydb["Stored-User"]


def hashGenerator(password):
    digest = hashes.Hash(hashes.SHA3_256(), backend=default_backend())
    digest.update(bytes(bytearray(password, 'utf-8')))
    hashVal = digest.finalize()
    return hashVal


userProfiles = [
    {"China" : hashGenerator("GreatChink")},
    {"Canada" : hashGenerator("HockeyLeaf")},
    {"United States": hashGenerator("FreedomForOil")},
    {"Vietnam" : hashGenerator("WannabeChink")},
    {"Iran" : hashGenerator("StillSanctioned")},
    {"Russia" : hashGenerator("VodkaLadaAdidas")},
    {"Italy" : hashGenerator("PizzaMafiaLasagna")},
    {"Mexico" : hashGenerator("TacoCartelCocaine")}
]

# you should comment this line out after you run the program ONCE
# x = mycollection.insert_many(userProfiles)