###############################################################################
# DONE: 1. (3 pts)
#
#   Sometimes, we want to create a function that does some things but then
#   gives us some information back when it is done. We call that "returning"
#   the information. In other words the function, returns the information back
#   to where it was called from.
#   
#   To get us started lets create a function that we would want to get
#   information from. How about a function that would calculate the volume of
#   an object. As a reminder, you calculate the volume of an object by
#   multiplying the length times the width times the height of the object.
#   
#   So, write a function below this _TODO_ called volume() that takes three
#   parameters (length, width, and height) and returns the result of that
#   calculation. Feel free to look back at the pre-class materials to remember
#   how to return information.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def volume(length, width, height):
    return length * width * height
calculation = volume(3, 4, 2)
print(calculation)

###############################################################################
# DONE: 2. (2 pts)
#
#   Now let's call that function and get its information.
#
#   Start by simply calling the function (you can use any numbers you wish as
#   your arguments).
#   
#   If you run your code at this point, you will notice that it doesn't seem
#   like it is doing anything. That is because we haven't done anything with
#   the information.
#
#   Just like we used variable names to give a name to a value, we can do the
#   same thing with the value that comes back from a function. The pattern is
#   the same, so it would look something like this:
#
#   variable_name = function_to_call()
#
#   Try that now with the function above with a variable name of your choosing.
#
#   But we still can't see the information. As always, we need to print it to
#   see it. Now print the value of the function using the variable that you
#   just made.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################