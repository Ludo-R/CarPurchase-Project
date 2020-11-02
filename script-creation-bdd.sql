CREATE DATABASE IF NOT EXISTS carpurchase;

USE carpurchase
;

CREATE TABLE cardata (
Car_Name VARCHAR(99) COMMENT "nom_voitures"
,Year INT(4) COMMENT "annee d'achat"
,Selling_Price FLOAT(50) COMMENT "prix_de_vente actuelle"
,Present_Price FLOAT(50) COMMENT "prix"
,Kms_Driven INT(10) COMMENT "Kilometrages"
,Fuel_type VARCHAR(50) COMMENT "type de carburant"
,Seller_Type VARCHAR(99) COMMENT "type de vendeur"
,Transmission VARCHAR(99) COMMENT "Manuel, auto"
,Owner VARCHAR(9) COMMENT "main ?"
)
;