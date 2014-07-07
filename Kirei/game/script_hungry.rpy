label hungry:

    $ kirei = "???"
        
    play ambience "assets/music/PrologueEpilogue.mp3" fadein 4
    
    k "Are you feeling alright?"
    
    $ renpy.pause(1)
    
    k "[protag]..."
    
    k "Wake up..."

    "Man. I can't move."
    
    "There’s something on top of me."

    "Someone..."

    mc "Kirei?"

    play sound "assets/sfx/cackle.mp3"
    
    "A laugh."

    "My neck feels wet..."

    "And my back feels drenched."
    
    $ heartbeat()

    "My heart’s pumping so fast."

    "And it’s cold.{w=.5} I feel so cold."

    "I need to open my eyes."
    
    play music "assets/music/Hungry.mp3" fadein 4

    with dissolve
    scene bg kireiCG:
        pos (0.0, getY(-265))
        linear 10 pos (0.0, 0.0)
    with dissolve

    $ kirei = "Kirei?!"
    
    k "Oh, wonderful! You’re still with me!"
    
    mc "Kirei? Is that..?"

    "She's covered in blood!"
    
    $ heartbeat()

    "A shot of pain courses through my body as she brings a hand to my neck."

    "She brings her hand back up in front of my face."
    
    $ double_vision_on("bg kireiCG")

    "It’s stained a dark red."

    k "You're surprisingly concious right now."
    
    k "I won't act like I'm not impressed. You've lost a lot of blood, after all."
    
    $ double_vision_off()

    "I’m bleeding?"

    "She... she bit me!"

    "And I'm gonna die."

    "Oh my god, I'm gonna die!"

    "Please... please, no."

    "Not like this..."
    
    $ kirei = "Kirei"

    k "What's the matter, [protagchan]?"
    
    k "That's an awful mark on your neck."
    
    mc "You..."
    
    k "Shall I kiss it and make it better?"
    
    show bg BGkireiCG with dissolve
    
    play sound "assets/sfx/spiritbreath.mp3"
    play sound2 "assets/sfx/heartbeat.mp3"
    
    show bg black
    with dissolve
    
    "Kirei puts her mouth on my neck and drinks gently."
    
    show bg BGkireiCG with dissolve
    
    play sound2 "assets/sfx/heartbeat.mp3"
   
    scene bg kireiCG:
        linear 0 pos (0.0,0.0)
    with dissolve
    
    $ double_vision_on("bg kireiCG")
    
    k "Mmm..."

    "I feel..."

    k "Oh, my poor [protagchan]."

    k "You’re such a damn fool."
    
    $ double_vision_off()
    
    k "But at least you found your vampire. You can take comfort in knowing that you're not crazy."

    mc "You...{w=.5} the shadow..."
    
    k "Hm..?"
    
    "She was tricking me..."
    "Just not how I expected..."
    
    k "You're so easy to manipulate."

    k "Like putty."

    k "And you fell for it."
    
    $ heartbeat()

    $ double_vision_on("bg kireiCG")
    
    "Vampires..."

    "I never expected to be right..."
    
    mc "What about...{w=.5} you said before...{w=.5} about a person's soul..."
    
    $ double_vision_off()
    
    play sound "assets/sfx/cackle.mp3"
    
    k "A soul.{w=.5} HA!"
    k "Lot of good that did you."
    k "What's so special about a damn soul?"
    
    "No..."
    
    mc "But you said..."
    mc "Do you even have a..."
    
    $ heartbeat()
    show bg kireiCG:
        pos (0.0, 0.0)
        linear 1 pos (0.0, getY(-265))
    with None
    show black
    with dissolve
    
    $ renpy.pause(3)
   
    k "Do I have a soul? Of course I do."
    k "At least I think I do..."
    
    play sound2 "assets/sfx/heartbeat.mp3"
    
    "She grabs my hair and pulls my head up."
    
    scene bg kireiCG:
        pos (0.0, getY(-265))
        linear 3 pos (0.0, 0.0)
    with dissolve
    
    k "But when you look at it from my point of view..."
    k "It's just so much more fun to give in."

    k "Human feelings? Vampire instinct?"
    play sound2 "assets/sfx/heartbeat.mp3"
    k "What’s the difference?"
    k "We’re all just acting on our desires...{w=.5} for our own selfish reasons."
    k "It’s nothing personal, [protagchan]."
    k "I've only been like this for a year or so."
    k "I thought maybe you'd know something about vampires that would be useful."
    k "We don't exactly have instructional meetings, you know."
    k "I thought maybe you'd be a bit of fun."
    play sound2 "assets/sfx/heartbeat.mp3"

    "She shrugs."

    k "I guess not."
    
    $ double_vision_on("bg kireiCG")
    
    k "You’re just like everyone else."
    
    k "Completely useless."
        
    play ambience2 "assets/sfx/heartbeat.mp3"
    
    k "Well..."
    k "Not entirely useless..."
    
    "She puts her hand to her face and inhales."
    
    k "Ah..."
    k "Blood tastes so much sweeter when accompanied by fear."

    "I... I can’t move."
    "I can’t get her off me."
    
    k "And so, my [protagchan], I'm going to tell you something."
    
    k "I'm going to kill you."
    k "But then, I think I'll snack on your friend, too."
    
    "Tomo!"
    
    mc "No...{w=.5} Please..."
    
    "I can feel my back getting wetter and wetter with my blood."
    "This is how it ends?"
    
    "I'm sorry, Tomo..."
    
    show black with dissolve
    hide black with dissolve

    k "Oh, and [protag]?"
    k "Can I ask you a question?"
    
    show black with dissolve
    $ renpy.pause(1)
    hide black with dissolve
    
    k "Just one last exchange before you have to go?"
    k "Why did you decide to spend time with me in the first place?"

    "Wh-what?"

    k "Is it because you think I’m pretty?"
    k "I heard you talking to that brat."
    k "You said you wouldn’t mind me taking a bite out of you..."
    k "If I were pretty enough."
    
    $ double_vision_off()
    
    stop music fadeout 3
    
    k "[protagchan].{w=.5}.{w=.5}.{w=.5}.{w=.5}.{w=.5}.{w=.5}. {w=2} am I pretty enough for you?"
    
    scene bg black
    
    play vocal "assets/sfx/finalbite.mp3"
    play sound "assets/sfx/cackle.mp3"
    #play sound2 "assets/sfx/spiritbreath.mp3"
    stop ambience2
    stop ambience fadeout 3
    
    $ renpy.pause(5)
    
    return