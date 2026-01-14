# Solde initialise qui va fonctionner sur tout le programme
import os
import json

def sauvegarder_solde():
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(argent, f, indent=4)

fichier = "solde.json"
argent = {"solde": 100000}


# ================= Gestion de l'historique des transferts =================
fichier_tran = "historique_transfert.json"

tran_eff = []
trans_annule = []
historique = []

if os.path.exists(fichier_tran):
    try:
        with open(fichier_tran, "r", encoding="utf-8") as f:
            contenu = f.read().strip()
            if contenu == "":
                historique = [tran_eff, trans_annule]
            else:
                historique = json.loads(contenu)

        if len(historique) == 2:
            tran_eff = historique[0]
            trans_annule = historique[1]
        else:
            historique = [tran_eff, trans_annule]

    except json.JSONDecodeError:
        historique = [tran_eff, trans_annule]

else:
    with open(fichier_tran, "w", encoding="utf-8") as f:
        json.dump([tran_eff, trans_annule], f, indent=4)


def sauvegarder_tran():
    print("\n====================================")
    with open(fichier_tran, "w", encoding="utf-8") as f:
        json.dump([tran_eff, trans_annule], f, indent=4)

    with open(fichier_tran, "r", encoding="utf-8") as f:
        resul = json.load(f)

        print("=== TRANSFERTS EFFECTUES ===")
        k = 1
        for i in resul[0]:
            print(f"{k}. le numero est: {i['numero']} et le montant est: {i['montant']}")
            k += 1

        print("=== TRANSFERTS ANNULES ===")
        w = 1
        for i in resul[1]:
            print(f"{w}. le numero est: {i['numero']} et le montant est: {i['montant']}")
            w += 1
        print("====================================")

def affichage_tran():
    with open(fichier_tran, "r", encoding="utf-8") as f:
        print(json.load(f))

# ==========================================================================

