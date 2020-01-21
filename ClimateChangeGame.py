GlowScript 2.7 VPython
#
# game_starter.py
#
# Building an interaction with 3D graphics using python
#   Documentation: http://www.glowscript.org/docs/GlowScriptDocs/index.html
#   Examples:      http://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
#

scene.title = "                                       Play Climate Change: A Reality"
scene.caption = "Control the human - starting in the middle of the screen.<br>Change the color of the human by pressing any letter or arrow key on your keyboard.<br>Use the up, down, left and right arrow keys to navigate through trees, snowballs and lava rocks.<br>Win the game by capturing - colliding - with every alien."
scene.bind('keydown', keydown_fun)     # Function for key presses
#scene.bind('click', click_fun)         # Function for mouse clicks
scene.background = 0.8*vector(1, 1, 1) # Light gray (0.8 out of 1.0)
scene.width = 640                      # Make the 3D canvas larger
scene.height = 480


# +++ start of OBJECT_CREATION section
# These functions create "container" objects, called "compounds"

def make_alien(starting_position, starting_vel = vector(0, 0, 0)):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to make_alien allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vector(0, 0, 0).

       Compounds can have any number of components.  Here are the
       alien's components:
    """
    alien_body = sphere(size = 1.0*vector(1, 1, 1), pos = vector(0, 0, 0), color = vector(0,0,0))
    alien_eye1 = sphere(size = 0.3*vector(1, 1, 1), pos = .42*vector(.7, .5, .2), color = color.white)
    alien_eye2 = sphere(size = 0.3*vector(1, 1, 1), pos = .42*vector(.2, .5, .7), color = color.white)
    alien_eye3 = sphere(size = 0.3*vector(1, 1, 1), pos = .42*vector(.5, .5, .5), color = color.white)
    alien_hat = cylinder(pos = 0.42*vector(0, .9, -.2), axis = vector(.02, .2, -.02), size = vector(0.2, 0.7, 0.7), color = color.magenta)
    alien_objects = [alien_body, alien_eye1, alien_eye2, alien_eye3, alien_hat]  # make a list to "fuse" with a compound
    # now, we create a compound -- we'll name it com_alien:
    com_alien = compound(alien_objects, pos = starting_position)
    com_alien.vel = starting_vel   # set the initial velocity
    return com_alien



# The ground is represented by a box (vpython's rectangular solid)
# http://www.glowscript.org/docs/GlowScriptDocs/box.html
ground = box(size = vector(20, 1, 20), pos = vector(0, -1, 0), color = vector(0.62,0.32,0))

# Create two walls, also boxes
wallA = box(pos = vector(0, 0, -10), axis = vector(1, 0, 0), size = vector(20, 1, .2), color = color.blue) # amber
wallB = box(pos = vector(-10, 0, 0), axis = vector(0, 0, 1), size = vector(20, 1, .2), color = color.blue)   # blue
wallC = box(pos = vector(10, 0, 0), axis = vector(0, 0, 1), size = vector(20, 1, .2), color = color.blue)   # blue
wallD = box(pos = vector(0, 0, 10), axis = vector(1, 0, 0), size = vector(20, 1, .2), color = color.blue)

# A ball - now person that we will be able to control
body = cone( pos=vec(1,3,1), axis=vec(0,1,0), size=vec(5,3,3) ) #1,-.6,.2
head = sphere(size=vec(1,1,1), pos=vec(1,8,1), color=vec(0,.5,0))
#head = sphere(size = 1.0*vector(1, 1, 1), color = vector(0.8, 0.5, 0.0)) 
person_objects = [body, head]
com_body = compound(person_objects, pos = vec(1,-.6,.2))
ball = com_body   # ball is an object of class sphere
ball.vel = vector(0, 0, 0)     # this is its initial velocity



# Alien snowballs
# We make two aliens using two calls to the make_alien function (from above)
alien = make_alien(starting_position = vector(2, 0, -2), starting_vel = vector(0, 0, -1))
alien2 = make_alien(starting_position = vector(7, 0, -7), starting_vel = vector(0, 0, -1))  # zero starting velocity
alien3 = make_alien(starting_position = vector(-6, 0, 6), starting_vel = vector(0, 0, -1))

def make_tree(starting_position, starting_vel = vector(0, 0, 0)):
    """The lines below make a new "frame", which is a container with a
       local coordinate system.
       The arguments to make_alien allow for any initial starting position
       and initial starting velocity, with a default starting velocity
       of vector(0, 0, 0).

       Compounds can have any number of components.  Here are the
       alien's components:
    """
    tree_trunk = cylinder(size=vec(5.5,.4,.2), axis = vector(0,5,0), pos = vec(3.5,-.5,0), color=vec(0.72,0.42,0), vel=vector(0, 1, 0) )
    tree_bush = sphere(size=vec(1.6,1.6,1.6), pos = vec(3.5,5.5,0), color=vec(0,1,0), vel=vector(0, 1, 0) )
    #tree_trunk = cylinder(size=vec(1,.2,.2), axis = vector(0,1,0), pos = vec(3.5,-.5,0), color=vec(0.72,0.42,0), vel=vector(0, 1, 0) )
    #tree_bush = sphere(size=vec(.6,.6,.6), pos=vec(3.5,0.6,0), color=vec(0,1,0), vel=vector(0, 1, 0) )
    tree_objects = [tree_trunk, tree_bush]  # make a list to "fuse" with a compound
    # now, we create a compound -- we'll name it com_alien:
    com_tree = compound(tree_objects, pos = starting_position)
    com_tree.vel = starting_vel   # set the initial velocity
    return com_tree

# Tree
#tree1 = make_tree(starting_position = vector(3, 0, 7), starting_vel = vector(0,0,-1))
#tree2 = make_tree(starting_position = vector(-1, 0, -3), starting_vel = vector(0,0,-1))
#trunk = cylinder(size=vec(1,.2,.2), axis = vector(0,1,0), pos = vec(3.5,-.5,0), color=vec(0.72,0.42,0) )
#bush = sphere(size=vec(.6,.6,.6), pos=vec(3.5,0.6,0), color=vec(0,1,0))




# Lava Boxes
mybox = box(pos=vec(-4,0,-4), size=vec(1.5,1.5,1.5), color=vec(1,0,0) )
mybox1 = box(pos=vec(-8,0,4), size=vec(1.5,1.5,1.5), color=vec(1,0,0) )
mybox2 = box(pos=vec(-1,0,6), size=vec(1.5,1.5,1.5), color=vec(1,0,0) )
mybox3 = box(pos=vec(5,0,-2), size=vec(1.5,1.5,1.5), color=vec(1,0,0) )
mybox4 = box(pos=vec(7,0,7), size=vec(1.5,1.5,1.5), color=vec(1,0,0) )

# +++ end of OBJECT_CREATION section


# +++ start of ANIMATION section

# a ball that we WILL be able to control
b = ball   # ball is an object of class sphere
b.pos = vec(0,0,0)
b.vel = vec(0,0,0)     # this is its initial velocity

# create a list of (moving) objects: LoO
LoO = [ b ]

# several that we will NOT be able to control
for i in range(1,5):
    """
    Creates a line of balls.
    """
    s = sphere(size=1.0*vector(1,1,1), color = color.white)   # ball is an object of class sphere
    s.pos = vec(0+2*i,0,0+2*i)   
    s.vel = vec(0,0,0)            # initial velocity - not moving
    s.vel.y = 0.0                 # make sure that the y-component is 0!
    LoO = LoO + [ s ]             # add the most recent sphere into the list, LoO

for i in range(1,5):
    """
    Creates a line of balls.
    """
    s = sphere(size=1.0*vector(1,1,1), color = color.white)   # ball is an object of class sphere
    s.pos = vec(0-2*i,0,0-2*i)   
    s.vel = vec(0,0,0)            # initial velocity - not moving
    s.vel.y = 0.0                 # make sure that the y-component is 0!
    LoO = LoO + [ s ]             # add the most recent sphere into the list, LoO
    
#for i in range(1,5):
    """
    Creates a line of balls.
    """
    #s = sphere(size=1.0*vector(1,1,1), color = color.white)   # ball is an object of class sphere
    #s.pos = vec(0-2*i,0,0-2*i)   
    #s.vel = vec(0,0,0)            # initial velocity - not moving
    #s.vel.y = 0.0                 # make sure that the y-component is 0!
    #LoO = LoO + [ s ]             # add the most recent sphere into the list, LoO

#for i in range(1,5):
    """
    Creates a line of balls.
    """
   # s = sphere(size=1.0*vector(1,1,1), color = color.white)   # ball is an object of class sphere
    #s.pos = vec(0+2*i,0,0+2*i)   
    #s.vel = vec(0,0,0)            # initial velocity - not moving
    #s.vel.y = 0.0                 # make sure that the y-component is 0!
    #LoO = LoO + [ s ]             # add the most recent sphere into the list, LoO

for i in range(1,5):
    """
    Creates a line of trees.
    """
    s = make_tree(starting_position = vector(3, 0, 7), starting_vel = vector(0,0,-1))   # ball is an object of class sphere
    s.pos = vec(0+2*i,0,0-2*i)   
    s.vel = vec(0,0,0)            # initial velocity - not moving
    s.vel.y = 0.0                 # make sure that the y-component is 0!
    LoO = LoO + [ s ]             # add the most recent sphere into the list, LoO
    
for i in range(1,5):
    """
    Creates a line of trees.
    """
    s = make_tree(starting_position = vector(3, 0, 7), starting_vel = vector(0,0,-1))   # ball is an object of class sphere
    s.pos = vec(0-2*i,0,0+2*i)   
    s.vel = vec(0,0,0)            # initial velocity - not moving
    s.vel.y = 0.0                 # make sure that the y-component is 0!
    LoO = LoO + [ s ]             # add the most recent sphere into the list, LoO


# Other constants
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/(1.0*RATE)      # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vector(0, -3, -2)  # Ask for a bird's-eye view of the scene...

# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt
#

alien_hit_count = 0

while True:

    rate(RATE)   # maximum number of times per second the while loop runs
        
        
    for b in LoO:
        b.pos = b.pos + b.vel*dt   # update each object's position


    # +++ end of PHYSICS UPDATES - be sure new objects are updated appropriately!


    # +++ start of COLLISIONS - check for collisions + do the "right" thing

    for i1 in range(0, len(LoO)):
        """
        Checks for collisions
        """
        b1 = LoO[i1]
        for i2 in range(i1+1, len(LoO)):
            b2 = LoO[i2]
            collided = spheres_collide( b1, b2 )      # check for sphere collisions!
            if (collided == True): print("Colliding were objecets with indices:", i1, i2)
        
    for b in LoO:
        corral_collide( b )   # updates
    
    # +++ Start of PHYSICS UPDATES -- update all positions here, every time step

    alien.pos = alien.pos + alien.vel*dt   # Update the alien's position
    alien2.pos = alien2.pos + alien2.vel*dt
    alien3.pos = alien3.pos + alien3.vel*dt
    ball.pos = ball.pos + ball.vel*dt      # Update the ball's position

    # +++ End of PHYSICS UPDATES -- be sure new objects are updated appropriately!

    corral_collide(ball)
    # +++ Start of COLLISIONS -- check for collisions & do the "right" thing

    corral_collide(alien)
    corral_collide(alien2)
    corral_collide(alien3)
    lavabox_collide(ball)
    lavabox_collide0(alien)
    lavabox_collide2(alien2)
    lavabox_collide3(alien3)
    ############ -> here is maybe bug!!!
    #lavabox_collides0(sphere)
    #lavabox_collides2(sphere)
    #lavabox_collides3(sphere)
    # If the ball collides with the alien, give the alien a vertical velocity
    
    if mag(ball.pos - alien.pos) < 1.0:
        #Sends alien up towards infinity and adds one to alien hit count.
        print("To infinity and beyond!")
        alien.color = color.gray(.8)
        alien.vel = vector(0, 1, 0)
        alien_hit_count += 1
        alien.pos += vector(0, 3, 0)
        
    if mag(ball.pos - alien2.pos) < 1.0:
        #Sends alien up towards infinity and adds one to alien hit count.
        print("To infinity and beyond!")
        alien2.color = color.gray(.8)
        alien2.vel = vector(0, 1, 0)
        alien_hit_count += 1
        alien2.pos += vector(0, 3, 0)
        
    if mag(ball.pos - alien3.pos) < 1.0:
        #Sends alien up towards infinity and adds one to alien hit count.
       print("To infinity and beyond!")
       alien3.color = color.gray(.8)
       alien3.vel = vector(0, 1, 0)
       alien_hit_count += 1   
       alien3.pos += vector(0, 3, 0)
        
    if alien_hit_count == 3:
        """
        Ends game after player hits all of the aliens.
        """
        print ("Game over! YOU WON!")
        return False
        

    # If the alien ventures too far, restart randomly -- but only if it's
    # not moving vertically.
    #if mag(alien.pos) > 10 and alien.vel.y < 1:
        #alien.pos.x = choice([-6, 6])
        #alien.pos.z = choice([-6, 6])
        #alien.vel = 2*vector.random() # Library-supplied random vector
        #alien.vel.y = 0.0             # No vertical component of velocity

    # +++ End of COLLISIONS



# +++ start of EVENT_HANDLING section -- separate functions for
#                                keypresses and mouse clicks...

def keydown_fun(event):
    """This function is called each time a key is pressed."""
    ball.color = randcolor()
    key = event.key
    ri = randint(0, 10)
    print("key:", key, ri)  # Prints the key pressed -- caps only...

    amt = 0.42              # "Strength" of the keypress's velocity changes
    if key == 'up': #or key in 'wWiI':
        ball.vel = ball.vel + vector(0, 0, -amt)
    elif key == 'left': #or key in 'aAjJ':
        ball.vel = ball.vel + vector(-amt, 0, 0)
    elif key == 'down': #or key in 'sSkK':
        ball.vel = ball.vel + vector(0, 0, amt)
    elif key == 'right': #or key in "dDlL":
        ball.vel = ball.vel + vector(amt, 0, 0)
   # elif key in ' rR':
       # ball.vel = vector(0, 0, 0) # Reset! via the spacebar, " "
       # ball.pos = vector(0, 0, 0)

#def click_fun(event):
    """This function is called each time the mouse is clicked."""
    #print("event is", event.event, event.which)

# +++ End of EVENT_HANDLING section



# +++ Other functions can go here...

def choice(L):
    """Implements Python's choice using the random() function."""
    LEN = len(L)              # Get the length
    randomindex = int(LEN*random())  # Get a random index
    return L[randomindex]     # Return that element

