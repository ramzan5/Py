from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('SNAKE')
screen.tracer(0)
snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on = False
        score_board.game_over()


    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        score_board.score_increment()

    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            score_board.game_over()
screen.exitonclick()