if os.path.exists(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        argent = json.load(f)
else:
    sauvegarder_solde()


#================== Fonction qui va permettre a l'utilisateur de retourner sur le menu ===================
def retour_while_true():
    while True:
        print()
        print("================")
        choix = input("Taper Entrer pour retourner au menu.")
        if choix == "":
            print("====================================")
            print()
            break
        else:
            print("====================================")
            print("Vous ne pouvez que taper sur Entrer pour retourner au menu.")
            print("====================================")
            print()


#================================ Fonction pour consulter le solde ===================================
def consulter_solde():
    print("\n====================================")
    print(f"Votre solde est {argent['solde']} FCFA.")
    print("====================================")
    print()


# =================================== Fonction pour achecter du credit ===============================
def acheter_credit():
    indicateur = "+221"
    mot_pass()

    while True:
        try:
            montant = float(input("Veuillez saisir le montant: "))
        except:
            print("Le montant choix doit etre un numerique.")
            continue

        if montant <= 0 or montant > argent["solde"]:
            print("====================================")
            print(f"Veuillez entrer un montant inferieur a votre solde {argent['solde']}.")
            print("====================================")
            break
        else:
            while True:
                numero = input(f"Veuillez saisir le numero {indicateur}: ")
                numero = numero.replace(" ", "")
                if numero.isdigit() and len(numero) == 9:
                    break
                else:
                    print("Veuillez saisir un numero de 9 chiffres.")

            argent["solde"] -= montant
            sauvegarder_solde()

            print("==============================================")
            print(f"Vous avez acheter un credit de {montant} au {indicateur}{numero} et votre nouveau solde est de {argent['solde']}")
            print("==============================================")
            return retour_while_true()


# =================================== Fonction pour effectuer un transfert =========================
def effectuer_transfert():
    indicateur = "+221"
    mot_pass()

    while True:
        try:
            montant = float(input("Veuillez saisir le montant: "))
        except:
            print("Le montant choix doit etre un numerique.")
            continue

        if montant <= 0 or montant > argent["solde"]:
            print(f"Veuillez entrer un montant inferieur a votre solde {argent['solde']}.")
            print("===================================\n")
            break
        else:
            while True:
                numero = input(f"Veuillez saisir le numero {indicateur}: ")
                numero = numero.replace(" ", "")
                if numero.isdigit() and len(numero) == 9:
                    break
                else:
                    print("Veuillez saisir un numero de 9 chiffres.")

            argent["solde"] -= montant

            tran_eff.append({
                "id": len(tran_eff) + 1,
                "numero": f"{indicateur}{numero}",
                "montant": montant
            })

            sauvegarder_tran()
            sauvegarder_solde()

            print("\n===================================")
            print(f"Vous avez effectuez un transfert de {montant} au {indicateur}{numero} et votre nouveau solde est de {argent['solde']}")
            print("===================================\n")
            retour_while_true()
            break


# ========================== Annuler la transaction 
def annule_tran():
    if len(tran_eff) == 0:
        print("Vous n'avez pas effectuer de transaction")
    else:
        mot_pass()
        dernier = tran_eff.pop()
        argent["solde"] += dernier["montant"]
        trans_annule.append(dernier)

        sauvegarder_solde()
        sauvegarder_tran()

        print("Vous avez annule votre dernier transfert")
        retour_while_true()


# ================= Fonction pour confirmer et annuler la transaction du forfait   
def confirmer_forfait(prix, message):
    if argent["solde"] < prix:
        print("Solde insuffisant.")
        return

    while True:
        print()
        print("1. Confirmer")
        print("2. Annuler")
        print("3. Retour au menu")

        choix = input("Faites un choix: ")

        if choix == "1":
            argent["solde"] -= prix
            sauvegarder_solde()
            print(f"Vous venez d'acheter un {message}")
            retour_while_true()
            break
        elif choix == "2":
            break
        elif choix == "3":
            menu()
            break
        else:
            print("Choix invalide.")


# ======================== Fonction pour le menu des forfaits
def menu_forfait():
    while True:
        print("========== MENU DES FORFAITS ==========")
        print("1. Pass 100 Mo – 500 F")
        print("2. Pass 500 Mo – 1 000 F")
        print("3. Pass 1 Go – 2 000 F")
        print("0. Retour")

        choix = input("Faites un choix: ")

        if choix == "1":
            mot_pass()
            confirmer_forfait(500, "pass de 100 Mo")
        elif choix == "2":
            mot_pass()
            confirmer_forfait(1000, "pass de 500 Mo")
        elif choix == "3":
            mot_pass()
            confirmer_forfait(2000, "pass 1 Go")
        elif choix == "0":
            break
        else:
            print("Faite un choix entre les option present")


#======================== Pour le mot de passe
def mot_pass():
    mot_depass = 1234
    while True:
        try:
            mot_depass_saisi = int(input("Veuillez entre votre mot de passe: "))
        except:
            print("Le mot de passe doit etre numerique.\n")
            continue

        if mot_depass_saisi != mot_depass:
            print("Votre mot de passe est incorrect\n")
        else:
            break


# =================================== Fonction de validation du code #144# ==================================
def menu_code():
    code = '#144#'
    while True:
        code_utilisateur = input("Entrer le code: ")
        if code_utilisateur != code:
            print("Votre code est incorect")
        else:
            break


# =================================== Menu pricipal du programme ==================================
def menu():
    menu_code()
    while True:
        print("========== MENU ORANGE MONEY ==========")
        print("1. consulter le solde")
        print("2. acheter du crédit")
        print("3. effectuer un transfert")
        print("4. acheter forfait")
        print("5. annuler une transation")
        print("6. historique des transferts")
        print("7. quitter le programme")

        choix = input("Veuillez faire un choix: ")
        if choix == "1":
            consulter_solde()
        elif choix == "2":
            acheter_credit()
        elif choix == "3":
            effectuer_transfert()
        elif choix == "4":
            menu_forfait()
        elif choix == "5":
            annule_tran()
        elif choix == "6":
            sauvegarder_tran()
        elif choix == "7":
            print("Merci d'avoir utiliser notre service !")
            break
        else:
            print("Merci de faire un choix entre les differentes options.")


menu()
