﻿# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # If there's a side image, display it above the text.
    if side_image and persistent.config["show_portrait"]:
        add side_image
    else:
        if persistent.config["show_portrait"]: # Side image is explicitly declared, and portraits are enabled.
            add SideImage() xalign getX(-284) yalign 1.0
    
    # Decide if we want to use the one-window or two-window variant.
    
    if not two_window:

        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(400)
        xmaximum int(800)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    #tag menu
    
    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    #frame:
    #    style_group "mm"
    #    xalign .98
    #    yalign .98
    #
    #    has vbox
    #
    #    textbutton _("Start Game") action Start()
    #    textbutton _("Load Game") action ShowMenu("load")
    #    textbutton _("Preferences") action ShowMenu("preferences")
    #    textbutton _("Help") action Help()
    #    textbutton _("Quit") action Quit(confirm=False)
    
    imagemap:
        auto "assets/ui/mainmenu_%s.jpg"
        hotspot (66,633,174,39) action Start()
        hotspot (300,621,176,50) action ShowMenu("load")
        hotspot (532,623,115,50) action ShowMenu("preferencesAtMenu")
        hotspot (702,617,77,55) action Help()
        hotspot (834,622,70,51) action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    frame:
        #style_group "gm_nav"
        xalign .98
        yalign .98
        
        has vbox
        
        imagemap:
            auto "assets/ui/menu_%s.png"
            #(xpos,ypos,xsize,ysize)
            hotspot (25,7,100,38) action Return()
            hotspot (26,46,101,44) action ShowMenu("preferences")
            hotspot (42,94,68,25) action ShowMenu("save")
            hotspot (45,121,65,36) action ShowMenu("load")
            hotspot (17,161,115,32) action MainMenu()
            hotspot (43,195,66,48) action Help()
            hotspot (45,244,63,45) action Quit()

   ## The background of the game menu.
    # window:
        # style "gm_root"

    ##The various buttons.
    # frame:
        # style_group "gm_nav"
        # xalign .98
        # yalign .98

        # has vbox

        # textbutton _("Return") action Return()
        # textbutton _("Options") action ShowMenu("preferences")
        # textbutton _("Save Game") action ShowMenu("save")
        # textbutton _("Load Game") action ShowMenu("load")
        # textbutton _("Main Menu") action MainMenu()
        # textbutton _("Help") action Help()
        #textbutton _("About") action ShowMenu("about")
        # textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:

    frame:
        #style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            #textbutton _("Previous"):
            #    action FilePagePrevious()

            #textbutton _("Auto"):
            #    action FilePage("auto")

            #textbutton _("Quick"):
            #    action FilePage("quick")

            #for i in range(1, 2):
            #    textbutton str(i):
            #        action FilePage(i)

            #textbutton _("Next"):
            #    action FilePageNext()

        $ columns = 3
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text " [file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker
    
screen loadAtMenu:

    # This ensures that any other menu screen is replaced.
    tag menu

    #use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            #frame:
            #    style_group "pref"
            #    has vbox
            #
            #    label _("Transitions")
            #    textbutton _("All") action Preference("transitions", "all")
            #    textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            # frame:
                # style_group "pref"
                # has vbox

                # label _("After Choices")
                # textbutton _("Stop Skipping") action Preference("after choices", "stop")
                # textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"
                            
            frame: # Begin character portrait toggle block
                style_group "pref"
                has vbox
                
                label _("Character Portraits")
                if persistent.config["show_portrait"]:
                    textbutton "Enabled" action ToggleDict(persistent.config, "show_portrait")
                else
                    textbutton "Disabled" action ToggleDict(persistent.config, "show_portrait")
                            
screen preferencesAtMenu:

    tag menu

    # Include the navigation.
    #use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            #frame:
            #    style_group "pref"
            #    has vbox
            #
            #    label _("Transitions")
            #    textbutton _("All") action Preference("transitions", "all")
            #    textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            # frame:
                # style_group "pref"
                # has vbox

                # label _("After Choices")
                # textbutton _("Stop Skipping") action Preference("after choices", "stop")
                # textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"
                            
            frame: # Begin character portrait toggle block
                style_group "pref"
                has vbox
                
                label _("Character Portraits")
                if persistent.config["show_portrait"]:
                    textbutton "Enabled" action ToggleDict(persistent.config, "show_portrait")
                else
                    textbutton "Disabled" action ToggleDict(persistent.config, "show_portrait")

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    
    modal True
    
    imagemap:
        auto "assets/ui/YesNo_%s.png"
        hotspot (528,370,60,38) action yes_action
        hotspot (690,370,60,38) action no_action
    label _(message):
            xalign 0.5
            yalign 0.45

    # window:
        # style "gm_root"

    # frame:
        # style_group "yesno"

        # xfill True
        # xmargin .05
        # ypos .1
        # yanchor 0
        # ypadding .05

        # has vbox:
            # xalign .5
            # yalign .5
            # spacing 30

        # label _(message):
            # xalign 0.5

        # hbox:
            # xalign 0.5
            # spacing 100

            # textbutton _("Yes") action yes_action
            # textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.

screen quick_menu:

# Add an in-game quick menu.
    mousearea:
        area(getX(650), getY(510), 440, 80)
        hovered Show("quick_menu_sub", transition=None)
        unhovered Hide("quick_menu_sub", transition=wipedown)
    
screen quick_menu_sub:
    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign getX(1006)
        yalign getY(564)
        
        imagemap:
            auto "assets/ui/quickmenu/%s.png"
            hotspot (0,0,78,30) action Rollback()
            hotspot (78,0,59,30) action ShowMenu("save")
            hotspot (137,0,59,30) action ShowMenu("load")
            hotspot (196,0,55,30) action Skip()
            hotspot (251,0,62,30) action Preference("auto-forward", "toggle")
            hotspot (313,0,77,30) action ShowMenu("preferences")
            
init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

##############################################################################
# Wavedash's Custom Crap
#
# 
# 
        
screen about:
    tag menu

    window:
        style "gm_root"

    frame:
        style "menu_frame"
        xmargin 10
        ymargin 10
        has side "t c r b"

        label "\"Pretty\"" bottom_margin 10
        viewport id "vp":
            mousewheel True
            has vbox spacing 10

            text "v1.0"
            text "\
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean \
adipiscing tellus sit amet augue ultrices adipiscing. Suspendisse \
fermentum imperdiet lobortis. Duis non lectus at massa ornare \
tincidunt. Duis ultricies nisi ac elit rhoncus commodo. In nec \
commodo enim. Vivamus luctus rutrum est eget scelerisque. In ligula \
sapien, consectetur et faucibus at, porttitor id dui. Quisque \
aliquam augue faucibus odio ultrices sagittis. Cras odio orci, \
varius sit amet vulputate eleifend, pulvinar ac augue."

        vbar value YScrollValue("vp")
        textbutton "Return to menu":
            action Return()
            top_margin 10
            
init python hide:

    class KonamiListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame
            
            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_UP,
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_b,
                pygame.K_a,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            # If it's not the key we want, go back to the start of the statem
            # machine.
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # Otherwise, go to the next state.
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)


    # Create a KonamiListener to actually listen for the code.
    store.konami_listener = KonamiListener('konami_code')

    # This adds konami_listener to each interaction.
    def konami_overlay():
        ui.add(store.konami_listener)

    config.overlay_functions.append(konami_overlay)


# This is called in a new context when the konami code is entered.
label konami_code:

    show kc
    
    "{i}Pretty{/i} is proudly presented in WIDESCREEN"

    return