def randint(low, hi):
    """Implements Python's randint using the random() function.
       returns an int from low to hi _inclusive_ (so, it's not 100% Pythonic)
    """
    if hi < low:
        low, hi = hi, low               # Swap if out of order!
    LEN = int(hi) - int(low) + 1.       # Get the span and add 1
    randvalue = LEN*random() + int(low) # Get a random value
    return int(randvalue)               # Return the integer part of it

def randcolor():
    """Returns a vector of (r, g, b) random from 0.0 to 1.0."""
    r = random(0.0, 1.0)
    g = random(0.0, 1.0)
    b = random(0.0, 1.0)
    return vector(r, g, b)       # A color is a three-element vector
    
def corral_collide(ball):
     # If the ball hits wallA
    if ball.pos.z < wallA.pos.z:  # Hit -- check for z
        ball.pos.z = wallA.pos.z  # Bring back into bounds
        ball.vel.z *= -1.0        # Reverse the z velocity

    # If the ball hits wallB
    if ball.pos.x < wallB.pos.x:  # Hit -- check for x
        ball.pos.x = wallB.pos.x  # Bring back into bounds
        ball.vel.x *= -1.0        # Reverse the x velocity
        
    # If the ball hits wallC
    if ball.pos.x > wallC.pos.x:  # Hit -- check for z
        ball.pos.x = wallC.pos.x  # Bring back into bounds
        ball.vel.x *= -1.0        # Reverse the z velocity

    # If the ball hits wallD
    if ball.pos.z > wallD.pos.z:  # Hit -- check for z
        ball.pos.z = wallD.pos.z  # Bring back into bounds
        ball.vel.z *= -1.0        # Reverse the z velocity   

