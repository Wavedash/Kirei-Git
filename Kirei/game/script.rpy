# Here's the splash screen that goes before the main menu.
label splashscreen:

    #This variable controls what version we're running. For android versions, set to True.
    #This will disable anything that the android version of Ren'Py can't handle
    #such as text input, and replace it with something else.
    
    if config.developer == False:
        $ overriding_on = True
    
    scene black
    
    if config.developer:
        show rosinlogo at truecenter
        # This checks to see if you've remembered to turn off developer mode when
        # running the game. If it's on, it warns you.
        show text "{font=assets/engine/AndBasR.ttf}\n\n\n\n\n\nDEVELOPER MODE IS ACTIVE{/font}"
        with dissolve
        
        $ renpy.pause(3.0)
        
        hide text
        hide rosinlogo
        with dissolve
        
    if not config.developer:
        show rosinlogo at truecenter with dissolve 
        $ renpy.pause(3.0)
        hide rosinlogo with dissolve  
        
    show nanologo at truecenter with dissolve 
    $ renpy.pause(3.0)
    hide nanologo with dissolve 

    $ overriding_on = False
    
    # scene bg mainmenu
    # with dissolve
    
    return
    
# The game starts here.
label start:
    
    # Just a little jump scare to start your day.
        
    scene bg park
        
    # Myth always masters his music at a volume that's super loud in Ren'Py.
    # The easiest way to fix that is to set the music channel to a level
    # based on a fraction of the music volume slider in the options menu.
    
    $ renpy.music.set_volume(0.4, 0, channel="music")
    
    # This is basically our Table of Contents. It can be shuffled around or changed, but it
    # doesn't look for files. It looks for the scene labels INSIDE the files.

    menu:
        "Original NaNoRenO Version":
            call originalVersion
        
        "Director's Cut":
            call prologue # done
            call titleSequence # done
            call enterAkira # done
            call kireisPlace # done
            call phantomShadows # done
            call sleepyMorning # done
            call sunblock # done
            call interviewWith # done
            call externalStimuli # Done
            call cycle  # done
            call hungry # done
            call credits1 # done
            call prey  # done
            call credits2 # done

    return
    