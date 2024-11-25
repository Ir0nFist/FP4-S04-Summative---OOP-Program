import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("OOP Example Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# GameObject class - Base class
class GameObject:
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Player class - Subclass of GameObject
class Player(GameObject):
    def __init__(self, x, y, color, width, height, speed):
        super().__init__(x, y, color, width, height)
        self.speed = speed
    
    # Method to handle player movement based on keypress
    def move_player(self, keys):
        if keys[pygame.K_LEFT]:
            self.move(-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.move(self.speed, 0)
        if keys[pygame.K_UP]:
            self.move(0, -self.speed)
        if keys[pygame.K_DOWN]:
            self.move(0, self.speed)

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    player = Player(400, 300, BLUE, 50, 50, 5)  # Create a player object

    while True:
        screen.fill(WHITE)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player movement handling
        keys = pygame.key.get_pressed()
        player.move_player(keys)

        # Draw the player
        player.draw(screen)
        
        # Update the display
        pygame.display.update()
        
        # Frame rate
        clock.tick(60)

class Enemy(GameObject):
    def __init__(self, x, y, color, width, height, speed):
        super().__init__(x, y, color, width, height)
        self.speed = speed
    
    def move_enemy(self):
        # Make the enemy move downwards
        self.y += self.speed
        if self.y > screen_height:
            self.y = -self.height  # Reset to top once it goes off-screen

# Run the game
game_loop()

# What is the difference between OOP and Procedural coding?
# OOP is a programming paradigm based on the concept of "objects," which can contain data and code. 
# OOP organizes code into classes and objects, making it easier to structure and maintain large applications. It supports concepts like inheritance, polymorphism, and encapsulation.
# Procedural programming, focuses on writing a sequence of instructions that the computer executes step by step. It typically uses functions and is not based on classes or objects.

# How would your program differ if it were made in procedural coding instead?
# If this program were written in a procedural style, the focus would be on functions that directly manipulate the game state rather than defining classes for game objects.
# The player and other objects would likely be represented as dictionaries or variables, and movement and drawing would be handled in separate functions, not as methods of objects.
# The code would likely be less modular, harder to maintain, and less reusable.

# What are the benefits of OOP?
# 1. Encapsulation: OOP allows for better data encapsulation by bundling data and methods that operate on that data into objects.
# 2. Reusability: Once a class is written, it can be reused in other programs or contexts, promoting code reuse.
# 3. Modularity: OOP promotes modularity, where objects can be developed, tested, and maintained independently.
# 4. Inheritance: Classes can inherit from other classes, enabling the creation of new classes based on existing ones, reducing code duplication.

# What are the drawbacks?
# 1. Complexity: OOP can introduce complexity, especially for simple programs or when overused, which can make the code harder to understand.
# 2. Performance: In some cases, OOP can be less efficient than procedural programming due to the overhead of object creation and method calls.
