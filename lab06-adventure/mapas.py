import arcade
import random


class MapManager:
    def __init__(self):
        self.map_data = []

    def load_map(self):
        """Carga un mapa básico."""
        self.map_data = [[0] * 10 for _ in range(10)]  # Mapa vacío de 10x10

    def draw(self):
        """Dibuja el mapa (placeholder)."""
        pass  # Se puede mejorar con tiles de arcade

    def spawn_enemies(self):
        """Genera enemigos en posiciones aleatorias."""
        enemies = []
        for _ in range(3):  # Generar 3 enemigos
            x, y = random.randint(0, 800), random.randint(0, 600)
            enemies.append((x, y))  # Placeholder hasta implementar la clase Enemy
        return enemies

    def spawn_items(self):
        """Genera objetos en el mapa."""
        items = []
        for _ in range(2):  # Generar 2 objetos
            x, y = random.randint(0, 800), random.randint(0, 600)
            items.append((x, y))  # Placeholder hasta implementar la clase Item
        return items
