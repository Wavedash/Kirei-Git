label prey:
        
    play ambience "assets/sfx/night.mp3" fadein 4
    play ambience2 "assets/music/PrologueEpilogue.mp3" fadein 4
    play sound "assets/sfx/spiritbreath.mp3"
    show tomo sad night at offscreenleft
    show bg park night with None
    hide white with dissolve
        
    Tomo "Where are they?"
    
    Tomo "I race towards the tree line."
    
    show kirei special shadows with easeinbottom
    play sound "assets/sfx/sharpBreath.mp3"
    show bg park night
    with vpunch
    
    Tomo "Freezing in my tracks, I spot them."
    
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

    Tomo "I should have noticed...."
    
    tTomo "I'm so sorry, [protagchan]."

    hide kirei with dissolve
    
    Tomo "Shit, she must’ve heard me."

    show tomo armdown empty night at offscreenleft

    show kirei concern night with dissolve
    
    tTomo "Ah!"

    kTomo "I see you finally decided to show your face again."

    tTomo "..."

    kTomo "Whats the matter? You were never the quiet one before."

    Tomo "She wipes the blood from her mouth."

    tTomo "You..."

    show tomo armdown yandere night at offscreenleft

    Tomo "My blood begins to boil."

    tTomo "You took... From me..."

    show kirei wrist happy night with dissolve

    kTomo "Oh my, I’m sorry. Was this yours?"
    
    kTomo "I didn’t realize it had your name on it."

    Tomo "Everything is wrong."

    kTomo "A pretty girl like you doesn’t need someone like that anyway."

    Tomo "Everything..."

    Tomo "Everything is..."

    Tomo "She’s smiling."

    show kirei smile night with dissolve

    kTomo "Truth be told, from the beginning, I had no intention of killing [protagchan] if it proved useful."

    tTomo "Don't..."
    
    tTomo "Don't you dare say that name!"
    
    kTomo "Now now. Weren't you just using your 'friend' as well? You're just like me."
    
    kTomo "Well, save for the blood and gore."
    
    Tomo "She licks her fingers."
    
    Tomo "Like her? I’m..."
    
    Tomo "She... doesn't realize..."

    show tomo mad night at offscreenleft

    tTomo "I’m nothing like you!"

    show kirei concern night with dissolve

    kTomo "Then tell me... why did you come here?"

    tTomo "I-{w=.5}I..."

    show kirei arm concern night with dissolve

    kTomo "Like always, following like a puppy on a leash."
    kTomo "Spending so much time with your dear friend."
  
    show tomo hip cry night at offscreenleft

    tTomo "..."

    kTomo "What a shame."
    
    kTomo "Your tears tell me enough."

    #$ double_vision_on("bg park night")

    show kirei concern night with dissolve

    kTomo "Well farewell, Tomo."
    kTomo "Enjoy your life."
    kTomo "Or what's left of it."
    kTomo "I don't have room for dessert right now, but you're still on the menu."
    kTomo "I'll see you later."
    
    stop ambience fadeout 5
   
    hide kirei with dissolve

    Tomo "I... can’t believe you’re gone."
    
    $ renpy.pause(1)
    
    show bg tomoCG2 with dissolve
    
    Tomo "Why am I crying?"
    Tomo "Why did I have to care for such a simple human?"
    Tomo "I knew this was inevitable anyway..."
    Tomo "I just didn’t expect it to come so soon."

    Tomo "You...{w=.5} should have listened, [protag]."

    Tomo "I told you not to trust her."
    
    Tomo "I didn't think she was like me..."

    Tomo "You’re gone now."

    Tomo "My only tie to this human world."

    Tomo "My only friend..."

    Tomo "Gone."

    Tomo "What am I now?"

    Tomo "Am I just like her?"
    
    Tomo "..."

    Tomo "That’s the curse I’ve been bound to..."

    Tomo "And the fate that I’ve been trying to escape from this whole time."

    Tomo "Nothing can hold me back any longer."

    Tomo "I enjoyed the time we had together, [protag]...{w=.5} even if this was supposed to happen...{w=.5} one way or another."

    Tomo "You were supposed to be mine, but...{w=.5} she stole you away."
    
    Tomo "This...{w=.5} this was your blood."
  
    $ renpy.pause(1)
    
    show bg tomoCG1 with dissolve
  
    $ renpy.pause(3)
    
    Tomo "But... don’t worry, [protagchan]... She’s not getting away that easy."
    
    show bg tomoCG2 with dissolve
    
    Tomo "I swear it."
    
    stop ambience fadeout 1
    stop ambience2 fadeout 1
    
    $ renpy.pause(2)
    
    show bg tomoCG3 with vpunch
    play sound "assets/sfx/cackle.mp3"
        
    Tomo "I’ll kill her."
    
    scene bg black with dissolve
    
    
    return