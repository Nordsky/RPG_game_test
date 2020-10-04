import pygame


pygame.init()
screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption("Grand adventure v 0.7")  # A background image always sits behind the sprites

agent = makeSprite("fire_1/f1.png")     # We create the sprite with the default image
addSpriteImage(agent, "fire_1/f1.png")  # Add extra images. They are stored in the Sprite object
addSpriteImage(agent, "fire_1/f2.png")  # but not displayed yet
addSpriteImage(agent, "fire_1/f3.png")
addSpriteImage(agent, "fire_1/f4.png")
addSpriteImage(agent, "fire_1/f5.png")
addSpriteImage(agent, "fire_1/f6.png")  # See the alternative way of doing this with a Sprite Sheet

agentX = 200        # Set the X position on the screen
agentImage = 0      # This lets us track the current animation frame for the agent
moveSprite(agent, agentX, 120)
showSprite(agent)
nextFrame = clock() # This lets us schedule the time for the next animation frame using the internal clock

while True:
    
    if keyPressed("right"):
        if clock() > nextFrame:   # It is time for the next animation frame
            agentImage +=1        # Move the animation on by one frame
            if agentImage > 7:    # We have 8 frames, so loop round to the start
                agentImage = 0
            changeSpriteImage(agent, agentImage)
            nextFrame = clock() + 60  #schedule the next frame 60 milliseconds from now
            
        agentX +=7          # Change the position for the sprite
        if agentX>500:      # If reached the edge, loop round the screen
            agentX=-20
            
        moveSprite(agent, agentX, 120)  # Actually move the sprite
        
    else:
        agentImage = 0  # If the key is not being pressed, switch back to "standing" frame
        changeSpriteImage(agent, agentImage)
        
    tick(30)  #The movement runs at 30 frames per second, even though the agent image is only changed every 60ms


