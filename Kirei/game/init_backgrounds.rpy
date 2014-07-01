# Declare backgrounds
image bg mainmenu = "assets/ui/mainmenu_ground.jpg"
image bg park = "assets/bg/park.jpg"
image bg park evening= "assets/bg/park_evening.jpg"
image bg park night= "assets/bg/park_night.jpg"
image bg classroom = "assets/bg/classroom.jpg"
image bg classroom flip =im.Flip("assets/bg/classroom.jpg", horizontal=True)
image bg classroom grey = im.Grayscale("assets/bg/classroom.jpg")
image bg classroom evening = eveningbg("assets/bg/classroom.jpg")
image bg hallway = "assets/bg/hallway.jpg"
image bg hallway evening = eveningbg("assets/bg/hallway.jpg")
image bg apartment = "assets/bg/apartment.jpg"
image bg apartment evening = "assets/bg/apartment_evening.jpg"

image bg white = Solid((255, 255, 255, 255))
image bg black = Solid((0, 0, 0, 255))

image bg kireiCG = "assets/cg/kirei.jpg"
image bg BGkireiCG = "assets/cg/BGkirei.jpg"

image bg tomoCG1 = "assets/cg/kiss1.jpg"
image bg tomoCG2 = "assets/cg/kiss2.jpg"
image bg tomoCG3 = "assets/cg/kiss3.jpg"

image bg credits = "assets/images/creditsBG.jpg"

init -9 python:
    def eveningbg(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(1.5, .9, .4) * im.matrix.brightness(0.01) * im.matrix.saturation(.8) * im.matrix.contrast(1.2))
        
    def nightbg(img_in):
        return im.MatrixColor(img_in, im.matrix.tint(0.6, 0.6, 0.7) * im.matrix.saturation(0.6))