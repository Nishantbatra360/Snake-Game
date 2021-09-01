import random
import time

import pygame

from Apple import Apple
from Direction import Direction
from Snake import Snake


def get_apple_coordinates():
    apple_x = 9 + random.randint(0, 51) * difference
    apple_y = 30 + random.randint(0, 40) * difference
    return {"x": apple_x, "y": apple_y}


def heading(dis, snake):
    my_font = pygame.font.SysFont('Comic Sans MS', 20)
    text_surface = my_font.render('Score: ' + str(snake.get_score()), False, (0, 255, 0))
    dis.blit(text_surface, (width / 2 - 30, 0))
    pygame.draw.line(dis, (0, 255, 0), (0, 28), (width, 28))


def ate_apple():
    global apple_coordinates, new_x, new_y, apple
    apple_coordinates = get_apple_coordinates()
    new_x = coordinates[-1].get("x") + x_change
    new_y = coordinates[-1].get("y") + y_change
    coordinates.append({"x": new_x, "y": new_y})
    snake.increase_length(1)
    snake.increase_score(apple.get_score())
    if random.randint(0, 10) == 5:
        apple = Apple((255, 215, 0), 50)
    else:
        apple = Apple()


def input_validations(message, accepted_input, minimum_value, max_value):
    while True:
        try:
            option = input(message)
            option = int(option)
            if accepted_input and option not in accepted_input:
                print("I don't think you input right value")
            elif option < minimum_value:
                print("Minimum value should be", minimum_value)
            elif option > max_value:
                print("Maximum value should be", max_value)
            else:
                return option
        except ValueError:
            print("I don't think you input right value")
            print()


while True:
    print()
    print("Play Snake Game")
    print("Red apple = 10 points")
    print("Golden apple = 50 points")
    print()
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Exit")
    choice = input_validations("Enter choice:- ", [], 0, 4)
    if choice == 1:
        fps = 10
    elif choice == 2:
        fps = 20
    elif choice == 3:
        fps = 30
    else:
        break
    print("Game is running, select GUI window")

    pygame.init()
    width = 600
    height = 500
    dis = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake game")
    pygame.display.update()
    game_over = False
    snake = Snake()
    temp_x = 20
    temp_y = height / 2
    difference = 11
    coordinates = []
    direction = "none"
    apple = Apple()
    apple_coordinates = get_apple_coordinates()
    for i in range(snake.get_length()):
        coordinates.append({"x": temp_x, "y": temp_y})
        temp_x = temp_x + difference

    x_change = 0
    y_change = 0
    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if direction != Direction.Right:
                        x_change = -difference
                        y_change = 0
                        direction = Direction.Left
                elif event.key == pygame.K_RIGHT:
                    if direction != Direction.Left:
                        x_change = difference
                        y_change = 0
                        direction = Direction.Right
                elif event.key == pygame.K_UP:
                    if direction != Direction.Down:
                        x_change = 0
                        y_change = -difference
                        direction = Direction.Up
                elif event.key == pygame.K_DOWN:
                    if direction != Direction.Up:
                        x_change = 0
                        y_change = difference
                        direction = Direction.Down
        if x_change != 0 or y_change != 0:
            new_x = coordinates[-1].get("x") + x_change
            new_y = coordinates[-1].get("y") + y_change
            coordinates.append({"x": new_x, "y": new_y})  # Adding tail to head
            coordinates.pop(0)

        dis.fill((0, 0, 0))

        heading(dis, snake)

        pygame.draw.rect(dis, apple.get_color(), [apple_coordinates.get("x"), apple_coordinates.get("y"), 10, 10])
        for coordinate in coordinates:
            x = coordinate.get("x")
            y = coordinate.get("y")
            pygame.draw.rect(dis, snake.get_color(), [x, y, 10, 10])
        pygame.display.update()
        if coordinates[-1].get("x") < 0 or coordinates[-1].get("x") > width or coordinates[-1].get("y") < 29 or \
                coordinates[
                    -1].get("y") > height:
            game_over = True
        for i in range(len(coordinates) - 1):
            if coordinates[i] == coordinates[-1]:  # Snake ate itself :)
                game_over = True
        if coordinates[-1] == apple_coordinates:
            ate_apple()
        clock.tick(fps)

    dis.fill((0, 0, 0))
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render("Your Score: " + str(snake.get_score()), False, (0, 255, 0))
    dis.blit(text_surface, ((width / 2) - 80, height / 2 - 50))
    text_surface = my_font.render("Game Over", False, (255, 0, 0))
    dis.blit(text_surface, ((width / 2) - 80, height / 2))
    pygame.display.update()

    time.sleep(2)
    pygame.display.quit()
    # pygame.quit()
