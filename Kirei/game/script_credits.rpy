label credits1:

    if config.developer == False:
        $ overriding_on = True
        $ renpy.block_rollback()
    
    #play sound2 "assets/music/Full.mp3"
    
    $ credits_speed = 35
    show cred at Move((0.5, 4.8), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(3)
    $ heartbeat()
    $ renpy.pause(2)
    $ heartbeat()
    $ renpy.pause(1)
    $ heartbeat()
    $ heartbeat()

    stop sound2
    play sound "assets/sfx/whoosh.mp3"
    #play sound "assets/sfx/sharpBreath.mp3"
    #play sound2 "assets/sfx/spiritbreath.mp3"
    
    show white with dissolve
    hide cred
    $ renpy.pause(1)
    stop sound
    $ renpy.pause(2)

    show tomo sad at offscreenleft
    $ tomoNar = "Tomo"
    $ kireiNar = "Kirei"
    
    if config.developer == False:
        $ overriding_on = False
        $ renpy.block_rollback()
    
    Tomo "Please... no..."

    Tomo "Don’t leave me."
    
    tTomo"I... I don’t want to be lost again."
    
    return
    
label credits2:

    if config.developer == False:
        $ overriding_on = True
        $ renpy.block_rollback()

    play sound "assets/music/Full.mp3"
    $ renpy.pause(2)
    scene bg credits
    show title at truecenter
    with dissolve
        
    $ credits_speed = 35
    $ renpy.pause(3)
    hide title with dissolve
    $ renpy.pause(2)

    show cred at Move((0.5, 4.8), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
  
    show thanks at truecenter with dissolve
    
    $ renpy.pause(5)
    

    if config.developer == False:
        $ overriding_on = False
        $ renpy.block_rollback()
        
    $ ctc_float_on()
    
    $ renpy.pause()
    
    $ ctc_float_off()
    
    scene black with dissolve
    stop sound
    $ renpy.pause(3)
    
    return