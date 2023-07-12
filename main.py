import turtle,pandas

s= turtle.Screen()
s.title("US state game")
img="blank_states_img.gif"
s.addshape(img)

turtle.shape(img)

states= pandas.read_csv("50_states.csv")
guessed_state=[]
state_n=[]
state_x=[]
state_y=[]
st=states.state.tolist()

while guessed_state!=st:
    # def get_mouse_click_coor(x, y):
    #     print(x, y)
    #
    # turtle.onscreenclick(get_mouse_click_coor)
    #
    # turtle.mainloop()

    ans=s.textinput(title="Guess the State",prompt="Enter the name of another state")



    for sn in states.state:
        if sn.lower()== ans.lower():
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            x= int(states.x[states.state==ans.capitalize()])
            y= int(states.x[states.state==ans.capitalize()])
            t.goto(x,y)
            t.write(sn)
            guessed_state.append(sn)


    guessed_state.sort()
    if ans.lower()=="exit":
        for sn in states.state:
            if sn not in guessed_state:
                state_n.append(sn)
                dict={"Missed State":state_n}
                ms=pandas.DataFrame(dict)
                ms.to_csv("Missed state.csv")
        break






s.exitonclick()