import copy
import random
import pygame
from colors import Colors 
from tetrisai import TetrisAI 

class Genetic:
    def __init__(self, tetris_ai):
        self.tetris_ai = tetris_ai
        self.population_size = 10
        self.mutation_rate = 0.1  # Adjust the mutation rate as needed
        self.population = [self.generate_random_individual() for _ in range(self.population_size)]
        self.current_individual_index = 0

        pygame.init()
        self.screen_width = 600
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Genetic Tetris")
        self.clock = pygame.time.Clock()

    # ... (existing methods remain unchanged)

    def mutate_individual(self, individual):
        mutated_individual = [
            max(0.5, min(2.5, round(gene + random.uniform(-self.mutation_rate, self.mutation_rate), 2)))
            for gene in individual
        ]
        return tuple(mutated_individual)

    def crossover_individuals(self, parent1, parent2):
        crossover_point = random.randint(0, 3)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return tuple(child1), tuple(child2)

    def genetic_algorithm(self):
        # ... (unchanged code)

        while self.current_individual_index < self.population_size:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            parent1, parent2 = self.select_parents()

            child1, child2 = self.crossover_individuals(parent1, parent2)

            child1 = self.mutate_individual(child1)
            child2 = self.mutate_individual(child2)

            self.population[-2] = child1
            self.population[-1] = child2

            self.display_population()

            print(f"Generation {self.current_individual_index + 1} - Best Fitness: {self.evaluate_individual(parent1)}")

            self.current_individual_index += 1
            self.clock.tick(60)

        best_individual = max(self.population, key=self.evaluate_individual)
        print("Best Multipliers:", best_individual)
        pygame.quit()
        return best_individual
