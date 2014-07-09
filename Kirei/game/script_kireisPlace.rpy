label kireisPlace:

    play ambience "assets/sfx/ParkAmbience.mp3" fadein 3
    scene bg park
    with dissolve

    "The park Kirei was talking about is Circle Park."
    "It's on the way back home."
    "On the way to a lot of things, actually."
    "Like the name implies, it's smack dab in the middle of town, and despite being called a \"park\", it's actually huge."
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
    # but tim hates it
    
    show bg black with dissolve
    
    "As we walk around for a while, she tells me more about herself."
    "About how her family came to town from a larger city."
    "The old schools she's been to and some other simple stories."
    stop ambience fadeout 3
    "If I'm being honest, I don't really hear much of what she's saying. Her voice is kinda mesmerizing in that cartoon princess sing-song kinda way."
    
    # Consider actually writing this stuff out    
    
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

    # fuck you black guy for saying i quoted this wrong. I looked it up and straight copypasta'd it.
    
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

    "I nod lightly to agree."
    
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

    mc "It’s probably about time I’d get home anyways."

    "Kirei slowly nods and smiles, standing up."
    "I’m pretty sure my math homework isn't gonna do itself."
    "I stand up and pick my backpack up from the floor."
    
    show kirei arm concern with dissolve

    k "Oh, [protag]?"
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
    return