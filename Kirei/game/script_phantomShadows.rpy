label phantomShadows:

    "Kirei smiles as she waves from her door."
    "Well, she certainly had a lot to share."
    "Never really had her pegged as someone like me."
    "Just going through the motions, with a whole different kind of person on the inside."
    
    play ambience "assets/sfx/ParkAmbience.mp3" fadein 3
    
    scene bg park evening
    with dissolve
    
    "I enter the park gates - quickest way home and all that."
    "It’s a bit chilly for April, but the sun sets behind the clouds as I walk."
    "The cold air feels a bit thin to breathe."
    "My feet hit the pavement at a rhythm unfamiliar to me."
    "The park paths are fairly empty, but people are here nonetheless."
    "A couple of kids in hoodies, keeping to themselves."

    play ambience "assets/music/PrologueEpilogue.mp3" fadein 4

    "What if...{w=.5} they’re vampires?"
    "Oh man, now I’m on edge."
    "They look up at me, but I can’t quite make out their faces."
    "I look back down to avert my eyes."
    "When I see them pass out of my periphery, I look back up to find the path out to my street."
    show bg park night with longdissolve
    "The sun tips over the horizon."
    "As I pull my head up, I see some dark form in the distance."

    #show kirei special shadows with dissolve
    
    $ shadow_vision_on("shadowblowing")
    #hide shadowblowing

    mc "A-a shadow?"

    "It stands there... almost flickering."
    "Blowing in the wind."
    "Stealing my breath."

    play sound "assets/sfx/spiritbreath.mp3"
    
    show black with dissolve
    
    $ double_vision_off_instant()
    
    hide black with dissolve

    "I rub my eyes and the silhouette is gone." 
    mc "..."
    "I look around and pick up the pace, anxious to get home."
    "My footsteps quicken as I hold my backpack tighter to my person."
    "That... shadow."
    "Whatever the hell that was..."
    "Probably nothing, right?"
    "It’s just been a long day."
    "Probably my eyes just playing tricks on me."
    "My heart’s beating fast. I’m not sure if it was just from me walking faster, or if I’m actually scared."
    
    scene black with dissolve
    
    "At least I’m home now."
    "I unlock the door and slide inside."

    stop ambience fadeout 1
    
    $ renpy.pause(.5)

    "I flip a couple of lights on and make my way to the living room."

    "Surprisingly, my parents aren’t home yet. "
    
    "I check the clock."
    
    mc "Oh."

    "I thought it was a lot later on in the day."
    
    $ renpy.pause(.5)
    
    "I drop to my bed and close my eyes."

    "What was that shadow from earlier?"

    $ ringphone()

    mc "Ah!"
    
    "My phone caught me completely off guard."
    
    "I fumble around my pocket."

    $ showphone()

    "It’s Tomo."

    mc "Hello?"

    show tomo worry at offscreenleft
    
    play music "assets/music/FriendsForever.mp3"

    t "[protag]... hi."

    "Hearing her voice, even through a static filter of the phone, is comforting, for some reason."

    "I hear her let out a heavy sigh."

    mc "Need something?"

    show tomo hip happy at offscreenleft

    t "N-no, nothing. I just wanted to talk."

    mc "Aww, that’s cute."

    mc "You actually miss me."

    "And there’s Tomo’s signature scoff."

    mc "Yeah, I just got home from Kirei’s house."

    show tomo happy at offscreenleft

    t "Oh yeah, how was that?"

    mc "She’s..."
    mc "How do I put this..."
    mc "More interested in vampires than I am."

    show tomo sass at offscreenleft

    "I hear Tomo lightly giggle."

    t "Didn’t even think that’d be possible."

    "I sigh."

    mc "Hey! I’m not {i}that{/i} bad, am I?"

    t "You’re the only one I know who visits the websites you do."

    "That’s because I’m probably her only friend."

    $ ellipses()

    show tomo chestnut at offscreenleft

    t "[protag]? Are you still there?"

    mc "Wha? Oh, yeah, I’m still here."

    show tomo chestnut at offscreenleft

    t "Something on your mind?"

    "Yeah... that unnerving dark visage."

    "The splotch of black."

    mc "I saw something today."

    show tomo concern at offscreenleft

    t "You did? Like what?"

    mc "I don’t know what it was... some shadowy looking thing."

    mc "Like a dark blur."

    "Tomo goes quiet for a bit. Her tone becomes a bit more solemn."

    show tomo hip mad at offscreenleft

    t "S-seriously?"

    mc "No joke."
    mc "It was just standing there for a split second."
    mc "Then it disappeared."
    mc "I froze up when I saw it."

    show tomo hip empty at offscreenleft

    t "You’re okay though, right?"

    mc "Yeah, just a bit startled, maybe."

    "I hear her sigh again."

    show tomo hip happy at offscreenleft

    t "Well, I’m glad you’re okay."

    t "Just... remember to do your homework."

    "Yeah, totally not doing that."

    mc "Yeah, whatever."

    mc "See you tomorrow."

    t "Yeah, of course."
    
    stop music fadeout 3

    $ hidephone()

    hide tomo

    "I’ve been feeling a little preoccupied about the shadow since I got home."

    "Couldn’t really enjoy dinner."

    "Don’t think I plan to tell my parents."

    "They’d get way too excited about the Kirei news."

    "So I decide to stay quiet about the whole issue."

    $ ellipses()

    "I laid in my bed thinking of that shadow I saw earlier."

    "If I try to shut my eyes, they’d snap right back open."

    "It was just too dark."

    "All I see are shadows."

    "Sleep isn’t coming easy tonight."

    "I reach for my nightstand."

    "Let’s see what the Internet has to say..."
    
    $ showphone_night()
    show phonex
    
    show white with dissolve

    "Agh! Bright!"
    
    hide white with dissolve
    
    "I rub my eyes vigorously."
    
    $ ellipses()
    
    $ ellipses()
    
    hide phonex
    $ hidephone()

    $ ellipses()
    
    "Crap. I forgot to do my homework."
    
    $ renpy.pause(1)
    
    return
