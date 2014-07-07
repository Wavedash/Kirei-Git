# Declare non-background images
image title = "assets/images/title.png"
image nanologo ="assets/images/NaNoLoGo.png"
image rosinlogo ="assets/images/rosinlogo.png"
image kc = "assets/images/kc.jpg"
image phone = "assets/images/phone.png"
image phone night = night("assets/images/phone.png")
image phonex = "assets/images/phonex.png"
image heartbeat = "assets/images/heartbeat.png"
image white = Solid((255, 255, 255, 255))
image shadowblowing = im.Composite((1280, 720),
                                    (280, 0), "assets/sprites/kirei/special/shadows.png")
                                                                    
                                                                    
#"assets/sprites/kirei/special/shadows.png", xanchor = "center"

image ctc_default = Animation("assets/ui/ctc/default_01.png", 0.5, "assets/ui/ctc/default_02.png", 0.5, "assets/ui/ctc/default_03.png", 0.5, "assets/ui/ctc/default_04.png", 0.5, xpos=getX(1080), ypos=getY(706), xanchor=1.0, yanchor=1.0)
image ctc_tomo = Animation("assets/ui/ctc/tomo_01.png", 0.5, "assets/ui/ctc/tomo_02.png", 0.5, "assets/ui/ctc/tomo_03.png", 0.5, "assets/ui/ctc/tomo_04.png", 0.5, xpos=getX(1080), ypos=getY(706), xanchor=1.0, yanchor=1.0)

# Transitions

define eyeopen = ImageDissolve("assets/vfx/eyeopen.png", 1.0)