# Cours Predictive Analytics

## Table des matières

0. [Documents de cours](/000-%5BTP%20Machine%20Learning%20COURS%5D)
1. [Initiation Python](/001-%5BTP%20Machine%20Learning%20Initiation_Python%5D)
2. [Data Preprocessing](/002-%5BTP%20Machine%20Learning%20Data_Preprocessing%5D)
    1. [Linear Regression](/002a-%5BTP%20Machine%20Learning%20Regression_lineaire%5D)
3. [Classification](/003-%5BTP%20Machine%20Learning%20Classification%5D)

# Notes

# Machine Learning - C1 -- 8 Feb 2019 at 08:30 - 12:00

# General Concepts

- De plus en plus de données => Besoin de traitement => Data Science
- Data Scientist = stats + proga
	- Statisticien
	- Informaticien
	- Connaissance métier
- Data Science = Comment générer de la **valeur** pour les entreprises


# Projet Data Science

1. Compréhension métier et des datas
	- Talk to teammates !
2. Phase de préparation des datas et tests de qqs hypothèses
	- « lisser » les données
3. Phase d’évaluation et de modélisation


## L’équipe

- Data engineer (expert récupération)
- Data scientist
- Data/Product owner (responsable métier)
- Data architect
- Data visualisation expert (KPIs)


# Analyse prédictive

- Pendant de la Data Science
- Permet de voir une **tendance** basée sur un **historique **de données
- Très important pour pouvoir les budgets, investissements, startégies…


# Machine Learning

- **Définition:** Faire apprendre la machine avec des exemples
- Champs d’étude qui donne aux PC la capacité d’apprendre sans avoir été programmés explicitement
- Apprend a un PC a prendre des décision sur des échantillons
- **Concepts**:
	- l’_Experience_ (les donnés)
		- ex : Liste de mails
	- les _Tâches_
		- ex: Classer les mails
	- la _Performance_
		- ex: le nombre d’e-mails correctement classés
- **Variables**
	- Numériques
	- Catégoriques (Charactère)
		- Ordinace (ordonée)
		- Nominale (non-ordonée)


## 4 étapes

1. Récupérer
2. Nettoyer
3. Construire
4. Expérimenter


# Familles d’algorithmes ML


## Supervisé

	- **Classification** or **regression** problems
		- **Regression** prediction variable numerique
		- **Classification** prediction oui/non
	- besoin d’une **variable de contrôle** [_label_]
	- **Feature** // propriétés (surface, nb de chambres, geoloc)
	- **Label** // valeur (prix)
	- **XTrain** // Features du Training set
	- **YTrain** // Label du Training set
	- **XTest** // Feature de l’Input data
	- **YPred** // Label de l’Input data (résultat)


## Non supervisé

	- **Clustering** or **anomaly detection** problems
	- Prend en input que des datasets contenant uniquement des Features (pas de Label)
	- Pas de notion de classe
	- Détecte les similarité pour créer des groupes
	- ML apprend afin de génèrer des **MODELS** qui sont utilisés pour traités de nouvelles données
	- **Features vectors** //


#### [OPTION] Systèmes de recommandation


# Cas d’usage de ML

1. _Connaissance Client_
	- Segmentation client
	- Segmentation usages web
	- Segmentation de scores
	- Satisfaction client
2. _Connaissance marché_
	- Analyse tendance
	- Analyse RS
	- Analyse sentiments
	- Analyse communauté
3. _Optimisation marketing_
	- Attribution
	- Allocation
4. _Personnalisation_
	- Recommandations
		- 2 types recommandations produits [SUR TEST]
	- (Re)Targeting
	- Campagnes promotionnelles
5. _Detection_
	- Fraude (flagging)
	- Anomalies
	- Pannes
	- Personnes/Objets


# Les outils


## Top tools

- Python (scikit learn)
- R
- Octave
- Matlab


## ML tools

- data iku
- knime


## Cloud tools

- Amazon ML
- Azure ML
- Big ML
- Google ML


## Systeme distribue

- Spark


