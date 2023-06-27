from neo4j.v1 import GraphDatabase


driver = GraphDatabase.driver('bolt://127.0.0.1:7687', auth=('neo4j', 'password'))