def lavabox_collide(ball):
    """
    If the ball / person hits a box of lava, they wil bounce off of the lava.
    This makes the game harder to play.
    """
    
    #If the ball hits mybox
    if ball.pos.z > (mybox.pos.z - 1.5) and ball.pos.z < (mybox.pos.z + 1.5) and ball.pos.x > (mybox.pos.x - 1.5) and ball.pos.x < (mybox.pos.x + 1.5):
        ball.vel.z *= -1.0
        ball.vel.x *= -1.0
        
    if ball.pos.z > (mybox1.pos.z - 1.5) and ball.pos.z < (mybox1.pos.z + 1.5) and ball.pos.x > (mybox1.pos.x - 1.5) and ball.pos.x < (mybox1.pos.x + 1.5):
        ball.vel.z *= -1.0
        ball.vel.x *= -1.0
                
    if ball.pos.z > (mybox2.pos.z - 1.5) and ball.pos.z < (mybox2.pos.z + 1.5) and ball.pos.x > (mybox2.pos.x - 1.5) and ball.pos.x < (mybox2.pos.x + 1.5):
        ball.vel.z *= -1.0
        ball.vel.x *= -1.0
        
    if ball.pos.z > (mybox3.pos.z - 1.5) and ball.pos.z < (mybox3.pos.z + 1.5) and ball.pos.x > (mybox3.pos.x - 1.5) and ball.pos.x < (mybox3.pos.x + 1.5):
        ball.vel.z *= -1.0
        ball.vel.x *= -1.0
        
    if ball.pos.z > (mybox4.pos.z - 1.5) and ball.pos.z < (mybox4.pos.z + 1.5) and ball.pos.x > (mybox4.pos.x - 1.5) and ball.pos.x < (mybox4.pos.x + 1.5):
        ball.vel.z *= -1.0
        ball.vel.x *= -1.0
        
