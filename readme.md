# Image Entropy Generator - Exercice de Formation

Ce projet est un exercice de formation qui implémente un générateur d'entropie basé sur l'analyse d'images en Python, démontrant l'utilisation de la vision par ordinateur et de la cryptographie.

## Description

Cet outil génère une valeur d'entropie unique dérivée d'une image en combinant :
- **Détection de visages** : Utilisation d'OpenCV avec classificateur Haar Cascade
- **Analyse statistique** : Calcul d'entropie basé sur la distribution des pixels
- **Horodatage** : Intégration du timestamp de création du fichier
- **Hachage cryptographique** : Utilisation de SHA-256 pour renforcer l'unicité

## Objectifs Pédagogiques

Ce projet illustre :
- Les techniques de vision par ordinateur (détection de visages)
- Le calcul d'entropie et l'analyse statistique d'images
- L'utilisation de fonctions de hachage cryptographiques
- La manipulation de métadonnées de fichiers
- L'intégration de multiples sources d'entropie

## Prérequis

- Python 3.6+
- OpenCV pour la vision par ordinateur
- NumPy pour les calculs statistiques
- hashlib (module standard Python)

## Structure du Projet

```
image-entropy-generator/
├── main.py              # Script principal
├── cascade.xml          # Classificateur Haar Cascade
├── requirements.txt     # Dépendances Python
├── sample1.jpg         # Image d'exemple
├── README.md           # Documentation
└── LICENSE             # Licence MIT
```

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ArtanisInc/image-entropy-generator-formation
cd image-entropy-generator
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

## Utilisation

### Génération d'entropie basique

```bash
python main.py --length 50
```

### Exemples d'utilisation

```bash
# Entropie de 32 caractères
python main.py --length 32

# Entropie maximale (100 caractères)
python main.py --length 100

# Test avec votre propre image
# (remplacez sample1.jpg par votre image)
python main.py --length 64
```

## Fonctionnalités Implémentées

### ✅ Détection de Visages
- Utilisation du classificateur Haar Cascade pré-entraîné
- Comptage automatique des visages détectés

### ✅ Calcul d'Entropie Statistique
- Analyse de la distribution des pixels
- Calcul de variance et d'entropie de Shannon

### ✅ Intégration Temporelle
- Extraction du timestamp de création du fichier
- Précision jusqu'à la milliseconde

### ✅ Hachage Cryptographique
- Génération de checksum SHA-256
- Combinaison de multiples sources d'entropie

### ✅ Personnalisation
- Longueur configurable (jusqu'à 100 caractères)
- Support de différents formats d'images

## Sortie Attendue

```
Number of faces detected: 2
Creation date and time: 01/03/2025 15:45:32.789
SHA256 Checksum: 3a7d3e8b9f6c...
Final product (length 50): 239817462392847612039472...
```

## Concepts Techniques Démontrés

1. **Vision par Ordinateur** : Détection d'objets avec OpenCV
2. **Entropie Informationnelle** : Mesure du désordre dans les données
3. **Cryptographie** : Fonctions de hachage sécurisées
4. **Métadonnées** : Extraction d'informations système
5. **Combinaison d'Entropie** : Fusion de sources multiples

## Personnalisation

Vous pouvez modifier :
- **MAX_LENGTH** : Changer la longueur maximale autorisée
- **Image source** : Utiliser vos propres images
- **Classificateur** : Remplacer `cascade.xml` par d'autres modèles
- **Algorithme de hachage** : Expérimenter avec d'autres fonctions

## Extensions Possibles

- Support de multiples images simultanément
- Détection d'autres objets (yeux, sourires, etc.)
- Interface graphique pour sélection d'images
- Export des résultats en différents formats
- Analyse comparative d'entropie entre images

## Commandes Utiles

```bash
# Test avec l'image par défaut
python main.py --length 32

# Vérification des dépendances
pip list

# Test de performance
time python main.py --length 100
```

## Notes de Formation

Ce projet combine plusieurs domaines de l'informatique :
- **Traitement d'images** : OpenCV, analyse de pixels
- **Machine Learning** : Classificateurs pré-entraînés
- **Cryptographie appliquée** : Génération d'entropie sécurisée
- **Programmation système** : Manipulation de fichiers et métadonnées
- **Statistiques** : Calculs d'entropie et de variance

