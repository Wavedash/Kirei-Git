label prologue:
    play sound "assets/sfx/ohdearscare.mp3"
    stop music fadeout 4
    scene bg park night 
    with dissolve
    
    $ renpy.pause(2)
    play ambience "assets/sfx/night.mp3" fadein 4
    play ambience2 "assets/music/PrologueEpilogue.mp3" fadein 4
    
    $ renpy.pause(2)
    
    # show tomo worry night at left with dissolve
    
    $ kireiNar = "Creature"
    $ tomoNar = "???"
    
    Tomo "Where are they?"
    
    Tomo "I race towards the tree line."
    
    show kirei special shadows with easeinbottom
    play sound "assets/sfx/sharpBreath.mp3"
    
    
    Tomo "Freezing in my tracks, I spot them."

    Tomo "I've found you, but..."
    
    Tomo "I’m...{w=.5} I'm too late."
 
    play sound "assets/sfx/cackle.mp3"
 
    Tomo "The creature laughs loudly as it takes a bite."
    
    play vocal "assets/sfx/chewing.mp3"
   
    #$ double_vision_on("bg park night")
    
    Tomo "I can’t watch this."
    
    stop vocal fadeout 2

    Tomo "There’s so much blood."
    
    $ heartbeat()

    Tomo "I should have paid more attention."
    
    $ heartbeat()

    Tomo "I...{w=.5} I could have done something."
    
    #$ double_vision_off()
    
    stop ambience fadeout(2)
    scene black
    with dissolve
    
    Tomo "I could have stopped this."
    
    stop vocal fadeout 5

    return