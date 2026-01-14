# Simulation d’un service USSD Orange Money en Python

## Présentation générale

Ce projet consiste à concevoir une application en ligne de commande simulant un service USSD Orange Money.  
L’application permet à un utilisateur d’effectuer des opérations financières simples telles que la consultation du solde, l’achat de crédit et de forfaits, le transfert d’argent, l’annulation du dernier transfert et la consultation de l’historique des transactions.

Le programme repose sur l’utilisation de fichiers JSON afin d’assurer la persistance des données (solde et historique des transferts) entre plusieurs exécutions.

Ce projet est réalisé dans le cadre de la formation Développeur Web et Web Mobile (2023), avec pour objectif de renforcer la maîtrise de la logique métier, de l’algorithmique et de la gestion des données persistantes en Python.

---

## Objectifs du projet

- Simuler le fonctionnement d’un menu USSD Orange Money
- Implémenter des règles de gestion simples et réalistes
- Manipuler des fichiers JSON pour la persistance des données
- Structurer un programme Python de manière claire et maintenable
- Utiliser Git pour le versionnement du projet

---

## Technologies et outils utilisés

- Langage : Python 3
- Format de stockage : JSON
- Outils :
  - Terminal
  - Jupyter lab
  - Git / GitHub

---

## Organisation des fichiers

- USSD Orange.py : fichier principal contenant l’ensemble du code source
- solde.json : fichier de sauvegarde du solde utilisateur
- historique_transfert.json : fichier de sauvegarde de l’historique des transferts
- README.md : documentation du projet

---

## Description fonctionnelle du programme

### Initialisation et persistance des données

Le programme initialise un solde par défaut de 100 000 FCFA.  
Si le fichier `solde.json` existe, le solde est chargé depuis ce fichier.  
Dans le cas contraire, le fichier est créé automatiquement.

De la même manière, l’historique des transferts est chargé depuis `historique_transfert.json`.  
Si ce fichier n’existe pas ou est vide, une liste vide est initialisée afin de garantir la continuité du programme.

---

## Description détaillée des fonctions

### sauvegarder_solde()

Cette fonction permet d’enregistrer le solde actuel dans le fichier `solde.json`.  
Elle est appelée après chaque opération modifiant le solde afin d’assurer la persistance des données.

---

### sauvegarder_tran()

Cette fonction sauvegarde l’historique des transferts dans le fichier `historique_transfert.json`.  
Elle garantit que chaque transfert effectué est conservé même après la fermeture du programme.  
Elle permet également d’afficher le contenu actuel de l’historique.

---

### retour_while_true()

Cette fonction permet à l’utilisateur de revenir au menu principal après l’exécution d’une opération.  
Elle force l’utilisateur à appuyer sur la touche Entrée afin d’améliorer la lisibilité et le contrôle du flux du programme.

---

### consulter_solde()

Cette fonction affiche le solde actuel de l’utilisateur à l’écran.  
Aucune modification des données n’est effectuée.

---

### acheter_credit()

Cette fonction permet à l’utilisateur d’acheter du crédit téléphonique.

Elle :
- Demande la saisie du mot de passe
- Vérifie que le montant est valide et inférieur au solde disponible
- Vérifie la validité du numéro de téléphone
- Débite le solde du montant saisi
- Sauvegarde le nouveau solde dans le fichier JSON

---

### effectuer_transfert()

Cette fonction permet d’effectuer un transfert d’argent vers un numéro donné.

Elle :
- Vérifie le mot de passe
- Valide le montant du transfert
- Vérifie la validité du numéro de téléphone
- Débite le solde
- Enregistre la transaction dans l’historique avec un identifiant unique
- Sauvegarde le solde et l’historique

Chaque transfert est enregistré sous forme de dictionnaire contenant l’identifiant, le numéro et le montant.

---

### annule_tran()

Cette fonction permet d’annuler le dernier transfert effectué.

Elle :
- Vérifie l’existence d’au moins un transfert
- Demande la confirmation via le mot de passe
- Recrédite le montant du dernier transfert au solde
- Sauvegarde le solde mis à jour

L’annulation concerne uniquement la dernière transaction enregistrée.

---

### confirmer_forfait(prix, message)

Cette fonction gère la confirmation ou l’annulation de l’achat d’un forfait.

Elle :
- Vérifie que le solde est suffisant
- Propose à l’utilisateur de confirmer ou d’annuler l’achat
- Débite le solde si l’achat est confirmé
- Sauvegarde le nouveau solde

---

### menu_forfait()

Cette fonction affiche le menu des forfaits disponibles.

Elle permet à l’utilisateur de :
- Choisir un forfait parmi plusieurs options
- Valider son choix via le mot de passe
- Appeler la fonction de confirmation du forfait

---

### mot_pass()

Cette fonction assure la sécurité des transactions.

Elle :
- Demande la saisie d’un mot de passe numérique
- Vérifie la conformité du mot de passe
- Bloque l’exécution tant que le mot de passe est incorrect

---

### menu_code()

Cette fonction simule l’accès USSD au service.

Elle :
- Demande à l’utilisateur de saisir le code `#144#`
- Refuse l’accès tant que le code n’est pas correct

---

### menu()

Cette fonction représente le cœur du programme.

Elle :
- Appelle la fonction de validation du code USSD
- Affiche le menu principal
- Oriente l’utilisateur vers les différentes fonctionnalités
- Gère la sortie du programme

---

## Règles de gestion respectées

- Le solde ne peut jamais devenir négatif
- Les montants doivent être numériques et valides
- Les numéros de téléphone doivent contenir exactement 9 chiffres
- L’annulation ne concerne que le dernier transfert
- Les fichiers JSON sont créés automatiquement si absents

---

## Modalités pédagogiques

- Travail individuel
- Durée estimée : 6 heures
- Environnement : ligne de commande
- Versionnement du projet avec Git

---

## Conclusion

Ce projet illustre une implémentation simplifiée mais fonctionnelle d’un service USSD Orange Money.  
Il met en pratique les fondamentaux de la programmation Python, la gestion des fichiers, la persistance des données et la logique métier, tout en respectant un cahier des charges précis.

---

Auteur : ALPHONSE DESIRE HABA 
Formation : Développeur Web / Web Mobile + (IA)
