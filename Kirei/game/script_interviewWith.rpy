label interviewWith:

    $ ellipses()
    
    $ renpy.pause(1)

    play sound "assets/sfx/schoolbell.mp3"
    $ renpy.pause(2)
    
    scene bg hallway
    with dissolve
    
    play ambience "assets/sfx/hallway.mp3" fadein 1
    # play music "assets/music/HangingOut.mp3"
    
    "That was a little more awkward than it should have been."
    "I wonder what's gotten to her."
    "At least morning classes are over."

    show tomo sad with dissolve
    
    "Tomo's still mad, it looks like."
    
    mc "Hey."
    
    show tomo chestnut with dissolve
    
    mc "I’ll see you later."
    
    show tomo concern with dissolve

    t "Yeah..."

    hide tomo with dissolve

    "I can’t blame Tomo for not wanting to come along."
    "If I’ve learned one thing in high school..."
    "It’s that not everyone’s a fan of this kind of stuff."
    "Fortunately, I know someone that is."
    
    $ renpy.pause(1)
    
    "I'm pretty sure Kirei’s class is right down the hall."
    "I pass by a handful of people on their way out the door."
    mc "Room 112..."
    
    stop ambience fadeout 3
    
    "I think this is it."

    scene bg classroom flip
    show kirei arm concern
    with dissolve
    
    play music "assets/music/LeaningIn.mp3"

    "Yup."
    "And there’s Kirei."
    "Sitting at her desk, eating an apple."

    show kirei arm happy with dissolve

    "She waves me over to her."
    "She’s got a book open on her desk."

    k "Hey, you."

    "She smiles at me as I sit down across from her."

    mc "What are you reading?"

    k "Vampire novel."

    mc "Not with the sparkly..."

    show kirei wrist smile with dissolve

    "Kirei laughs a bit."

    k "Of course not."

    k "This one’s pretty grisly."

    mc "What, vampires tearing humans apart?"

    show kirei arm concern with dissolve

    k "Nope."

    k "Vampires versus vampires."

    "Is that even a thing?"

    mc "That’s crazy."

    show kirei arm happy with dissolve

    k "Well, the one vampire used to be a human."

    k "A vampire hunter actually."

    mc "And... his hunts weren’t all too successful, I’m guessing?"

    show kirei concern with dissolve

    k "Right, so the only way he could actually defeat a vampire was to become one himself."

    k "Losing his identity in the process."

    show kirei arm surprise with dissolve

    mc "Sounds like the hunter was too obsessed with his prey."

    k "I felt more like the hunter was making a noble sacrifice."

    mc "Well when you put it that way, I guess he was doing a justice."

    "But at what cost?"
    "Kirei takes a bite out of her apple."

    mc "Could you imagine being a vampire?"

    "She shakes her head."

    mc "It must suck."

    show kirei wrist happy with dissolve

    k "Really, [protag]? It sucks?"

    show kirei wrist smile with dissolve

    "Kirei snickers and shakes her head."

    "Stupid puns."
    "I swear I didn’t mean to."

    mc "Vampirism is a curse."

    show kirei arm worry with dissolve

    mc "Could you imagine?"
    mc "After the hunter becomes a vampire, he’s just kinda stuck like that."
    mc "He’d be dependent on blood."
    mc "He’d feel alienated from his old friends and family."

    "Y’know... not too different from me."

    "Aside from the whole blood part."

    "Kirei finishes her apple and flips back through the book."

    show kirei arm happy with dissolve

    k "Did you know that vampires don’t have reflections either?"

    mc "Of course I did."

    "Soulless creatures with nothing else to live for except killing."

    "If they’re still even alive."

    mc "Are vampires considered living beings?"
    mc "Or are they like really smart zombies?"

    show kirei arm surprise with dissolve

    k "Y’know, that’s a pretty good question."

    "Kirei’s silent for a bit while she thinks."

    show kirei happy with dissolve

    k "I’d say they’re alive."

    mc "Why so?"

    k "Well, they have feelings and emotions, right?"

    mc "Do they?"

    mc "I’ve always known vampires to be the cool, collected type that are strictly business."

    show kirei arm happy with dissolve

    k "Well, if a human can become a vampire, then they’re sure to be somewhat human-like."
    
    mc "So you're saying they still have a soul, then?"
    
    k "A soul?"
    k "Hmm..."
    k "I'd imagine. At least I think so."

    mc "How does that vampire hunter character act in the book?"

    k "Dunno. The book ends after he kills the other vampire."

    "Well that’s lame."

    mc "So you said that vampires can’t be killed by humans?"

    show kirei concern with dissolve

    k "Well, I’m sure it’s possible."
    k "But vampire versus vampire seems like a more fair fight."

    "Probably more entertaining too."

    play sound "assets/sfx/schoolbell.mp3"
    
    show kirei arm surprise with dissolve
    
    $ renpy.pause(2)

    k "Oh... wow, lunch is over?"

    mc "Time flies, right?"

    show kirei smile with dissolve

    k "I’ll see you later, [protag]. This was fun."

    "I’d best be heading back to my class."

    "Kirei and I both pack up our things before leaving the room."
    
    scene bg black
    with dissolve

    return