###############################################################################
# DONE: 1. (4 pts)
#
#   As you saw in your pre-class quiz, we can also define functions that take
#   information and do stuff with it. This information that the function uses
#   comes through as parameters/arguments. You may see those two terms used
#   interchangeably. There is a nuanced difference between them (that you
#   ecountered on your quiz), but for our purposes they reference the same
#   thing (information being passed into a function as its input).
#
#   Using the same process as described in the pre-class materials, define a
#   function called name_and_color() that takes two parameters:
#     - name
#     - color
#   and prints out a phrase that uses those two strings. For example,
#       "Your name is John and your favorite color is green!"
#
#   Make sure to use the parameters as a part of your solution as well as the
#   f-strings we talked about in Session 3.
#
#   Be sure to call your function, so you can see that it works.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

identity = input("What is your name? ")
fancy = input("And what is your favorite color? ")
def name_and_color(name, color):
    print("Hello, " + name + "! I think " + color + " is a great color!")
name_and_color(identity, fancy)

###############################################################################
# DONE: 2. (4 pts)
#
#   Now, let's do something similar, but let's use keyword arguments (this is
#   also something that you saw in the pre-class materials).
#
#   Define a function called display_user_info() that takes three parameters:
#     - name
#     - email
#     - age
#   and outputs the information like so:
#  
#   Name: John Smith
#   Email: jsmith@gmail.com
#   Age: 19
#
#   (Obviously, make sure your function uses the values given by your
#   parameters.)
#
#   Then, call your function using keyword arguments. As a refesher, you use a
#   keyword argument by setting the name of the argument equal to the value you
#   want to give it, so:
#
#       name="John Smith"
#
#   Notice that when you use keyword arguements, the order of the arguments
#   when you call the function doesn't matter. However, in the first _TODO_
#   above, the order mattered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
user_name = input("What is your name? ")
user_email = input("What is your email address? ")
user_age = input("What is your age? ")
def display_user_info(name, email, age):
    print("Name: " + name + "\nEmail: " + email + "\nAge: " + age)
display_user_info(name=user_name, email=user_email, age=user_age)