def lavabox_collide0(alien):
    """
    If the alien hits a box of lava, they wil bounce off of the lava.
    This makes the game harder to play.
    """
    
    #If the alien hits mybox
    if alien.pos.z > (mybox.pos.z - 1.5) and alien.pos.z < (mybox.pos.z + 1.5) and alien.pos.x > (mybox.pos.x - 1.5) and alien.pos.x < (mybox.pos.x + 1.5):
        alien.vel.z *= -1.0
        alien.vel.x *= -1.0
        
    if alien.pos.z > (mybox1.pos.z - 1.5) and alien.pos.z < (mybox1.pos.z + 1.5) and alien.pos.x > (mybox1.pos.x - 1.5) and alien.pos.x < (mybox1.pos.x + 1.5):
        alien.vel.z *= -1.0
        alien.vel.x *= -1.0
                
    if alien.pos.z > (mybox2.pos.z - 1.5) and alien.pos.z < (mybox2.pos.z + 1.5) and alien.pos.x > (mybox2.pos.x - 1.5) and alien.pos.x < (mybox2.pos.x + 1.5):
        alien.vel.z *= -1.0
        alien.vel.x *= -1.0
        
    if alien.pos.z > (mybox3.pos.z - 1.5) and alien.pos.z < (mybox3.pos.z + 1.5) and alien.pos.x > (mybox3.pos.x - 1.5) and alien.pos.x < (mybox3.pos.x + 1.5):
        alien.vel.z *= -1.0
        alien.vel.x *= -1.0
        
    if alien.pos.z > (mybox4.pos.z - 1.5) and alien.pos.z < (mybox4.pos.z + 1.5) and alien.pos.x > (mybox4.pos.x - 1.5) and alien.pos.x < (mybox4.pos.x + 1.5):
        alien.vel.z *= -1.0
        alien.vel.x *= -1.0
        
