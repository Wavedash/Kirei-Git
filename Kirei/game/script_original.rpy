# The original game starts here.

label originalVersion:
    
    # Just a little jump scare to start your day.
    
    play sound "assets/sfx/ohdearscare.mp3"
    
    # Myth always masters his music at a volume that's super loud in Ren'Py.
    # The easiest way to fix that is to set the music channel to a level
    # based on a fraction of the music volume slider in the options menu.
    
    $ renpy.music.set_volume(0.4, 0, channel="music")
    
    #Prologue ---------------------------------------------------------------
    
    stop music fadeout 4
    show bg mainmenu
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

    # Title Sequence ---------------------------------------------------------------
    
    if config.developer == False:
        $ overriding_on = True
    
    $ renpy.pause(2.0)
    
    show text "{font=assets/engine/AndBasR.ttf}rosin entertainment\npresents{/font}" with dissolve
    
    $ renpy.pause(3.0)
    
    hide text with dissolve
    
    show text "{font=assets/engine/AndBasR.ttf}a\nnanoreno 2014\nlast minute challenge{/font}" with dissolve
    
    $ renpy.pause(3.0)
    
    hide text with dissolve
    
    $ renpy.pause(1.5)
    
    $ renpy.pause(0.5)

    show title at truecenter with dissolve
    
    $ renpy.pause(3.0)
    
    hide title with dissolve
    
    stop ambience2 fadeout 3
    
    $ renpy.pause(5.0)
    
    if config.developer == False:
        $ overriding_on = False
        $ renpy.block_rollback()
    
    # Enter Akira ---------------------------------------------------------------
    
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

    "Tomo. I’ve known her since we were freshman." 
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

    mc "I read it on a blog{nw}" # {nw} makes the game move to the next line of text right away without waiting.
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

    mc "You know that girl, Kirei?"
    
    stop ambience fadeout 15

    show tomo hip happy with dissolve

    t "What would Little Miss Popular want with you?"

    mc "Hey!"

    "I nudge Tomo with my elbow."

    mc "What {i}wouldn’t{/i} a pretty girl like that want with me?"

    t "..."

    mc "..."
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

    "I’ll just send Kirei a text."

    "I scroll through my contacts."

    "It doesn’t take long. I only have four people in my phone."

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
    
    # Kirei's Place ---------------------------------------------------------------
    
    play ambience "assets/sfx/ParkAmbience.mp3" fadein 3
    scene bg park
    with dissolve

    "The park Kirei was talking about is Circle Park."
    "It's on the way back home."
    "On the way to a lot of things, actually."
    "Like the name implies, it's smack in the middle of town, and despite being called a \"park\", it's actually huge."
    "A forested area with a ton of hiking trails and some clearings here and there where the park \"features\" are."
    "But if you want to get across town on foot, the fastest way from point A to point B is through park C."

    "I used to play here as a kid, but now I just pass through it on my way to school."
    "Kirei's waiting for me at the gate."

    show kirei arm happy with dissolve

    "She waves and walks to meet me."

    k "Hello, [protag]!"
    k "Thanks for meeting up with me."

    mc "Uh, hi."
    mc "It's no trouble."

    "I look around. I'm still expecting the hidden camera crew to jump out at any moment."

    show kirei smile with dissolve

    k "Well then...{w=.5} shall we?"

    "I nod and stand up and walk by her side."
    "So far, so good."
    "She hasn’t shown signs of cold feet."
    "And it doesn’t look like I’m gonna get tarred or feathered."
    "I’m walking home with one of the most popular girls in school."
    "And she’s actually talking to me."

    # we should add more here. make use of that background.
    
    show bg black with dissolve
    
    "We walk around for a while."
    "She tells me about how her family came to town from a larger city."
    stop ambience fadeout 3
    "If I'm being honest, I don't really hear much of what she's saying. Her voice is kinda mesmerizing in that cartoon princess sing-song kinda way."
    
    k "And I’m fortunate enough for my parents to be paying rent."

    "I can’t believe she invited me over."
    show kirei arm worry with dissolve

    k "I’m sorry if my place is a mess. I’ve just been very busy lately."

    "She fiddles with her keys as she pushes the door open with her body."
    
    play music "assets/music/LeaningIn.mp3"
    
    show bg apartment
    hide kirei
    with dissolve

    "Her apartment isn’t even dirty."
    "Well, at least not compared to my room." 
    "Quiet colored walls."
    "Basic furnishings."

    show kirei arm happy at offscreenleft

    "A spot of trash here and there, but otherwise, immaculate."

    k "Make yourself at home. Need anything to drink?"

    mc "No thanks."

    show kirei arm surprise

    k "Are you sure?"

    "Kirei walks over to her fridge and opens it, revealing a wonderful array of drinks and food."
    "I raise my hand to decline, but..."
    "Wow."
    "She’s really lucky if she gets to live on her own like this."
    "I’d have to wait until college before I get to live by myself."
    
    show kirei happy at center with dissolve
    
    "She takes a juice for herself and crashes onto her couch in the corner of the room."

    mc "And your parents pay for all of this?"

    k "They have been for the past year now."

    mc "Doesn’t it get lonely?"

    show kirei arm worry with dissolve

    k "Kinda. But that’s why I appreciate having company over."
    k "And my parents do visit on occasion."
    k "But they’re currently out of the country on a business trip."

    "Business trip?"
    "I look at the view of the town from the window."
    "This is a really nice apartment."
    "Her parents must be rich."

    show kirei happy with dissolve

    k "So... since you’re the expert here... What do you know about vampires?"

    "Expert? Me?"

    mc "They uh, drink blood, right?"

    "I move closer to the couch and sit down next to her, setting my backpack near my feet."

    show kirei smile with dissolve

    k "Come on, [protag]. Even I knew that."

    "What does she want to hear?"
    "A Transylvanian accent?"

    mc "They’re super strong and cunning."
    mc "Sharp teeth."
    mc "A weakness to garlic and silver..."
    mc "...and a common practice of killing them was driving a stake through their heart."

    k "Whoa."
    
    "Kirei almost has this strange smile on her face."
    "Tomo was never really interested in the violent details."
    "I’m actually a bit excited I’ve got someone to talk to about this stuff."

    show kirei arm happy with dissolve

    k "Oh, right. I’ve got something to show you."

    "Kirei flips through an open book on top of her coffee table."

    k "It says here, 'Humans unwittingly interact with vampires on a daily basis.'"

    mc "Hiding in plain sight is a classic vampire M.O..."

    show kirei arm concern with dissolve

    k "The finest trick of the devil is to persuade you he doesn’t exist."
    k "So... you could be friends with a vampire, and you wouldn’t even know it!"

    "I shake my head."

    mc "Pff... doubt it. I don’t have too many friends to begin with."

    show kirei wrist smile with dissolve

    "Kirei stifles a laugh."

    mc "Why would a vampire want to be friends with a human anyway?"
    mc "We’re so boring."

    "We’re not as strong or as fast as them."
    "Wouldn’t it make sense for them to just be after our blood?"

    show kirei arm worry with dissolve

    "Kirei shrugs and tilts her head."

    k "Vampires are people too, right?"
    k "I’d be lonely too if I had to kill a quarter of the people I’ve met."

    mc "When you put it that way, I guess a vampire would need a support group."
    mc "Talk about Hemoholics Anonymous."
    mc "Hello, my name is Dracula, and I’m a hemoholic."

    "Kirei looks at me, confused."
    "Oh man, that was stupid."

    show kirei wrist happy with dissolve

    k "..."

    show kirei wrist smile with dissolve

    "Kirei giggles softly."
    "Hopefully that wasn’t a pity laugh."
    "My self-confidence is already shot as it is."

    mc "Do you think humans would consciously befriend vampires?"

    show kirei concern with dissolve

    k "You’d think the answer would be no."

    mc "It’s not?"

    k "No, I meant, having a vampire friend could have its perks."
    k "It’s like being friends with a superhero, or a police officer."

    mc "Except superheroes and police officers wouldn’t suck your blood."

    show kirei smile with dissolve

    k "Neither would a good friend, right?"

    mc "Not if they were the two last living things on Earth."

    "People do extraordinary things in extraordinary circumstances."
    "And I don’t think I’d put friendship in front of survival."
    "Then again, like I said... {w=.5} I don’t have too many friends to begin with."

    show kirei concern with dissolve

    k "Well... better to have them as a friend than an enemy, I suppose."

    "..."

    hide kirei with dissolve

    "Kirei pulls out a short stack of newspapers and magazines."

    scene black with dissolve
    
    $ renpy.pause(1)
    
    scene bg apartment evening with dissolve

    "I spent the majority of the early afternoon reading what she had to offer."
    "Historic occurrences of vampirism."
    "A tuft of police and medical reports describing incidents of mutilated victims."
    "And of course the good handfuls of phony magazine articles."
    "‘Vampire Wins Local Chess Tournament by Mind Reading.’"
    "Credible or not, I still had a pretty good time."

    show kirei arm happy with dissolve

    "Kirei yawns and stretches."

    k "Wow... it’s getting pretty late."

    mc "Is that my cue to leave?"

    show kirei arm worry with dissolve

    k "Oh, no, you don’t have to."

    "I check my watch."

    mc "It’s probably about time I’d get home."

    "I’m pretty sure math homework isn't gonna do itself."
    "I stand up and pick my backpack up from the floor."

    show kirei arm concern with dissolve

    k "Oh, and [protag]?"
    k "Can I ask you a question?"
    k "Just one last exchange before you have to go?"

    "I turn around to hear her out."

    mc "Yeah, what is it?"

    show kirei arm worry with dissolve

    k "Why did you decide to come with me today?"

    mc "What kind of question is that?"

    k "Is it because you think I’m pretty or popular?"
    k "Because you didn’t think I’d be into these sorts of things?"

    "Of course she’s super pretty and popular."
    "But... that can’t be the only reason, right?"
    "Think, [protag]..."

    mc "N-no... it’s not that."
    mc "I don’t have too many people to talk to about this stuff."
    mc "Hell, I don’t have too many people to talk to at all."

    show kirei concern with dissolve

    k "It’s just..."
    k "A lot of people know who I am..."
    k "But you’re the one of few who has actually taken the time to get to know me."

    "You’d think a girl as popular as her would have tons of friends."
    "Turns out she’s just as lonely as the rest of us."

    show kirei smile with dissolve

    "Kirei looks at me and smiles."

    k "So, thank you [protag]."
    k "I’ll see you out."

    "Kirei stands up and follows behind me."

    k "I’ll see you tomorrow, [protag]. Stay safe."
    
    stop music fadeout 3
    scene black with dissolve
    
    # Phantom Shadows ---------------------------------------------------------------
    
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
    
    # Sleepy Morning ---------------------------------------------------------------
    
    play sound "assets/sfx/schoolbell.mp3"
    $ renpy.pause(2)
    
    scene bg hallway
    with dissolve
    
    play ambience "assets/sfx/hallway.mp3" fadein 1
    play music "assets/music/HangingOut.mp3"
    
    mc "Uuuuungh."
    
    stop ambience fadeout 15

    "Only a couple more months before I don’t have to come back here."

    "I walk up the stairs and through the open door."

    "I didn’t recognize her from behind but I pass by Kirei."

    show kirei happy with dissolve

    "She spots me."

    show kirei smile

    k "Oh, good morning [protag]! How are you doing today?"

    "She’s awfully chipper."

    mc "Can’t complain. Couldn’t sleep much last night, but that’s nothing special."

    "I yawn to cement my point."

    k "What are you doing for lunch today?"

    mc "Not much, I guess."

    k "Would you like to have lunch with me? We could read up on more vampire things if you’d like."

    k "I found a couple new books in the school library this morning."

    "The library? Does anyone even go there anymore?"

    mc "Well, I guess it’s bound to have something I haven’t seen before."

    show kirei wrist smile with dissolve

    k "I sincerely doubt it."

    "I shoot her a sour look."

    "She playfully taps me on the head."

    show kirei happy with dissolve

    k "But how about it?"

    "I shrug."

    "Can’t hurt, could it?"

    "I might learn something new."

    mc "Sure."

    show kirei smile

    k "Great! I usually have lunch in Ms. Koh's classroom."
    k "It's nice and quiet. Perfect for reading."
    
    mc "Alright."
    
    k "I’ll see you then!"

    hide kirei with dissolve

    "Kirei smiles and walks off to her class."

    play sound "assets/sfx/schoolbell.mp3"
    $ renpy.pause(2)

    "Speaking of class..."
    
    scene bg classroom
    show tomo chestnut at left
    with dissolve

    "I enter the room and spot Tomo."
    "She waves lazily."
    "I take my seat next to her."

    t "Morning."

    mc "You look tired."

    show tomo concern

    t "Hardly got any sleep last night."
    t "Felt like I was running around everywhere."

    mc "Looks like the sleepiness is contagious."

    "The teacher sets his bag down at the front desk and lecture begins."

    $ ellipses()

    "I’m definitely not in the mood to hear about evolution right now."
    "I seriously can’t wait to graduate and be done with this place."

    show tomo sass with dissolve

    "Tomo can read the apathy on my face."
    "Hopefully the teacher can’t."
    "I look up at him quickly."
    "He’s got his back to the class and is writing on the board."
    "Now would be a perfect time for a nap."
    
    $ renpy.music.set_volume(0.0, 2, channel="music")
    
    scene black with dissolve

    $ renpy.pause(1)

    "So dark."

    $ renpy.pause(1)

    "The surface of the desk chills my face."

    "Why does the teacher have to talk so loud?"
    
    # Sunblock ---------------------------------------------------------------
    
    $ renpy.music.set_volume(0.4, 2, channel="music")
    
    scene bg classroom
    show tomo concern at left
    with eyeopen

    "This isn’t working."

    "I lean over to Tomo."
    
    mc "Is class almost over yet?"
    
    show tomo glare with dissolve

    t "Not yet, but we’re doing group work."

    "Oops."

    t "Pull your weight, you bum."

    "I smirk at her and sit up straight in my desk."

    mc "So... what do you know about vampires?"

    show tomo hip mad with dissolve

    "Tomo scoffs and shakes her head."

    t "I know they’re not real."

    mc "You don’t know that for sure."

    show tomo hip quizzical with dissolve

    t "Why are you asking me?"

    t "Aren’t you the vampire expert?"

    "Since when did I become an expert?"

    mc "I’m just wondering what you know."

    show tomo sass with dissolve

    t "Are you trying to impress Kirei with some brand new facts?"

    "I shake my head."

    "She smirks and puts down her pencil."

    "As if Tomo would know something that I won’t know."

    show tomo hip happy with dissolve

    t "Aren’t they allergic to garlic salt or something?"

    mc "Garlic, yeah. There's plenty of sources for vampire lore though. Some legends don't mention garlic. Sometimes they can turn into bats. Some stories include some weird rules about running water."
    mc "But there are a few common themes in all the legends."
    mc "They drink blood and can't go out into sunlight."

    show tomo glare with dissolve

    t "Sunlight? I know that's one of the legends, but come on. There's no way sunlight would take out a vampire."

    mc "How do you mean?"
    
    t "You'd think after thousands of years and modern technology they'd figure out ways around something as simple as sunlight, wouldn't you?"
    
    mc "Like?"

    show tomo happy with dissolve

    t "Sunblock.{w=.5} Duh."

    "Is she even serious right now?"

    mc "Would that even work?"

    show tomo armdown happy with dissolve

    t "How should I know?"
        
    "She taps me on the forehead."
    
    t "They're not real."

    "Tomo and I share a quiet laugh."

    mc "Well you brought it up."
    
    t "Well think about it. What are they supposed to do? Stay inside all day with the curtains drawn?"

    "I shrug my shoulders."

    show tomo chestnut with dissolve

    t "Like, how do they get their groceries?"
    t "It’s not like there are too many places that are open at night."

    mc "Do vampires even eat regular food?"
    mc "I mean, they're undead right?"
    
    t "What does that even mean? Undead?"
    t "It's dumb. You can't be alive and dead."
    t "I’m sure they’d need their other vitamins and minerals."
    t "And their proteins and fats."

    show tomo sass with dissolve

    t "Just not the garlic flavored kind."

    "Poor vampires."
    "They’re missing out."
    
    show tomo hip happy with dissolve

    t "Did Kirei manage to teach you anything new?"

    mc "Nothing that I couldn’t have figured out on my own."

    show tomo sass with dissolve

    t "Yeah, I’m sure you already know all there is to know."
    t "You probably spent all of last night researching vampires."

    "I nod admittingly."
    "She’s almost right."
    "I was thinking about that shadow."

    show tomo hip quizzical with dissolve

    t "So your excuses suck. You don’t deserve to be sleepy."

    mc "I told you about that shadow, right?"

    mc "I had to figure out what that was."

    show tomo glare with dissolve

    t "Doesn’t matter. You spent the whole night on the internet!"

    t "Slacker."

    mc "And what are your reasons?"

    show tomo sad with dissolve

    t "I... had a bad dream."

    "How is that excuse any better than mine?"

    mc "Aww, poor baby."

    "I put on my most insincere sympathy face."

    mc "What was it about?"

    show tomo worry with dissolve

    t "I can hardly remember."
    t "It felt like something was chasing me, but I was chasing something."

    mc "So you were running a marathon?"

    show tomo happy with dissolve

    t "I was definitely running, that’s for sure."
    t "But where I was going, I have no idea."

    "Talking about running brings back bad memories of P.E. class."

    "Yeesh."

    show tomo armdown quizzical with dissolve

    t "So Kirei actually let you in her apartment?"

    mc "Yeah, believe it or not."

    mc "It was actually a pretty impressive place."

    show tomo glare with dissolve

    t "I’ve known you for longer, and I don’t think I’m letting you anywhere near my house."

    t "Weirdo."

    "Tomo sticks a tongue out at me."

    show tomo chestnut with dissolve

    mc "She actually had a lot of things to share."
    mc "Books I haven’t seen before."
    mc "And these crazy photos and reports."
    mc "Awesome stuff."

    show tomo sass with dissolve

    t "What are you, in love with her?"

    mc "You're just hilarious."

    mc "We’re actually getting lunch together. Wanna join us?"

    show tomo armdown empty with dissolve

    t "I... I don’t know. I’ve got other things to do."

    "She looks away nervously."

    mc "Like what?"

    t "Y’know... stuff."

    "I’ve known her long enough to know that she’s lying to me."

    mc "Is this about Kirei?"

    show tomo worry with dissolve

    "Tomo looks down."

    mc "You know, if you got to know her, you might actually like her."

    t "I don’t hate her..."
    t "It’s just..."

    "Tomo lets out a frustrated sigh."

    show tomo concern with dissolve

    t "What do you think she’s after?"

    "I shrug."

    "Some excitement?"

    "A break from the normal world."

    mc "Maybe she’s actually interested in the stuff."

    mc "Certainly seemed like it yesterday."

    show tomo mad with dissolve

    t "And how exactly did yesterday go?"

    mc "We had a good time talking about vampires. I told you this."

    t "Are you sure she’s just not playing you?"

    mc "I had my suspicions at first... but really?"
    mc "You honestly think I’m {i}that{/i} gullible?"

    show tomo glare with dissolve

    t "Last I checked, you’re gullible enough to believe in all of this supernatural crap."

    mc "I don’t believe in them."

    t "Then why do you keep spending time with Kirei?"

    mc "Is it wrong to have an interest in vampires?"

    mc "Come on, you should know me better."

    show tomo hip mad with dissolve
    
    "Tomo opens her mouth like she's going to say something, but stops."

    stop music fadeout 2
    
    show tomo glare with dissolve

    t "I don’t want to hear anything more about vampires."
    t "You know I hate that supernatural garbage."
    t "It makes me sick."
    
    hide tomo with dissolve
    
    "She stands up and moves to another table."

    $ renpy.pause(1)
    
    scene bg black with dissolve

    "Tomo stayed relatively quiet for the rest of classes."
    "If I had to talk to her, I stayed away from the topics of Kirei or monsters."
    
    # Interview With... ---------------------------------------------------------------
    
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
    
    # External Stimuli ---------------------------------------------------------------
    
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
    
    "The final bell."
    "Finally."
    
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
    show tomo armdown yandere with dissolve

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
    
    # Cycle ---------------------------------------------------------------
    
    play music "assets/music/LeaningIn.mp3"
    show bg apartment
    with dissolve

    mc "So why are we headed to the park?"

    show kirei arm concern with dissolve

    k "I heard a rumor of a vampire attack there last night."

    mc "Wouldn’t the police be all over the place?"

    k "Vampires don’t tend to leave messes behind."

    mc "And you think we’re gonna be able to find some clues?"

    show kirei arm surprise with dissolve

    k "It’s worth a shot, right?"

    mc "Sure. We should head out right now."

    show kirei concern with dissolve

    k "Let’s not."

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
    
    # Hungry ---------------------------------------------------------------
    
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
    
    # Credits 1 ---------------------------------------------------------------
    
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
    
    # Prey ---------------------------------------------------------------
    
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
    
    # Credits 2 ---------------------------------------------------------------

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
    