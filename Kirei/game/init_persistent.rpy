# Initializes persistent variables if they are not set.

init -999 python:
    if persistent.config is None:
        persistent.config = dict()
    
    def config_default(key, val):
        if key not in persistent.config.keys():
            persistent.config[key] = val
        return
 
# Workaround for Ren'Py's awful fraction-based image display 
    def getX(val):
        calc = val / 1280.0
        return calc
    
    def getY(val):
        calc = val / 720.0
        return calc
    
    # Displays the character portrait. If false, sets as two-window with name tag.
    config_default("show_portrait", True) 
    
init python:

# Phone call stuff
    
    def ringphone():
        renpy.music.play("assets/sfx/phone.mp3", channel='sound', loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)
        renpy.pause(1)
        
    def showphone_right():
        renpy.music.play("assets/sfx/phoneFlip.mp3", channel='sound', loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)
        renpy.show("phone", at_list=[right], tag="phoneOverlay")
        renpy.with_statement(easeinbottom)
        renpy.music.play("assets/sfx/phoneBeeps.mp3", channel='sound2', loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)
        
    def showphone():
        renpy.music.play("assets/sfx/phoneFlip.mp3", channel='sound', loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)
        renpy.show("phone", at_list=[center], tag="phoneOverlay")
        renpy.with_statement(easeinbottom)
        renpy.music.play("assets/sfx/phoneBeeps.mp3", channel='sound2', loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)
        
    def showphone_night():
        renpy.music.play("assets/sfx/phoneFlip.mp3", channel='sound', loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)
        renpy.show("phone night", at_list=[center], tag="phoneOverlay")
        renpy.with_statement(easeinbottom)
        renpy.music.play("assets/sfx/phoneBeeps.mp3", channel='sound2', loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)
        
    def hidephone():
        # renpy.music.play("assets/sfx/phoneFlip.mp3", channel='sound', loop=None, fadeout=None, synchro_start=False, fadein=0, tight=None, if_changed=False)
        renpy.hide("phoneOverlay")
        renpy.with_statement(easeoutbottom)
        
# VFX

    def heartbeat():
        renpy.music.play("assets/sfx/heartbeat.mp3", channel="sound", loop=None, fadeout=None, synchro_start=False, fadein=0, tight=False, if_changed=False)
        renpy.show("heartbeat")
        renpy.with_statement(None)
        renpy.hide("heartbeat")
        renpy.with_statement(dissolve)
        
# window

    def ellipses():
        narrator(".{w=.5}.{w=.5}.{w=.5}{nw}")

init:

# Positions

    $ floatctc = Position(xanchor='center', yanchor='center', xpos=0.95, ypos=0.9)

# Transitions

    $ quickdissolve = Dissolve(0.12)
    $ longdissolve = Dissolve(3)

# Drunk-O-Vision (TM)

    transform transpa:

        alpha 0.5

    python hide:

        def gen_randmotion(count, dist, delay):

            import random

            args = [ ]

            for i in range(0, count):
                args.append(anim.State(i, None,
                                       Position(xpos=random.randrange(-dist, dist),
                                                ypos=random.randrange(-dist, dist),
                                                xanchor='left',
                                                yanchor='top',
                                                )))

            for i in range(0, count):
                for j in range(0, count):

                    if i == j:
                        continue

                    args.append(anim.Edge(i, delay, j, MoveTransition(delay)))

            return anim.SMAnimation(0, *args)

        store.randmotion = gen_randmotion(5, 10, 1.0)


init python:

    def double_vision_on(picture):

        # renpy.scene()

        renpy.show(picture)

        renpy.show(picture, at_list=[transpa,randmotion], tag="blur_image")

        renpy.with_statement(dissolve)


    def double_vision_off():

        renpy.hide("blur_image")

        renpy.with_statement(dissolve)
        
    def double_vision_off_instant():

        renpy.hide("blur_image")

        renpy.with_statement(None)
        
    def shadow_vision_on(picture): # It's like the doublevision, but it's just one image kinda moving around a bit

        # renpy.scene()

        renpy.show(picture, at_list=[transpa,randmotion], tag="blur_image")
        renpy.with_statement(dissolve)
        
    def night_vision_on(picture):

        renpy.show(picture, at_list=[transpa, center], tag="blur_image")
        renpy.with_statement(longdissolve)
         
    def ctc_float_on():
        renpy.show("ctc_default", at_list=[floatctc], tag="ctc_float")
        renpy.with_statement(dissolve)
        
    def ctc_float_off():
        renpy.hide("ctc_float")
        renpy.with_statement(None)
        
init python:
    credits = ('sprites', 'cartelet'), ('scenario', 'optimistic'), ('music', 'senator myth'), ('backgrounds | additional art', 'timbaer'), ('scenario | programming | ui', 'wavedash')
    creditsVoice = ('kirei', 'madamvicious'), ('tomo', 'wavedash')
    creditsThanks = ('programming support', 'fork~less anon'), ('support', 'jekoh'), ('pipeline support', 'jeremy miller'), ('engine', 'pytom'), ('home of nanoreno', 'lemma soft forums'), ('support', 'zap apple project')
    credits_s = "{size=100}{font=assets/engine/Rujis.ttf} project staff{size=40}\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "{size=20}{font=assets/engine/AndBasR.ttf}\n" + c[0] + "\n"
        credits_s += "{size=50}{font=assets/engine/Rujis.ttf}" + c[1] + "\n"
        c1=c[0]
    
    credits_s += "\n{size=100}{font=assets/engine/Rujis.ttf}voices{size=40}\n"
    
    c1 = ''
    for c in creditsVoice:
        if not c1==c[0]:
            credits_s += "{size=20}{font=assets/engine/AndBasR.ttf}\n" + c[0] + "\n"
        credits_s += "{size=50}{font=assets/engine/Rujis.ttf}" + c[1] + "\n"
        c1=c[0]
    
    credits_s += "\n{size=100}{font=assets/engine/Rujis.ttf}special thanks{size=40}\n"
    
    c1 = ''    
    for c in creditsThanks:
        if not c1==c[0]:
            credits_s += "{size=20}{font=assets/engine/AndBasR.ttf}\n" + c[0] + "\n"
        credits_s += "{size=50}{font=assets/engine/Rujis.ttf}" + c[1] + "\n"
        c1=c[0]    
    
init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
#    image theend = Text("{size=80}pretty", text_align=0.5)
    image thanks = Text("{size=40}.:. end .:.", text_align=0.5)
    
    # madamvicious
    
    
    
    
    
    