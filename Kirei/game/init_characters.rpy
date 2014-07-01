# First, we'll set up the function to load the sprites. This will grab the files corresponding to the character, pose, and expression.
# It will then create an evening and night filter for both of them. Last, we crop and shrink character portraits for everything.

init -9 python:
    
    def load_sprite(character, pose, expression):
        filename = "assets/sprites/" + character + "/" + pose + "/" + expression + ".png"
        base = "assets/sprites/" + character + "/" + pose + "/base.png"
        
        #tags = [character, pose, expression]

        if renpy.loadable(filename):
            
            if pose == "default":
                
                # Set afternoon/indoor sprites
                renpy.image((character, expression), im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename))
                renpy.image(("side", character, expression), im.FactorScale(im.Crop(im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename), 0,0,720,325), 0.75))
                # Set evening sprites
                renpy.image((character, expression, "evening"), evening(im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename)))
                renpy.image(("side", character, expression, "evening"), evening(im.FactorScale(im.Crop(im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename), 0,0,720,325), 0.75)))
                # Set night sprites
                renpy.image((character, expression, "night"), night(im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename)))
                renpy.image(("side", character, expression, "night"), night(im.FactorScale(im.Crop(im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename), 0,0,720,325), 0.75)))
            else:
                # Set afternoon/indoor sprites
                renpy.image((character, pose, expression), im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename))
                renpy.image(("side", character, pose, expression), im.FactorScale(im.Crop(im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename), 0,0,720,325), 0.75))
                # Set evening sprites
                renpy.image((character, pose, expression, "evening"), evening(im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename)))
                renpy.image(("side", character, pose, expression, "evening"), evening(im.FactorScale(im.Crop(im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename), 0,0,720,325), 0.75)))  
                # Set night sprites
                renpy.image((character, pose, expression, "night"), night(im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename)))
                renpy.image(("side", pose, character, expression, "night"), night(im.FactorScale(im.Crop(im.Composite((720, 720),
                                                                    (0, 0), base,
                                                                    (0, 0), filename), 0,0,720,325), 0.75)))

                
    def night(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(0.6, 0.6, 0.7) * im.matrix.saturation(0.6))
    
    def evening(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(1.02, 0.95, 0.9) * im.matrix.brightness(0.05) * im.matrix.saturation(1.1))

        
        
# Character sprites
        
    ## Kirei
    
    load_sprite("kirei", "default", "concern")
    load_sprite("kirei", "default", "happy")
    load_sprite("kirei", "default", "smile")
    
    load_sprite("kirei", "arm", "concern")
    load_sprite("kirei", "arm", "happy")
    load_sprite("kirei", "arm", "surprise")
    load_sprite("kirei", "arm", "worry")
    
    load_sprite("kirei", "wrist", "happy")
    load_sprite("kirei", "wrist", "smile")
    
    load_sprite("kirei", "special", "shadows")
    
    ## Tomo
    
    load_sprite("tomo", "default", "chestnut")
    load_sprite("tomo", "default", "concern")
    load_sprite("tomo", "default", "glare")
    load_sprite("tomo", "default", "happy")
    load_sprite("tomo", "default", "mad")
    load_sprite("tomo", "default", "sad")
    load_sprite("tomo", "default", "sass")
    load_sprite("tomo", "default", "worry")
    

    load_sprite("tomo", "armdown", "cry")
    load_sprite("tomo", "armdown", "empty")
    load_sprite("tomo", "armdown", "happy")
    load_sprite("tomo", "armdown", "mad")
    load_sprite("tomo", "armdown", "quizzical")
    load_sprite("tomo", "armdown", "yandere")
    
    load_sprite("tomo", "hip", "cry")
    load_sprite("tomo", "hip", "empty")
    load_sprite("tomo", "hip", "happy")
    load_sprite("tomo", "hip", "mad")
    load_sprite("tomo", "hip", "quizzical")
    load_sprite("tomo", "hip", "yandere")

#Declare characters used by this game.
define narrator = Character('', color="#000000", what_color="#DDDDDD", ctc="ctc_default", ctc_position="fixed")
define mc = Character('protag', dynamic="true", color="#FFFF73", what_prefix="“", what_suffix="”", ctc="ctc_default", ctc_position="fixed", show_two_window=True)
define k = Character('kirei', image="kirei", dynamic="true", color="#42A0FA", what_prefix="“", what_suffix="”", ctc="ctc_default", ctc_position="fixed", show_two_window=True)
define t = Character('tomo', image="tomo", dynamic="true", color="#17BE7D", what_prefix="“", what_suffix="”", ctc="ctc_default", ctc_position="fixed", show_two_window=True)

define mcPhone = Character('protag', dynamic="true", color="#FFFF73", what_prefix="", what_suffix="", ctc="ctc_default", ctc_position="fixed", what_font="assets/engine/phone.ttf", what_size=12, show_two_window=True)
define kPhone = Character('kirei', dynamic="true", color="#42A0FA", what_prefix="", what_suffix="", ctc="ctc_default", ctc_position="fixed", what_font="assets/engine/phone.ttf", what_size=12, show_two_window=True)
define tPhone = Character('tomo', dynamic="true", color="#17BE7D", what_prefix="", what_suffix="", ctc="ctc_default", ctc_position="fixed", what_font="assets/engine/phone.ttf", what_size=12)

define Tomo = Character('', color="#FF0000", what_color="#FFFFFF", window_background="assets/ui/whatboxTomo.png", ctc="ctc_default", ctc_position="fixed")
define kTomo = Character('kireiNar', dynamic="true", image="kirei", color="#022E59", what_color="#FFFFFF", what_prefix="“", what_suffix="”", window_background="assets/ui/whatboxTomo.png", ctc="ctc_default", ctc_position="fixed", show_two_window=True)
define tTomo = Character('tomoNar', dynamic="true", image="tomo", color="#4E7155", what_color="#FFFFFF", what_prefix="“", what_suffix="”", window_background="assets/ui/whatboxTomo.png", ctc="ctc_default", ctc_position="fixed", show_two_window=True)