def lavabox_collide2(alien2):
    """
    If the alien2 hits a box of lava, they wil bounce off of the lava.
    This makes the game harder to play.
    """
    
    #If the alien hits mybox
    if alien2.pos.z > (mybox.pos.z - 1.5) and alien2.pos.z < (mybox.pos.z + 1.5) and alien2.pos.x > (mybox.pos.x - 1.5) and alien2.pos.x < (mybox.pos.x + 1.5):
        alien2.vel.z *= -1.0
        alien2.vel.x *= -1.0
        
    if alien2.pos.z > (mybox1.pos.z - 1.5) and alien2.pos.z < (mybox1.pos.z + 1.5) and alien2.pos.x > (mybox1.pos.x - 1.5) and alien2.pos.x < (mybox1.pos.x + 1.5):
        alien2.vel.z *= -1.0
        alien2.vel.x *= -1.0
                
    if alien2.pos.z > (mybox2.pos.z - 1.5) and alien2.pos.z < (mybox2.pos.z + 1.5) and alien2.pos.x > (mybox2.pos.x - 1.5) and alien2.pos.x < (mybox2.pos.x + 1.5):
        alien2.vel.z *= -1.0
        alien2.vel.x *= -1.0
        
    if alien2.pos.z > (mybox3.pos.z - 1.5) and alien2.pos.z < (mybox3.pos.z + 1.5) and alien2.pos.x > (mybox3.pos.x - 1.5) and alien2.pos.x < (mybox3.pos.x + 1.5):
        alien2.vel.z *= -1.0
        alien2.vel.x *= -1.0
        
    if alien2.pos.z > (mybox4.pos.z - 1.5) and alien2.pos.z < (mybox4.pos.z + 1.5) and alien2.pos.x > (mybox4.pos.x - 1.5) and alien2.pos.x < (mybox4.pos.x + 1.5):
        alien2.vel.z *= -1.0
        alien2.vel.x *= -1.0
    
