label sleepyMorning:

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

    return