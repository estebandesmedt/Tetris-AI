import copy
import random
import pygame
from colors import Colors 
from tetrisai import TetrisAI 

class Genetic:
    def __init__(self, tetris_ai):
        self.tetris_ai = tetris_ai
        self.population_size = 10
        self.population = [self.generate_random_individual() for _ in range(self.population_size)]
        self.current_individual_index = 0

        pygame.init()
        self.screen_width = 600
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Genetic Tetris")
        self.clock = pygame.time.Clock()

    def generate_random_individual(self):
        return (
            random.uniform(0.5, 2.5),
            random.uniform(0.5, 2.5),
            random.uniform(0.5, 2.5),
            random.uniform(0.01, 2.5)
        )

    def evaluate_individual(self, individual):
        self.tetris_ai.height_multiplier, self.tetris_ai.lines_cleared_multiplier, self.tetris_ai.holes_multiplier, self.tetris_ai.bumpiness_multiplier = individual

        while not self.tetris_ai.tetris.game_over:
            self.tetris_ai.make_best_move()
            self.tetris_ai.tetris.update()

        return self.tetris_ai.tetris.score

    def display_population(self):
        self.screen.fill(Colors.dark_blue)
        font = pygame.font.Font(None, 30)

        for i, individual in enumerate(self.population):
            individual_info = f"Individual {i + 1}: {individual}"
            text = font.render(individual_info, True, Colors.white)
            self.screen.blit(text, (10, i * 30 + 10))

        pygame.display.flip()

    def mutate_individual(self, individual):
        mutation_range = 0.1
        return (
            max(0.5, min(2.5, round(individual[0] + random.uniform(-mutation_range, mutation_range), 2))),
            max(0.5, min(2.5, round(individual[1] + random.uniform(-mutation_range, mutation_range), 2))),
            max(0.5, min(2.5, round(individual[2] + random.uniform(-mutation_range, mutation_range), 2))),
            max(0.01, min(2.5, round(individual[3] + random.uniform(-mutation_range, mutation_range), 2)))
        )

    def crossover_individuals(self, parent1, parent2):
        crossover_point = random.randint(0, 3)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    def select_parents(self):
        # Select parents based on fitness
        sorted_population = sorted(self.population, key=self.evaluate_individual, reverse=True)
        return sorted_population[0], sorted_population[1]

    def genetic_algorithm(self):
        while self.current_individual_index < self.population_size:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            parent1, parent2 = self.select_parents()

            # Crossover
            child1, child2 = self.crossover_individuals(parent1, parent2)

            # Mutation
            child1 = self.mutate_individual(child1)
            child2 = self.mutate_individual(child2)

            # Replace the least fit individuals with the new children
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
