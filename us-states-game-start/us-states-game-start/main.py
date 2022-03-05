import turtle
import pandas
screen = turtle.Screen()
screen.title('US-GAME')
img = 'blank_states_img.gif'

screen.addshape(img)
turtle.shape(img)


data = pandas.read_csv('50_states.csv')

state_list = data.state.to_list()
guessed_list = []

while len(guessed_list)<50:
    answer = screen.textinput(title='US-Quiz',prompt="What's an other state name").title()
    if answer == "Exit":
        missing_state = [stat for stat in state_list if stat not in guessed_list]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("missing_state.csv")
        break
    if answer in state_list:
        guessed_list.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        pos = (int(data[data.state == answer].x),int(data[data.state == answer].y))
        t.goto(pos)
        t.write(answer)


# screen.exitonclick()

