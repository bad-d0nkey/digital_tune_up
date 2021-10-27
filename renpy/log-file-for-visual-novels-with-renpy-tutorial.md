---
tutorial: visual novels with renpy
date: 23-10-21
tags: digital_tune_up, IF, renpy
---

# what I was trying to do

build a novel in ren'py.

+ tutorial: https://graddh.netlify.app/docs/tutorials/renpy/
+ repo: `[renpy](https://github.com/bad-d0nkey/bad-d0nkey.github.io)`
  + this directory is a mess and i don't know if i can delete anything or not - i had a "verion 1.0" that went nowhere but want still to tinker with
  + this link is to "version 2.0", the one that worked out 

## how it might connect to other research I'm doing

3d models and ar experiences are something i want to do as a "next step" after building archives. start with collecting stories and studying words -> end with making those histories relatable through experience

## what I did

+ step 1: read
  + read through all the things, identified things i needed more info on in the renpy documentation, got to understand the lay of the land

+ step 2: pirated shawn's version
  + ran through shawn's version a dozen times to see what each part *looked* like in action (this was super helpful)
  + pirated shawn's code and made minor changes (e.g., pictures, music)
  + this didn't work. tinkered through methodically. 
 
+ step 3: troubleshooting
  + here's the tricky thing - the documentation offers different advice from stackoverflow, which offers different advice from....
  + trying to identify why certain code is written differently isn't that easy for someone who doesn't know the _why_ of things -> mac/windows stuff is easy enough to identify, but the rest weren't quite clear
  + tried applying some of the fixes consistently in the code to see if that took care of the issues -> some did, some didn't; repeat
  + take-away: i got my head around what some things did and why there were some differences - that's something and it's a success worth having. i don't need perfect understanding - just frameworks so i can fill in spaces as i learn more overall

+ step 4: start fresh
  + tried my own. quickly wireframed a simple story. looked at assets i had available (the music and photos, btw, are licenced, hence no credits for them)
  + started with shawn's code. thud, thud, thud. worked through this in stages, saving code with descriptive titles at each round. 
  + start mocking up a "proofreading list" checklist. i'm sure there's an actual computer person phrase for this. it's like what i use for editing - but for code. ;)

+ step 5: recognised defeat
  + there are other files that were creating issues. i tinkered with those a bit (the options file, the start file) so i could see how it all came together. the code ultimately got too complicated for me to understand the contingencies. but at least i know there are other things that the main script file calls on. that, too, is a success. 
  + put a pin in this. i want to see how this works out and will ask for help in discord. but it is time to try a new angle.    

+ step 6: started fresh
  + grabbed the renpy "demo script" and identified the basic parts i wanted
  + the thing that struck me most is that the options in menus need to be addressed in order (like brackets in python) -> you see one full path through, _then_ go back to the second-closest "or" point, _then_ do the one further up the line and so forth  
  + this worked reasonably well. nothing other than obvious errors (file names, paths, picture size/format) happened here, so nothing to report, really, other than i am very glad i have my "proofreading" checklist/process list

+ step 7: splash screen
  + once i got the basic thing running, i decided it was safe to put time into detail work - like a splash screen with text that explains where the text comes from for the script and what it's about/why it relates to the story
  + this simply would not go -> i kept getting directed by the error messages to look at my options file -> editing the options file, though, did not help
  + time to take to discord about this, too

+ step 8: help
  + shawn has provided some tweaks that i'm excited to look at when i'm back at my own place on my desktop -> i can't comment on what i've wokred thorugh/learned re: that, as i won't be back there until the week's end, but i will be working through it. 
  + i also was the grateful recipient of tweaks for the second problem, which i'll also take a look at when i'm back at home. 

+ step 9: in sum...
  + i have a file that runs on my static website. it's incomplete, but it runs and i made it. win. 
  + i really like renpy. i am really looking forward to working through the tweaks shawn provided and being able to map the "after" onto the "before" and understanding the why. this is pretty cool. 
        
## challenges 

code logic. i can parrot things. but not knowing how to order things or why gets tricky. i don't know how to spot a problem if i don't know that there are conventions i'm breaking. shawn summed this best when he described why stackoverflow isn't super helpful a lot of the time for newbies. i really can't put it better, so i won't. it was really nice to read and is the entire of the sentiment that describes my challenges here. i don't know enough to know. but it's building and will change. that's really all i can ask for while learning. and that's a good place to be.

## thoughts on where to go next

i think i've finally found a thing that will give me a frame to hang other detail knowledge on. this might be a good place to start learning more about python. i need a context - vague exercises without cause/effect don't really help. but having a _thing_ to do does. this is happy-making. 

