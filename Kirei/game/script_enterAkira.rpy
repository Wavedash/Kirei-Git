label enterAkira:
    
    $ protag = "You"
    $ kirei = "???"
    $ tomo = "Tomo"
    
    play sound "assets/sfx/schoolbell.mp3"
    scene bg classroom
    with eyeopen
    play music "assets/music/HangingOut.mp3"
    $ renpy.pause(2.0)
    
    "The bell rings loudly in my ear."
    "Where am I?"
    "Oh."
    "I must’ve dozed off."
	"And I probably shouldn't have sat so close to the bell to take a nap."
    "I stretch."
    "Math has always been boring, but sometimes the teacher can just drone on forever."
    "What’s the point of giving a lecture on precalc, anyway?"
    
    "I let out an unintentionally loud yawn."
    "A stifled giggle floats from across the room."
    
    show tomo sass at left
    with dissolve
    
    "I'd recognize that laugh anywhere."
    
    show tomo hip happy with quickdissolve
    show tomo hip happy at center with ease
    show bg classroom grey
    with dissolve

    "Tomo. I’ve known her since we were freshmen." 
    "She’s been my friend since we started high school."
    "We don’t have much in common, but for some reason, we really click."
    "It's lucky for me. I don’t make friends well."
    "Lately, we’ve been spending a lot of time together."
    "More than usual since the beginning of our last semester."
    "Guess it all falls into place when your schedules are exactly the same."
    "As a matter of fact, we have the next class together, too."
    
    show kirei wrist happy at right with easeinright
    show tomo armdown empty with quickdissolve

    k "Hey, you!"

    show kirei smile at center with ease
    hide tomo with dissolve
    
    "My view is suddenly obstructed."

    "I look up and recognize her face but a name doesn’t immediately come to mind."

    "She’s one of the popular girls on campus. Definitely not on my level of social class." 
    "Why is she talking to me?"
    "She looks excited."

    show kirei concern at center with ease
    
    k "Hey, you okay there?"
    
    play sound "assets/sfx/thud.mp3"
    show kirei arm happy
    show bg classroom
    with vpunch

    "She drops her books on my desk to capture my attention."

    mc "Huh? Uh... yeah, I’m fine."

    k "Can I ask you a question?"
    
    show kirei happy with dissolve

    "She taps her fingers together and looks me in the eye."

    k "You’re into that paranormal stuff, right? "
    k "Like ghosts and zombies and all that?"

    "I nod slowly."
    "Last week, I brought one of my hunter magazines to class."
    "\"Hunter,\" as in ghost hunter."
    "It fell out of my bag in class and I've gotten hell for it ever since."
    "It’s not like I’m addicted to the stuff. I just...{w=.5} dabble."
    "But I suppose if someone like her wants to talk about it, I wouldn’t mind so much..."

    k "Oh, I can’t believe I’ve forgotten your name..."

    "I wonder if she knew it in the first place."
    
    show kirei smile with dissolve
    
    "She sighs and pokes her cheek."
    "Oh well. I didn’t expect her to know it anyway."

    # name entry junk
    
    $ protag = ""
    
    $ protag = renpy.input("It's...", "Akira", length=20)

    if not protag:
        $ protag = "Akira"
 
    if protag == "Akira":
        $ protagchan = "Aki"
    if protag != "Akira":
        $ protagchan = protag

    mc "It's [protag]."
    
    show kirei happy with dissolve

    k "Right! [protag]! I won’t forget it."

    mc "And you’re Kirei, right?"
    
    $ kirei = "Kirei"
    show kirei smile with dissolve

    "Yeah, that’s her name. Most everyone in school knows it."
    "She nods and reaches her hand out to me."
    "What is this girl even after? My vote for class president?"
    "No. That wouldn't make sense. We’ve only got a few months of school left."

    play sound "assets/sfx/heartbeat.mp3"
    
    "As I grab her hand to shake, she squeezes mine and giggles."
    
    show kirei happy with dissolve

    k "So... have you heard about the recent vampire sightings?"

    mc "Vampires, huh? Never really piqued my interest."

    "Of course, typical for a girl to be interested in vampires."
    "Probably some skewed fantasy of romance and drama."
    # "I’m sure she doesn’t actually know the gruesome details."
    "But of course I’ve heard about the sightings."

    mc "But I did see something about it. Last night I was on the Inter{nw}" # {nw} makes the game move to the next line of text right away without waiting.
    mc "Er... The news. I saw it on the news."

    "Smooth, [protag]. Just show her how much of a dork you are. Blog? Really?"

    mc "They were talking about how there had been strange sightings in the area before the murders."
    mc "Bats, and strange shadows. Shady figures and pale skin."
    mc "And the victims..."
    
    show kirei arm happy with dissolve

    k "Isn’t that just fascinating?"

    mc "Er..."

    "Who is this girl again?"
    "\"Little miss popular\" Kirei? \"Loved and adored by the entire student body\" Kirei?"
    "I guess even the normal ones have their dark secrets. "
    "And I guess it’s pretty cool that it’s coming from Kirei."
    "Most girls like her would never give me the time of day."
    
    k "Do you wanna hang out with me after class today? I’ve got something I’d like to show you."

    "Show me what?"
    "Is this even happening right now?"
    "I’ve seen her around almost all year, but..."
    "She’s actually talking to me."

    mc "I’ve got nothing else to do today."
    
    "Goddammit. Should have gone with, \"Oh. I'd love to, Kirei\". What is wrong with me?"
    
    show kirei smile with dissolve

    k "Great. Text me after school lets out?"

    "She grins softly and slides me a sheet of paper."
    "A phone number."

    mc "Sure thing."

    "I fold the paper."

    stop music fadeout 1
    hide kirei with dissolve
    $ renpy.pause(1)
    play music "assets/music/FriendsForever.mp3"
    show tomo worry with dissolve

    t "So what was that about, [protagchan]?" # The variable that stores his nickname. It’s the same as {protag} if the player uses a custom name, but "Aki" if they use the default.

    "I stand up to meet Tomo and sling my backpack around my shoulder, as we both walk out of the classroom on our way to the next period."
    
    play ambience "assets/sfx/hallway.mp3" fadein 3
    
    scene black
    with dissolve
    
    scene bg hallway
    show tomo worry
    with dissolve

    mc "You know that girl Kirei?"
    
    stop ambience fadeout 15

    show tomo hip happy with dissolve

    t "What would Little Miss Popular want with you?"

    mc "Hey!"

    "I nudge Tomo with my elbow."

    mc "What {i}wouldn’t{/i} a pretty girl like that want with me?"

    t "..."

    mc "..."
    
    show tomo sass
    
    t "Nice try. But really, what's the story?"
    
    mc "No idea. But she gave me her phone number."

    $ showphone_right()
    
    "I smile as I type it into my phone contacts."
    
    $ hidephone()
    
    show tomo armdown quizzical with dissolve
    
    t "I don’t know about this, [protagchan]."

    mc "What’s not to get? A girl gave me her phone number."
    
    t "Isn’t that a little...{w=.5} y’know,{w=.5} odd?" # pauses the text for a moment.

    "I’d take offense to that if she wasn’t entirely right."
    "But who knows? It could be my lucky day."

    t "I mean..."

    t "Yeah, she seems nice... but what do you think she’s after?"

    mc "She said she’s interested in the recent vampire sightings."
    mc "Unlike {i}some{/i} people I know..."

    show tomo worry with dissolve
    
    "Tomo sighs."
    
    mc "I don't really know much about vampires, but they seem interesting enough."
    mc "It's not like I've never seen a vampire movie. I just don't spend my free time reading about them."
    mc "If someone like that's interested, though, I may as well take a look, right?"

    t "Just{w=.5} watch your back, okay? What if {i}she’s{/i} a vampire?"

    mc "Sure. And I'm the pope."
    
    t "Hey now, you never know."
    t "She's only been here for a year. How do you think she could she have become so popular so fast?"
    
    mc "By not having a super-abrasive personality?"
    
    t "Hey!"

    show tomo happy with dissolve
    
    "Tomo giggles a bit."
    
    mc "Hell, if I ever met a vampire that pretty, maybe I wouldn’t mind her taking a bite out of me."
    
    show tomo glare with dissolve

    "Another sigh."

    t "Typical."

    "I smirk."
    "Tomo hates it when I talk about girls."

    t "Do you even know what it's like to be bitten?"

    mc "I haven’t met a vampire, so no."
    
    show tomo concern with dissolve

    t "I meant in general, dummy."

    mc "Still a 'no'. Why, do you want to bite me?"

    show tomo happy with dissolve

    t "Don’t tempt me."

    t "So, I’m guessing we’re not hanging out after class today?"

    mc "I’m not sure."

    show tomo worry with dissolve

    mc "I mean, Kirei just gave me her number."

    mc "Maybe it won’t be such a big deal, though."

    mc "I’ll see what she wants, and then call you to let you know if I’m free."

    t "..."

    "She doesn’t look too thrilled."

    mc "Hey now, we’ll hang out tomorrow."
    mc "Promise."
    
    show tomo happy with dissolve

    t "We’d better."

    stop music fadeout 1
    scene black with dissolve
    
    $ renpy.pause(1)
    play music "assets/music/HangingOut.mp3" fadein 0.5
    scene bg classroom with dissolve

    "Ah. there we are."

    $ showphone()

    "I scroll through my contacts."
    
    "I’ll just send Kirei a text."

    "It doesn’t take long to find her number. I only have four people in my phone."

    # grab blocky font for texting and apply it to this conversation.

    mcPhone "hey where do you want to meet"
    
    $ hidephone()

    "I pack up my belongings."

    "Suddenly, I’m feeling a bit of panic."

    "What if this is all some sort of sick joke?"
    "What if she{nw}"

    $ ringphone()
    $ showphone()

    kPhone "Meet you at the park entrance." # trying to think of a way to make life easier for Tim. Generic street vs outside the school.
    
    $ hidephone()

    "Well, I guess I’ve already dug myself a hole."

    "My reputation can’t possibly get any worse."

    "Despite what Tomo had to say,{w=.5} I’m going along with this."
    
    stop music fadeout 1
    
    scene black with dissolve
    
    $ renpy.pause(1)
    
    return