def lavabox_collide3(alien3):
    """
    If the alien3 hits a box of lava, they wil bounce off of the lava.
    This makes the game harder to play.
    """
    
    #If the alien hits mybox
    if alien3.pos.z > (mybox.pos.z - 1.5) and alien3.pos.z < (mybox.pos.z + 1.5) and alien3.pos.x > (mybox.pos.x - 1.5) and alien3.pos.x < (mybox.pos.x + 1.5):
        alien3.vel.z *= -1.0
        alien3.vel.x *= -1.0
        
    if alien3.pos.z > (mybox1.pos.z - 1.5) and alien3.pos.z < (mybox1.pos.z + 1.5) and alien3.pos.x > (mybox1.pos.x - 1.5) and alien3.pos.x < (mybox1.pos.x + 1.5):
        alien3.vel.z *= -1.0
        alien3.vel.x *= -1.0
                
    if alien3.pos.z > (mybox2.pos.z - 1.5) and alien3.pos.z < (mybox2.pos.z + 1.5) and alien3.pos.x > (mybox2.pos.x - 1.5) and alien3.pos.x < (mybox2.pos.x + 1.5):
        alien3.vel.z *= -1.0
        alien3.vel.x *= -1.0
        
    if alien3.pos.z > (mybox3.pos.z - 1.5) and alien3.pos.z < (mybox3.pos.z + 1.5) and alien3.pos.x > (mybox3.pos.x - 1.5) and alien3.pos.x < (mybox3.pos.x + 1.5):
        alien3.vel.z *= -1.0
        alien3.vel.x *= -1.0
        
    if alien3.pos.z > (mybox4.pos.z - 1.5) and alien3.pos.z < (mybox4.pos.z + 1.5) and alien3.pos.x > (mybox4.pos.x - 1.5) and alien3.pos.x < (mybox4.pos.x + 1.5):
        alien3.vel.z *= -1.0
        alien3.vel.x *= -1.0
        
