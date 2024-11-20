from neo4j import GraphDatabase

# Configuration de connexion
URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "neo4jneo4j"

# Création de la connexion
connection = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# Requête pour récupérer les films dirigés par Nancy Meyers
query1 = """
MATCH (d:Person {name: 'Nancy Meyers'})-[:DIRECTED]->(m:Movie)
RETURN m.title
"""

# Exécution de la requête sur la base de données et affichage des résultats
with connection.session(database="neo4j") as session:
    result = session.run(query1)
    for record in result:
        print(record["m.title"])  # Affiche les titres des films dirigés

# Test de la connexion en comptant les nœuds
with connection.session() as session:
    result = session.run("MATCH (n) RETURN count(n)")
    print("Nombre total de nœuds dans la base :", result.single()["count(n)"])
