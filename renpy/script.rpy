init:

#background images

    image bg openscene = "open.PNG"
    image bg street1 = "street1.PNG"
    image bg street2 = "street2.PNG"
    image bg street3 = "street3.PNG"
    image bg street4 = "street4.PNG"
    image bg street5 = "street5.PNG"
    image bg fence = "fence.PNG"
    image bg apartment = "apartment.PNG"
    image bg computer = "computer.PNG"
    image bg dissolve = "dissolve.PNG"
    image bg freedom = "freedom.PNG"
    image bg shhhh = "shhhh.PNG"

# The game starts here.

label start:
    
    show bg "start.PNG"

    show text "The Gods Are Neon."
    with Pause(2)
    hide text with fadeout

    scene bg street1 with fade
   
    show text "Pay attention."
    hide text with fade

    "Listen up, \ntake your stance! \nIn-deed."

    scene bg street2
    
    "Arms oustretched, \nout and back! \nKss! Kss!"
   
    scene bg street3
    
    "What is right is always right! \nWhat is right is always right!"

    menu:

        "In-deed.":

            jump next

        "Whatever.":

            jump start

label next:
    
    scene bg street4
    
    "Be true to yourself, \nmy son!"

    scene bg street5
    
    "You have raised my concerns, \nso listen up."

    menu:

        "In-deed.":

            jump continue

        "Whatever.":

            jump start

label continue:

    scene bg fence
    
    "What's this problem that you carry? \nHow long have you carried it for?"

    scene bg apartment
    
    "So, son, it may be difficult for you, \nand, son, seem to be unyielding \nalthough long you reflect on it."

    scene bg computer
    
    "The answer to the problem \nis here inside you. \nIn-deed! In-deed! In-deed!"
   
    stop music fadeout 1.0
    
    play music "tick.mp3" loop  

    scene bg dissolve

    show text "Upload virus?"

    menu:

        "Yes.":

           jump freedom

        "No.":

           jump shhhh

    stop music

label freedom:

    play music "splashmusic.mp3"

    scene bg freedom with fade
    
    "Freedom."

    scene bg "open.PNG"
    show text "The Gods Were Neon."
    with Pause(2)
    hide text with fade

    return
    
label shhhh:

    play music "splashmusic.mp3"

    scene bg shhhh with fade
    
    "Shhhhhhh..."

    scene bg "start.PNG"
    show text "The Gods Are Yet Neon."
    with Pause(2)
    hide text with fade
 
    return