label externalStimuli:

    scene bg hallway
    with dissolve
    
    # play ambience "assets/sfx/hallway.mp3" fadein 1

    "It’s kinda strange."

    "We spent the entirety of lunch discussing something that probably isn’t even real."

    "I had a lot of fun with it."
    
    # stop ambience fadeout 3
    
    scene bg black
    with dissolve
    
    $ ellipses()
    
    "And so the rest of day goes on."
    
    $ renpy.pause(1)

    play sound "assets/sfx/schoolbell.mp3"
    $ renpy.pause(2)
    
    "The final bell... Finally."
    
    scene bg classroom
    with dissolve

    show tomo worry at left with dissolve

    t "Hey, [protag], we’re still gonna... um... hang out today, right? Just you and me?"

    mc "Yeah, sounds good."
    
    scene bg black
    with dissolve
    $ renpy.pause(.5)
    scene bg hallway
    show tomo concern at center
    with dissolve
    
    play ambience "assets/sfx/hallway.mp3" fadein 1

    "Y’know, it has been a little while since the last time I had some one on one time with her." 

    "Something must be bugging her. She seemed different today."

    "Tomo sighs loudly as we walk."

    mc "Something on your mind?"

    stop music fadeout 3
    $ renpy.music.set_volume(0.3, 10, channel="ambience")
    
    show tomo worry with dissolve

    t "We kinda need to talk about something."

    mc "Is this about Kirei? What’s the matter, are you jealous?"

    show tomo concern with dissolve

    "She sighs."

    t "No! That’s not it."

    mc "Then what’s the issue then?"

    t "It’s about...{w=.5} {size=15}Um...{/size}{w=.75} {size=10}Kirei...{/size}"
    show tomo sad with dissolve
    "I sigh."

    "Of course it is."

    mc "And what about her?"

    show tomo worry with dissolve

    t "I...{w=.5} I don’t know, I just {w=.5} don’t think you should be spending so much time with her."

    "Of course she doesn’t. I tune out for a bit. This isn’t worth me listening to."

    "Nobody tells me who I can and can’t be friends with."

    show tomo chestnut with dissolve

    "She has no reason to be talking about Kirei."

    "She hardly even knows her!"

    "Why can’t she just accept the fact that I can make new friends?"

    show tomo worry with dissolve

    "Is she actually jealous?"

    "I just don’t understand why she isn’t willing to give her a chance."

    show tomo concern with dissolve

    "Why she isn’t willing to give {i}me{/i} a chance."

    "What’s gotten into you, Tomo?"

    show tomo sad with dissolve

    t "[protag], are you even listening to me?"

    #zoom if possible?

    "Tomo puts her hands on my arms and looks me in the eyes."

    show tomo armdown cry with dissolve

    "She’s never looked this sincere before."

    t "Kirei’s bad news, okay? Just... please, stay with me."

    mc "I-{w=.5}I..."
    
    "Just then, I feel a hand on my shoulder."

    show kirei happy at right with easeinright
    show tomo worry at left with ease
    
    "I instinctively turn around to see Kirei smiling at me."

    "I smile back at her."

    k "Hey, [protag], oh... is this your friend? Hi, I’m Kirei."

    show kirei arm happy at right with dissolve

    "She offers Tomo a handshake."

    t "Hmph."

    show tomo hip mad at left with dissolve

    "Tomo crosses her arms."

    "Could she be more immature?"

    show kirei wrist happy at right with dissolve

    k "Okay, then. You don’t mind me stealing our little [protagchan] for a second, do you?"

    hide tomo with dissolve
    show kirei happy with dissolve

    "Kirei pulls me close to her and whispers in my ear."

    k "Let’s meet in the park after school today."

    show kirei wrist smile with dissolve

    "She smiles as grabs my hand and leads me away."

    hide kirei with dissolve
    show tomo worry with dissolve

    t "N-no... [protagchan]."

    "Her voice falters."

    "Her words break."

    hide tomo with dissolve

    "Some friend she turned out to be."

    show kirei concern with dissolve

    "We walk further away from Tomo."

    mc "I’m sorry for earlier."
    
    stop ambience fadeout 5

    mc "Tomo’s not usually like that."

    show kirei happy with dissolve

    k "Oh, it’s not a problem."
    
    $ renpy.music.set_volume(1, 5, channel="ambience")

    "Kirei smiles and waves it off."

    hide kirei
    scene bg black
    with dissolve

    $ renpy.pause(1)
    
    "Tomo’s been different lately."

    "A little more worried about me."

    "She’s got nothing to worry about."

    "I’m fine on my own."

    "And she should be fine on hers."

    $ renpy.music.set_volume(1, 0, channel="ambience")
    
    $ renpy.pause(2)

    return