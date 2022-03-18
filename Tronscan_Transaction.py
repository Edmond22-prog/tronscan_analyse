import requests

# Compte dans lequel on doit travailler
account = "TE7PfgeMuivv9UXkKTrGXinjfmfqE9mZyd"
# API renvoyant les 40 dernieres transaction du compte
url = "https://apilist.tronscan.org/api/transaction?sort=-timestamp&count=true&limit=40&start=0&address=TE7PfgeMuivv9UXkKTrGXinjfmfqE9mZyd"

# Reponse a la requete envoye au serveur
response = requests.get(url)

# Transformation du contenu l'information recu depuis le serveur en format json
content = response.json()

# Recuperation des donnees du contenu
datas = content['data']

usdt_transactions = []

# Remarque: toutes les transactions USDT, dans la cle 'contractData' (dont la valeur est un dictionnaire) ont
# une cle interne 'data'
# On va recuperer ces transactions la
for data in datas:
    # Recuperation de la valeur (dictionnaire) contenu dans la cle 'contractData'
    item = data['contractData']
    try:
        # On teste s'il y a une cle interne 'data'
        test = item['data']
    except:
        # En cas d'absence, on continue a la donnee suivante
        continue
    else:
        # En cas de presence, on la stocke dans la liste
        usdt_transactions.append(data)

total_amount_transaction = 0

# On calcule ici le montant total des transactions USDT
for data in usdt_transactions:
    total_amount_transaction += float(data['amount'])
print(f"Total amount of USDT transaction : {total_amount_transaction}\n")

# Liste des transactions justifiants ce montant total
for data in usdt_transactions:
    print(f"{data['ownerAddress']} ==> {data['toAddress']}, amount : {data['amount']}")
print("\n")