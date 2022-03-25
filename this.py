# import turtle

# tinny = turtle.Turtle()

# print(tinny)
# tinny.shape('turtle')
# tinny.color('blue')
# tinny.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

def spin_words(sentence):
  new_lst = ""
  for n in sentence:
    print(n[::-1])
    if len(n) >= 5:
      new_lst = new_lst + n[::-1]
    else:
      new_lst = new_lst + n
  return new_lst
      
    
  
  
print(spin_words("This is me another"))