def tree_collide(ball):
    """
    If the ball hits the tree.
    """
    
    if ball.pos.z > (tree1.pos.z - 1.5) and bal.pos.z < (tree1.pos.z + 1.5) and bal.pos.x > (tree1.pos.x - 1.5) and ball.pos.x < (tree1.pos.x + 1.5):
        ball.vel.z *= -1.0
        ball.vel.x *= -1.0
        
    if ball.pos.z > (mybox1.pos.z - 1.5) and ball.pos.z < (mybox1.pos.z + 1.5) and ball.pos.x > (mybox1.pos.x - 1.5) and ball.pos.x < (tree1.pos.x + 1.5):
        ball.vel.z *= -1.0
        ball.vel.x *= -1.0
                
    if ball.pos.z > (mybox2.pos.z - 1.5) and ball.pos.z < (mybox2.pos.z + 1.5) and ball.pos.x > (mybox2.pos.x - 1.5) and ball.pos.x < (mybox2.pos.x + 1.5):
        ball.vel.z *= -1.0
        ball.vel.x *= -1.0
        
    if ball.pos.z > (mybox3.pos.z - 1.5) and ball.pos.z < (tree1.pos.z + 1.5) and ball.pos.x > (mybox3.pos.x - 1.5) and ball.pos.x < (mybox3.pos.x + 1.5):
        ball.vel.z *= -1.0
        ball.vel.x *= -1.0
        
    if ball.pos.z > (mybox4.pos.z - 1.5) and ball.pos.z < (mybox4.pos.z + 1.5) and alien3.pos.x > (mybox4.pos.x - 1.5) and ball.pos.x < (mybox4.pos.x + 1.5):
        ball.vel.z *= -1.0
        ball.vel.x *= -1.0
        
"""
def lavabox_collides0(sphere):
    #Spheres collide with lava.
    
    if sphere.pos.z > (mybox.pos.z - 1.5) and sphere.pos.z < (mybox.pos.z + 1.5) and sphere.pos.x > (mybox.pos.x - 1.5) and sphere.pos.x < (mybox.pos.x + 1.5):
        sphere.vel.z *= -1.0
        sphere.vel.x *= -1.0
        
    if sphere.pos.z > (mybox1.pos.z - 1.5) and sphere.pos.z < (mybox1.pos.z + 1.5) and sphere.pos.x > (mybox1.pos.x - 1.5) and sphere.pos.x < (mybox1.pos.x + 1.5):
        sphere.vel.z *= -1.0
        sphere.vel.x *= -1.0
                
    if sphere.pos.z > (mybox2.pos.z - 1.5) and sphere.pos.z < (mybox2.pos.z + 1.5) and sphere.pos.x > (mybox2.pos.x - 1.5) and sphere.pos.x < (mybox2.pos.x + 1.5):
        sphere.vel.z *= -1.0
        sphere.vel.x *= -1.0
        
    if sphere.pos.z > (mybox3.pos.z - 1.5) and sphere.pos.z < (mybox3.pos.z + 1.5) and sphere.pos.x > (mybox3.pos.x - 1.5) and sphere.pos.x < (mybox3.pos.x + 1.5):
        sphere.vel.z *= -1.0
        sphere.vel.x *= -1.0
        
    if sphere.pos.z > (mybox4.pos.z - 1.5) and sphere.pos.z < (mybox4.pos.z + 1.5) and sphere.pos.x > (mybox4.pos.x - 1.5) and sphere.pos.x < (mybox4.pos.x + 1.5):
        sphere.vel.z *= -1.0
        sphere.vel.x *= -1.0
"""
        
def spheres_collide( sphere1, sphere2 ):
    """ takes two inputs, sphere1 and sphere2
        (1) checks for a collision (centers within DISTANCE of each other)
        (2) if colliding,
            (2a) undo the last time step's motion
            (2b) compute the new velocities of the two spheres
            (2c) assign those new velocities
        (3) returns True if they collided; False otherwise
        both sphere1 and sphere2 need a .pos field and a .vel field!
    """
    DISTANCE = 1.0   # collision-check distance
    s1 = sphere1
    s2 = sphere2  # simpler!
    diff = s1.pos - s2.pos  # vector between the two
    if mag( diff ) < DISTANCE:
        # vector perpendicular to the diff vector
        dtan = rotate( diff, radians(90), vector(0,1,0) )
        # get the two velocities
        v1 = s1.vel; v2 = s2.vel
        # undo the last time step
        s1.pos -= v1*dt; s2.pos -= v2*dt
        # find the radial and tangent parts of each 
        v1_rad = proj(v1, diff); v1_tan = proj(v1, dtan)
        v2_rad = proj(v2, -diff); v2_tan = proj(v2, dtan)
        # swap the radials and keep the tangents
        s1.vel =  v2_rad + v1_tan
        s2.vel =  v1_rad + v2_tan
        return True   # did collide
    else:
        return False  # did not collide