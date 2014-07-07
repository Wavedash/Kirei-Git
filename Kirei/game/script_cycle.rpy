label cycle:

    play music "assets/music/LeaningIn.mp3"
    show bg apartment
    with dissolve

    mc "So why are we headed to the park?"

    show kirei arm concern with dissolve

    k "I heard a rumor of a vampire attack there last night."

    mc "Wouldn’t the police be all over the place?"

    k "Vampires don’t tend to leave messes behind, so I doubt the cops would be anywhere close."

    mc "And if the \"crime scene\" is supposedly clean, how do you think we’re gonna be able to find some clues?"

    show kirei arm surprise with dissolve

    k "It’s worth a shot, right?"
    
    "Well... it's not like I have anything else to do today."

    mc "Sure. We should head out right now."

    show kirei concern with dissolve

    k "Hold on a minute... Let’s not."

    mc "Why not?"

    k "There’s bound to be people there."

    show kirei happy with dissolve

    k "We don’t want to look weird scouring the park while there’s people around."

    k "We should go later at night."
    show black with dissolve
    show kirei happy evening with dissolve
    $ renpy.pause(.5)
    show bg apartment evening
    hide black
    with dissolve
    
    k "We can head out soon."
    k "We won't be spotted."
    
    mc "Hey, Kirei?"
    
    k "Hm?"
    
    mc "Why are you so interested in vampires?"
    mc "I mean, not that it's a bad thing."
    mc "I'm just curious."
    
    show kirei arm surprise evening with dissolve
    
    k "That's a good question."
    
    "She searches for an answer."
    
    show kirei happy evening with dissolve
    
    k "I guess you could say I find them fascinating. The whole thing."
    k "Humans and supernatural beings."
    k "The relationship between the two."
    k "What does it mean to be human?"
    
    "That's...{w=.5} much deeper than I expected."
     
    k "Now come on. Let's get going. It'll be dark by the time we get there."

    #(insert h-scene for time skip)

    scene bg black with dissolve
    
    stop music fadeout 3
    
    "And with that, we were on the hunt."
    
    play ambience "assets/sfx/night.mp3" fadein 3
    
    scene bg park night with dissolve
    
    $renpy.pause(.5)

    "I’ve lived near this park my whole life."

    "I can’t believe something like a vampire attack could happen so close to me."

    "It’s kind of unsettling at this hour."

    "Some of the street lights aren’t even on."

    show kirei arm happy night with dissolve

    k "Well, let’s get investigating."

    "Kirei scans her flashlight along the pathway."

    "I begin to search around as well."

    mc "What is it exactly that we should be looking for?"

    k "Anything out of the ordinary."

    show kirei arm happy night at offscreenleft with dissolve
    
    play sound "assets/sfx/spiritbreath.mp3"

    "A slight breeze blows by."

    k "Things like bloodstains, signs of a struggle."

    k "Anything out of place?"

    "This park looks about the same as it always had at night."

    "It is pretty hard to see out here right now."

    "It’s so dark."

    k "Find something?"

    mc "Nothing yet."

    "Man, I have no idea what I should be looking for."

    "I’m almost certain blood would’ve dried up by now."

    "Most clues would’ve been picked up by the police."

    $ ellipses()

    "If there were any clues to begin with."

    "This better not be some prank."

    "Popular Kirei finally snaps her trap on the unpopular kid."

    "No... Kirei wouldn’t do that."

    "We’re out here investigating."

    "And... {w=.5}failing."

    play sound "assets/sfx/spiritbreath.mp3"
    
    "Another breeze makes me shiver."

    "I sigh as I stoop down to check below a bench."

    "I don’t feel quite like myself right now."

    "It’s dark... and cold."

    "And I'm actually a little bit uneasy."

    "The overcast clouds block what moonlight is actually here."
    
    $ night_vision_on("bg black")

    "And the park lights are dimming, too."
    
    "Suddenly, I remember the shadow from before."
    
    "I can't decide which is sillier: Believing in vampires and dismissing the shadow..."
    "Or trying to convince myself I saw nothing when I'm out here looking for vampires."
    
    stop ambience fadeout 8
    
    $ renpy.pause(1)

    k "Hey, [protag]?"

    "I stand back up and look around to find the source of her voice."

    "I can hardly see."

    "It’s just so dark."

    mc "Y-yes... Kirei?"

    "I can hear her moving closer to me."

    "There..."
    
    # $ double_vision_off()
    
    show kirei happy night at center with dissolve
    
    "There she is."
    play sound "assets/sfx/whoosh.mp3"
    $ renpy.pause(.5)
    play sound2 "assets/sfx/punch.mp3"
    show heartbeat with vpunch
    scene bg black with None
    hide heartbeat with dissolve
    stop sound
    stop sound2
    
    $ renpy.pause(4)
    
    return