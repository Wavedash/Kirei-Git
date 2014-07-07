label titleSequence:

    if config.developer == False:
        $ overriding_on = True
    
    $ renpy.pause(2.0)
    
    show text "{font=assets/engine/AndBasR.ttf}rosin entertainment presents{/font}" with dissolve
    
    $ renpy.pause(3.0)
    
    hide text with dissolve
    
    show text "{font=assets/engine/AndBasR.ttf}team tomo's\nnanoreno 2014\nlast minute challenge{/font}" with dissolve
    
    $ renpy.pause(3.0)
    
    hide text with dissolve
    
    $ renpy.pause(1.5)
    
    $ renpy.pause(0.5)

    show title at truecenter with dissolve
    
    $ renpy.pause(3.0)
    
    hide title with dissolve
    
    stop ambience2 fadeout 3
    
    $ renpy.pause(5.0)
    
    if config.developer == False:
        $ overriding_on = False
        $ renpy.block_rollback()

    return