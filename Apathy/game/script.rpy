# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define lucas = Character(_("Lucas"), color="#B2BEB5")
define naomi = Character(_("Naomi"), color="#3EFF00")
define scarlet = Character(_("Scarlet"), color="#BB2202")
define gabriel = Character(_("Gabriel"), color="#FFAA28")
define carson = Character(_("Carson"), color="#2C9FFF")
define adrian = Character(_("Adrian"), color="#EAFF52")
define brandon = Character(_("Brandon"), color="#AB5D00")
define london = Character(_("London"), color="#EE7DD9")
define sarah = Character(_("Sarah"), color="#FFDCF9")
define claus = Character(_("Claus"), color="#B2BEB5")

image apathy_up = "apathy up.jpg"
image apathy_down = "apathy down.jpg"

#GROUP
define glsa = Character(_("Gabriel, London, Sarah"), color="#C0C0C0")

#NPC
define attendant = Character(_("Attendant"), color="#B2BEB5")

#define positions
transform midleft:
    xalign 0
    yalign 0.5
transform midright:
    xalign 1.0
    yalign 0.5
transform midmidleft:
    xalign 0.25
    yalign 0.5
transform midmidright:
    xalign 0.75
    yalign 0.5

#initial variables
init python:
    apathy = 10
    happiness = 10
    magic_shown = False
    grade = 0
    tempGrade = 0
    stay = False
    force_stay = False
    smile = False
    dating = False
    last_person = "Scarlet"
    lucas_choice = "Claus"

    naomi1 = False
    naomi2 = False
    naomi3 = False
    naomi_check = False
    naomi_death = False
    naomi_dead = False

    scarlet1 = False
    scarlet2 = False
    scarlet3 = False

    gabriel1 = False
    gabriel2 = False
    gabriel3 = False
    gabriel_check = False

    carson1 = False
    carson2 = False
    carson3 = False
    carson_check = False
    carsonGrade = 2
    carson_dead = False

    adrian1 = False
    adrian2 = False
    adrian3 = False
    adrian_check = False
    adrianGrade = 2

    brandon1 = False
    brandon2 = False
    brandon3 = False
    brandon_check = False
    brandonGrade = 3
    brandon_known = False
    brandon_stay = True
    brandonr1 = False
    brandon_dead = False
    brandon_alive_checks = 0

    london1 = False
    london2 = False
    london3 = False
    london_check = False
    londonGrade = 3
    london_known = False

    sarah1 = False
    sarah2 = False
    sarah3 = False
    sarah_check = False
    sarahGrade = 1

label start:
    #tragic backstory
    "Many years ago..."
    scene bg blurred barn
    with fade
    #play music "flashback_start_Brandon Morris.ogg"
    naomi "Can you guys help me find doggy? I think I dropped her somewhere..."
    claus "Of course!"
    lucas "Where'd you lose her?"
    naomi "I don't know..."
    claus "Lucas, you check the trees left of the barn. Naomi, you check in and around the barn. I'll get the forest to the right."
    scene black
    with fade
    "After some time, you couldn't find doggy and returned to the barn."
    scene bg blurred barn
    with fade
    naomi "Find her?"
    lucas "No, I'm sorry. Maybe Claus will find her."
    "The two wait for a bit in silence."
    naomi "Oh! Want to see something?"
    lucas "Ok!"
    naomi "Look at what I can do with magic! I can become a hose for the flowers!"
    "Water trickles out of Naomi's fingertips, and she begins to water some flowers."
    lucas "That's so cool!"
    "The two laugh."
    naomi "I wonder-"
    "You hear a scream from the forest."
    lucas "Was...that Claus?"
    naomi "Let's go help him find doggy."
    scene bg blurred forest
    with fade
    "You walk into the forest."
    "A bear is on top of Claus!"
    claus "Lucas, Naomi, run! Don't get hurt!"
    scene bg blurred barn
    with fade
    "You ran."
    "You didn't look back."
    "You reached the barn, anxiously looking at the forest."
    "Naomi came back some time later."
    "Blood is on her face, tears rolling down, but she isn't hurt."
    "It was Claus' blood."
    scene black
    with fade
    "Nothing matters."
    "Your brother, young and naive, didn't see the dangers of the world. He didn't understand how frail his body was."
    "Your heart was frail, too."
    "It was...difficult seeing your own face go into the grave."
    "Your brother, someone with the same face as you, someone who went through everything with you...gone."
    "Why deal with pain if you can avoid it?"
    "Don't care about anything. Don't feel the world. You won't be hurt again."
    menu:
        "I'll be watching your actions at the top left...for the one controlling the strings."
        "I understand.":
            "Enjoy."
        "I don't understand.":
            "Various choices may increase or decrease your apathy. An image is displayed in the top left depending on an increase or decrease."
            "These choices are displayed AFTER the choice is made."
            "Enjoy the consequences of your actions."
    #arrive at the city with Naomi
    scene bg city
    with fade
    #play music "city_music_remaxim.flac"
    show lucas at midleft
    show naomi at midright
    naomi "We're here! Isn't this exciting! The city! We'll have a fun time here, I'm sure of it!"
    lucas "I guess so."
    naomi "Not even a smile? Look at how big it all is! And we haven't even seen the college yet, it's going to be so cool!"
    lucas "It's just a college, nothing special."
    naomi "I'm going to beat that attitude out of you someday, that apathy is on a timer. I'm going to see you laugh and hear you smile again!"
    lucas "You mixed those two around."
    naomi "C'mon, let's just go see it!"
    scene bg city walkway
    with fade
    show lucas at midleft
    show naomi at midright
    naomi "Ohh, I can't wait! This is going to be great! How could you not be excited?!"
    lucas "It's not that exciting. It's just the next step."
    naomi "Can you...just try to have fun?"
    menu:
        naomi "Can you...just try to have fun?"
        "Alright.":
            lucas "Alright."
            naomi "You always say that! I ask for something and I just get an 'alright' as if you don't care. It gets on my nerves."
            $ happiness -= 1
        "No promises.":
            lucas "No promises."
            naomi "Well, that's at least something...better than just an 'alright'."
            $ happiness += 1
    naomi "I don't know what your dad said, but I'll reiterate what my mom said before we left."
    naomi "{i}Don't show your magic to ANYONE. We don't know what the culture is around here. Just pretend that we're normal{/i}."
    menu:
        naomi "{i}Don't show your magic to ANYONE. We don't know what the culture is around here. Just pretend that we're normal{/i}."
        "Alright.":
            lucas "Alright."
            naomi "I hate it when you say that."
            $ happiness -= 1
        "If you insist.":
            lucas "If you insist."
            naomi "I mean it!"
    #college first look
    scene bg berger hall
    with fade
    #play music "campus_meeting_ztn.flac"
    show lucas at midleft
    show naomi at midright
    attendant "What's your housing plan?"
    naomi "We're going to live on campus."
    attendant "Alright, I'll have you two fill out these forms-that we've run out of. I'll go make more, why don't you sit in the cafe nearby and I'll hand them to you when I get them? Right behind you, past the double doors, on the left."
    naomi "Thanks!"
    "The attendant leaves."
    naomi "Isn't this place amazing?"
    lucas "I guess so."
    naomi "That's probably the best I'm going to get out of you, isn't it? Hey look, there's a big group at the tables over there, why don't we join them?"
    lucas "Sure."
    #meet the gang
    scene bg cafeteria
    with fade
    "Naomi walks the two of you to a group of six people sitting in a corner of the cafeteria."
    show naomi at midleft
    naomi "Hey, mind if we join you? We're new here, just getting a feel for the place."
    show gabriel serious at midright
    gabriel "I don't think that's a good idea-"
    naomi "I'm Naomi, this is Lucas. What are you all doing here? What are you studying?"
    show london at midmidright
    london "I think you took a wrong turn, Naomi."
    gabriel "That's no way to speak to them now, is it London?"
    london "Shut up."
    gabriel "Sorry. What she's trying to say is, are you sure you want to be seen near us?"
    show lucas at midmidleft
    lucas "It can't be that bad."
    gabriel "Maybe you're not getting my point, you {i}know{/i} who we are, right?"
    lucas "No idea."
    naomi "We're from way out east, in the countryside. This place is so huge! Are you guys used to the scale? That's amazing!"
    "The friends turn to each other for a brief moment, before turning back to you."
    gabriel "Well, what brings you here?"
    show brandon at topright
    brandon "This is a waste of time. I've already submitted my work. I'll see you later."
    show adrian at right
    adrian "Brandon, wait up!"
    hide brandon
    hide adrian
    "The two leave."
    naomi "Oh, we're waiting for the person to get our housing paperwork. He ran out of forms."
    show carson at truecenter
    carson "We got a lot of space, why don't you room with us?"
    hide carson
    hide gabriel
    hide london
    show london at topright
    show sarah at right
    show gabriel serious at midmidright
    glsa "Carson!"
    gabriel "Yes Carson, we have the room, but do you honestly think that's a good idea? With what happened with Fortune?"
    lucas "It'll save me money."
    naomi "Making friends already, Lucas?"
    lucas "It's just to save money."
    show carson at truecenter
    carson "Welcome aboard, friend!"
    london "Oh, this is a terrible idea."
    hide london
    gabriel "Carson..."
    sarah "I don't know about that, Carson. Would they really be ok with us?"
    hide sarah
    gabriel "I make the call, not Carson. We can't let them into our home, man."
    carson "C'mon, we gotta make friends with other people! It can't just be us hanging out for our entire college career! This will be a step towards re-entering society, like we should've done awhile ago!"
    gabriel "I can't shake the feeling that this is a bad idea."
    carson "This is our chance to have more normal friends! And its not like we'll let them freeload, right?"
    gabriel "I...hate that you have a point."
    show london at topright with moveinright
    london "Grow a spine, Gabe."
    gabriel "You're one to talk."
    hide london
    carson "But let's leave it to them, yeah? Whaddaya say?"
    lucas "I'll take it."
    naomi "If it's good with you..."
    gabriel "Alright, well, if you're sure, I'll give you the address and you can bring your gear there. There should be extra rooms on the second floor, pick whichever ones you want."
    naomi "What about those other two?"
    gabriel "They can introduce themselves later. For now, there's Carson,"
    carson "Hello!"
    gabriel "London,"
    hide carson
    show london at midright
    london "Hey."
    gabriel "Sarah,"
    hide london
    show sarah at midright
    sarah "H-hi."
    hide sarah
    show gabriel at truecenter with moveinright
    gabriel "And I'm Gabriel. Earn your keep and you're good with me. Who knows, we might be good friends."
    menu:
        gabriel "And I'm Gabriel. Earn your keep and you're good with me. Who knows, we might be good friends."
        "No, we won't.":
            lucas "No, we won't."
            $ happiness -= 1
        "I don't care.":
            show apathy_up at topleft
            lucas "I don't care."
            $ happiness -= 1
            $ apathy += 1
            hide apathy_up
    naomi "Lucas!"
    lucas "What?"
    naomi "He's probably just tired, it's good to meet you all!"
    gabriel "Here, I'll write down the address. Put it on the application and you can drop your gear off."
    naomi "Thank you!"
    hide gabriel
    "The attendant returns."
    if apathy < 11:
        show apathy_down at topleft
        "The attendant eyes Gabriel's friends."
        $ apathy -= 1
        hide apathy_down
    attendant "Here's your forms...have a good one."
    hide lucas
    hide naomi
    "The attendant walks away. You and Naomi head to another table."
    show lucas at midleft
    show naomi at midright
    if apathy < 11:
        lucas "That attendant was eyeing them."
        naomi "Yeah...I saw that, too. Do you think this is a good idea?"
        menu:
            naomi "Yeah...I saw that, too. Do you think this is a good idea?"
            "It'll save us money.":
                lucas "It'll save us money."
                naomi "Ok...if you're sure. I trust you."
            "No idea, but we'll find out.":
                lucas "No idea, but we'll find out."
                naomi "Yeah! What am I worrying for, I'm sure they're fun people!"
                $ happiness += 1
    else:
        lucas "They seem fine."
        naomi "What do you think their deal is? They seemed surprised that we didn't know them."
        menu:
            naomi "What do you think their deal is? They seemed surprised that we didn't know them."
            "Who knows.":
                show apathy_up at topleft
                lucas "Who knows."
                naomi "I guess we'll find out. It'll be fun!"
                $ apathy += 1
                hide apathy_up
            "Who cares.":
                show apathy_up at topleft
                lucas "Who cares."
                naomi "Well that's a little harsh, Lucas."
                $ happiness -= 1
                $ apathy += 1
                hide apathy_up
    "You finish filling out the forms with Naomi."
    naomi "That should be everything done. Let's go see the place!"
    #heading to the new place
    scene bg city walkway
    with fade
    #play music "adrian_bistro_remaxim.wav"
    "You're heading towards the address with Naomi."
    show lucas at midleft
    show naomi at midmidleft
    if apathy > 11:
        show apathy_up at topleft
        "The city looks boring."
        $ apathy += 1
        hide apathy_up
    else:
        show apathy_down at topleft
        "The city looks to have many fun places."
        $ apathy -= 1
        hide apathy_down
    "You notice one of Gabriel's friends at a nearby restaurant."
    show adrian at topright
    if apathy < 12:
        show apathy_down at topleft
        "He's holding a napkin to his knee."
        $ apathy -= 1
        hide apathy_down
    naomi "Isn't that one of Gabriel's friends? We should introduce ourselves!"
    "Naomi grabs your arm and takes you to his table."
    #joining one of the new friends at the bistro
    scene bg bistro
    with fade
    show adrian at midright
    adrian "Can I help-wait, didn't I just see you guys?"
    show naomi at midleft
    naomi "Yeah, you did! We were talking to Gabriel, and we'll be staying with you guys!"
    adrian "That sounds like a terrible idea. Uh, no offense, sorry."
    naomi "It's ok! Don't worry, we're not worried. I'm Naomi, and this is Lucas."
    adrian "I'm Adrian, it's a pleasure to meet you guys. What are you doing here?"
    naomi "We saw you and thought to introduce ourselves, which we did! What are you doing here?"
    adrian "Brandon and I got into a bit of an altercation. Just scraped my knee is all, nothing major."
    naomi "How horrible! Is there anything we can do?"
    adrian "I'll just walk it off, no sweat."
    "Naomi turns to you, and lowers her voice."
    naomi "Lucas...can you...you know..."
    show lucas at midmidleft
    lucas "Can I...what?"
    naomi "That thing that my mom said...we can just...ignore that for a few seconds, right?"
    "Naomi is referring to my magic. I can patch up his scrape."
    if apathy > 11:
        "You shouldn't. Don't reveal your magic under any circumstance. Do as you're told."
    else:
        "I could help him. It would be a risk, but I would be doing him a solid."
    menu:
        "Help Adrian?"
        "Cure his wound.":
            show apathy_down at topleft
            $ apathy -= 3
            $ happiness += 3
            $ magic_shown = True
            $ adrianGrade = 0
            "You cauterize the wound with fire magic."
            hide apathy_down
            naomi "Thanks, Lucas!"
            adrian "You also have magic?"
            lucas "Also?"
            adrian "Oh, great, me and my big mouth."
            naomi "Your secret is safe with us, don't worry!"
            adrian "It's not my secret, it's our secret, and it's not exactly secret because we're all a bit infamous. Gabriel didn't tell you?"
            naomi "No, he just gave us the address. What happened?"
            adrian "That's not for me to say, that's something for Gabriel. Consider us ex-military, if you want an idea. There's a reason we were alone in that corner."
            adrian "Honestly, I'm shocked that you approached us, and even more shocked that Gabriel is fine with you staying at our place."
            naomi "We were looking to make new friends!"
            lucas "I don't need friends."
            $ happiness -= 1
        "Leave him be.":
            show apathy_up at topleft
            $ apathy += 3
            $ happiness -= 3
            $ adrianGrade = 2
            lucas "No, Naomi."
            hide apathy_up
            naomi "Lucas..."
            lucas "Under any circumstances."
            adrian "You two alright? What's going on?"
            naomi "It's fine...we have something to talk about later, that's all."
            adrian "Ha! You two sound like me and Brandon, that's a good friendship the two of you have."
            naomi "What's going on with Brandon?"
            adrian "We're in a bit of a disagreement, nothing major. He likes to shut himself in his 'library' as he calls it, but don't tell him it's just the study. Fittingly enough, he spends all his time studying and keeping his distance from us, but I'll get through to him."
            lucas "Just let him go. It's not worth the hassle."
            $ happiness -= 1
    naomi "Lucas, how could you say that!"
    adrian "Making and keeping friends is an important aspect of life, at least for me. You never know when your friendships could end, and they really change your life for the better. Life is all about cherishing the people around you, even if they don't return the favors."
    adrian "It's about more than just yourself. Hold onto them while you can, and you'll find yourself smiling a lot more."
    naomi "Maybe he'll take that to heart, if he wants to keep his limbs intact."
    "Naomi stares daggers at you."
    naomi "{i}Right, Lucas?{/i}"
    lucas "We'll see."
    adrian "Whoa, hey, hey, no need to cause a scene here!"
    "Adrian gets between you and Naomi."
    adrian "Let's not hurt each other in public, now! How about I show you around town? We can drop your stuff off and explore."
    naomi "That sounds like a great plan!"
    if not magic_shown:
        adrian "Let me clean this up a bit more then we'll head out."
    "After some time, you arrive at the address. You drop your luggage off in the entryway, and Adrian shows you around."
    "It's getting late, so you head back."
    #arrive at the house
    scene bg entrance
    with fade
    #play music "house_music_VWolfDog.mp3"
    "You arrive at the house. Your luggage is just inside, and it seems everyone else has returned."
    show brandon at midright
    brandon "Can I help you?"
    show naomi at midleft
    naomi "We're ok, thanks! Where were we supposed to pick rooms, again?"
    brandon "This isn't a hotel."
    show carson at topright with moveinright
    carson "They're staying in some of the extra rooms upstairs."
    brandon "They're staying {i}here?{/i} You're joking, right?"
    carson "It's fine, Brandon. They're not allowed to freeload, they'll have to take on some work!"
    show brandon at midmidright with moveinright
    brandon "That's not the issue! The issue is that some people think we're terrorists! Why would we allow ANYONE to live with us!"
    show gabriel serious at right
    gabriel "We'll be careful. We'll just lay low and we'll sort everything out."
    brandon "You still don't understand!"
    "Brandon walks towards you. Naomi steps in between the two of you."
    show brandon at truecenter with moveinright
    show naomi at midmidleft with moveinleft
    show lucas at midleft
    brandon "You need to leave. You're not safe here, we are dangerous people. You shouldn't involve yourselves with us. Nothing can help us."
    naomi "That's not true, you can always be helped."
    brandon "You'll have to see for yourself."
    "Brandon clenches his fist and pulls it back. The air gets unusually cold."
    "You feel a burning sensation in your hands."
    "There's a fire in your heart, brighter than any before."
    "Protect."
    lucas "No!"
    show apathy_down at topleft
    $ apathy -= 3
    "Instinctively, you reach out to Naomi. A ring of fire envelopes her. Brandon stops his hand, and the air warms again."
    hide apathy_down
    naomi "Lucas, you..."
    brandon "Do you have ANY idea what you may have just doomed yourself to?"
    gabriel "Brandon, stop! Let's be civil and talk about this!"
    show brandon at midmidright
    brandon "There's no hope for you now."
    naomi "Don't say that!"
    gabriel "Let's just grab seats in the lobby, let's just calm down and talk."
    "You relinquish the fire shield."
    scene bg lobby
    with fade
    "You find a spot next to Naomi."
    show gabriel serious at midright
    gabriel "Ok...we're good? No magic, got it?"
    show brandon at top
    brandon "Sure. Now, who exactly are you two?"
    show lucas at midleft
    show naomi at midmidleft
    naomi "I'm Naomi, and this is Lucas."
    brandon "No, not that. What can you two do?"
    naomi "Are you asking for a demonstration?"
    gabriel "Let's not resort to violence for the moment, just tell us."
    naomi "I can fire water from my fingers and palm, and Lucas can burn wounds to fix them, and...whatever that was."
    lucas "I didn't know I could do that."
    #if adrian helped, argument breaks out
    if magic_shown:
        show adrian at topright
        adrian "He fixed up that scrape I got earlier. Oh, I appreciate it, by the way."
        brandon "You KNEW they had magic and you didn't think to tell any of us?! You didn't tell Gabriel?!"
        show adrian serious
        adrian "Brandon, I-"
        brandon "This is pointless, all of this is pointless! You, you of all people should know to say something if you know it! Do you want a repeat of Miss Fortune?!"
        gabriel "Brandon!"
        "Silence comes across the table."
        gabriel "Brandon, get out of here. We'll talk later."
        brandon "Alright."
        hide brandon
        "Brandon leaves. His footsteps are loud against the stairs."
        adrian "Well, that stings."
        gabriel "I can't say I blame him, considering what happened with him and Blake."
        adrian "Yeah...I guess he had it the worst of us."
        show london mad at top
        london "Oh, we're just brushing past what you did to me? How you all treated me?"
        gabriel "It's not a competition."
        london "BRANDON had the worst? Really? We're just glossing over the fact that I was effectively exiled for Sarah's curse?"
        gabriel "She's sitting right next to you!"
        london "It doesn't change the fact that it happened, no matter whos curse it was!"
        gabriel "Listen, can we not talk about this while we have guests?"
        london "What, you going to send me off too? Like the girls did? Is that what you want?"
        gabriel "I'm just asking for courtesy-"
        london "You don't get my courtesy! None of you do! None of you know what I went through! You abandoned-"
        show sarah at midmidright
        sarah "PLEASE SHUT UP!"
        show sarah sad
        "Silence returns to the table."
        sarah "I'm going to my room...I'm sorry. I...shouldn't have shouted..."
        gabriel "Sarah..."
        hide sarah
        "Sarah leaves."
        gabriel "What a show. Well...We'll talk later. There should be extra rooms upstairs on the right. Pick whichever you want."
        hide adrian
        hide london
        hide gabriel
        "The table empties until it's just you, Naomi, and Carson."
        show carson at midright
        carson "Well, that was bound to happen eventually. I'm surprised they went this long without bringing anything up."
        naomi "I feel bad for them...but...let's drop it for the night."
        carson "Yeah. Poor guys. I hope they'll be happy, despite their differences."
        naomi "It sounds pretty bad..."
        carson "Well, I'll make them laugh, and they won't think about it!"
        show apathy_up at topleft
        lucas "That's why friends are a pain."
        $ apathy += 1
        hide apathy_up
        naomi "They'll come around."
    #argument doesn't happen
    else:
        show adrian serious at topright
        adrian "Ohhh, so earlier Naomi was trying to get you to fix my knee. I'm a little hurt that you didn't trust me enough to help."
        brandon "You might be the first person to have fire. Remarkable. As for water, that was seen before...but he was a medic, if I recall correctly."
        naomi "It's nothing special, I can just shoot water from my hands. It even hurt a bear when we were younger."
        brandon "Water...as a weapon. Interesting. There might be branches to some forms of magic. I'd be curious to learn more-"
        gabriel "Let's not interrogate them just yet, Brandon. Let's give them some rest and talk with them another time."
        brandon "Oh, alright. You at least recognize the significance of a new branch of magic though, right?"
        gabriel "Yeah, sure. Lucas, Naomi, there are extra rooms upstairs on the right. Pick whichever suits your fancy. As for the rest of you, you're free to go."
    #lobby with recap of yesterday's new friends
    scene bg lobby
    with fade
    if magic_shown:
        "Yesterday was an eventful day."
        "The arguments were a pain to listen to."
        show apathy_up at topleft
        "Just another reason why friendships don't work."
        $ apathy += 1
        hide apathy_up
    else:
        "Yesterday went by quickly."
        "The new friends work well together."
        "Friends? Really?"
        "Already calling them friends."
        show apathy_down at topleft
        "Maybe Naomi was right."
        $ apathy -= 1
        hide apathy_down
    #event 1 with gabriel
    show gabriel at midright with moveinright
    show lucas at midleft
    gabriel "Lucas, help me do some dishes, would you?"
    lucas "Alright."
    #lucas and gabriel talk
    scene bg kitchen
    with fade
    show lucas at midleft
    show gabriel at midright
    if magic_shown:
        show gabriel serious
        gabriel "Hey, so...I wanted to apologize for all their behavior yesterday."
        lucas "Why are you apologizing?"
        gabriel "They won't apologize, and we treated you unfairly. Neither of you deserved to see that."
        lucas "That's how friends are."
        gabriel "They're not as bad as you think."
        show apathy_up at topleft
        lucas "Sending Brandon away?"
        $ apathy += 1
        hide apathy_up
        gabriel "He's not usually like that."
        show apathy_up at topleft
        lucas "London's argument?"
        $ apathy += 2
        hide apathy_up
        gabriel "She's just...troubled."
        show apathy_up at topleft
        lucas "Sarah shouting?"
        $ apathy += 3
        hide apathy_up
        gabriel "Alright, alright, I get it, they're hard to control when things get out of hand."
        show apathy_up at topleft
        lucas "You wouldn't have that problem if you didn't care about them."
        $ apathy += 2
        hide apathy_up
        "You continue to wash dishes, in silence."
        gabriel "..what'd London say, grow a spine?"
        lucas "Yeah."
        gabriel "I guess she knew something like this could happen."
        lucas "Naomi said your trauma or whatever sounded bad."
        gabriel "Yeah...something like that."
        lucas "Care to share?"
        gabriel "I supposed you'd have to find out sooner or later."
    else:
        gabriel "Did you get some good rest?"
        lucas "I guess so."
        gabriel "Good, that's good to hear. I'm surprised Brandon didn't do anything yesterday."
        lucas "What was he going to do?"
        gabriel "As you may have figured out...we all have some form of magic. Brandon can punch your soul from your body. You have to swim back to your body, it feels very surreal."
        lucas "Don't get close to Brandon, got it."
        $ brandon_known = True
        gabriel "You don't have to do that, he only does it to people who ask for it. Or to prove a point."
        lucas "Better to be safe than sorry."
        gabriel "They're a rowdy bunch, but I keep them together. We stick up for each other, we poke fun at each other, like friends do."
        lucas "Sounds like you have your hands full."
        gabriel "At times, it can be. That's just how a bunch of friends are, yeah? Something sets one of them off and it just spirals from there."
        show apathy_up at topleft
        lucas "It's a hassle to have friends."
        $ apathy += 1
        hide apathy_up
        gabriel "Look at it from a different perspective, life wouldn't be interesting without them. You should at least want interesting things to happen, right?"
        if apathy < 11:
            show apathy_down at topleft
            lucas "I guess so, yeah."
            $ apathy -= 1
            hide apathy_down
        else:
            show apathy_up at topleft
            lucas "No."
            $ apathy += 1
            hide apathy_up
            gabriel "Well, maybe you'll change your mind later. Just a thought to throw out there."
        "You continue to wash dishes."
        gabriel "You two ok here? Have any questions about us? What'd Brandon say, that we might be terrorists? That has to at least be an alarm of some sort."
        lucas "You could share your story."
        gabriel "I suppose there's no harm in telling you."
    #scenes of the new friend's backstory
    scene black
    with fade
    gabriel "The most recent war we had, the one that ended roughly twenty years ago-that's when we first started to see magic."
    gabriel "I don't know the details of how it happened, just that it happened."
    gabriel "From what Brandon has said, magic is tied to our genetics. If one of your parents had magic, you'll have magic."
    gabriel "Someone looking to abuse unearned power was bound to appear."

    scene bg bridge
    with fade
    gabriel "One of the war vets, a friend of my father, he grouped us."
    gabriel "We were the 'Children of Lucky', Lucky apparently being his codename during the war."
    gabriel "Ten men and ten women with magic were put onto this team, to protect...whatever we were supposed to protect."
    gabriel "Or rather, ten boys and ten girls. The oldest of us was twenty, the youngest sixteen, and we all had unearned power."
    gabriel "I guess we were no different from Miss Fortune."

    scene bg hallway
    with fade
    gabriel "Once we had our ceremony, we went out for an icebreaker."
    gabriel "There was a fortune teller, which we've since called Miss Fortune."
    gabriel "It was a cursed magic...it would give blessings to half of us and curses to half of us, and we wouldn't know which applied to who."

    scene black
    with fade
    gabriel "It was gambling, in a way. We gambled our lives away for an icebreaker. I'm why we're in this situation. I was their leader, and I lead them to their doom."
    gabriel "We uncovered Miss Fortune's machinations. We stopped her from giving more curses to anyone else."
    gabriel "The Acrad government didn't know what to do with us afterwards. They saw the power we had, and how easily it could be misused."
    gabriel "They still don't know what to do. They split us in half and are paying for our first year until they decide what to do."

    scene bg entrance
    with fade
    gabriel "We started with twenty, and we were reduced to twelve at the end."
    gabriel "We were all only thinking for ourselves. We wanted to know which blessing or curse was ours."
    gabriel "We were afraid of the people we thought had curses. We shunned them. We treated them horribly."
    gabriel "The curses were designed to tear us apart."
    gabriel "None of us were immune to it. We all took part in it at different times. We were supposed to be a team and instead we were terrible friends."

    scene bg kitchen
    with fade
    show lucas at midleft
    show gabriel serious at midright
    gabriel "Learn from my mistakes. Cherish the friends you may have, before they may be taken from you."
    menu:
        gabriel "Learn from my mistakes. Cherish the friends you have, before they may be taken from you."
        "Alright.":
            lucas "Alright."
        "No.":
            show apathy_up at topleft
            lucas "No."
            $ apathy += 1
            hide apathy_up
            gabriel "I urge you to reconsider. Being selfish will just hurt the rest of us, man. You don't have to be best friends, just...spend time with them, yeah? Might discover something within."
            lucas "I'll consider it."
    show gabriel
    gabriel "I don't know how you'll be studying, but if you have time, see if you can spend time with anyone. If they want to, that is."
    gabriel "Nothing against you. Some people will care about your grades."
    gabriel "Just keep it in mind."
    lucas "Alright."
    gabriel "Good, good to hear. Was good talking with you. Just do something like this with the other people, yeah? I enjoyed it."
    lucas "Sure."
    $ gabriel1 = True
    scene black
    with fade
    "The days until classes start are uneventful."
    if magic_shown:
        "Things were tense at the house."
    else:
        "People kept to themselves."
    #arrive back at home after classes
    scene bg entrance
    with fade
    "You arrive home from your first day."
    "You hear voices in the lobby."
    if magic_shown:
        gabriel "Yeah, well, sure doesn't feel like it at the moment."
        carson "Take it from me, you have to be happy! We look up to you, and how you're feeling will spread to the rest of us!"
        naomi "We're here if you need us."
        gabriel "Thanks, but this is something I have to fix on my own. I appreciate the help, but this is something for me to do."
        carson "You don't have to go alone."
        naomi "Yeah, we have your back!"
    else:
        gabriel "Carson..."
        carson "Oh c'mon, it's the first day! Nothing happened anyway!"
        gabriel "Dude, you can't be skipping classes. I get that they might be boring, but at least try to go to them, man."
        carson "Hey, it wasn't just me. London didn't go to class either!"
        london "You rat! You dirty rat! I did nothing to you!"
        gabriel "Carson..."
    "You enter the lobby."
    show lucas at midleft
    show carson at midright
    carson "Oh, hey Lucas! How has your day been?"
    lucas "Fine."
    carson "Why don't we go pay a visit to the market, get some food for everyone?"
    lucas "You don't need me to come with you."
    carson "It'll be fun, promise!"
    menu:
        carson "It'll be fun, promise!"
        "Sure.":
            lucas "Sure."
        "No.":
            show apathy_up at topleft
            lucas "No."
            $ apathy += 1
            hide apathy_up
            show gabriel serious at top
            gabriel "You're going."
            lucas "I am?"
            "Gabriel frowns at you."
            lucas "I guess I'm going."
            hide gabriel
    carson "Great, it's settled! Let's go!"
    #carson event 1
    scene bg market
    with fade
    show lucas at midleft
    show carson at midright
    carson "That's some nifty magic you have there."
    lucas "It's not that interesting."
    carson "Compared to me, I think it's great. I can only cause the ground to shake so many times before it becomes a novelty, but it's a fun party trick!"
    lucas "Are you always this excited?"
    carson "Of course! Everyone should find the happiness in their life and enjoy it while we can! You never know when you'll topple over, so take advantage while you can!"
    lucas "A lot to say from a man who creates earthquakes."
    "Carson gives a hearty chuckle."
    carson "I suppose that is ironic. You're more fun than you give yourself credit!"
    lucas "I'm only here because Gabriel told me to talk with you guys."
    carson "And not to enjoy my company, the nerve!"
    "Carson laughs."
    carson "You're a good jokester, keep it up and you might be a great comedian!"
    lucas "No, that was the truth."
    carson "Ha! Keep it up!"
    "Your words seem to have gone completely over Carson's head."
    if magic_shown:
        carson "About last night, I'm sorry things went so terribly. Just know I have your back!"
        lucas "It was fine, and you don't need to."
        carson "Well that's too bad for you, because I already have it!"
        lucas "I guess you do."
    else:
        carson "Brandon didn't interrogate you about magic, did he?"
        lucas "No. I haven't seen him since the first night."
        carson "He tends to stay in the study. Sorry, 'library.' Don't tell him I said that. Or do, if you find a funny opportunity to!"
        lucas "Sure."
    carson "Great! Good to know."
    lucas "Weren't we supposed to buy food?"
    carson "Oh! Right! Let's do that!"
    "You shopped with Carson."
    $ carson1 = True
    #back at home
    scene bg entrance
    with fade
    "You have free time."
    "During your free time, you may spend time with someone that's available, or study for upcoming exams."
    "People will be available on different days."
    "At the moment, you don't think many people trust you."
    "Be careful with who you ask, fragile man."
    #recurring calendar events, every 5 events, a special event happens
    scene bg lobby
    with fade
    "What should you do today? Who should you spend time with?"
    menu day2:
        "Naomi?":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            call scene_naomi1
        "Carson?":
            "You decide to ask Carson."
            show carson at truecenter
            lucas "What's up, Carson?"
            carson "Not much, not much, what's up with you?"
            lucas "You up to do something?"
            carson "Thought you'd never ask!"
            call scene_carson2
        "Adrian?" if not adrian_check:
            "You decide to ask Adrian."
            show adrian at truecenter
            if magic_shown:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                call scene_adrian1
            else:
                call adrian_deny
                hide adrian
                jump day2
        "Brandon?" if not brandon_check:
            "You decide to ask Brandon."
            call brandon_deny
            jump day2
        "London?" if not london_check:
            "You decide to ask London."
            show london at truecenter
            call london_deny
            hide london
            jump day2
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "What should you do today?"
    menu day3:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            call scene_naomi1
        "Gabriel?" if not gabriel_check:
            "You decide to ask Gabriel."
            show gabriel at truecenter
            if magic_shown:
                show gabriel serious
                call gabriel_deny
                hide gabriel
                jump day3
            else:
                lucas "Hey Gabriel, want to do something?"
                gabriel "Yeah, I got time. Let's hit the gym, yeah?"
                call scene_gabriel2
        "Brandon?" if not brandon_check:
            "You decide to ask Brandon."
            call brandon_deny
            hide brandon
            jump day3
        "London?" if not london_check:
            "You decide to ask London."
            show london at truecenter
            call london_deny
            hide london
            jump day3
        "Sarah?" if not sarah_check:
            "You decide to ask Sarah."
            show sarah at truecenter
            call sarah_deny
            hide sarah
            jump day3
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "What's on the menu today?"
    menu day4:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            else:
                call scene_naomi2
        "Carson?":
            "You decide to ask Carson."
            show carson at truecenter
            lucas "What's up, Carson?"
            carson "Not much, not much, what's up with you?"
            lucas "You up to do something?"
            carson "Thought you'd never ask!"
            if not carson2:
                call scene_carson2
            else:
                call scene_carson3
        "Adrian?" if not adrian_check:
            "You decide to ask Adrian."
            show adrian at truecenter
            if magic_shown:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                else:
                    call scene_adrian2
            else:
                call adrian_deny
                hide adrian
                jump day4
        "Brandon?" if not brandon_check:
            "You decide to ask Brandon."
            call brandon_deny
            hide brandon
            jump day4
        "Sarah?" if not sarah_check:
            "You decide to ask Sarah."
            show sarah at truecenter
            call sarah_deny
            hide sarah
            jump day4
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "Midterms are soon...what should you do?"
    menu day5:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            else:
                call scene_naomi2
        "Gabriel?" if not gabriel_check:
            "You decide to ask Gabriel."
            show gabriel at truecenter
            if magic_shown:
                show gabriel serious
                call gabriel_deny
                hide gabriel
                jump day5
            else:
                lucas "Hey Gabriel, want to do something?"
                gabriel "Yeah, I got time. Let's hit the gym, yeah?"
                if not gabriel2:
                    call scene_gabriel2
                else:
                    call scene_gabriel3
        "Adrian?" if not adrian_check and last_person is not "Adrian":
            "You decide to ask Adrian."
            show adrian at truecenter
            if magic_shown:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                else:
                    call scene_adrian2
            else:
                call adrian_deny
                hide adrian
                jump day5
        "Sarah?" if not sarah_check:
            "You decide to ask Sarah."
            show sarah at truecenter
            call sarah_deny
            hide sarah
            jump day5
        "Study?":
            call study
    call set_false
    #midterm events
    scene bg hallway
    with fade
    "Midterms have arrived..."
    "..."
    "..."
    "..."
    scene black
    with fade
    if tempGrade == 0:
        "You failed your midterms."
        $ happiness -= 5
    elif tempGrade == 1:
        "You got a D average."
        $ happiness -= 3
    elif tempGrade == 2:
        "You got a C average."
        $ happiness -= 1
    elif tempGrade == 3:
        "You got a B average."
        $ happiness += 1
    elif tempGrade == 4 or tempGrade > 4:
        "You aced your midterms!"
        $ happiness += 3
    else:
        "There was an error with your grade, so you were given a C."
        $ happiness -= 1
        $ tempGrade = 2
    $ grade = tempGrade
    if tempGrade > 0:
        $ tempGrade -= 1
    #bowling with the boys or join brandon
    scene bg lobby
    with fade
    show gabriel at midright
    gabriel "We've all got our grades back. Some of you did well, others...well, there's always next time."
    gabriel "It's been a long time since we've done something fun, right?"
    gabriel "Let's split up our groups and do something, yeah? Split men and women, like the old days."
    show lucas at midleft
    menu:
        gabriel "How about it? Care to join us?"
        "I'll pass.":
            show apathy_up at topleft
            lucas "I'll pass."
            $ stay = True
            $ apathy += 3
            hide apathy_up
            gabriel "Alright. Keep the place warm for us."
            call scene_brandon1
        "Sure.":
            #if naomi doesn't like lucas' choices, lucas is forced to stay home
            if happiness < 6:
                lucas "Sure."
                show naomi at top
                naomi "Oh no you don't, you haven't earned it. You can go with them when you fix that attitude."
                lucas "I'm not?"
                "Naomi aims her hands at you."
                "You'd rather not be on the receiving end of magic."
                lucas "Nevermind then, I'll stay here."
                gabriel "Alright. Keep the place warm for us."
                $ force_stay = True
                call scene_brandon1
            else:
                lucas "Sure."
                gabriel "Nice. Let's go bowling with the guys."
                show brandon at top
                brandon "I'll stay here. You guys enjoy yourself."
                gabriel "Alright."
                call bowling
    #people much more willing to talk with lucas now, depends on grade rather than instant decline
    scene bg lobby
    with fade
    "The mood is more lively among the group. More people might be willing to spend time with you."
    "Finals aren't for awhile...what should you plan for today?"
    menu day6:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            else:
                call scene_naomi3
        "Gabriel?" if last_person is not "Gabriel":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            else:
                call scene_gabriel3
        "Carson?" if not carson_check:
            "You decide to ask Carson."
            show carson at truecenter
            if grade < carsonGrade:
                lucas "What's up, Carson?"
                carson "Not much, not much, what's up with you?"
                lucas "You up to do something?"
                carson "Thought you'd never ask!"
                if not carson2:
                    call scene_carson2
                elif not carson3:
                    call scene_carson3
                else:
                    call max("Carson")
            else:
                show carson at truecenter
                call carson_deny
                hide carson
                jump day6
        "Brandon?" if not brandon_check:
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
            else:
                call brandon_deny
                hide brandon
                jump day6
        "London?" if not london_check:
            "You decide to ask London."
            show london at truecenter
            if grade < londonGrade:
                lucas "Are you up for a chat, London?"
                london "You know what? I guess I am."
                call scene_london1
            else:
                call london_deny
                hide london
                jump day6
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "Where should you spend your time?"
    menu day7:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            else:
                call scene_naomi3
        "Carson?" if not carson_check and last_person is not "Carson":
            "You decide to ask Carson."
            show carson at truecenter
            if grade < carsonGrade:
                lucas "What's up, Carson?"
                carson "Not much, not much, what's up with you?"
                lucas "You up to do something?"
                carson "Thought you'd never ask!"
                if not carson2:
                    call scene_carson2
                elif not carson3:
                    call scene_carson3
                else:
                    call max("Carson")
            else:
                show carson at truecenter
                call carson_deny
                hide carson
                jump day7
        "Adrian?" if not adrian_check:
            "You decide to ask Adrian."
            show adrian at truecenter
            if grade > adrianGrade:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                elif not adrian2:
                    call scene_adrian2
                else:
                    call scene_adrian3
            else:
                call adrian_deny
                hide adrian
                jump day7
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
            else:
                call brandon_deny
                hide brandon
                jump day7
        "London?" if not london_check and last_person is not "London":
            "You decide to ask London."
            show london at truecenter
            if grade < londonGrade:
                lucas "Are you up for a chat, London?"
                london "You know what? I guess I am."
                call scene_london1
            else:
                call london_deny
                hide london
                jump day7
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "Who should join you today?"
    menu day8:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Gabriel?":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                elif not brandon2:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon3
            else:
                call brandon_deny
                hide brandon
                jump day8
        "London?" if not london_check and last_person is not "London":
            "You decide to ask London."
            show london at truecenter
            if grade < londonGrade:
                lucas "Are you up for a chat, London?"
                london "You know what? I guess I am."
                if not london1:
                    call scene_london1
                else:
                    call scene_london2
            else:
                call london_deny
                hide london
                jump day8
        "Sarah?" if not sarah_check:
            "You decide to ask Sarah."
            show sarah at truecenter
            if grade > sarahGrade:
                lucas "Hi Sarah, do you want to do something today?"
                sarah "That...sounds nice, actually."
                call scene_sarah1
            else:
                call sarah_deny
                hide sarah
                jump day8
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "What's planned for today?"
    menu day9:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Carson?" if not carson_check:
            "You decide to ask Carson."
            show carson at truecenter
            if grade < carsonGrade:
                lucas "What's up, Carson?"
                carson "Not much, not much, what's up with you?"
                lucas "You up to do something?"
                carson "Thought you'd never ask!"
                if not carson2:
                    call scene_carson2
                elif not carson3:
                    call scene_carson3
                else:
                    call max("Carson")
            else:
                show carson at truecenter
                call carson_deny
                hide carson
                jump day9
        "Adrian?" if not adrian_check:
            "You decide to ask Adrian."
            show adrian at truecenter
            if grade > adrianGrade:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                elif not adrian2:
                    call scene_adrian2
                elif not adrian3:
                    call scene_adrian3
                else:
                    call max("Adrian")
            else:
                call adrian_deny
                hide adrian
                jump day9
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                elif not brandon2:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon3
            else:
                call brandon_deny
                hide brandon
                jump day9
        "Sarah?" if not sarah_check and last_person is not "Sarah":
            "You decide to ask Sarah."
            show sarah at truecenter
            if grade > sarahGrade:
                lucas "Hi Sarah, do you want to do something today?"
                sarah "That...sounds nice, actually."
                call scene_sarah1
            else:
                call sarah_deny
                hide sarah
                jump day9
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "Finals are coming up soon...what should you do?"
    menu day10:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Gabriel?":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Adrian?" if not adrian_check and last_person is not "Adrian":
            "You decide to ask Adrian."
            show adrian at truecenter
            if grade > adrianGrade:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                elif not adrian2:
                    call scene_adrian2
                elif not adrian3:
                    call scene_adrian3
                else:
                    call max("Adrian")
            else:
                call adrian_deny
                hide adrian
                jump day10
        "Sarah?" if not sarah_check and last_person is not "Sarah":
            "You decide to ask Sarah."
            show sarah at truecenter
            if grade > sarahGrade:
                lucas "Hi Sarah, do you want to do something today?"
                sarah "That...sounds nice, actually."
                if not sarah1:
                    call scene_sarah1
                else:
                    call scene_sarah2
            else:
                call sarah_deny
                hide sarah
                jump day10
        "Study?":
            call study
    call set_false
    scene bg hallway
    with fade
    "Finals have arrived..."
    "..."
    "..."
    scene black
    with fade
    "You arrive early for your last final."
    "A woman in your class notices you and walks up to you."
    #scarlet introduction
    scene bg hallway
    with fade
    show lucas at midleft
    show scarlet at midright with moveinright
    scarlet "You know, I don't think I've ever heard you speak in class."
    lucas "I'm not much of a talker."
    scarlet "I'm Scarlet, a pleasure to meet you. What about Psychology interests you?"
    "Scarlet extends her hand to you."
    "You shake her hand without thinking anything of it."
    lucas "One of my friends wanted me to join her in this."
    scarlet "Psychology is just so interesting, isn't it? Figuring out how people work, seeing mindsets in action, showing people the truth..."
    lucas "It's a fine subject."
    scarlet "I'm still a little new to this city, and I won't have anything to do over winter break. It'd be great to have a friend like you!"
    lucas "I can show you around."
    scarlet "Great! That sounds like fun!"
    "Naomi, Gabriel, and Carson arrive."
    "Naomi scowls as she notices you, and turns to Scarlet."
    show lucas at midmidleft
    show naomi at midleft
    naomi "What do you think you're doing?"
    scarlet "Making a friend?"
    "Naomi scoffs and turns away from you."
    hide naomi
    "Scarlet bombards you with questions as you wait."
    show scarlet at midmidright with moveinright
    scarlet "Where are you from?"
    scarlet "How long have you been here?"
    scarlet "Do you think revenge has any merits?"
    scarlet "If you had to change something about yourself, what would you change?"
    scarlet "What do you envy?"
    "You answer them to the best of your ability."
    "Gabriel seems to notice how long you've been talking."
    show gabriel at midleft
    gabriel "Well, haven't heard your voice go on for that long before."
    lucas "It happens."
    show naomi at top
    naomi "No, it doesn't."
    $ happiness -= 3
    gabriel "Who's your friend?"
    scarlet "I can speak for myself. I'm Scarlet, good to meet-all of you."
    "Scarlet's smile slowly disappears."
    scarlet "You're..."
    gabriel "Yeah."
    scarlet "And Lucas, you're...with them?"
    lucas "Yeah."
    gabriel "You don't have anything to be afraid of. We're just trying to get our educations."
    scarlet "No, I believe you. I just didn't...expect to be talking to you."
    gabriel "We understand people avoiding us. Actually, Lucas and Naomi here live with us."
    scarlet "They do?"
    naomi "They've been nice."
    scarlet "I shouldn't have been caught up in rumors. I'm sorry."
    gabriel "No no, it's on us."
    scarlet "Well, actually, if you still have room...I won't have a place to stay next semester."
    naomi "I don't-"
    scarlet "I can pay! I'll be good, I swear!"
    gabriel "You want to be associated with us?"
    scarlet "Carson is fun, we've been to a couple parties. What's the worst that can happen?"
    hide naomi
    show carson at top
    carson "Hey, that's my line!"
    hide carson
    show naomi at top
    gabriel "You know about magic, right? That part's not a rumor, that's real."
    scarlet "Well, I know a thing or two."
    gabriel "About?"
    scarlet "I um...I have, well...yeah. You know...what you have."
    naomi "You have to be joking. There's no-"
    #scarlet invited to the gang
    gabriel "You don't have to say. I understand. You can join us for the next semester, if you like. Maintain the place like the rest of us and you're fine to join."
    scarlet "Thank you!"
    naomi "I really don't think this is a good idea."
    scarlet "Aww. Here I was thinking we'd be good friends."
    naomi "Yeah...not happening."
    hide naomi
    show carson at top
    carson "We did the same for you, Naomi, if you recall. She's great fun, don't worry about it! We'll have a blast!"
    "The professor arrives. You finish your last final."
    #finals score
    scene black
    with fade
    "..."
    if tempGrade == 0:
        "You failed your finals."
        $ happiness -= 5
    elif tempGrade == 1:
        "You got a D average."
        $ happiness -= 3
    elif tempGrade == 2:
        "You got a C average."
        $ happiness -= 1
    elif tempGrade == 3:
        "You got a B average."
        $ happiness += 1
    elif tempGrade == 4 or tempGrade > 4:
        "You aced your finals!"
        $ happiness += 3
    else:
        "There was an error with your grade, so you were given a C."
        $ happiness -= 1
        $ tempGrade = 2
    $ grade = tempGrade
    if tempGrade > 0:
        $ tempGrade -= 1
    #scarlet talks with the gang
    scene bg entrance
    with fade
    "You arrive at the house."
    "You can hear voices in the lobby."
    brandon "And who's this?"
    gabriel "This is Scarlet. She'll be joining us for the next semester."
    scarlet "Good to meet you."
    brandon "Are you running a zoo, now? Is that what this place is?"
    gabriel "Our other two guests have been great, what's one more?"
    brandon "I think we just got lucky with the other two. I wouldn't push our luck."
    "You head into the lobby."
    scene bg lobby
    with fade
    show lucas at midleft
    show scarlet at midmidleft
    show gabriel at midmidright
    show brandon at midright
    gabriel "Welcome back."
    scarlet "Oh, hey!"
    brandon "Let's just be careful, alright? Now that we have a civilian here, we'll have to be even more careful."
    scarlet "I'm not a civilian, I have magic like you."
    brandon "You...do? That can't be a coincidence, that's an omen. Twice now? That's improbable."
    scarlet "Whatever you say, old man."
    brandon "Old man? I'm the youngest one here!"
    "Gabriel is laughing."
    brandon "It's not funny."
    "Gabriel continues laughing."
    brandon "Whatever. I'm heading to my library. You can sort things out."
    hide brandon
    "Brandon walks away."
    scarlet "He should try using that stick up his ass instead of magic."
    gabriel "'Old man', oh man, he definitely hates that. Scarlet, take one of the rooms upstairs. We'll figure out whatever work we need you to do later."
    scarlet "Oh, thank you!"
    hide scarlet
    "Scarlet heads upstairs."
    gabriel "I haven't found something that funny in a long time. 'Old man', it suits him too well!"
    "Gabriel eventually stops laughing."
    gabriel "Well, enjoy the winter break. Oh, and I got everyone's grades back. They're likely not going to care until the semester starts up again, so you might be able to hang with someone you normally wouldn't."
    #next set of events ignore grades
    scene bg lobby
    with fade
    "How should you enjoy the break?"
    menu day11:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Scarlet?":
            "You decide to ask Scarlet."
            show scarlet at truecenter
            scarlet "Lucas, just who I was looking for! Let's go out somewhere."
            lucas "Alright."
            $ happiness -= 1
            call scene_scarlet1
        "Gabriel?" if last_person is not "Gabriel":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Carson?" if not carson_check:
            "You decide to ask Carson."
            show carson at truecenter
            lucas "What's up, Carson?"
            carson "Not much, not much, what's up with you?"
            lucas "You up to do something?"
            carson "Thought you'd never ask!"
            if not carson2:
                call scene_carson2
            elif not carson3:
                call scene_carson3
            else:
                call max("Carson")
        "Brandon?" if not brandon_check:
            "You decide to ask Brandon."
            if not brandon1:
                "You head to the study."
                "You knock on the door."
                show brandon at truecenter
                brandon "What?"
                lucas "Do you want to do something?"
                brandon "Sure. Come inside and we'll study."
                call scene_brandon1
            elif not brandon2:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's head to my library."
                call scene_brandon2
            elif not brandon3:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's head to my library."
                call scene_brandon3
            else:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's have a chat."
                call max("Brandon")
        "London?" if not london_check:
            "You decide to ask London."
            show london at truecenter
            lucas "Are you up for a chat, London?"
            london "You know what? I guess I am."
            if not london1:
                call scene_london1
            elif not london2:
                call scene_london2
            elif not london3:
                call scene_london3
            else:
                call max("London")
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "Where should you spend your time?"
    menu day12:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Scarlet?" if last_person is not "Scarlet":
            "You decide to ask Scarlet."
            show scarlet at truecenter
            scarlet "Lucas, just who I was looking for! Let's go out somewhere."
            lucas "Alright."
            $ happiness -= 1
            call scene_scarlet1
        "Carson?" if not carson_check and last_person is not "Carson":
            "You decide to ask Carson."
            show carson at truecenter
            lucas "What's up, Carson?"
            carson "Not much, not much, what's up with you?"
            lucas "You up to do something?"
            carson "Thought you'd never ask!"
            if not carson2:
                call scene_carson2
            elif not carson3:
                call scene_carson3
            else:
                call max("Carson")
        "Adrian?" if not adrian_check:
            "You decide to ask Adrian."
            show adrian at truecenter
            lucas "Adrian, do you want to do something today?"
            adrian "Yeah, sure, sounds like fun."
            if not adrian1:
                call scene_adrian1
            elif not adrian2:
                call scene_adrian2
            elif not adrian3:
                call scene_adrian3
            else:
                call max("Adrian")
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if not brandon1:
                "You head to the study."
                "You knock on the door."
                show brandon at truecenter
                brandon "What?"
                lucas "Do you want to do something?"
                brandon "Sure. Come inside and we'll study."
                call scene_brandon1
            elif not brandon2:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's head to my library."
                call scene_brandon2
            elif not brandon3:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's head to my library."
                call scene_brandon3
            else:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's have a chat."
                call max("Brandon")
        "London?" if not london_check and last_person is not "London":
            "You decide to ask London."
            show london at truecenter
            lucas "Are you up for a chat, London?"
            london "You know what? I guess I am."
            if not london1:
                call scene_london1
            elif not london2:
                call scene_london2
            elif not london3:
                call scene_london3
            else:
                call max("London")
        "Study?":
            call study
    call set_false

    #the party, unfortunately for carson
    scene bg lobby
    with fade
    "Winter break continues..."
    "Rain platters against the windows."
    show carson at midright
    carson "There's this big party some friends of mine are going to, why don't you guys come join us? It'll be a blast!"
    show gabriel at midleft
    gabriel "In this weather? You'll catch a cold, man."
    carson "Cold, shmold, it would be worth it! And we can all go, too! A bunch of people are going to be there!"
    gabriel "Alright, but it's your funeral."
    show brandon at truecenter
    brandon "You guys can go have your fun."
    hide gabriel
    hide carson
    show adrian at midright
    show lucas at midright
    adrian "You should come with us, you'll have plenty of time to be alone in your library afterwards."
    brandon "It's just not for me."
    menu:
        brandon "It's just not for me."
        "You should come with us.":
            lucas "You should come with us."
            adrian "Hey, how about if it really is that boring, we can just head back early?"
            "Brandon frowns."
            brandon "Alright, I'll go."
            adrian "Nice! C'mon, let's go!"
        "Keep the place warm for us.":
            lucas "Keep the place warm for us."
            adrian "Hey, hey, whoa there, you can't give up that easily!"
            lucas "He just wants to stay here."
            adrian "Alright, alright, I get it. We'll be sure to tell you all the fun things you missed, though!"
            $ brandon_stay = False
    scene bg party
    with fade
    "The party is lively."
    "Some people are wary of your friends, and others are welcoming."
    "You manage to have a little fun."
    show lucas at midleft
    show naomi at midmidleft
    naomi "Hey Lucas! Isn't this great?"
    lucas "I guess."
    naomi "You should enjoy yourself more! It's a party!"
    #if brandon joins the party, he talks a bit about his studies
    if brandon_stay:
        show brandon at midright
        show adrian at midmidright
        brandon "I'm with Lucas on this. Parties just aren't our thing."
        adrian "You need to enjoy yourself every once in a while, you can't just sit in that library all day."
        naomi "What do you even do in there? You're in there so often, you can't be studying all the time."
        brandon "I'm studying magic, actually. Browsing through history is very interesting, and with how little we know of magic, I'm bound to find something."
        show adrian serious
        adrian "Wait, you're not just studying all day?"
        show brandon happy
        brandon "I get some studying done. In my free time I look at magic. I don't know how to describe it, it's just...fascinating."
        naomi "What do you study about magic?"
        brandon "Anything I can. The origin, the aftermath, the catalog, it's all there."
        menu:
            brandon "Anything I can. The origin, the aftermath, the catalog, it's all there."
            "The origin?":
                lucas "The origin?"
                brandon "It's not exactly exemplary. I don't know how, but supposedly the Acrad government found that magic could be given to use through modifying our genetics."
                adrian "How...would that even work? How would they even find that out?"
                brandon "I have no idea. They were desperate during the war. They were probably just happy that they could turn the tide."
                "Carson and Scarlet walk past you, and go out the door."
                adrian "Carson, you sly dog."
                naomi "The war was that bad?"
                brandon "They'd almost lost half the country. Desperate measures lead to their terrible actions."
                naomi "Why would giving magic to us be terrible?"
                brandon "Taking children away from families to give them magic, I'd say that's terrible. Some people also shouldn't have been given the power."
                adrian "Like Miss Fortune."
                brandon "They didn't know magic would pass down, we can't blame them for that. They did create some abominations, though. London's mother, for example...just terrible what they did to her."
                naomi "How bad...was it?"
                brandon "Let's see...if I remember right, flexibility, flammability, invisibility, duplication, unstable teleportation..."
                adrian "Oh."
                brandon "Aura reading for death, blood, bond, empathy, wealth, life, magic..."
                naomi "Oh my."
                brandon "Doppelganger, ghost form, guardian angel, gaze, levitation, charge, duel, and immunity...I think that's all."
                adrian "So that's why London can do more than us...that, actually is kinda interesting."
                brandon "Her mother must have been in so much pain from all the testing they did. Supposedly, it wasn't just 'flick a switch and it works.'"
                adrian "Which ones did London inherit?"
                brandon "She has the least of her siblings, just aura read death, ghost form, flammability, and invisibility."
                $ london_known = True
                adrian "Oh, she's gotta be jealous, right?"
            "The aftermath?":
                lucas "The aftermath?"
                brandon "We are the aftermath. We all found out magic was passed down genetically after the war. It'll spread, and that worries me a little."
                naomi "I think everyone should have magic! Magic is just so cool and fun!"
                brandon "'Cool' and 'fun' don't mean anything if magic can just as easily be misused. That's why we're all here in the first place."
                "Carson and Scarlet walk past you, and go out the door."
                adrian "Carson, you sly dog."
                lucas "Gabriel said your first year of college is being paid for."
                brandon "They don't know what to do with us. Magic can be dangerous, and even children can wield magic. Do you trust a toddler with magic?"
                naomi "I guess not..."
                adrian "Did you two have issues growing up with magic?"
                lucas "No."
                naomi "Well, we lived in the countryside. My dad and Lucas' mom had magic, so they both knew what to do."
                brandon "That's great and all, but imagine if you instead grew up in the city. Kids will do and say anything. It's a miracle we don't have that many stories."
                adrian "That was probably why most of us were sheltered, then. That was actually smart of them, I wouldn't have thought to do that."
                brandon "That's only what we know of in Acrad. There might be stories from other countries that we just haven't heard, though they'd point fingers at us if there was a story."
                naomi "We haven't heard of anything out east."
                adrian "Where are you from, Galm?"
                lucas "You nailed it."
                naomi "It doesn't hold a candle to how cool Acrad is!"
                lucas "That's just because we lived on barns."
                naomi "Yes, but this place is still amazing!"
                brandon "I wonder...did your parents move out there to get away from potential Acrad laws?"
                naomi "What do you mean?"
                brandon "If magic was made illegal, the Acrad government would have a list of people with magic. Maybe your parents noticed that, and moved out there just in case."
                naomi "Our parents with magic left us awhile ago..."
                adrian "Damn, I'm sorry, I don't know what that'd be like. Did they leave to protect you, assuming Brandon is right?"
                lucas "It's a possibility."
            "The catalog?":
                lucas "The catalog?"
                adrian "Oh boy, here we go..."
                brandon "The catalog, great question! I've been noting down all the forms of magic we've come across, and looking back at the people in the war and logging their magic."
                adrian "I still think that's a little weird that you just have that..."
                "Carson and Scarlet walk past you, and go out the door."
                adrian "Carson, you sly dog."
                brandon "It's wonderful that I have it, actually! Think about the possibilities of being able to publish my work in the future! I'd be set for life."
                adrian "You want to publish that we have magic? That feels a little weird...like, everyone knowing what I can do? That can't go right."
                brandon "It does invade privacy a little bit, yes, but think! If everyone has their magic catalogued in the future, then it would be fair to everyone."
                naomi "I don't want everyone knowing what I can do."
                brandon "Think of the bigger picture!"
                lucas "I'm good, thanks."
                brandon "You just don't see my vision, and that's ok. I'd be the first person to have ruthlessly studied magic!"
                adrian "Sounds to me like you're ruthlessly asking for all of us to beat you up when you publish that."
                brandon "'When' I publish it, I like how you think!"
                adrian "You...seriously don't see anything wrong with telling the world about our magic? No problems whatsoever?"
                brandon "In the short term, it might be an issue, yes. Think of the long term! When genetics move around enough in the distant future, it'd be fantastic to see!"
                adrian "You're not even going to be alive to see it, that's way too far off in the future."
                brandon "I'd be a founding father for magic studies. Think of how famous I would be!"
                adrian "The second London finds out about what you'd done, you're gone, she would hunt you down and kill you relentlessly."
                brandon "We all make sacrifices in the pursuit of knowledge. You'll see."
        hide adrian
        hide brandon
    #brandon not at the party
    else:
        show london at midright
        show sarah at midmidright
        sarah "That's what you need to do, London."
        london "Enjoy parties?"
        sarah "Just enjoy things in general...you haven't been doing that for a long time..."
        #if london and gabriel are dating, the london is more relaxed
        if dating:
            show london happy
            london "Gabriel's been helping me with that."
            sarah "Well, I think he's doing great. You're much happier than before."
            london "I'd rather not talk about what happened."
            sarah "It's ok...I think we all want to forget some things..."
            "Carson and Scarlet walk past you, and go out the door."
            sarah "Oh, are we leaving already?"
            london "It was just those two."
            sarah "Are they tired already?"
            naomi "I don't-"
            london "You're joking, right?"
            sarah "I...what?"
            "London begins to laugh."
            london "I need to protect that inno-wait, hang on, you're not innocent!"
            sarah "I'm...not?"
            london "I was never a-"
            "Sarah gasps loudly."
            sarah "Please don't talk about that!"
            london "Sorry."
            sarah "It's...fine."
            london "You seem cheery as well."
            sarah "Do I?"
            london "Considering how much you've talked just here?"
            naomi "You're a lot happier than when we went to get smoothies, and I think it's great!"
            sarah "Oh, thank you. You're too kind."
        else:
            london "What, are you trying to throw a pity party? Save it."
            sarah "I was just...trying to-"
            london "I don't care what you were trying to do, you can save it for someone else."
            sarah "Ok! Sorry!"
            "Carson and Scarlet walk past you, and go out the door."
            sarah "I guess we're leaving..."
            london "No, they're just leaving."
            sarah "Are they tired already?"
            naomi "I don't-"
            london "Do I {i}really{/i} have to spell it out for you?"
            sarah "Why are you looking at me like that?"
            london "I don't know how you do it."
            sarah "Do what?"
            london "How are you so thick headed?"
            sarah "That hurts, London."
            naomi "Let's not have another fight, ok?"
            show london mad
            london "Like you'd know anything about what we went through!"
            sarah "It's fine, London, you don't have to overreact, we're all friends here."
            london "{i}I'M{/i} overreacting? Let's not forget when you tried to jump off the school roof! Or when-"
            "Sarah lets out a large gasp."
            sarah "Why would you say that!"
            "Sarah is holding back tears."
            sarah "That was so mean! Why would you ever say that?!"
        hide london
        hide sarah
    #scarlet rushes back in
    show scarlet at midright
    "Scarlet rushes through the front door."
    scarlet "Where's Gabriel? Gabriel!"
    naomi "What's wrong?"
    scarlet "Help me find Gabriel!"
    "You help find Gabriel. He's with the rest of your friends."
    scarlet "Gabriel, it's Carson, he...just follow me!"
    "Scarlet rushes to the door."
    "The rest of you look at each other and follow Scarlet."
    #surely nothing bad happens to carson
    scene bg rainy city
    with fade
    "The city is lively at this time of night."
    "The rain pours as you run after Scarlet."
    "Through the pitter patter of your feet against the concrete, you wonder what could have happened."
    "Scarlet turns a corner, and as you turn the same corner, you see Scarlet over a figure lying on the ground."
    "You see where the panic in her voice came from."
    "Carson is immobile on the ground, lifeless."
    "Panic comes over the group as they try to wake Carson up."
    "Naomi and Sarah begin to cry, Adrian and London console them."
    show lucas at midleft
    if brandon_stay:
        show gabriel serious at midright
        show brandon at midmidright
        "Gabriel and Brandon look Carson over."
    else:
        show gabriel serious at midright
        "Gabriel looks Carson over."
    gabriel "What the hell happened?!"
    show scarlet at midmidleft
    scarlet "I don't know! I turned away from him for a bit and when I turned back, he had walked into traffic!"
    gabriel "Don't give me that, what actually happened?!"
    scarlet "That's what happened, what else am I supposed to say?!"
    gabriel "Lucas, you can fix him, right?!"
    "You aim your hands at Carson."
    "Your magic turns to steam in the rain. Your hands feel notably warmer than usual."
    if brandon_stay:
        brandon "Oh, now that's very interesting to see..."
    gabriel "C'mon man, do something!"
    "You can't fix Carson."
    "He's gone."
    if brandon_stay:
        brandon "He's dead."
        gabriel "He can't be! We can't lose him! We have to do something!"
        brandon "There's nothing more we can do. No amount of magic can bring life back."
        "You hear Naomi and Sarah's cries grow much louder."
    else:
        show london at midmidright
        london "He's dead, Gabriel."
        gabriel "He can't be! We can't lose him! We have to do something!"
        london "Gabriel...I'm sorry. There's nothing we can do."
        "You hear Naomi and Sarah's cries grow much louder. London turns away from you and continues comforting them."
        hide london
    gabriel "C'mon Lucas! You have to help him!"
    lucas "I can't bring him back to life."
    gabriel "Don't give me that monotone voice! Just help him!"
    scarlet "He said he can't! We're sorry, but...I think he's...gone."
    "Gabriel gets out of your face and turns back to Carson."
    gabriel "Damn it...damn it all! Why would you do this?! You were doing so well!"
    $ carson_dead = True
    #bump up apathy a ton
    scene bg black
    with fade
    "Carson is gone."
    show apathy_up at topleft
    $ apathy -= 10
    if apathy > 0:
        $ apathy += 15
    else:
        $ apathy *= -1
        $ apathy += 15
    "All the care that you showed was a waste."
    "It was all worthless."
    "You should've known better."
    "The walk back to the house was silent, with mixed sniffling from your friends."
    "Friends until they leave you."

    scene bg room
    with fade
    show apathy_up at topleft
    "You arrived home and went straight to your room."
    "You've been staring at the ceiling for what feels like ages."
    if carson2:
        $ apathy += 5
    "You hear a thud from downstairs."
    "It must be lively down there."
    "Time continues to pass as you think of Carson."
    "To spend time with him, just for him to walk into death..."
    "Shows how much he really cared."
    if carson3:
        $ apathy += 10
    "Shows why you shouldn't have cared."
    "Time drifts further into the night."

    scene bg black
    with fade
    "You should leave."
    "If you leave now, you won't be hurt again."
    "They can't leave you if you leave them first."

    scene bg entrance
    with fade
    show lucas at midleft
    show naomi sad at midright with moveinright
    naomi "Where are you going?"
    lucas "Does it matter?"
    naomi "I'll go with you."
    luacs "You don't have to."
    naomi "But I want to. Ow! Stop, please!"
    "You turn to Naomi, who appears to be gripping her leg."
    lucas "You'll just end up hurting yourself."
    "You stop walking out. Naomi walks towards you."
    naomi "I don't care! I want to protect-"
    "Naomi falls down and yelps in pain."
    "You rush to pick her up."
    lucas "You don't need to protect me."
    naomi "I want to. Please. Just take me with you, wherever you're going. I want to be your strength. My life will be worth living if I can see you happy. Please, don't abandon me, too."
    "Naomi is on the verge of tears."
    "You stop and think."
    "Do you really want to leave?"
    "Do you really want to leave your friends behind? Naomi behind?"
    "For the first time in forever, you have a choice that you want to take, something that won't be made for you."
    "You want to stay."
    "As foolish as I may think, you still want to be with your friends."
    lucas "I'll stay."
    show naomi
    show apathy_down at topleft
    $ apathy -= 5
    "Naomi jumps up to hug you."
    "You awkwardly have to wait for her to release you."
    "It feels like an eternity."
    hide apathy_down
    lucas "How'd you hurt your leg, anyway?"
    naomi "I kicked a wall."
    lucas "You...what?"
    naomi "I was just angry and upset, and I didn't want to break anything magic so I...kicked one of the walls."
    lucas "And the wall won?"
    naomi "Don't you rub it in! I know!"
    "Despite her words, Naomi is smiling."
    naomi "I'm going to just rest for the rest of winter break. I need to get my leg checked out. You should still talk to the others, ok?"
    lucas "Alright."
    "Naomi aims her hands at you."
    naomi "You know I hate it when you say that!"
    lucas "Yeah, yeah."
    hide naomi
    "You help Naomi to her room."
    "When you go to head back to your room, you see Gabriel in the hallway."
    show gabriel at midright
    gabriel "Hey, man, I'm sorry. I know you did what you could. Sorry for how I treated you."
    lucas "I understand. It's alright."
    gabriel "Yeah. Anyway, though...get some rest. I'm sure people will want to talk tomorrow. Get some rest, yeah?"
    #meet with everyone
    scene bg lobby
    with fade
    "Yesterday was a nightmare."
    "You head down to the lobby. Everyone is gathered and talking."
    show lucas at midleft
    show naomi at midmidleft
    show gabriel at midright
    gabriel "Hey, sleepyhead."
    naomi "Cut him some slack!"
    gabriel "Alright, alright."
    show london at midmidright
    if not dating:
        london "So we can just cut anyone slack, now?"
        gabriel "I understand you're upset."
        london "I'm not upset about Carson, I'm upset about your special treatment."
        gabriel "No one's getting special treatment."
        london "Uh huh."
    else:
        london "Are you alright, Naomi?"
        naomi "I'm fine. I'm fine!"
        london "It's alright. I understand your frustrations. It's ok."
    hide london
    show brandon at midmidright
    if not brandon_stay:
        call scene_brandonr1
    else:
        show brandon happy
        brandon "Before I forget, there was something that happened with your magic that piqued my interest."
        brandon "You saw what happened with your magic, right? Where it turned to steam in the rain?"
        lucas "I guess I've never used it in the rain before."
        brandon "Remember that well. It looks like your magic dissipates and turns to steam in water."
        brandon "You know, with how that shield works, you might be able to effectively cook someone if you shield them and they fall into water. I'd be very curious as to-"
        gabriel "Let's not jump to tests with magic, man. Remember, we're trying to use it as little as possible."
        brandon "Maybe next time, then."
    hide brandon
    hide lucas
    hide naomi
    hide gabriel

    "It seems like the friends are lively, despite the recent death."
    "Are they used to it?"
    #continue events
    "Regardless, winter break continues..."
    scene bg lobby
    with fade
    "Who should join you today?"
    menu day13:
        "Scarlet?" if last_person is not "Scarlet":
            "You decide to ask Scarlet."
            show scarlet at truecenter
            scarlet "Lucas, just who I was looking for! Let's go out somewhere."
            lucas "Alright."
            if not scarlet1:
                call scene_scarlet1
            else:
                call scene_scarlet2
        "Gabriel?":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if not brandon1:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's head to my library."
                call scene_brandon1
            elif not brandon2:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's head to my library."
                call scene_brandon2
            elif not brandon3:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's head to my library."
                call scene_brandon3
            else:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's have a chat."
                call max("Brandon")
        "London?" if not london_check and last_person is not "London":
            "You decide to ask London."
            show london at truecenter
            lucas "Are you up for a chat, London?"
            london "You know what? I guess I am."
            if not london1:
                call scene_london1
            elif not london2:
                call scene_london2
            elif not london3:
                call scene_london3
            else:
                call max("London")
        "Sarah?" if not sarah_check:
            "You decide to ask Sarah."
            show sarah at truecenter
            lucas "Hi Sarah, do you want to do something today?"
            sarah "That...sounds nice, actually."
            if not sarah1:
                call scene_sarah1
            elif not sarah2:
                call scene_sarah2
            else:
                call scene_sarah3
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "Carson's death is still fresh in your mind..."
    menu day14:
        "Scarlet?" if last_person is not "Scarlet":
            "You decide to ask Scarlet."
            show scarlet at truecenter
            scarlet "Lucas, just who I was looking for! Let's go out somewhere."
            lucas "Alright."
            if not scarlet1:
                call scene_scarlet1
            else:
                call scene_scarlet2
        "Adrian?" if not adrian_check:
            "You decide to ask Adrian."
            show adrian at truecenter
            lucas "Adrian, do you want to do something today?"
            adrian "Yeah, sure, sounds like fun."
            if not adrian1:
                call scene_adrian1
            elif not adrian2:
                call scene_adrian2
            elif not adrian3:
                call scene_adrian3
            else:
                call max("Adrian")
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if not brandon1:
                "You head to the study."
                "You knock on the door."
                show brandon at truecenter
                brandon "What?"
                lucas "Do you want to do something?"
                brandon "Sure. Come inside and we'll study."
                call scene_brandon1
            elif not brandon2:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's head to my library."
                call scene_brandon2
            elif not brandon3:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's head to my library."
                call scene_brandon3
            else:
                show brandon at truecenter
                lucas "Do you want to do something, Brandon?"
                brandon "Sure. Let's have a chat."
                call max("Brandon")
        "Sarah?" if not sarah_check and last_person is not "Sarah":
            "You decide to ask Sarah."
            show sarah at truecenter
            lucas "Hi Sarah, do you want to do something today?"
            sarah "That...sounds nice, actually."
            if not sarah1:
                call scene_sarah1
            elif not sarah2:
                call scene_sarah2
            else:
                call scene_sarah3
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "Winter break is over soon...how have they forgotten about Carson?"
    menu day15:
        "Scarlet?" if last_person is not "Scarlet":
            "You decide to ask Scarlet."
            show scarlet at truecenter
            scarlet "Lucas, just who I was looking for! Let's go out somewhere."
            lucas "Alright."
            if not scarlet1:
                call scene_scarlet1
            elif not scarlet2:
                call scene_scarlet2
            else:
                call scene_scarlet3
        "Gabriel?":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Adrian?" if not adrian_check and last_person is not "Adrian":
            "You decide to ask Adrian."
            show adrian at truecenter
            lucas "Adrian, do you want to do something today?"
            adrian "Yeah, sure, sounds like fun."
            if not adrian1:
                call scene_adrian1
            elif not adrian2:
                call scene_adrian2
            elif not adrian3:
                call scene_adrian3
            else:
                call max("Adrian")
        "Sarah?" if not sarah_check and last_person is not "Sarah":
            "You decide to ask Sarah."
            show sarah at truecenter
            lucas "Hi Sarah, do you want to do something today?"
            sarah "That...sounds nice, actually."
            if not sarah1:
                call scene_sarah1
            elif not sarah2:
                call scene_sarah2
            elif not sarah3:
                call scene_sarah3
            else:
                call max("Sarah")
        "Study?":
            call study
    call set_false

    scene bg berger hall
    with fade
    "The spring semester starts..."
    #people care about grades, naomi is back
    scene bg lobby
    with fade
    "What should you do?"
    menu day16:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Scarlet?" if last_person is not "Scarlet":
            "You decide to ask Scarlet."
            show scarlet at truecenter
            scarlet "Lucas, just who I was looking for! Let's go out somewhere."
            lucas "Alright."
            if not scarlet1:
                call scene_scarlet1
            elif not scarlet2:
                call scene_scarlet2
            elif not scarlet3:
                call scene_scarlet3
            else:
                call max("Scarlet")
        "Gabriel?" if last_person is not "Gabriel":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Brandon?" if not brandon_check:
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                elif not brandon2:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
                elif not brandon3:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon3
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's have a chat."
                    call max("Brandon")
            else:
                call brandon_deny
                hide brandon
                jump day16
        "London?" if not london_check:
            "You decide to ask London."
            show london at truecenter
            if grade < londonGrade:
                lucas "Are you up for a chat, London?"
                london "You know what? I guess I am."
                if not london1:
                    call scene_london1
                elif not london2:
                    call scene_london2
                elif not london3:
                    call scene_london3
                else:
                    call max("London")
            else:
                call london_deny
                hide london
                jump day16
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "Where should you spend your time?"
    menu day17:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Adrian?" if not adrian_check:
            "You decide to ask Adrian."
            show adrian at truecenter
            if grade > adrianGrade:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                elif not adrian2:
                    call scene_adrian2
                elif not adrian3:
                    call scene_adrian3
                else:
                    call max("Adrian")
            else:
                call adrian_deny
                hide adrian
                jump day17
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                elif not brandon2:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
                elif not brandon3:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon3
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's have a chat."
                    call max("Brandon")
            else:
                call brandon_deny
                hide brandon
                jump day17
        "London?" if not london_check and last_person is not "London":
            "You decide to ask London."
            show london at truecenter
            if grade < londonGrade:
                lucas "Are you up for a chat, London?"
                london "You know what? I guess I am."
                if not london1:
                    call scene_london1
                elif not london2:
                    call scene_london2
                elif not london3:
                    call scene_london3
                else:
                    call max("London")
            else:
                call london_deny
                hide london
                jump day17
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "What are the plans today?"
    menu day18:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Gabriel?":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                elif not brandon2:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
                elif not brandon3:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon3
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's have a chat."
                    call max("Brandon")
            else:
                call brandon_deny
                hide brandon
                jump day18
        "London?" if not london_check and last_person is not "London":
            "You decide to ask London."
            show london at truecenter
            if grade < londonGrade:
                lucas "Are you up for a chat, London?"
                london "You know what? I guess I am."
                if not london1:
                    call scene_london1
                elif not london2:
                    call scene_london2
                elif not london3:
                    call scene_london3
                else:
                    call max("London")
            else:
                call london_deny
                hide london
                jump day18
        "Sarah?" if not sarah_check:
            "You decide to ask Sarah."
            show sarah at truecenter
            if grade > sarahGrade:
                lucas "Hi Sarah, do you want to do something today?"
                sarah "That...sounds nice, actually."
                if not sarah1:
                    call scene_sarah1
                elif not sarah2:
                    call scene_sarah2
                elif not sarah3:
                    call scene_sarah3
                else:
                    call max("Sarah")
            else:
                call sarah_deny
                hide sarah
                jump day18
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "What's going to happen today?"
    menu day19:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Scarlet?":
            "You decide to ask Scarlet."
            show scarlet at truecenter
            scarlet "Lucas, just who I was looking for! Let's go out somewhere."
            lucas "Alright."
            if not scarlet1:
                call scene_scarlet1
            elif not scarlet2:
                call scene_scarlet2
            elif not scarlet3:
                call scene_scarlet3
            else:
                call max("Scarlet")
        "Adrian?" if not adrian_check:
            "You decide to ask Adrian."
            show adrian at truecenter
            if grade > adrianGrade:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                elif not adrian2:
                    call scene_adrian2
                elif not adrian3:
                    call scene_adrian3
                else:
                    call max("Adrian")
            else:
                call adrian_deny
                hide adrian
                jump day19
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                elif not brandon2:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
                elif not brandon3:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon3
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's have a chat."
                    call max("Brandon")
            else:
                call brandon_deny
                hide brandon
                jump day19
        "Sarah?" if not sarah_check and last_person is not "Sarah":
            "You decide to ask Sarah."
            show sarah at truecenter
            if grade > sarahGrade:
                lucas "Hi Sarah, do you want to do something today?"
                sarah "That...sounds nice, actually."
                if not sarah1:
                    call scene_sarah1
                elif not sarah2:
                    call scene_sarah2
                elif not sarah3:
                    call scene_sarah3
                else:
                    call max("Sarah")
            else:
                call sarah_deny
                hide sarah
                jump day19
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    "Midterms are coming up..."
    menu day20:
        "Naomi?" if last_person is not "Naomi":
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Gabriel?":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Adrian?" if not adrian_check and last_person is not "Adrian":
            "You decide to ask Adrian."
            show adrian at truecenter
            if grade > adrianGrade:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                elif not adrian2:
                    call scene_adrian2
                elif not adrian3:
                    call scene_adrian3
                else:
                    call max("Adrian")
            else:
                call adrian_deny
                hide adrian
                jump day20
        "Sarah?" if not sarah_check and last_person is not "Sarah":
            "You decide to ask Sarah."
            show sarah at truecenter
            if grade > sarahGrade:
                lucas "Hi Sarah, do you want to do something today?"
                sarah "That...sounds nice, actually."
                if not sarah1:
                    call scene_sarah1
                elif not sarah2:
                    call scene_sarah2
                elif not sarah3:
                    call scene_sarah3
                else:
                    call max("Sarah")
            else:
                call sarah_deny
                hide sarah
                jump day20
        "Study?":
            call study
    call set_false

    scene bg hallway
    with fade
    "Midterms have arrived..."
    "..."
    "..."
    "..."
    scene black
    with fade
    if tempGrade == 0:
        "You failed your midterms."
        $ happiness -= 5
    elif tempGrade == 1:
        "You got a D average."
        $ happiness -= 3
    elif tempGrade == 2:
        "You got a C average."
        $ happiness -= 1
    elif tempGrade == 3:
        "You got a B average."
        $ happiness += 1
    elif tempGrade == 4 or tempGrade > 4:
        "You aced your midterms!"
        $ happiness += 3
    else:
        "There was an error with your grade, so you were given a C."
        $ happiness -= 1
        $ tempGrade = 2
    $ grade = tempGrade
    if tempGrade > 0:
        $ tempGrade -= 1
    #the group is is vacationing for the break
    scene bg lobby
    with fade
    "You arrive home."
    show gabriel at truecenter
    gabriel "Hope none of you have plans, because I've made plans for us."
    show lucas at midleft with moveinleft
    show naomi at midmidleft with moveinleft
    show gabriel at midmidright with moveinleft
    naomi "What plans?"
    gabriel "For one of our classes, we have to visit another city. I figured it'd be great for all of us to go, and I managed to get all of us on the trip."
    show adrian at midright
    adrian "Do we have to fill anything out for it?"
    gabriel "Nah, just have to visit for a day or two."
    adrian "Then it's just an honor system, so why don't we just say we went?"
    gabriel "I would expect that from Carson, but you, man?"
    "Silence falls on the room."
    gabriel "Sorry."
    adrian "No, you're good, I think I speak for all of us when I say we all understand."
    if gabriel3:
        gabriel "Yeah. We all miss him, but all we can do is move on."
        adrian "I'm with you. We're all right there with you, chief."
        gabriel "I'll let the 'chief' comment slide this time...next time you're not going to be so lucky."
        adrian "You got it, chief."
        "Gabriel looks blankly at Adrian"
        adrian "Aaaaaanyway, where are we going for the trip?"
    else:
        show gabriel serious
        gabriel "Wish I could've done something about it."
        show adrian serious
        adrian "Don't beat yourself up over it, you did everything you could."
        gabriel "I just wish I could've done more...I wasn't good enough to stop it."
        adrian "Dude, just shut the hell up. We're all missing him, alright?"
        gabriel "Sorry."
        adrian "Where are we going for the trip?"
        show gabriel
    gabriel "We're headed to Athvel. It's about an hour west of here."
    naomi "Isn't that your capital?"
    gabriel "Yeah, but it's nothing impressive. It's just a bigger place than here."
    naomi "How could you get bigger than this city? This place is so huge!"
    "Gabriel and Adrian look at each other."
    adrian "Well you see, it's bigger."
    "Gabriel chuckles."
    gabriel "Yeah, yeah. Nice one, smartass."
    adrian "When do we head out?"
    gabriel "As soon as everyone's here and packed. We'll only be out for a couple days, so pack light."
    #visit the city
    scene bg city2
    with fade
    show gabriel at midright
    show lucas at midleft
    show scarlet at truecenter
    gabriel "Here we are. Looks different than what we're used to, yeah?"
    scarlet "I haven't been here in such a long time."
    gabriel "Good memories of this place?"
    scarlet "Not in the slightest."
    if gabriel3:
        gabriel "Sorry to hear."
        scarlet "Save it."
        gabriel "I'm just giving consolation, no need to be so testy."
    else:
        gabriel "I'm sorry to hear that."
        scarlet "Save it."
        gabriel "Oh...sorry. I was just-nevermind."
    hide scarlet
    show naomi at midmidleft
    naomi "This place is so huge!"
    gabriel "It's not as big as you think, a lot of the size comes from residential areas."
    naomi "I thought the college was big, this is enormous by comparison!"
    gabriel "We're only here for a couple of days, so enjoy it while you can. It's about time we got to visit this place by choice."
    naomi "You've been here before? What for?"
    gabriel "This was...where we became a group, and where we killed Miss Fortune. We were only here for our work."
    show scarlet at midmidright
    scarlet "Oh? You killed her?"
    gabriel "Wasn't it Brandon?"
    hide naomi
    show brandon at midmidleft
    brandon "Was what me?"
    gabriel "Remember when we fought Miss Fortune, that was you next to her at the end, right?"
    brandon "I try not to think about it."
    scarlet "Did she deserve it? Was she that bad of a person?"
    brandon "She did terrible things not just to us, but to anyone who visited her."
    scarlet "That's still murder."
    brandon "She directly 'murdered' two of us there. Indirectly, she killed six more of us. I'd say it was deserved."
    gabriel "Hey, hey, let's calm down. We're here to enjoy ourselves, move on from the experience. Let's drop our stuff off and find something to do, yeah?"
    brandon "I agree."
    scarlet "Don't you think about what you've done all the time? How do you live with yourself?"
    brandon "Shit things happen. I'd rather move on than live in the past all the time."
    gabriel "Alright, that's enough of that. We're enjoying ourselves."
    #the gang tours the city
    scene black
    with fade
    "After dropping your things in a hotel, your friends drag you around the city."
    show gabriel at midleft
    show london at midright
    london "Why the hell are we going to a museum?"
    gabriel "To see all the relics from the war!"
    hide gabriel
    hide london
    show adrian at midleft
    show sarah at midright
    sarah "There's a monument over there to my dad...for all the work he did in the war."
    adrian "Really? That looks nothing like your dad, it's just a statue of a clover."
    sarah "You...ok, that was good."
    hide sarah
    hide adrian
    show naomi at midleft
    show brandon at midright
    brandon "See that over there? That's where Miss Fortune ran her business."
    naomi "We can actually go inside?"
    brandon "It was only dangerous with her inside."
    hide brandon
    hide naomi
    show lucas at midleft
    show scarlet at midright
    scarlet "They seem to be having a grand time."
    lucas "You're not?"
    scarlet "I want to get as far away from here as I can."
    lucas "Sorry to hear."
    scarlet "Just...go have fun with them."
    show apathy_down at topleft
    "After time with your friends, it grows dark and you head back."
    $ apathy -= 3
    hide apathy_down
    #invited to talk with naomi
    scene bg lake
    with fade
    "After dark, Naomi invited you for a walk."
    "You talk about your experience in the city, and sit at a bench viewing the lake."
    show lucas at midleft
    show naomi sad at midright
    "Naomi falls suddenly silent."
    lucas "Something wrong?"
    naomi "No, I just...remembered something about Claus."
    lucas "What about?"
    naomi "Claus died in my arms. I was holding him and crying and just hoping it wasn't real. Even in those last moments, he was just wiping the tears off my face and saying it'd be ok."
    lucas "That must have been terrible to experience."
    naomi "He asked me to protect you. His dying wish was for you to be safe. I don't care about anything that happens, I want to keep you safe."
    lucas "You don't need-"
    naomi "I see your potential, I remember your smiles and your laugh and I want to see you happy again."
    lucas "I feel fine, what do you mean?"
    naomi "I believe in friends and laughter and the wonders love can do, I believe in second chances and that's why I believe in you."
    show naomi
    "Naomi rests her head on your shoulder, and continues to look at the lake."
    $ happiness += 5
    "It doesn't seem like she plans to move off you."
    "You open your mouth to say something, but are interrupted."
    show naomi at midmidleft
    show scarlet at midright with moveinright
    scarlet "Aww, I'm touched."
    "Naomi jumps from her position and turns to face Scarlet."
    scarlet "Really wonderful what you have going on. So dreamy."
    naomi "Were you listening to us?!"
    scarlet "Course I was. You two walk off when we're supposed to be resting for the night, obviously something bad might happen. It was all for your safety."
    naomi "You listened to me pouring my heart out! That wasn't meant for anyone else to hear!"
    "Scarlet walks to the lake."
    show scarlet at midmidright with moveinright
    scarlet "Does it matter? So what, I know something about you? I don't care."
    naomi "I care! It's super embarrassing!"
    "Scarlet turns back to you."
    scarlet "You've been hovering around Lucas all this time and you still haven't made him happy. Don't you think it's time to take the hint and leave him alone?"
    naomi "WHAT?"
    scarlet "He can make his own choices, and you'd have been his choie by now if he reciprocated that heartful cry."
    show naomi at truecenter
    "Naomi walks up to Scarlet and slaps her."
    naomi "Just what are you saying, that {i}you{/i} care about him?! You're so fake!"
    scarlet "You think {i}I'M{/i} being fake?"
    "Something is going to happen between them, and it won't be pretty."
    show lucas at midmidleft with moveinleft
    "You walk to get between them and try to diffuse the situation."
    "Scarlet reaches around you and pushes Naomi into the lake."
    "In her stumble, Naomi grabs onto you and drags you down with her."
    "{i}Sploosh!{/i}"
    "You both fall into the lake."
    naomi "Lucas! I'm sorry!"
    "Naomi climbs up and yanks Scarlet into the lake."
    "The two proceed to throw light magic at each other, while you try to calm them down."
    "The situation you find yourself in is unbelievably stupid."
    show apathy_down at topleft
    if smile:
        "So stupid that you get a laugh out of it."
        $ apathy -= 5
        $ happiness += 5
        hide apathy_down
        "Naomi's face lights up with a loud gasp."
        "Scarlet takes the opportunity and knocks Naomi into the water."
        "Naomi shrugs it off and wades straight to you."
        "You're the victim of Naomi's bear hug. She almost knocks you underwater with how she's leaning straight into you."
        naomi "You laughed! You actually did it! I knew I'd make you happy again!"
    else:
        "So stupid that you manage a smile."
        $ apathy -= 3
        $ happiness += 5
        hide apathy_down
        "Naomi's face lights up with a loud gasp."
        "Scarlet takes the opportunity and knocks Naomi into the water."
        "Naomi shrugs it off and wades straight to you."
        "You're the victim of Naomi's bear hug. She almost knocks you underwater with how she's leaning straight into you."
        naomi "You actually smiled! I knew you had it in you!"
    scarlet "Don't you think that's a little long for a hug?"
    naomi "You're just jealous that I'm real, and you have to fake your way through everything. You don't care about anyone but yourself!"
    scarlet "I care enough to let people be free! Look at how you've chained yourself to Lucas, as if you'll get something more! He should be free to make his own decisions!"
    naomi "Lucas is perfectly fine with me making him happy."
    scarlet "Then let's leave it to him. Let him decide."
    lucas "What am I deciding?"
    scarlet "Would you rather be entangled and shackled to Naomi, or would you rather I show you the freedom you deserve?"
    naomi "You can't-"
    scarlet "Leave it to him to decide."
    menu:
        scarlet "Leave it to him to decide."
        "Naomi.":
            lucas "Naomi has been with me since the beginning. She's done so much for me that I couldn't replace her with anyone."
            $ happiness += 10
            scarlet "You should reconsider."
            naomi "It was his choice, right? Why are you mad about it? He's free to make his choice, and I'm what he chose."
            scarlet "Just don't say I didn't warn you."
            hide scarlet
            "Scarlet gets out of the lake and walks back."
            "You and Naomi get out of the lake and return to the bench."
            show lucas at midleft
            show naomi at midright
            naomi "I was a little scared there for a bit. I thought you might've gone with her, to be 'free' as she says."
            lucas "Why would I do that?"
            naomi "I don't know what you two have talked about, so maybe she could've found something for you to care about."
            show apathy_down at topleft
            lucas "I care about you and my friends."
            $ apathy -= 3
            hide apathy_down
            "Naomi looks shyly away from you."
            naomi "Do you really mean that?"
            lucas "Why...wouldn't I?"
            "Naomi looks back at you and smiles."
            naomi "I'm glad you care."
            "You spend time with Naomi, until you have to head back."
        #naomi dies
        "Scarlet." if scarlet3:
            lucas "Scarlet has made some valid points about freedom. I'm sorry, but I'll have to side with Scarlet on this one."
            show naomi sad
            $ happiness -= 100
            $ naomi_death = True
            naomi "No, you can't possibly think that! This isn't funny!"
            scarlet "You heard him, he wants his freedom."
            naomi "Lucas, no! You can't believe that!"
            "You turn away from Naomi's innocent gaze."
            naomi "This...can't be happening..."
            scarlet "Get lost."
            hide naomi
            "Naomi runs away in tears."
            "You and Scarlet get out of the lake and sit on the bench."
            show lucas at midleft
            show scarlet at midright
            scarlet "I'm glad I was able to get through to you."
            lucas "I didn't want to make Naomi upset, though."
            scarlet "Unfortunately, that was bound to happen. You would've had to unshackle yourself someday. While tragic, it's better sooner than later."
            lucas "I guess that makes sense."
            scarlet "Well...you're free! You can do as you please without anything holding you back!"
            lucas "Yeah. I guess so."
            scarlet "C'mon, where's the enthusiasm? You're free!"
            lucas "I don't care."
            scarlet "That is like you, actually. Let's go back to get rest, ok?"
            lucas "Alright."
            "You head back with Scarlet."
    #arrive back at the hotel
    scene bg hotel
    with fade
    #gabriel scolds lucas for siding with scarlet
    if naomi_death:
        show gabriel serious at midright
        gabriel "Well, you were out rather late...do you know why Naomi was in tears?"
        show lucas at midleft
        show scarlet at midmidleft
        scarlet "She can't handle the truth."
        gabriel "Is that so?"
        "Gabriel sits upright, and looks towards Scarlet."
        gabriel "What...truth?"
        scarlet "Don't worry about it."
        gabriel "Am I supposed to drop this after what I saw with Naomi?"
        scarlet "I assure you, she could've been worse."
        gabriel "Just...have a good rest. Lucas, let's have a chat."
        lucas "Alright."
        scarlet "You don't need to talk if you don't want to. That's part of your freedom."
        lucas "I don't care either way."
        scarlet "Fine, fine. Have fun."
        hide scarlet
        "Gabriel waits until a door clicks, then walks up to you."
        show lucas at midmidleft with moveinleft
        show gabriel serious at midmidright with moveinright
        gabriel "What the hell did you do?"
        lucas "With...?"
        gabriel "What did you do to Naomi?"
        lucas "She and Scarlet were having an argument about me being free."
        gabriel "Why in hell would you side with Scarlet? You have to know Naomi wants the best for you, surely."
        lucas "They both have their reasons."
        gabriel "Dude, you have to talk with Naomi and fix this."
        lucas "I'm sure she'll be fine."
        gabriel "It's going to take a lot of forgiving on her end, and I'm sure she's going to tell the other girls about what happened."
        lucas "And?"
        gabriel "And...you messed up real bad. Just remember it the next time you try to talk to her."
    else:
        show gabriel at midright
        gabriel "Well, you were out rather late...do you know why Scarlet stormed through here?"
        show lucas at midleft
        show naomi at midmidleft
        naomi "She was just upset about something we talked about, that's all."
        gabriel "Is that so?"
        "Gabriel sits upright, and looks towards Naomi"
        gabriel "Just...be careful who you make enemies with, alright?"
        naomi "I'm not worried!"
        gabriel "I wasn't saying you were, but maybe sleep with an eye open."
        naomi "You worry too much!"
        gabriel "Well, you two go off to bed. We're heading out tomorrow morning, so don't stay up too late."
        naomi "Ok!"
        "You head off to your room and sleep."
    #walk out of the hotel
    scene bg hotel
    with fade
    #scarlet talks with the group
    if naomi_death:
        "You're heading to the lobby with your friends."
        "Notably, the girls except Scarlet are lagging behind you."
        show adrian at midmidright
        show lucas at midmidleft
        adrian "Y'know, this was actually pretty cool, I never would've been able to travel like this for leisure."
        show brandon at midmidright
        brandon "I'll say. We always had to look for something wherever we went back then. It's a refreshing change of pace."
        adrian "Did you ever travel like this, Lucas?"
        lucas "No, we always had work to do on the barn."
        adrian "Damn, guess we were in the same boat then, always working and never enjoying yourself."
        lucas "Less dramatic than what you were doing, though."
        brandon "It...was something, that's for sure."
        adrian "What about you, Scarlet?"
        show scarlet at midleft
        scarlet "Oh, me? We never went anywhere fun. We've just been sitting here working."
        brandon "What work?"
        scarlet "Oh, nothing special...my dad is a manager at a supermarket, and my sister...well...died, so..."
        adrian "C'mon, Brandon, it's probably a touchy subject."
        brandon "Sorry."
        scarlet "You guys sound like you've done exciting things, though. Anything come to mind?"
        show adrian serious
        adrian "Not really, it was exciting at first but then turned into a giant mess."
        scarlet "Mess how?"
        brandon "Good people died."
        scarlet "And...do you feel sorry for them? Any remorse?"
        brandon "The power they had went to their heads. Their actions had consequences and they paid the price for them."
        adrian "That's kinda harsh."
        scarlet "No remorse at all?"
        adrian "He lost a good friend to it, of course he has remorse. Brandon just has a certain tone that doesn't show it."
        "You arrive in the lobby. Gabriel is waiting."
        adrian "Well, look who never sleeps!"
        hide brandon
        show adrian at midright with moveinright
        show gabriel serious at midright
        gabriel "You don't know the half of it."
        show adrian serious
        adrian "Whoa, ok, my bad."
        gabriel "You're not at fault, don't worry. You can head outside, I just need to talk to Lucas for a bit."
        adrian "O...k? Whatever you say. See you outside!"
        hide adrian
        hide scarlet
        show gabriel serious at midmidright with moveinright
        "The girls walk past you, and Gabriel waits until the door closes before saying anything."
        gabriel "Where the hell do I start..."
        lucas "Is this about last night?"
        gabriel "No, it's about lunch...of course it's about last night! What were you thinking?!"
        lucas "We already went over that."
        gabriel "Whatever, just...watch yourself. Naomi and I had a talk this morning, and through tears, she just told me to tell you to be happy. That that's all she wanted."
        lucas "Alright."
        gabriel "Was that just in one ear and out the other? You do know the kind of power she has, right? Sleep with an eye open, and...see if you might be able to salvage it."
        lucas "Alright."
        "You head outside with Gabriel to return to college."
        "The ride home is quiet."
    #naomi talks with the group
    else:
        "You're heading to the lobby with your friends."
        show adrian at midmidright
        show lucas at midmidleft
        adrian "Y'know, this was actually pretty cool, I never would've been able to travel like this for leisure."
        show brandon at midmidright
        brandon "I'll say. We always had to look for something wherever we went back then. It's a refreshing change of pace."
        adrian "Did you ever travel like this, Lucas?"
        lucas "No, we always had work to do on the barn."
        adrian "Damn, guess we were in the same boat then, always working and never enjoying yourself."
        lucas "Less dramatic than what you were doing, though."
        brandon "It...was something, that's for sure."
        adrian "What about you, Naomi?"
        show naomi at midleft
        naomi "Similar to Lucas, but it's still our home!"
        brandon "Must've been lonely out there."
        naomi "A little. Not a lot of people lived closed to us, so we didn't have a lot of friends."
        adrian "You seemed to turn out alright, thankfully."
        naomi "'Thankfully?'"
        adrian "Well, you could be like London."
        hide naomi
        show london at midleft
        london "Do you want to say that again?"
        adrian "Ohhh, heyyyy, did you hear something? I definitely didn't say anything."
        london "Sleep with an eye open tonight."
        brandon "As much as we all want to punch him, I don't think Gabriel would allow that."
        adrian "Waaaaaait a minute here, I don't like where this is going."
        "You arrive in the lobby. Gabriel is waiting."
        adrian "Well, look who never sleeps!"
        hide brandon
        show gabriel at midmidright
        gabriel "Yeah, yeah. I was just making sure everything's set to go."
        adrian "Why wouldn't something be ready?"
        gabriel "Good point, but hey, just making sure we're good. Don't want to leave anything behind here. Let's head out."
        "You return to college."
        "The ride home is filled with joy."
    #last semester starts
    scene bg lobby
    with fade
    "You're back from the trip."
    "What should you do today?"
    menu day21:
        "Naomi?" if not naomi_check and last_person is not "Naomi":
            "You decide to ask Naomi."
            if not naomi_death:
                show naomi at truecenter
                lucas "Hey."
                naomi "Hi! Do you want to go somewhere?"
                lucas "Sure."
                naomi "Ok, let's go do something!"
                if not naomi1:
                    call scene_naomi1
                elif not naomi2:
                    call scene_naomi2
                elif not naomi3:
                    call scene_naomi3
                else:
                    call max("Naomi")
            else:
                call naomi_deny
                jump day21
        "Scarlet?" if last_person is not "Scarlet":
            "You decide to ask Scarlet."
            show scarlet at truecenter
            scarlet "Lucas, just who I was looking for! Let's go out somewhere."
            lucas "Alright."
            if not scarlet1:
                call scene_scarlet1
            elif not scarlet2:
                call scene_scarlet2
            elif not scarlet3:
                call scene_scarlet3
            else:
                call max("Scarlet")
        "Gabriel?" if last_person is not "Gabriel":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Brandon?" if not brandon_check:
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                elif not brandon2:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
                elif not brandon3:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon3
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's have a chat."
                    call max("Brandon")
            else:
                call brandon_deny
                hide brandon
                jump day21
        "London?" if not london_check:
            "You decide to ask London."
            show london at truecenter
            if grade < londonGrade:
                lucas "Are you up for a chat, London?"
                london "You know what? I guess I am."
                if not london1:
                    call scene_london1
                elif not london2:
                    call scene_london2
                elif not london3:
                    call scene_london3
                else:
                    call max("London")
            else:
                call london_deny
                hide london
                jump day21
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    #lobby comments on naomi if lucas sided with scarlet
    if naomi_death:
        "The lobby is more lively than usual."
        show gabriel serious at midright
        show london at midleft
        gabriel "She's been skipping class?"
        london "I think she's only left her room to get food."
        show adrian at midmidright
        adrian "That can't be good."
        gabriel "I'll have a chat with her."
        london "Respectfully, that's not your place."
        gabriel "I know. I just need to check on something."
        london "Just...be nice, alright?"
        gabriel "I will."
        hide gabriel
        "Gabriel heads upstairs."
        adrian "He's already dead."
        london "I wouldn't doubt it, but we'll have to see."
        hide london
        hide adrian
    "What should you plan for today?"
    menu day22:
        "Naomi?" if not naomi_check and last_person is not "Naomi" and not naomi_death:
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Adrian?" if not adrian_check:
            "You decide to ask Adrian."
            show adrian at truecenter
            if grade > adrianGrade:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                elif not adrian2:
                    call scene_adrian2
                elif not adrian3:
                    call scene_adrian3
                else:
                    call max("Adrian")
            else:
                call adrian_deny
                hide adrian
                jump day22
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                elif not brandon2:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
                elif not brandon3:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon3
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's have a chat."
                    call max("Brandon")
            else:
                call brandon_deny
                hide brandon
                jump day22
        "London?" if not london_check and last_person is not "London":
            "You decide to ask London."
            show london at truecenter
            if grade < londonGrade:
                lucas "Are you up for a chat, London?"
                london "You know what? I guess I am."
                if not london1:
                    call scene_london1
                elif not london2:
                    call scene_london2
                elif not london3:
                    call scene_london3
                else:
                    call max("London")
            else:
                call london_deny
                hide london
                jump day22
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    if naomi_death:
        "The lobby is more lively than usual."
        show gabriel serious at midright
        show london at midleft
        gabriel "It's not looking good."
        london "No shit, it doesn't take a genius to understand that."
        gabriel "Something has to happen before it's too late."
        show sarah sad at midmidleft
        sarah "What do you mean by 'too late?'"
        gabriel "Just...go up and keep her company. It can't help her to be alone in there all day."
        london "You can't do it yourself?"
        gabriel "Do you really think I'd make any sort of impact? Just go up there. Do what you can."
        london "No promises."
        "London and Sarah head upstairs."
        hide london
        hide sarah
        gabriel "Well...shit."
        hide gabriel
    "Who are you spending the day with today?"
    menu day23:
        "Naomi?" if not naomi_check and last_person is not "Naomi" and not naomi_death:
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Gabriel?":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                elif not brandon2:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
                elif not brandon3:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon3
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's have a chat."
                    call max("Brandon")
            else:
                call brandon_deny
                hide brandon
                jump day23
        "London?" if not london_check and last_person is not "London" and not naomi_death:
            "You decide to ask London."
            show london at truecenter
            if grade < londonGrade:
                lucas "Are you up for a chat, London?"
                london "You know what? I guess I am."
                if not london1:
                    call scene_london1
                elif not london2:
                    call scene_london2
                elif not london3:
                    call scene_london3
                else:
                    call max("London")
            else:
                call london_deny
                hide london
                jump day23
        "Sarah?" if not sarah_check and not naomi_death:
            "You decide to ask Sarah."
            show sarah at truecenter
            if grade > sarahGrade:
                lucas "Hi Sarah, do you want to do something today?"
                sarah "That...sounds nice, actually."
                if not sarah1:
                    call scene_sarah1
                elif not sarah2:
                    call scene_sarah2
                elif not sarah3:
                    call scene_sarah3
                else:
                    call max("Sarah")
            else:
                call sarah_deny
                hide sarah
                jump day23
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    if naomi_death:
        "The lobby is more lively than usual."
        show scarlet at midleft
        show sarah sad at midright
        scarlet "What am I supposed to do about that?"
        sarah "I don't know...but something has to be better than nothing, right?"
        scarlet "I'm the last person she wants to see."
        "Naomi walks past the lobby into the kitchen, trudging her feet at the floor."
        scarlet "I'm surprised to see you."
        show naomi sad at truecenter
        naomi "Just leave me alone..."
        "Naomi heads back upstairs."
        hide naomi
        scarlet "As you can see-"
        sarah "I know, alright!"
        scarlet "No need for hostilities..."
        "Sarah stands up and heads towards the stairs."
        show adrian at truecenter
        adrian "Something up?"
        sarah "The stairs...have a lot of water on them..."
        scarlet "What, did Naomi cry a river?"
        adrian "I didn't hear any crying, let me see that."
        "Adrian heads to the staircase."
        show adrian serious
        adrian "That's strange. Is the ceiling leaking...or maybe a pipe burst somewhere?"
        sarah "Whatever it is, let's get this cleaned up..."
        hide sarah
        hide adrian
        hide scarlet
    "What's going to happen today?"
    menu day24:
        "Naomi?" if not naomi_check and last_person is not "Naomi":
            "You decide to ask Naomi."
            if not naomi_death:
                show naomi at truecenter
                lucas "Hey."
                naomi "Hi! Do you want to go somewhere?"
                lucas "Sure."
                naomi "Ok, let's go do something!"
                if not naomi1:
                    call scene_naomi1
                elif not naomi2:
                    call scene_naomi2
                elif not naomi3:
                    call scene_naomi3
                else:
                    call max("Naomi")
            else:
                call naomi_deny
                jump day24
        "Scarlet?":
            "You decide to ask Scarlet."
            show scarlet at truecenter
            scarlet "Lucas, just who I was looking for! Let's go out somewhere."
            lucas "Alright."
            if not scarlet1:
                call scene_scarlet1
            elif not scarlet2:
                call scene_scarlet2
            elif not scarlet3:
                call scene_scarlet3
            else:
                call max("Scarlet")
        "Adrian?" if not adrian_check:
            "You decide to ask Adrian."
            show adrian at truecenter
            if grade > adrianGrade:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                elif not adrian2:
                    call scene_adrian2
                elif not adrian3:
                    call scene_adrian3
                else:
                    call max("Adrian")
            else:
                call adrian_deny
                hide adrian
                jump day24
        "Brandon?" if not brandon_check and last_person is not "Brandon":
            "You decide to ask Brandon."
            if grade > brandonGrade:
                if not brandon1:
                    "You head to the study."
                    "You knock on the door."
                    show brandon at truecenter
                    brandon "What?"
                    lucas "Do you want to do something?"
                    brandon "Sure. Come inside and we'll study."
                    call scene_brandon1
                elif not brandon2:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon2
                elif not brandon3:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's head to my library."
                    call scene_brandon3
                else:
                    show brandon at truecenter
                    lucas "Do you want to do something, Brandon?"
                    brandon "Sure. Let's have a chat."
                    call max("Brandon")
            else:
                call brandon_deny
                hide brandon
                jump day24
        "Sarah?" if not sarah_check and last_person is not "Sarah":
            "You decide to ask Sarah."
            show sarah at truecenter
            if grade > sarahGrade:
                lucas "Hi Sarah, do you want to do something today?"
                sarah "That...sounds nice, actually."
                if not sarah1:
                    call scene_sarah1
                elif not sarah2:
                    call scene_sarah2
                elif not sarah3:
                    call scene_sarah3
                else:
                    call max("Sarah")
            else:
                call sarah_deny
                hide sarah
                jump day24
        "Study?":
            call study
    call set_false

    scene bg lobby
    with fade
    #naomi dies
    if naomi_death:
        show gabriel serious at midright
        show sarah at midleft
        gabriel "Poor girl..."
        sarah "We saw her come down a few days ago, she just looked so sad."
        gabriel "Well, as long as there weren't any puddles that trailed her, we'll just have to wait."
        sarah "Now that you mention it, the stairs and hallway to the kitchen had water on them the other day."
        show adrian at midmidleft
        adrian "Oh, yeah, meant to tell you about that. I think a pipe must have burst somewhere."
        gabriel "Did...did it happen to be on the stairs and lead to the kitchen?"
        adrian "Yeah, now that you mention it, it did. Do you know what would have caused that?"
        "Gabriel glances to you, then back to Adrian."
        gabriel "She's...dying."
        sarah "D-dying?"
        gabriel "She has strong magic and she's miserable, she could be dead for all we know!"
        "Gabriel rushes up the stairs."
        hide gabriel
        show adrian serious
        adrian "There's...no way, right?"
        sarah "She's sad, but she wouldn't kill herself!"
        adrian "I'm heading up there. I'll let you know."
        hide adrian
        "Sarah eyes the stairs for a bit, then turns to you."
        sarah "You...I can't believe..."
        show adrian serious at midmidright
        adrian "I don't know how to say this, but...I think you already know..."
        $ naomi_dead = True
        show sarah sad
        sarah "No! She would never hurt herself!"
        "Sarah rushes for the stairs."
        hide sarah
        show adrian serious at truecenter with moveinright
        adrian "I...don't even know what to say...I'm so sorry."
        "Sarah is yelling from upstairs."
        adrian "Looks like she sees it, too."
        "Gabriel comes downstairs."
        show gabriel serious at midleft
        gabriel "I-what do I even say?"
        adrian "What'd she do?"
        gabriel "It wasn't her that did it. Her magic killed her."
        adrian "Her magic...what? It can do that?"
        gabriel "Strong magic can. It's the downside of strong magic; per Carson, if you're sadder than when you got strong magic, your magic will attack you."
        adrian "Wait...really? Carson too?"
        gabriel "Ever wonder why he was always smiling? He had to. Naomi must've had something similar. I didn't see any damage around the house, though...I just didn't think it was happening."
        adrian "That's why there was water all over the floor, then."
        gabriel "It's sad to see..."
        scene bg black
        with fade
        "You head up to Naomi's room."
        "Through the doorway, you can see Sarah crying at Naomi's bedside."
        "The floor is covered in water."
        show apathy_up at topleft
        "Naomi is gone."
        $ apathy += 15
        hide apathy_up
        scene bg lobby
        with fade
    "Finals are coming up..."
    menu day25:
        "Naomi?" if last_person is not "Naomi" and not naomi_dead:
            "You decide to ask Naomi."
            show naomi at truecenter
            lucas "Hey."
            naomi "Hi! Do you want to go somewhere?"
            lucas "Sure."
            naomi "Ok, let's go do something!"
            if not naomi1:
                call scene_naomi1
            elif not naomi2:
                call scene_naomi2
            elif not naomi3:
                call scene_naomi3
            else:
                call max("Naomi")
        "Gabriel?":
            "You decide to ask Gabriel."
            show gabriel at truecenter
            lucas "Hey Gabriel, want to do something?"
            gabriel "Yeah, I got time. Let's hit the gym, yeah?"
            if not gabriel2:
                call scene_gabriel2
            elif not gabriel3:
                call scene_gabriel3
            else:
                call max("Gabriel")
        "Adrian?" if not adrian_check and last_person is not "Adrian":
            "You decide to ask Adrian."
            show adrian at truecenter
            if grade > adrianGrade:
                lucas "Adrian, do you want to do something today?"
                adrian "Yeah, sure, sounds like fun."
                if not adrian1:
                    call scene_adrian1
                elif not adrian2:
                    call scene_adrian2
                elif not adrian3:
                    call scene_adrian3
                else:
                    call max("Adrian")
            else:
                call adrian_deny
                hide adrian
                jump day25
        "Sarah?" if not sarah_check and last_person is not "Sarah" and not naomi_dead:
            "You decide to ask Sarah."
            show sarah at truecenter
            if grade > sarahGrade:
                lucas "Hi Sarah, do you want to do something today?"
                sarah "That...sounds nice, actually."
                if not sarah1:
                    call scene_sarah1
                elif not sarah2:
                    call scene_sarah2
                elif not sarah3:
                    call scene_sarah3
                else:
                    call max("Sarah")
            else:
                call sarah_deny
                hide sarah
                jump day25
        "Study?":
            call study
    call set_false

    scene bg hallway
    with fade
    "Finals have arrived..."
    "..."
    "..."
    "..."
    scene black
    with fade
    if tempGrade == 0:
        "You failed your finals."
        $ happiness -= 5
    elif tempGrade == 1:
        "You got a D average."
        $ happiness -= 3
    elif tempGrade == 2:
        "You got a C average."
        $ happiness -= 1
    elif tempGrade == 3:
        "You got a B average."
        $ happiness += 1
    elif tempGrade == 4 or tempGrade > 4:
        "You aced your finals!"
        $ happiness += 3
    else:
        "There was an error with your grade, so you were given a C."
        $ happiness -= 1
        $ tempGrade = 2
    $ grade = tempGrade
    if tempGrade > 0:
        $ tempGrade -= 1

    #2 of the below need to have happened for brandon to survive
    #brandon doesn't go to the party, brandon's first event is done, brandon's third event is done
    if brandonr1:
        $ brandon_alive_checks += 1
    if brandon1:
        $ brandon_alive_checks += 1
    if brandon3:
        $ brandon_alive_checks += 1

    if brandon_alive_checks < 2:
        $ brandon_dead = True
    
    if brandon_dead:
        scene bg lobby
        with fade
        show gabriel at midright
        show lucas at midleft
        show adrian serious at midmidright
        if not naomi_dead:
            show naomi at midmidleft
        gabriel "Glad that the year is over."
        adrian "Did Brandon go with you today?"
        gabriel "Nah, not today. He was probably getting last minute studying in."
        adrian "Brandon? Not studying enough? You really think that?"
        gabriel "Feel free to check on him in the study, man."
        adrian "I've got a bad feeling about this..."
        "Adrian heads to the study."
        hide adrian
        if not naomi_dead:
            gabriel "What's got him so worried?"
            naomi "He's just worried about his friend."
            gabriel "I've never seen Adrian worry about anything. Something is very wrong."
            naomi "Think positively! Everything is ok! I'll head up with him and turn that attitude around."
            "Naomi follows Adrian."
            hide naomi
            gabriel "She sure is dedicated."
            lucas "A little too dedicated."
            gabriel "She's good for you."
            lucas "If you say so."
            gabriel "You haven't seen the change? Look in the mirror, man. You're very different from when you first came here."
            lucas "I'm not-"
            "You hear Naomi scream from upstairs."
            gabriel "Well, that can't be good."
            "You and Gabriel hastily climb the stairs."
            scene bg library
            with fade
            "Naomi is in tears as you enter the room."
            "Brandon is facedown on his desk."
            "A desk that used to be brown, now topped with red."
            show adrian serious at midright
            show lucas at midleft
            show gabriel serious at truecenter
            adrian "No no, c'mon, wake up, this can't be happening again, c'mon Brandon!"
            gabriel "What the hell happened?!"
            adrian "How am I supposed to know?!"
            gabriel "Damn it all, what the hell is going on here!"
            "Gabriel sits in a nearby chair and takes a deep breath."
            gabriel "Get down to the lobby. Once everyone's here we can figure out what the hell is going on."
        else:
            gabriel "I wonder what's gotten into him."
            lucas "I wouldn't know."
            gabriel "Something rubs me wrong about it, man. Adrian doesn't worry about Brandon like that."
            lucas "I'm sure things are fine."
            gabriel "Eh, I'll check on him. Who knows what he's thinking."
            "Gabriel heads up the stairs."
            hide gabriel
            "You sit in silence for a bit."
            "The lobby has never been this quiet."
            "You've always seen this place with at least four others."
            "What a shallow graveyard it's become."
            show gabriel serious at midright
            gabriel "So...there's no easy way to say this, but...Brandon's also-"
            show adrian serious at midmidright
            adrian "Whoever it is just killed him and left him to rot!"
            gabriel "Listen, once everyone's back, we'll figure something out. I don't...Man, we're dropping like flies."

        show apathy_up at topleft
        "Brandon is gone."
        $ apathy += 10
        hide apathy_up
        scene bg lobby
        with fade
        show gabriel serious at midright
        show lucas at midleft
        show scarlet at midmidleft
        show adrian serious at midmidright
        gabriel "We have to figure out what the hell is happening with us. This can't just be a coincidence."
        scarlet "Why would someone have it out for you, did you murder a relative or something?"
        gabriel "I don't know, but we must have overlooked something."
        adrian "How are we supposed to look at anything, we don't have any monitoring here!"
        "Silence falls on the room."
        adrian "Sarah, you can get his memories, right?"
        hide lucas
        show sarah at midleft
        sarah "I can't if he's dead..."
        hide adrian
        show london at midmidright
        london "What about transfering to him through one of us?"
        sarah "That's only work if someone touched his hands while he was alive...and it doesn't work on people who died. Brandon's memories are...gone. I'm sorry."
        scarlet "Then there's nothing you can do?"
        sarah "Not really...I guess...I could look at all of us, and see if anyone missed something."
        gabriel "I'm all for it."
        adrian "I'll do whatever it takes."
        scarlet "Now wait a minute here, hold on. You mean you'd be going through ALL my memories?"
        gabriel "It's for the greater good, Scarlet. It doesn't hurt to try."
        scarlet "You're not getting my hands, my head is a mush of terrible memories."
        show adrian serious at truecenter
        "Adrian stands up and moves towards Scarlet."
        adrian "Did you kill Brandon?"
        scarlet "What? No. Why would I do that?"
        if naomi_dead:
            adrian "Did you kill Carson?"
        else:
            hide adrian
            show naomi at truecenter
            naomi "You left with Carson at that party, too..."
            hide naomi
            show adrian serious at truecenter
        scarlet "HE walked into traffic! Hell, I liked him! Why would I kill him!"
        london "Give Sarah your hands."
        scarlet "You're not getting my head!"
        "Scarlet bolts out of the house."
        hide scarlet
        adrian "Get back here!"
        hide adrian
        "Adrian starts to run out after her, but stops before he reaches the door."
        show adrian serious at midmidleft
        adrian "Damn murderer, what'd we ever do to her?"
        gabriel "Calm down, we'll figure this out."
        london "Awfully suspicious behavior she's got."
        gabriel "We can't do anything about her, we'll have to find some other way."
        "Silence falls on the group, with Sarah breaking it shortly."
        sarah "Well...if anyone touched one of her hands...I can still see her memories..."
        gabriel "Nada from me, man."
        adrian "Brandon might've, but not me."
        london "Maybe you did, Sarah?"
        sarah "Even if I did, I can't view my own memories."
        if not naomi_dead:
            hide adrian
            show naomi at midmidleft
            naomi "She was too depressing to be around..."
        "Your friends look to you."
        hide london
        show lucas at midmidright
        lucas "I don't remember."
        if not naomi_dead:
            naomi "Not even that day that you met each other? She was all over you!"
            lucas "She was?"
            naomi "Just...how'd that conversation start?"
        else:
            gabriel "Anything at all?"
            lucas "I wouldn't remember."
            sarah "What about when you first met her? Naomi...was complaining about that."
        "Didn't it go something like..."
        scene bg hallway
        with fade
        show lucas at midleft
        show scarlet at midright
        scarlet "I'm Scarlet, a pleasure to meet you. What about Psychology interests you?"
        "Scarlet extends her hand to you."
        scene bg lobby
        with fade
        show lucas at midmidright
        show gabriel at midright
        show sarah at midleft
        show london at midmidleft
        lucas "She introduced herself with a handshake."
        gabriel "It seems we've got her. Adrian, come help me look for something we can use."
        "Gabriel and Adrian leave the room. Sarah moves to a seat next to you."
        show sarah at midright
        sarah "Let me see your hands..."
        "Sarah moves her fingers along your palms."
        "You feel something moving inside your head!"
        "After some time, you don't notice the movement."
        london "Figure it out?"
        sarah "I'm not there yet..."
        london "The sooner you can get there, the better."
        sarah "I'm working on it...sorry..."
        london "I'm going to go help the other two. Have fun."
        "London leaves."
        show lucas at midmidleft
        show sarah at midmidright
        if not naomi_dead:
            show naomi at midleft
            naomi "That's amazing that you can look at memories!"
            sarah "It's not that impressive...other people can do a lot more than me..."
            naomi "Well, I think it's incredible! You don't have to compare yourself to anyone!"
            sarah "Th-thanks."
            "Some time passes in silence."
            sarah "She-oh. Oh no. She...pushed Carson into the road."
            naomi "What?!"
            sarah "Sorry, I need...to go further..."
            naomi "I knew she wasn't trustworthy! Lucas, how could you talk to someone like her?!"
            lucas "I didn't know she was going to murder anyone."
            naomi "How could you trust her?!"
            lucas "How was I supposed to know?"
            sarah "Can you please...quiet down...I'm trying to work..."
            naomi "Oh-sorry."
            "You continue in silence. Sarah interrupts the silence with various tidbits."
            sarah "Oh, wow..."
            "..."
            sarah "Interesting..."
            "..."
            sarah "How could she hate him that much..."
            "..."
            sarah "She said that?"
            "..."
            sarah "Oh my..."
            naomi "What are you seeing?"
            sarah "Oh, just...interesting things..."
            "Sarah suddenly stops."
            sarah "I'm...sorry Claus did that to you..."
            naomi "Wh...what do you mean?"
            sarah "You're sitting on a bench with Lucas, and-"
            naomi "Ahh! Hey, hey, you can just skip past that, that's not very important, don't worry about that!"
            sarah "I bet your face is bright red like it is in this memory."
            naomi "Hey, no fair!"
            "Sarah giggles to herself."
            sarah "Just teasing...it shouldn't be long now..."
            "..."
            sarah "Oh, there we are. She-"
            sarah "O-oh. That...was gruesome..."
            naomi "What happened?"
            sarah "She...took control of him...sat him still...and just...did that to him..."
            naomi "Poor Brandon..."
            sarah "Yeah..."
            hide naomi
        else:
            sarah "Sorry if it feels weird..."
            "Sarah looks through your memories."
        "The others return."
        hide lucas
        show london at midmidleft
        show gabriel at midleft
        show adrian serious at midright
        gabriel "They've completely disarmed us."
        sarah "It was definitely Scarlet...she killed both of them..."
        adrian "Why us?! What did we do to her?!"
        gabriel "Calm down, man. It'll be alright. We'll stop her."
        adrian "How am I supposed to be calm about this?!"
        sarah "Can you please...be quiet for a moment..."
        gabriel "What have you found? Anything we can use against her?"
        sarah "She has this mind control...and what looks like some sort of shockwave when she punches..."
        adrian "Mind...control? How do we beat that?"
        gabriel "Do you know how it works?"
        sarah "She just...looks at you...then...it works."
        adrian "So line of sight based, like me?"
        sarah "If I had to guess, yes..."
        gabriel "We need a way to break line of sight."
        adrian "An enclosed area, or something with a lot of cover?"
        gabriel "Man, there's no way she'd give us that power over her. She's going to be somewhere open."
        london "Let's rush her down fast."
        sarah "No...the shockwaves cover a wide area...it'd be suicide..."
        if not dating:
            london "You're one to talk."
            sarah "Can you just...shut up and focus, please?"
        gabriel "We can come back to that, what can we do to knock her down?"
        sarah "If I can get...close enough...I can."
        adrian "I can as long as I have line of sight, but it'd take time."
        gabriel "It's a start. We'll go for those, if we can. How do we break line of sight for brainwashing?"
        adrian "What about Lucas' shield thing? It'd block vision completely, right?"
        gabriel "Interesting idea...shield whoever is controlled, and they'll be freed...it could work."
        adrian "How do we protect Lucas, though?"
        gabriel "I could guard him. If only two people can occupy one mind, then that should cover our bases."
        adrian "And...you're confidant that will work?"
        gabriel "Brandon said only two people can be in your mind at a time, London's sister and I tested it. We both couldn't guard one person at the same time."
        adrian "Would it work with brainwashing?"
        gabriel "I have no idea, but it's our best option. I'll guard Lucas."
        adrian "What about your other sword? Should one of us get it?"
        gabriel "Sarah, probably."
        sarah "No...if she gets close enough to me...I can knock her out..."
        adrian "Memory can do that?"
        sarah "It's not exactly memory..."
        london "It's a...'unique' trick she's got."
        sarah "That's one way to phrase it...but...trust me, it'll work."
        gabriel "That make the next option for this...Lucas. You'll have one of my swords to protect yourself."
        lucas "Cool."
        gabriel "If that's everything, let's show her she can't get away with this. Is there anything else you need from Lucas' head, Sarah?"
        sarah "No, I'm just looking at some things..."
        london "What else is there?"
        if not naomi_dead:
            sarah "Naomi has some interesting things she writes down..."
            hide adrian
            show naomi at midright
            naomi "Hey!"
            "Naomi grabs Sarah's hands and pulls them from your palms."
            "You feel a sharp jab in your head."
            sarah "Don't do that, it hurts him!"
            lucas "I'm fine."
            naomi "You can't just say things like that in front of everyone!"
            "Naomi's face is bright red."
            sarah "It's fine, I didn't see anything major."
            naomi "You better not have!"
            "Sarah giggles."
            gabriel "If you're all done with that, let's head out. I have an idea of where she'd be."
            naomi "Yes! We're done! We don't need to see anything else! Let's go!"
        else:
            sarah "It's...nothing."
            gabriel "If you're all done with that, let's head out. I have an idea of where she'd be."
    else:
        #brandon is alive, talks with adrian about pattern of magic
        scene bg library
        with fade
        show brandon at midleft
        show adrian at midright
        adrian "C'mon brandon, you can't coop yourself up in your study all day, finals are over! Get some sunlight!"
        brandon "Something is wrong. I can't see the pattern. I'm so close to grasping it, but nothing works."
        adrian "Maybe I can help, what are you trying to look for?"
        brandon "You can certainly try. I've been looking into the genetics of magic, how it's distributed to children. There has to be a pattern. I'm so close to it."
        adrian "What's the closest you've gotten?"
        brandon "The closest...if your parents have magic, you'll have magic. That part is definitely confirmed."
        brandon "If your parents combined only have one form of magic, you will inherit a random form. Gabriel and his father don't share magic, for example."
        brandon "And if your parents combined have two or more forms of magic, you will inherit one of them."
        brandon "Look at London's family. London and her siblings have many forms from their mother, with London and Maya even sharing ghost form."
        adrian "Whoa, that sounds cool, I never would've thought to think about that."
        brandon "It doesn't work...I've looked through all the people, and it works for everyone...EXCEPT Scarlet. She came in here earlier today, too..."
        "The two sit in silence for a bit."
        show adrian serious
        adrian "Well, if her...mother? Had psionic, what would the chance be that the 'random magic' just happened to be psionic?"
        brandon "She'd be the first. We'd have seen it happen by now, statistically. Don't think I've looked through my records to make sure."
        "Brandon flips through more notes."
        adrian "Could she not know about one of her parents having another form of magic?"
        brandon "That could be the case, but I can't confirm it. I don't have a link to her father."
        adrian "What about just lying to us?"
        "Brandon looks through his notes."
        brandon "Why would she lie? What purpose would it serve?"
        "Adrian looks over Brandon's notes."
        adrian "Doesn't...doesn't she have the same hair color as Miss Fortune? That's been bothering me for a bit. It's a nice color, don't-"
        brandon "You don't know what you've just done."
        adrian "Wh-what? Why do you have that look on your face?"
        brandon "Look here-Miss Fortune and her father both have fortunes. And if you look over in these records...right here! Miss Fortune's mother is unknown."
        adrian "I still don't get it."
        brandon "Scarlet said her mother has psionic magic. If they both have it, their father must have at least one, or her mother two, and if we just combine these two..."
        adrian "You're saying...Scarlet is related to Miss Fortune?"
        brandon "Scarlet said that she had a dead sister. So that visit from her earlier...could've ended badly, if I didn't think something was off."
        adrian "We need to tell the others!"
        brandon "Where is everyone?"
        adrian "We're all in the lobby. I was going to see if I could get you to come celebrate the year with us."
        brandon "That's going to change."
        #brandon accuses scarlet
        scene bg lobby
        with fade
        show lucas at midleft
        show gabriel at midmidleft
        show adrian serious at midmidright
        show brandon at midright
        gabriel "Well, there you two are."
        adrian "Miss Scarlet Fortune."
        hide gabriel
        show scarlet at midmidleft
        scarlet "Come again?"
        brandon "Your sister was Miss Fortune, correct?"
        scarlet "I don't know what you're talking about."
        adrian "Well, then you wouldn't mind us taking a look at your memories, right?"
        "Scarlet gets up from her seat."
        scarlet "What are you implying?"
        adrian "You don't have anything to be afraid of, it'll be really quick."
        scarlet "Hey, let's not get too hasty, now! I haven't done anything!"
        brandon "What exactly do you want with us?"
        "Scarlet looks around the room."
        scarlet "So, that's it, huh? Why am I being questioned when I'm surrounded by murderers!"
        brandon "We're not going to hurt you, we just want to talk."
        scarlet "I'm not talking with you!"
        "Scarlet rushes out the door."
        hide scarlet
        show gabriel at midmidleft
        gabriel "Well then...good catch."
        brandon "I can't take all the credit, it was both of us."
        gabriel "Today just got a lot more interesting. What exactly can Scarlet do?"
        brandon "Psionic is close range magic, but has a wide spread. Scarlet also has strong psionic, which can brainwash a target within line of sight."
        adrian "So...fight her in an area with a lot of cover?"
        gabriel "No, she needs us to fight each other, we'd overpower her otherwise."
        hide lucas
        show london at midleft
        london "We can just rush her, then."
        brandon "Psionic has a large radius, specializing in close quarters. Even if multiple of us were close, she could handle us easily. We need a way we can stop her."
        hide gabriel
        show sarah at midmidleft
        sarah "If I get close...I should be able to knock her unconscious..."
        adrian "Memory can do that?"
        if dating:
            show london happy
            london "Just trust her, I believe she can do it."
            "Sarah smiles."
        else:
            london "She has a certain trick up her sleeve."
            sarah "What's that supposed to mean?"
        brandon "It can work. Adrian, you think you can do it?"
        adrian "Buy me enough time and she'll wear herself out."
        london "You might wear the rest of us out as well."
        brandon "It's just a possibility. You both need line of sight, though. That'd work against us."
        adrian "Pssh, it'd work!"
        brandon "It's just brainstorming. Gabriel's swords can do something similar."
        hide london
        show gabriel at midleft
        gabriel "I might need to guard someone if we're put on the back foot, let's not rely on it."
        brandon "That...actually, that might prevent the brainwash from happening in the first place. Only two minds can be in your head at once; yours and a visitor."
        gabriel "Yes, I remember testing something like that with London's sister. Who should get the other sword, then?"
        brandon "Fire magic can't defend itself. Lucas gets it."
        if not brandonr1 and not naomi_dead:
            brandon "This might actually be simple, thinking back to that rainy day. Lucas shields Scarlet directly, and Naomi fires water at the shield. It'd cook her."
            hide adrian
            show naomi at midmidright
            naomi "That seems a little extreme, right?"
            hide sarah
            show london at midmidleft
            london "Considering what she's already done to us, no. She deserves the worst death we can give her."
            gabriel "I wouldn't go that extreme."
            if dating:
                london "Alright, alright. I get it."
            else:
                london "She is the reason we are fucked in the first place, how am I supposed to just forget what she did to me?"
                gabriel "We all went through it, man. I understand where you're-"
                london "Fuck off, you don't know me."
            hide naomi
            hide london
            show adrian at midmidright
            show sarah at midmidleft
        elif not brandonr1:
            brandon "Actually, you can shield Scarlet directly. That'd break line of sight no matter the person."
        gabriel "Are we all set?"
        brandon "We're about as prepared as we can be."
        gabriel "I know this wasn't what we wanted to be involved with again, but we're ending it today. Nothing is stopping our victory! We've faced worse than this, and we'll succeed! To battle!"
        "The room falls silent. Sarah eventually laughs to break it."
        gabriel "Wh-what? What's so funny?"
        sarah "Are you trying to be like your dad?"
        gabriel "It felt like the right moment!"
        adrian "'These men and women have been selected by the greatest among us, and will steer us to a brighter future!'"
        gabriel "Laugh it up, you two. All goes well, I'll get some advice from him. Let's go."
    #showdown with scarlet
    scene bg bridge
    with fade
    "You find Scarlet on a wide bridge."
    show lucas at midleft
    show gabriel at midmidleft
    show adrian at midmidright
    if not naomi_dead:
        show naomi at midright
    else:
        show london at midright
    gabriel "Figured she'd be here, what a wide open space for her to control us."
    if not naomi_dead:
        naomi "Lucas' shield is invaluable."
        adrian "Are you trying to gas Lucas up?"
        naomi "No, just reminding everyone that he's the most important here."
    else:
        london "As long as Lucas shields us, should be easy."
        adrian "Are you trying to gas Lucas up?"
        london "More like reminding him to shield me."
    gabriel "Are we ready? Once we head over, we won't have another shot."
    hide lucas
    hide gabriel
    hide adrian
    if not naomi_dead:
        hide naomi
    else:
        hide london
    if not brandon_dead:
        show brandon at truecenter
        brandon "Ready."
        hide brandon
    show adrian serious at truecenter
    adrian "Count me in."
    hide adrian
    if not naomi_dead:
        show naomi at truecenter
        naomi "Ready to help!"
        hide naomi
    show london at truecenter
    london "Absolutely."
    hide london
    show sarah at truecenter
    sarah "I-I think so."
    hide sarah
    show gabriel at truecenter
    "Gabriel turns to you."
    show lucas at midmidleft
    lucas "Yeah."
    gabriel "You've come a long way, and let me be the first to say that I'm proud of you for being here, man."
    lucas "O...k?"
    "Gabriel pulls a pitch-black sword from behind his back, seemingly from nowhere, and hands it to you."
    gabriel "Treat him well...and don't lose him."
    lucas "'Him?'"
    show london at midmidright
    london "There's no way I'm hearing this, you've named your swords?!"
    gabriel "Yeah, yeah, laugh it up. Save it for after we win, alright?"
    "Gabriel materializes another sword from behind his back, this one a blinding white."
    gabriel "Alright. Let's head over."
    hide lucas
    hide gabriel
    hide london
    "You walk onto the bridge with your friends and find Scarlet."
    show scarlet at top
    scarlet "Took you long enough."
    show gabriel at midmidleft
    show lucas at midleft
    show adrian serious at midmidright
    show london at midright
    gabriel "Scarlet, stand down. We know what you've done and what you've been planning."
    scarlet "Save it, murderers. You're just getting what you deserve."
    adrian "Scarlet, those 'fortunes' were killing people! You have to understand why we had to stop her!"
    scarlet "You didn't have to kill her! You murdered her and you were rewarded for it! How is that fair?!"
    london "Why the hell are we still talking to her? Let's just get this over with."
    scarlet "I agree."
    if not naomi_dead:
        scarlet "Oh but one thing...Lucas, Naomi? I have no fight with you. Let the cowards fight their own battle."
        show naomi at truecenter
        naomi "I'm not letting you kill them!"
        scarlet "Then you'll join their corpses. Lucas, I know you don't care either way."
    else:
        scarlet "Oh, but one thing...Lucas? I know you don't care either way. You're free to leave."
        show lucas serious
    lucas "Stand down, Scarlet."
    scarlet "You can't possibly care about them NOW, of all times!"
    lucas "These are my friends. I'm not going to sit by and watch this happen. You've gone too far."
    if scarlet3:
        lucas "And to answer your question from the last time we were here...I wouldn't change anything about the past. I am who I am today because of the past, and I wouldn't change that for anyone."
    show scarlet mad
    scarlet "So you won't back away! Fine! You'll all be rolling in a grave together! Let's see how worth it really is to side with murderers!"
    gabriel "So much for all that. Lucas, I'll see you on the other side."
    "Gabriel turns to you and stabs you with his white sword."
    "You flinch away, but aren't in any pain."
    hide gabriel
    gabriel "I'll protect you, just win this for us."
    lucas "Where...are you?"
    gabriel "I'm in your head. Any harm to you will be done to me instead. Don't worry, nothing a little rest can't fix."

    scene bg black
    with fade
    if not naomi_dead and not brandon_dead and brandonr1:
        "You remember the plan from Brandon."
        brandon "This might actually be simple, thinking back to that rainy day. Lucas shields Scarlet directly, and Naomi fires water at the shield. It'd cook her."
        "It can't be that easy."
        "You cast a shield on Scarlet, and Naomi fires water at her."
        "Scarlet screams and quickly yields."
        "..."
        "It really was that simple."
    elif not naomi_dead and not brandon_dead:
        "You fight hard with your friends."
        "The fight is long, but you force Scarlet to yield."
    elif not brandon_dead and brandonr1:
        "Whenever you notice Scarlet mind controlling someone, you cast a shield on her."
        "The fight is long, but you force Scarlet to yield."
    elif not naomi_dead:
        "You fight hard with your friends."
        "The fight is long, but you force Scarlet to yield."
    elif not brandon_dead:
        "You fight hard with your friends."
        "The battle is tough and grueling at times, but you manage to pull through at the end."
        "You eventually force Scarlet to yield."
    else:
        "The fight is grueling."
        "You defend Adrian, London, and Sarah as best as you can."
        "Eventually, Sarah manages to grab one of Scarlet's hands."
        "You watch as Scarlet starts to tremble and scream."
        "She swiftly falls to the ground, unconscious."
    scene bg bridge
    with fade
    #naomi and brandon dead, london kills scarlet with no remorse
    if naomi_dead and brandon_dead:
        show lucas at midleft
        show adrian serious at midmidleft
        show gabriel at midmidright
        show sarah at midright
        adrian "What...was that?"
        sarah "What was what?"
        gabriel "I didn't...know you could do that...oh, I'm beat."
        sarah "It's nothing."
        adrian "She's out on the ground!"
        sarah "She's not going to wake up soon, don't worry."
        adrian "How long is 'soon?'"
        sarah "About...sixteen or so hours..."
        adrian "That's a little scary."
        sarah "She's fine! London can attest, too!"
        "You turn towards London, who is standing over Scarlet."
        "Or rather...where Scarlet once was."
        hide lucas
        show london at midleft
        london "Well, I made sure she won't get the chance."
        gabriel "What...did you do...?"
        london "I burned her body."
        adrian "You WHAT?"
        london "Her ashes are down there, right where she belongs."
        gabriel "Why would...you..."
        "Gabriel is gasping for air."
        london "You need to lie down."
        gabriel "No, I...can stand..."
        london "Are you stupid? With how long it took to bring her down? Just shut up and lie down."
        adrian "Are you ok, London?"
        london "Are you trying to be burned with her, too?"
        adrian "No, I-whatever. What are we supposed to do now?"
        london "I guess...I'll watch Gabriel. Someone will come down and he can explain this."
        gabriel "Why...you...you turned her..."
        london "Lie down, you moron!"
        "London turns to the rest of you."
        london "Get the hell out of here."
        adrian "Shouldn't we-"
        show london mad
        london "GET OUT OF HERE!"
        "London is visibly shaking."
        adrian "Alright, alright, we get it."
        "You head back home."
    else:
        show lucas at midleft
        show scarlet mad at midright
        show london at midmidright
        show sarah at midmidleft
        scarlet "Damn you! Damn you all! I hope you rot, murderers!"
        london "Murderers, huh?"
        "London walks over to Scarlet."
        show london at midright with moveinleft
        hide scarlet
        sarah "What are you doing?"
        london "Burn in hell, you son of a bitch."
        show sarah at midmidright with moveinleft
        sarah "Wait, no!"
        "Sarah jumps towards London, but backs away when London bursts into flames and grabs Scarlet."
        show london mad
        london "All that pain your sister gave us? All that pain she gave me? We should have let her suffer! You're the next best way to do that!"
        "Scarlet screams in pain, but none of you move to stop her."
        #london cries after killing scarlet, if dating gabriel
        if dating:
            "Gabriel makes the first move, and grabs London."
            hide sarah
            show gabriel serious at midmidright
            gabriel "Ack-that's hot-London! Stop!"
            london "She deserves this!"
            gabriel "Stop this at once!"
            "London looks back to Gabriel, and extinguishes herself."
            show london
            london "I..."
            gabriel "I understand you're upset, but killing her isn't going to change anything!"
            london "I just...I'm sorry. I know! I'm sorry!"
            "London begins to cry, and falls into Gabriel's arms."
            gabriel "Uh, it's alright, we'll figure something out."
            show adrian at midmidleft
            "Adrian starts to laugh."
            adrian "Look at Gabriel being such a softy."
            "Gabriel darts a glare back."
            adrian "Alright, alright, I get it, enjoy your moment."
            hide gabriel
            hide london
            show sarah at midmidright
            "Sarah walks over to Scarlet's body, grabs her hands, and walks back to you."
            sarah "She's dead...what do we do?"
            #brandon and naomi alive
            if not brandon_dead and not naomi_dead:
                show brandon at midright
                brandon "Gabriel will get it taken care of."
                adrian "Was...that crowd always there?"
                brandon "I guess she wanted her last bit of attention. Gabriel will figure something out."
                hide brandon
                show naomi at midright
                naomi "That seems unfair for Gabriel, though. We're really going to pile all this on him?"
                adrian "That's just what we've always done."
                naomi "You WHAT?"
                sarah "Not so loud!"
                "Gabriel walks over with London."
                hide sarah
                hide adrian
                show naomi at midmidleft
                show gabriel at midmidright
                show london at midright
                gabriel "Well...I guess that's how the story goes. You're all free to head home, I'll figure something out."
                naomi "That's not fair to you!"
                gabriel "It's...not about fairness, it's more like a duty. Some official will surely come down, and I'll...see what happens..."
                london "Are you ok?"
                gabriel "Prob...probably. Yeah."
                london "You look like you've seen a ghost."
                gabriel "Oh...yeah...that's from the guarding...I'm wiped."
                naomi "You didn't even fight!"
                london "That's just how guarding someone works, it tires them out."
                gabriel "Yeah, what she said...you can all go."
                london "I'm staying with you."
                gabriel "Sure...I guess your sister also did this, huh...see the rest of you later."
                "You head home with your friends."
            #brandon alive, naomi dead
            elif not brandon_dead:
                show brandon at midright
                brandon "Gabriel will get it taken care of."
                adrian "Was...that crowd always there?"
                brandon "I guess she wanted her last bit of attention. Gabriel will figure something out."
                "Gabriel eventually walks over with London."
                show brandon at midmidleft
                hide sarah
                hide adrian
                show gabriel at midmidright
                show london at midright
                gabriel "Well...I guess that's how the story goes. You're all free to head home, I'll figure something out."
                brandon "You sure you're good?"
                gabriel "Yeah, I'll...I'll be fine..."
                london "Are you ok?"
                gabriel "Prob...probably. Yeah."
                london "You look like you've seen a ghost."
                gabriel "Oh...yeah...that's from the guarding...I'm wiped."
                brandon "If you need anything, let us know."
                gabriel "Naw man, but thanks...you can all go."
                london "I'm staying with you."
                gabriel "Sure...I guess your sister also did this, huh...see the rest of you later."
                "You head home with your friends."
            #brandon dead
            else:
                show sarah at midright
                adrian "Was...that crowd always there?"
                sarah "I'm a little worried about that...but Gabriel will know what to do..."
                naomi "That seems unfair for Gabriel, though. We're really going to pile all this on him?"
                adrian "That's just what we've always done."
                naomi "You WHAT?"
                sarah "Not so loud!"
                "Gabriel walks over with London."
                hide sarah
                hide adrian
                show naomi at midmidleft
                show gabriel at midmidright
                show london at midright
                gabriel "Well...I guess that's how the story goes. You're all free to head home, I'll figure something out."
                naomi "That's not fair to you!"
                gabriel "It's...not about fairness, it's more like a duty. Some official will surely come down, and I'll...see what happens..."
                london "Are you ok?"
                gabriel "Prob...probably. Yeah."
                london "You look like you've seen a ghost."
                gabriel "Oh...yeah...that's from the guarding...I'm wiped."
                naomi "You didn't even fight!"
                london "That's just how guarding someone works, it tires them out."
                gabriel "Yeah, what she said...you can all go."
                london "I'm staying with you."
                gabriel "Sure...I guess your sister also did this, huh...see the rest of you later."
                "You head home with your friends."
        #london and gabriel not dating
        else:
            "Sarah grabs London."
            sarah "Ah! Ow! London! Stop!"
            london "She deserves this!"
            sarah "Please, stop!"
            "London looks back at Sarah, and pushes her away."
            london "You of all people should know we did what had to be done! You should revel in this!"
            sarah "This is inhumane! No one deserves this!"
            #naomi attacks and scolds london
            if not naomi_dead:
                show naomi at midmidleft
                "Naomi shoots water at London, pushing her off Scarlet."
                london "What the hell was that for?!"
                naomi "Stop this at once!"
                london "No! You don't know what her sister put us through! She deserves this!"
                "Naomi fires more water at London."
                london "Stop that!"
                naomi "Stand up and get out of here."
                london "Not until she suffers for what she's done!"
                naomi "GET OUT OF HERE!"
                "That might be the first time you've heard Naomi scream."
                "Silence quickly falls on the bridge."
                naomi "Get...out of here before I kill you."
                london "The fuck is your-"
                "Naomi aims her hands at London."
                sarah "Please, stop this! No one else needs to get hurt!"
                london "Fine...Fine! I'll go, happy?"
                "London walks away."
                hide london
                show gabriel at midright
                gabriel "That...was something..."
                hide naomi
                show adrian at midmidleft
                adrian "Dude, are you alright? You look exhausted."
                gabriel "Yeah...guarding does that...I'll...figure this mess out."
                adrian "I'll stay with you."
                gabriel "Naw, man...you can head out, they'll...send some official to look over this, and...I'll see what I can do. You're all good to go."
                adrian "Alright. Take care, man."
                "You head home with the rest of your friends."
            #no one scolds london
            else:
                "You all watch as Scarlet is burned to ashes."
                london "There, see? Problem solved. We're done here."
                show gabriel at midmidleft
                gabriel "Well then...I guess...you can all head home..."
                london "You look exhausted. Just lie down and you'll be fine."
                gabriel "Yeah, I'll...stay here until someone shows up...you're all good to head back."
                "You all head back, without muttering a word to each other."
    #back home to celebrate
    scene bg lobby
    with fade
    #brandon and naomi alive
    if not brandon_dead and not naomi_dead:
        show lucas at midleft
        show naomi at midmidleft
        show adrian at midmidright
        show brandon at midright
        adrian "Alright, we did it!"
        brandon "You could've said that anytime we were heading home."
        adrian "It wouldn't be as dramatic without being here!"
        naomi "Why don't we wait for Gabriel to come back before celebrating?"
        brandon "A sound plan."
    #naomi dead
    elif not brandon_dead:
        show lucas at midleft
        show adrian at midmidleft
        show brandon at midmidright
        show sarah at midright
        adrian "Alright, we did it!"
        brandon "You could've said that anytime we were heading home."
        adrian "It wouldn't be as dramatic without being here!"
        brandon "You have some intriguing moments."
        adrian "It's just...part of my charm! Yeah!"
        brandon "You can show that 'charm' when Gabriel gets home."
    #brandon dead
    elif not naomi_dead:
        show lucas at midleft
        show adrian serious at midmidright
        show naomi at midmidleft
        show sarah at midright
        adrian "Well...we did it."
        naomi "It feels...empty in here..."
        adrian "Yeah. I get what you're saying."
        naomi "Let's wait until Gabriel gets back. Maybe he'll have something for us?"
        adrian "We'll see."
    #brandon and naomi dead
    else:
        "The lobby is quiet."
        "You all sit in silence, making various bits of small talk."
    #gabriel comes back
    scene bg lobby
    with fade
    "After some time, Gabriel returns."
    #brandon and naomi alive
    if not brandon_dead and not naomi_dead:
        show lucas at midleft
        show naomi at midmidleft
        show adrian at midmidright
        show gabriel at midright
        adrian "Hey, look who it is!"
        gabriel "Yeah, yeah. Welcome home, and all that."
        hide adrian
        show brandon at midmidright
        brandon "What's the news?"
        gabriel "Honestly, not great. They weren't exactly thrilled with something like this happening again. We'll just have to see how it turns out."
        naomi "Everything will be ok!"
        gabriel "Probably, yeah. We'll see if they understand where we were coming from. It's been a hell of a year, I'll say. Let's go do something!"
        naomi "That sounds like fun! Doesn't it, Lucas?"
        lucas "I suppose so."
        naomi "C'mon, after this entire year! At least show some enthusiasm!"
        "You smile."
        lucas "Yeah...I guess it has been an interesting year."
        naomi "That's the spirit!"
    #naomi dead
    elif not brandon_dead:
        show lucas at midleft
        show brandon at midmidleft
        show adrian at midmidright
        show gabriel at midright
        adrian "Hey, look who it is!"
        gabriel "Yeah, yeah. Welcome home, and all that."
        brandon "What's the news?"
        gabriel "Honestly, not great. They weren't exactly thrilled with something like this happening again. We'll just have to see how it turns out."
        brandon "With any luck, we'll get through whatever they're planning."
        gabriel "Probably, yeah. We'll see if they understand where we were coming from. It's been a hell of a year, I'll say. Let's go do something!"
    #brandon dead
    elif not naomi_dead:
        show lucas at midleft
        show naomi at midmidleft
        show adrian serious at midmidright
        show gabriel at midright
        adrian "Welcome back."
        gabriel "Yeah, yeah. Welcome home, and all that."
        adrian "What happened after we left?"
        gabriel "The officials weren't exactly thrilled with something like this happening again. We'll just have to see how it turns out."
        naomi "Everything will be ok!"
        gabriel "Probably, yeah. We'll see if they understand where we were coming from. It's been a hell of a year, I'll say. Let's go do something!"
        naomi "That sounds like fun! Doesn't it, Lucas?"
        lucas "I suppose so."
        naomi "C'mon, after this entire year! At least show some enthusiasm!"
        lucas "I guess it has been an interesting year."
        naomi "That's the spirit!"
    #brandon and naomi dead
    else:
        show lucas at midleft
        show sarah at midmidleft
        show adrian serious at midmidright
        show gabriel at midright
        adrian "Welcome back."
        gabriel "Yeah, yeah. Welcome home, and all that."
        adrian "What happened after we left?"
        gabriel "The officials weren't exactly thrilled with something like this happening again. We'll just have to see how it turns out."
        adrian "Here's for hoping."
        gabriel "We'll see if they understand where we were coming from. It's been a hell of a year, I'll say. Let's go do something, get our heads into something more fun than standing around."
    #game done
    scene bg black
    with fade
    "It was a wild year."
    "Gabriel insists he's proud of you for sticking with him."
    "I suppose it was...intriguing to see this side of you."
    "You're lucky to still be standing."
    "I'll have to see what you make of your newfound future."

    #the end

    #person, day, most recent grade:
    #Naomi: Any, Any
    #Scarlet: Mon/Tues/Thurs, Any
    #Gabriel: Mon/Wed/Fri, Any
    #Carson: Mon/Tues/Thurs, 1 and below
    #Adrian: Tues/Thurs/Fri, 1 and above (magic shown) or 3 and above (magic not shown)
    #Brandon: Not Friday, 4 (first link), 3 and above
    #London: Mon/Tues/Wed, 2 and below
    #Sarah: Wed/Thurs/Fri, 2 and above

    #factors to influence the ending:
    #naomi alive
    #brandon alive
    #brandon at event 2
    #brandon at event 2 and alive

    return
#bowling scene: event 1
label bowling:
    scene bg bowling alley
    with fade
    show lucas at midleft
    show carson at midmidleft
    show gabriel at midright
    show adrian at midmidright
    carson "This was a fantastic idea!"
    adrian "Oh, it's been so long since we've been able to do something fun. I wish Brandon was here."
    gabriel "You know how he is with social situations nowadays, and I don't blame him necessarily."
    lucas "He can do what he wants."
    show carson at top with moveinleft
    adrian "Yeah, well, still wish he'd just move on and try to have some fun."
    lucas "Move on?"
    show adrian serious
    adrian "Well..."
    gabriel "No, I'll say it. He can be mad at me if he cares."
    adrian "All yours."
    gabriel "Brandon had to kill his best friend. His name was Blake, and he desperately wanted to be a hero. He loved comics a little too much. In a...weird way."
    adrian "How was killing Blake supposed to be a blessing? I still never understood that."
    gabriel "Brandon did some serious work in that final fight, which is my guess."
    lucas "What exactly are blessings? They haven't been explained."
    show carson at midmidleft with moveinright
    carson "You forgot to mention curses with them, those were much more important."
    gabriel "How could we forget about your dumb, stupid face?"
    carson "Haha! That's right, that was mine! I really saved our asses!"
    gabriel "The blessings and curses were given to us at random, and we would find out what was who later. Brandon, Carson, and I had the blessings in our group here."
    show adrian
    adrian "I had a curse, but it could've been so much worse compared to the rest of them, just not opening my mouth at the right time wasn't as bad as dying."
    gabriel "Yeah. London and Sarah weren't as lucky with theirs. I feel terrible for them."
    carson "Oh, don't sweat it Gabe! You-"
    gabriel "Don't call me Gabe."
    lucas "Didn't London call you Gabe?"
    adrian "Ohhh, you have a soft spot for London, do you?"
    gabriel "You shut your mouths, it's not like that. She's just really hurt, and-"
    show adrian at top with moveinright
    "Carson raises the pitch in his voice."
    carson "'Oh, if only someone strong and assertive could be there for me!'"
    gabriel "Yeah, yeah. Laugh it up, if it makes you feel better. It's not that funny."
    lucas "It is a little funny."
    gabriel "Even you? You don't laugh at anything!"
    carson "You're in charge, obviously we're going to poke fun of you! And you made it really easy, too!"
    show adrian at midmidright with moveinleft
    gabriel "Yeah, well, enjoy it while you have the chance."
    "It's your turn to bowl."
    show lucas at top with moveinleft
    "You used to bowl every summer with your family, practically every week."
    "You could never beat Claus."
    "You'll never get the chance."
    "..."
    "You line up your shot."
    "..."
    "You got a strike!"
    "You walk back to the group."
    show lucas at midleft with moveinright
    adrian "That redhead in our math class? Really?"
    carson "She's fun! We have a groove going when we're at the same parties."
    gabriel "Just don't have the balls?"
    carson "I don't want to ruin the fun. You know how I am with that..."
    gabriel "That's fair."
    "The guys turn to look at you."
    adrian "So what about you, you have the hots for Naomi, right?"
    lucas "It's not like that."
    carson "Suuuuuuure you don't, we toooootally believe you."
    lucas "I don't care if you believe it or not."
    gabriel "Alright, no need to bully the new roommate."
    "Carson brings out his high pitched voice again."
    carson "'Oh Gabey-poo, I'm so happy with you!'"
    gabriel "I never said to switch to me!"
    adrian "To be fair, you started this, so it's all fair."
    gabriel "Oh wow, would you look at the turn order, I'm up!"
    "Gabriel hastily walks to bowl."
    show gabriel at top with moveinright
    carson "He seems happier. It's good for him."
    adrian "Yeah, now we just have to convince Brandon."
    carson "That's all you. Brandon and I don't exactly have the same mindset."
    adrian "What, you have poor grades?"
    carson "I go to waaaaay too many parties to study. Besides, that's what nerds do!"
    adrian "You should at least care about your future a little bit, right?"
    carson "All that matters is being happy with life!"
    "Gabriel looks back."
    gabriel "You should be studying more, man."
    carson "I'll pass, thanks."
    show apathy_down at topleft
    "You enjoyed bowling with the guys."
    $ apathy -= 1
    hide apathy_down
    return
#brandon stays home from the party, and he spent the time working on a hunch
label scene_brandonr1:
    brandon "Something's bothering me. Something feels...wrong. It could just be a hunch, but if I'm right, things could be very bad for us."
    naomi "What is it?"
    brandon "Looking at the catalog of magic, it comes in many forms, and it may even come in forms we haven't seen yet."
    brandon "Some of these have their own category, like all the aura reading magic. For aura reading magic, their eyes change color when they're 'reading' something. They have the same ways of using them, in a sense."
    show london at truecenter
    london "What do I have to do with this?"
    brandon "There are many aura read magics, but we've only personally encountered London's family and Noah from the other group."
    hide london
    brandon "Yet, somehow...we have people with four elemental magics. Naomi's water, Carson's earth, Scarlet's psionic, Lucas' fire. All different elements, meeting at the same place? It rubs me the wrong way."
    naomi "Didn't Claus have something similar to us?"
    lucas "He had electric magic."
    brandon "That's insane. There was potential for every element we know of to meet in one spot. That can't be a coincidence, something or someone planned for this to happen."
    brandon "Do you know the odds of that? Excruciatingly low. We're being watched, to some extent. By what, I have no idea."
    hide naomi
    show scarlet at midmidleft
    scarlet "You sound crazy."
    brandon "It could just be speculation, but I'd be damned if it wasn't."
    hide scarlet
    show naomi at midmidleft
    return
#naomi's first scene; talk about Claus, Lucas' twin
label scene_naomi1:
    scene bg city walkway
    with fade
    "You're walking around town with Naomi."
    show lucas at midleft
    show naomi at midright
    naomi "Are you enjoying your new friends?"
    lucas "I guess."
    naomi "You should at least try to!"
    lucas "I'm working on it. Gabriel told me to hang out with the rest of them."
    naomi "That sounds like a great idea! How has it been?"
    lucas "It's been fine, so far."
    naomi "Well, you're hanging out with me right now!"
    lucas "We've always done that, though."
    naomi "Well, how about we talk about something we normally don't?"
    lucas "Like what?"
    naomi "How about...Claus?"
    lucas "You want to talk about my dead twin?"
    naomi "When you say it like that it sounds awful...I meant what happened to me after."
    lucas "What happened, then?"
    naomi "I remember you ran, when he said to run. Seeing him, in pain...something...changed. I felt power. I felt powerful! And it felt...good."
    naomi "There was a warmth in my heart. There was power in my hands. I felt alive."
    lucas "That was the same with the fire shield."
    naomi "I reached my hand out to that bear, and...water just gushed from my palm. I pushed towards the bear. When he ran off I almost wanted to chase after it."
    lucas "You sound like a psychopath."
    naomi "I might've if Claus hadn't said something. I tried to help him, I really did. I promise I tried."
    lucas "I understand. It's ok."
    naomi "Let's drop this...I don't want to think about Claus. It makes me sad thinking about him."
    lucas "Sure."
    naomi "Actually...sorry to cut this short, but I think I need to head back. I feel sick...I think."
    lucas "You think?"
    naomi "Well, when you put it like that, I don't know. Sorry. We'll do something next time, ok?"
    "Naomi smiles."
    show apathy_down at topleft
    "You enjoyed your time with Naomi."
    $ apathy -= 2
    $ happiness += 3
    hide apathy_down
    $ naomi1 = True
    $ last_person = "Naomi"
    return
#if scarlet is in the group, she and naomi are talking before naomi's second event
label scene_naomi2:
    if scarlet1:
        "You walk up to Naomi's room."
        scene bg door
        with fade
        "You can hear Naomi and Scarlet talking."
        menu:
            "You can hear Naomi and Scarlet talking."
            "Knock on the door.":
                "You knock on the door. Naomi opens it."
                show naomi at truecenter
                naomi "Oh, hey Lucas! Were you looking to do something?"
                lucas "Yeah, if you're not busy."
                naomi "I'll be out soon!"
            "Listen to the conversation.":
                "You listen to their conversation."
                naomi "You can't possibly believe that!"
                scarlet "Give it some years, and you'll see everyone is only looking out for themselves."
                scarlet "If you've got some hair sticking out, you're going to be thinking more about your hair than my discolored socks."
                scarlet "Everyone's too busy looking at their own flaws to see other people's flaws. These people are no different, including you."
                naomi "That's not true, I care about Lucas and he cares about me. How can you be so cynical? We're on the same side here!"
                scarlet "Does he? Does he really care about anything? Does he try to make you happy?"
                naomi "Well, I care for him, and that's enough for me."
                scarlet "I showed that same care and nothing came from it. It didn't matter how much I cared, it was all for nothing."
                naomi "I'm sorry you feel that way."
                scarlet "Save your pity. I'm your future if you keep that attitude up. I used to be all bubbly like you."
                scarlet "I used to enjoy every part of life and everyone in it. I used to be as happy as you. Just watch yourself."
                $ happiness -= 1
                "You hear footsteps coming towards you."
                "You hastily knock on the door. Naomi opens it."
                show naomi at truecenter
                naomi "Oh, hey. Did you want to do something?"
                lucas "Yeah, if you're not busy."
                naomi "I'll be out soon."
    #naomi's second scene; naomi feels guilty about lucas' apathy
    scene bg park
    with fade
    show lucas at midleft
    show naomi at midright
    "You're at the park with Naomi."
    naomi "How are you feeling?"
    lucas "Fine."
    naomi "That's good! Good. Happy to hear."
    lucas "What about you?"
    naomi "After last time, I...was thinking about Claus. Actually...I still do. I'm sorry."
    lucas "You don't have to apologize."
    naomi "No, but...I feel like he's dead because of me."
    lucas "That's not true at all."
    naomi "We were looking for one of my stuffed animals, and he just wanted to help. I feel terrible about it."
    lucas "No one could have predicted what would happen."
    naomi "But look what happened! You barely care or smile or laugh anymore and it torments me! I did this to you! I made you this way!"
    show naomi sad
    "Naomi has tears in her eyes."
    lucas "Naomi-"
    naomi "Don't look at me! I'm sorry! I'm so sorry, please...I'm sorry."
    lucas "Naomi!"
    "You didn't mean to shout."
    "Naomi turns back to you."
    lucas "It's not your fault. The only one to blame is that bear. It was our choice to help you, because you're our friend. My friend."
    naomi "I still feel so guilty about it! If you could just be happy again, I feel like all my guilt would go away."
    lucas "You don't have to worry about that."
    naomi "I don't want to feel guilty. I don't want to feel like it's my fault he's gone. I'm tired of it. I'm sick of it!"
    show apathy_down at topleft
    lucas "Listen! It's not your damn fault. No one is to blame, alright? What's done is done, and no matter what you feel, I'm happy you're here."
    $ apathy -= 1
    hide apathy_down
    naomi "Do you really mean that?"
    lucas "Yes, and you look ugly when you cry."
    show naomi
    naomi "Hey!"
    "Naomi wipes tears from her face."
    naomi "Th-Thanks. Sorry."
    show apathy_down at topleft
    "You enjoyed the park with Naomi."
    $ apathy -= 2
    hide apathy_down
    $ happiness += 3
    $ naomi2 = True
    $ last_person = "Naomi"
    return
#naomi's third scene; she feels less guilty about claus
label scene_naomi3:
    scene bg bridge
    with fade
    show lucas at midleft
    show naomi at midright
    "Naomi walks you through the city."
    naomi "Isn't this view amazing?"
    lucas "It looks like a river to me."
    naomi "You don't need to be so on the nose about it!"
    lucas "Sorry."
    "Naomi gazes out on the river."
    naomi "I don't feel so guilty anymore. I...think I'm starting to realize that Claus is gone."
    lucas "He died a long time ago."
    naomi "I know! I just kept thinking about him, or what he'd think, or how different you two are."
    lucas "He's not coming back."
    naomi "I know! I know. Geez, you don't have to be so blunt about it."
    lucas "How else am I supposed to say it?"
    naomi "Just ease into it, like 'I know you're upset, and I'm here if you need it.' Or something like that."
    lucas "I'm standing right here."
    naomi "Not like that!"
    "Naomi is smiling as she turns back to you."
    naomi "You can be so annoying sometimes."
    lucas "You seem to have stuck around."
    naomi "Yeah, well, someone's gotta make you see what life can offer you, might as well be me."
    "You gaze out onto the river."
    naomi "What do you see?"
    lucas "It's a river."
    "Naomi punches your arm."
    naomi "Not like that! Like...what are you thinking about?"
    lucas "Claus would've dragged me here, too. If he was alive."
    naomi "We would've been everywhere twice by now!"
    "Naomi's laugh turns into a more serious expression."
    naomi "I guess we'll just have to live the life he never had, and you're the one who's going to do that."
    lucas "I am?"
    "Naomi punches your arm again."
    naomi "Yes! You are! And I'm going to make sure it happens!"
    lucas "You sure about that?"
    naomi "It's how I can make up for not being with him here today. I'll just make sure you get the life he would've wanted you to have. Now c'mon! Let's go to more places!"
    show apathy_down at topleft
    "You enjoy your time in the city, Naomi dragging you everywhere she could think of."
    $ apathy -= 2
    hide apathy_down
    $ happiness += 3
    $ naomi3 = True
    $ last_person = "Naomi"
    return
#naomi is on her deathbed, doesn't want to talk to lucas
label naomi_deny:
    "Naomi isn't in the lobby, so you head up to her room."
    "You knock on the door. Naomi opens is slowly."
    show naomi sad at truecenter
    naomi "What...do you want?"
    lucas "Did you want to do something today?"
    naomi "Leave me alone..."
    "Naomi slowly closed the door."
    show apathy_up at topleft
    "Even Naomi?"
    $ apathy += 1
    hide apathy_up
    $ naomi_check = True
    return
#scarlet's first scene; she reveals she's resentful about something
label scene_scarlet1:
    scene bg park
    with fade
    show lucas at midleft
    show scarlet at midright
    "You're at a park with Scarlet."
    scarlet "It's nice to be somewhere peaceful. I don't normally pass by this place, but I should start."
    lucas "It's a little out of the way, I see what you mean."
    scarlet "I love all the nature we can see. Look at that tree there, that must be very old. Oh, and that flowerbed must be new! Look at nature thriving!"
    lucas "Nature grows everywhere, forever."
    scarlet "Like resetnment, right? Just grows and grows until it snaps."
    lucas "I wouldn't compare the two."
    scarlet "Why not? They both take up space until it's all you see. Only until something else strikes them down."
    lucas "That's a weird way to see nature."
    scarlet "We're understanding of nature, though. It's just doing what it was designed to do. Yet, somehow, resentment is always seen as bad."
    lucas "Resentment spreads pain, outside its environment. Nature sticks to its roots."
    scarlet "But nature can spread pain in that environment!"
    lucas "You are the environment. Nature grows in its small area, but your resentment travels."
    "Scarlet ponders."
    scarlet "Maybe I need to think about it more."
    lucas "Are you implying you're resetnful?"
    scarlet "Well...that's one way to put it. I'm resentful that I see the truth."
    lucas "What truth?"
    scarlet "Everyone's just out for themselves."
    lucas "Some people yes, but not everyone."
    scarlet "We can talk about it another time. I want to enjoy nature for now."
    show apathy_down at topleft
    "You enjoyed time with Scarlet."
    $ apathy -= 1
    hide apathy_down
    $ scarlet1 = True
    $ last_person = "Scarlet"
    return
#scarlet's second scene; talking about freedom
label scene_scarlet2:
    scene bg graveyard
    with fade
    show lucas at midleft
    show scarlet at midright
    "You're at a graveyard with Scarlet."
    lucas "Why did you want to visit a graveyard?"
    scarlet "I'd like to pay my respects."
    lucas "Anyone in particular?"
    scarlet "Yes, but I don't want to talk about her."
    "You pay your respects for the dead."
    scarlet "I want to continue that conversation from the park."
    lucas "Which is?"
    scarlet "That everyone's only out for themselves. I'm surprised you don't think the same way."
    lucas "Does that apply to everyone at the house?"
    scarlet "Have you listened to them? You have to have seen it, where they talk and talk and talk about themselves."
    lucas "It's interesting to learn more about them."
    scarlet "That's the thing! Where you see it as interesting, I think it's appalling. It should be push and take."
    lucas "There aren't rules for conversation, it just flows."
    scarlet "With the friends you have, I don't know how you do it."
    lucas "Gabriel told me to make friends with them."
    scarlet "What, so you just do as you're told? Don't you want to be free? Have your own choices? Choose your own path, no matter what you're up against?"
    lucas "I'm fine as is."
    scarlet "Look at this graveyard. You don't give a shit about most of these people, right? That's where you're going to end up. No one is going to care."
    scarlet "When are you going to be happy with your life, and be done living the life other people want you to live? You can be free, free from all these assholes."
    scarlet "You are in control of your life. Choose to be free!"
    lucas "You wouldn't say I'm free?"
    scarlet "C'mon, with how you've made friends because 'Gabriel told you to?' And look at how Naomi just orbits you, she won't leave you alone."
    lucas "Naomi's being a good friend."
    scarlet "She won't leave you alone. She won't let you be free. If she says otherwise, you'll bow to her. That's not freedom."
    lucas "I'm not bound to anyone, it's still my choice to listen to her."
    scarlet "Just keep it in mind. Don't say I didn't warn you. Everyone should be free."
    show apathy_down at topleft
    "You enjoyed talking with Scarlet."
    $ apathy -= 1
    hide apathy_down
    $ scarlet2 = True
    $ last_person = "Scarlet"
    return
#scarlet's third scene; scarlet wants revenge
label scene_scarlet3:
    scene bg bridge
    with fade
    show lucas at midleft
    show scarlet at midright
    "You're walking through the city with Scarlet."
    scarlet "I don't know why, but I enjoy talking with you. You don't just agree with everything I say."
    lucas "You say some outlandish things."
    scarlet "It's normal for me. When you go through hell, you think about all the things you can see that are wrong."
    lucas "Like what?"
    scarlet "Like...how we do justice, right? If you break my leg, your leg should be broken as well. That sounds fair to me."
    lucas "A leg for a leg cripples the world."
    scarlet "Alright mister philosopher, maybe there's merit to that. What about finally getting revenge, though?"
    lucas "It'll just blind you from moving on."
    scarlet "Well how is that fair?"
    lucas "It's not, and the world is never fair."
    scarlet "We should be trying to make things fair, then. Allow people to get their revenge and they'll be at peace faster."
    lucas "That'd just lead to more people getting revenge afterwards, it'd be many broken legs."
    "Scarlet looks at the ground."
    scarlet "Well, screw justice. I want revenge."
    lucas "From what?"
    scarlet "Wouldn't you like to know."
    lucas "You brought it up."
    "Scarlet looks back at your."
    scarlet "My...family. They robbed me of a normal life, me and my sister. They took away any sort of freedom we would've had, just because we have this damn magic."
    lucas "That wasn't their fault, they didn't know how magic worked."
    scarlet "How can you be so sure? Didn't anything go bad in your life?"
    lucas "My twin was attacked by a bear."
    "Scarlet averts your eyes."
    scarlet "Damn. That sucks."
    "Scarlet turns back to you."
    scarlet "We're not so different, then. Magic, sibling dying...yet, you don't want revenge. Why?"
    lucas "I don't care for it. What happened happened."
    scarlet "Would you change it, if you could?"
    lucas "I don't know."
    scarlet "That's not an answer."
    lucas "I am who I am today because of what happened. I don't have an answer at this time, I'd have to think about it more."
    scarlet "Well, maybe you can tell me that answer someday."
    lucas "Maybe I will."
    show apathy_down at topleft
    "You enjoyed a walk with Scarlet."
    $ apathy -= 1
    hide apathy_down
    $ scarlet3 = True
    $ last_person = "Scarlet"
    return
#gabriel's second scene; gabriel blames himself for the group's despair
label scene_gabriel2:
    scene bg gym
    with fade
    show lucas at midleft
    show gabriel at midright
    "You're working out with Gabriel."
    gabriel "I'll be honest, you can pull more weight than I thought you could."
    lucas "My family lives on a barn."
    gabriel "Yeah, that'll do it. Lot of work?"
    lucas "At times, yeah. I still got my work done."
    gabriel "Wish I could say the same about us. Getting things done, that is. I feel like we've fallen apart."
    lucas "You treat each other well enough."
    gabriel "We're not like we used to be, though. We used to be in the glory days. We WERE the glory days, and I fucked it all up."
    lucas "You said none of you were immune to what happened."
    gabriel "I let it slide, though. I held the same thoughts, to a lesser extent, and I never stopped it. I was too selfish."
    lucas "You need to grow a backbone and stop blaming yourself for everything."
    gabriel "And you need to show joy in your life."
    lucas "Funny."
    gabriel "Tell you what, I'll look into learning from past mistakes, and you look into being happier, deal?"
    lucas "If you say so."
    gabriel "Good. It'll keep us both accountable, then."
    lucas "You care about them, that should be good enough."
    gabriel "No amount of care can bring back the dead."
    lucas "Then why care at all, if it's pointless?"
    gabriel "It's not pointless. You're alive and kicking. You're here, with me, no matter how little you claim to not care."
    lucas "You told me to make friends."
    gabriel "You're enjoying socializing more than you give yourself credit. Life is about the people around you. I don't know where you lost it, but I'll help you find it."
    lucas "You don't have to."
    gabriel "You're one of us, man. You're finding happiness, whether you like it or not."
    lucas "If you say so."
    gabriel "Glad we agree."
    show apathy_down at topleft
    "You enjoyed working out with Gabriel."
    $ apathy -= 1
    hide apathy_down
    $ gabriel2 = True
    $ last_person = "Gabriel"
    return
#gabriel's third scene; gabriel feels beeter about his choices
label scene_gabriel3:
    scene bg gym
    with fade
    show lucas at midleft
    show gabriel at midright
    "You're working out with Gabriel."
    gabriel "How are you feeling?"
    lucas "Fine."
    gabriel "Don't give me that, you can be open with me."
    lucas "I feel fine."
    gabriel "We'll work on it, then."
    "You continue working out."
    gabriel "I've been feeling better. I've taken the time to reflect, and I don't think I would've changed anything."
    lucas "You don't want to change the mistakes you've made?"
    gabriel "I am who I am today because of everything I've been through. If I never went through it, I wouldn't be able to recognize myself."
    lucas "Even if it meant letting your friends die?"
    gabriel "I didn't let them die, it was just out of my control. The best I can do now is lead them to a better future."
    lucas "That's admirable."
    gabriel "Thanks, thought of it myself."
    lucas "Do you think you would've eventually changed for the better later, without your friends dying?"
    gabriel "I don't know. Maybe I would've been better in another life, without friends dying, but no one can say for certain. If I had to choose another life, I would choose mine every time."
    lucas "Good for you."
    if not london3:
        gabriel "Also, keep it on the down low, but I think I'm going to ask London out on a date."
        lucas "Really? Her?"
        gabriel "We've been through hell. She used to be...a lot different. I know the potential she has."
        lucas "Go for it."
        gabriel "Thanks, man. Even if it doesn't work out, oh well. Good talk, yeah?"
    else:
        gabriel "Also, sorry about...what happened when you were out with London."
        lucas "Where you got rejected?"
        gabriel "Just making sure you didn't have any hard feelings there. Didn't know if you were after her or not."
        lucas "I can't think of someone who would be worse to ask out."
        gabriel "She used to be a lot different, before Miss Fortune. She has that potential...somewhere. Probably not worth the hassle, though."
        lucas "There are other people."
        gabriel "Oh yeah, definitely. I'm not worried. Good talk, yeah?"
    show apathy_down at topleft
    "You enjoyed working out with Gabriel."
    $ apathy -= 1
    hide apathy_down
    $ gabriel3 = True
    $ last_person = "Gabriel"
    return
#if magic shown, gabriel won't hang out during week 1
label gabriel_deny:
    lucas "Hey Gabriel, you want to do something?"
    gabriel "I...have to sort some things. Sorry."
    "Gabriel turned you down."
    show apathy_up at topleft
    "And he's the leader..."
    $ apathy += 1
    hide apathy_up
    $ gabriel_check = True
    return
#carson's second scene; carson talks about his early life
label scene_carson2:
    scene bg arcade
    with fade
    show lucas at midleft
    show carson at midright
    "You're at an arcade with Carson."
    carson "What's your story?"
    lucas "What do you mean?"
    carons "When did you find out about magic? What was your early life like? How'd you choose to come to this city?"
    lucas "I think my brother and Naomi always knew we had magic, early life was fine besides my brother dying, and Naomi wanted to come here."
    carson "I don't think I've heard you say so many words at once! I'm impressed!"
    lucas "You asked three questions..."
    carson "And you answered them!"
    "Carson smiles."
    carson "Sorry about your brother. I don't have a family, so I can't relate."
    lucas "What happened with you?"
    carson "Orphaned. I got passed around families a lot, usually because of magic."
    lucas "Sounds tough."
    carson "Oh, it was! But I live in the moment and don't think about it, I always remember to think positively!"
    lucas "Do you even have negative thoughts?"
    carson "Oh, definitely. Part of me wishes I never had magic. Or sometimes, I think about just walking into traffic one day, and I wouldn't have to deal with life."
    "Carson notices a concerned expression on your face."
    carson "Not that I'd ever do that! The Call of the Void is a psyche thing. Can you believe pepple just think of throwing themselves off cliffs?"
    lucas "Some people, yeah."
    carson "I guess you don't care enough to even get to that cliff, do you?"
    lucas "I guess."
    carson "We'll knock that attitude out of you!"
    lucas "You want me to have a cliff jumping attitude?"
    carson "Don't actually do it!"
    "Carson laughs and punches your arm."
    show apathy_down at topleft
    "You enjoyed the arcade with Carson."
    $ apathy -= 1
    hide apathy_down
    $ carson2 = True
    $ last_person = "Carson"
    return
#carson's third scene; reveals rules of strong magic
label scene_carson3:
    scene bg entrance
    with fade
    show lucas at midleft
    show carson at midright
    "You're talking with Carson at the doorway."
    carson "So, how about the park?"
    lucas "And do what?"
    carson "I dunno. We'll find something!"
    "{i}*thud*{/i}"
    "Carson trips on the stairs."
    "You walk over to him and look him over."
    "Carson gets up and laughs."
    carson "Should've watched my step, ha!"
    lucas "Why are you laughing?"
    carson "I thought it was funny!"
    lucas "You ate the floor."
    carson "I sure did!"
    "Carson laughs at himself."
    lucas "How are you so happy?"
    carson "Well, everyone should be! Me personally, I have to be."
    lucas "No one has to be."
    carson "I do, unfortunately."
    lucas "Why?"
    carson "Strong magic. We're some of the unlucky ones that have it, you, me, and I'm guessing Naomi."
    lucas "That doesn't answer my question."
    carson "Stronger magic has a downside. If you don't maintain your general happiness from when you got the stronger magic, your magic starts to attack you."
    lucas "So magic is sentient?"
    carson "I wouldn't know, that'd be something for Brandon. Also, that explanation is courtesy of Brandon, too. Gabriel's the only one who knows about my strong magic."
    lucas "Sounds tough for you."
    carson "It was, until that war vet made us. My life has been a lot better since then. It's weird luck, right?"
    "Carson chuckles."
    carson "That's why I was passed around a lot. I was really small when I got strong magic, and the earthquakes scared them. I don't even know what my normal magic is supposed to be."
    lucas "I'm sure you'll find it."
    carson "See, now that's the attitude you need!"
    "Carson laughs."
    carson "You've been great to us. I hope one day I'll get to see you as happy as I am!"
    lucas "We'll see."
    "After your talk, you walked through a park with Carson."
    show apathy_down at topleft
    "You enjoyed talking with Carson."
    $ apathy -= 1
    hide apathy_down
    $ carson3 = True
    $ last_person = "Carson"
    return
#carson denies if lucas has too high grades
label carson_deny:
    lucas "What's up, Carson?"
    carson "Not much, not much, what's up with you?"
    lucas "You up to do something?"
    carson "Ooh, sorry, but there's this dope party tonight. Yeah...but hit the books less and we'll have fun!"
    "Carson smiles, likely thinking of this 'party.'"
    show apathy_up at topleft
    "What a bore..."
    $ apathy += 1
    hide apathy_up
    $ carson_check = True
    return
#adrian's first scene; talks about whether lucas healed adrian, or hid his magic
label scene_adrian1:
    scene bg bistro
    with fade
    "You're eating at a restaurant with Adrian."
    show lucas at midleft
    show adrian at midright
    adrian "I'm surprised you're eating with me, of all the people we have."
    lucas "Gabriel told me to talk with everyone."
    adrian "That sounds like a good idea, considering he invited you in and considering our status. Maybe you'll make friends, like me and Brandon!"
    lucas "We'll see."
    "You arrive at the restaurant."
    adrian "Wait, we met at this restaurant, right?"
    lucas "Yeah."
    if magic_shown:
        adrian "In case I didn't mention it, thanks for patching me up."
        lucas "It was nothing."
        adrian "Oh, on the contrary, you risked exposing magic to the public, and just to help me. Seriously, you don't know how much it means t hat you'd do something for me."
        lucas "Why are you so thankful?"
        adrian "I dunno, I guess I was raised well?"
        "Adrian thinks for a moment."
        adrian "I think I just don't want people to be upset at me."
        lucas "With how Brandon scolded you?"
        adrian "He's uh, complicated. Before you say anything, I know he's not the best friend, but he's my friend."
    else:
        adrian "I'm a little hurt that you didn't fix my scrape."
        lucas "We were told to not show magic under any circumstance."
        adrian "That...makes sense, sorry."
        lucas "You were still thinking about that?"
        adrian "I didn't mean to bring it up, I just blurted it out."
        lucas "Doesn't Brandon get annoyed at that?"
        adrian "Ha, you nailed it, but we're still on good terms."
    "You sit at the table in silence."
    adrian "What about you and Naomi?"
    lucas "What about?"
    adrian "How'd you two become friends?"
    lucas "We lived close to each other."
    adrian "But you both have magic, so when did you find that out?"
    lucas "Don't remember. I think we just always knew."
    adrian "Why don't you show more enthusiasm to Naomi?"
    lucas "Why should I do that?"
    adrian "It'd make her happy, more than anything, and you want her to be happy, right?"
    lucas "I guess so."
    adrian "You guess?"
    lucas "I guess."
    "Adrian chuckles."
    adrian "I like your funny words, magic man."
    lucas "Don't call me 'magic man.'"
    adrian "Just poking fun, don't sweat it."
    show apathy_down at topleft
    "You enjoyed time with Adrian."
    $ apathy -= 1
    hide apathy_down
    $ adrian1 = True
    $ last_person = "Adrian"
    return
#adrian's second scene; adrian talks about magic and happiness
label scene_adrian2:
    scene bg lobby
    with fade
    show lucas at midleft
    show adrian at midright
    "You're chatting with Adrian."
    adrian "What do you think about having magic?"
    lucas "It's fine."
    adrian "You have to have some sort of opinion on it though, right?"
    lucas "Not particularly."
    adrian "Let me rephrase that, would the world be better with or without magic?"
    lucas "I don't know."
    adrian "What's your best guess?"
    lucas "I don't have an answer. It can be dangerous, but can also be helpful."
    adrian "Interesting, very interesting...you learn that from someone?"
    lucas "You have plenty of time to think when you're working on a barn."
    adrian "You are full of surprises."
    "The two of you sit in silence for a bit."
    adrian "Do you think the same thing about happiness?"
    lucas "I don't care for that."
    adrian "So you think we could just take sadness away from our lives and be happy?"
    lucas "That would make sense."
    adrian "No, no, that's not right at all, you need the sad times so you know what the happy times really are."
    lucas "You think we need to be sad?"
    adrian "Yes, absolutely, we have to be sad at some point, how else would we know when we're actually happy? If everything was always good, nothing would be good, because you'd have nothing bad to compare it with."
    lucas "What does that make me, then?"
    adrian "Well, from what I've seen, you're actually the opposite. With you, because everything is sad, then nothing is sad, if that makes sense."
    lucas "You think I'm sad?"
    adrian "You certainly don't appear happy about anything, so I'd say so."
    lucas "I just don't care."
    adrian "Yeah, well, happy people usually care about things, so I'd say you don't have a lot of happiness there, magic man."
    lucas "You're still calling me that?"
    adrian "Only when it's just us two, and it's just a nickname."
    lucas "I'd rather you didn't call me that."
    adrian "Hey, you cared about something, for once."
    "You stare blankly at Adrian."
    adrian "Hey, uh, I have some work to do...big important things for our glorious chief, you know how important he is...so, uh...next time, alright?"
    lucas "Alright."
    show apathy_down at topleft
    "You enjoyed a chat with Adrian."
    $ apathy -= 1
    hide apathy_down
    $ adrian2 = True
    $ last_person = "Adrian"
    return
#adrian's third scene; adrian talks about the group's magic
label scene_adrian3:
    scene bg burger joint
    with fade
    show lucas at midleft
    show adrian at midright
    "You're at a burger joint with Adrian."
    adrian "Have you figured out the forms of magic some of us have?"
    lucas "Not everyone, but some."
    adrian "Which ones?"
    if brandon_known:
        lucas "Brandon can punch souls from their body."
    if london_known:
        lucas "Brandon said London had aura read death, ghost form, flammability, and invisibility."
    elif london2 == True:
        lucas "I know London has multiple, but not which or how many besides being able to tell when people are about to die."
    if sarah2 == True:
        lucas "Sarah can see people's memories."
    lucas "Carson can create earthquakes."
    adrian "Well, I'll add another, but it's not as impressive as the rest, so don't get your hopes up. Anyone around my target will start to take damage to their soul, not their body, as long as I can see them."
    lucas "I can see how that'd be valuable to a team."
    adrian "That's the thing, though, ANYONE around the target. Including me, including friends, including civilians, so it can get messy. The radius seems to increase the longer I hold it, too."
    lucas "That still sounds interesting."
    if brandon1 == True:
        adrian "Yeah, from the outside, I can see it. Gabriel can also attack souls, so-"
        "Adrian suddenly stops."
        adrian "Huh, that's weird, our group has almost everyone that can attack the soul, and the six people in the other group only has one person."
        lucas "Is that bad?"
        adrian "No idea, was just a strange thing I noticed. Brandon's been talking to me about various things he's noticed, so I guess I'm in the same mindset."
    else:
        adrian "Yeah, from the outside, I can see it. Gabriel can also attack souls, so I guess that helps us work together."
    lucas "So what can Gabriel do?"
    adrian "He's got these swords on his back, one of them protects you and the other one slices your soul. One of London's sisters also had it, interestingly enough. She's in the other group."
    lucas "Well, that sounds handy to have."
    adrian "The upsides are fantastic, but that's the thing, the swords aren't 'bound' to him, he just makes them appear."
    lucas "So anyone can use them?"
    adrian "Yes, but that means someone can steal a sword, and he can't just make it appear on his back again. If he loses a sword, it's gone."
    lucas "Does all magic have a drawback?"
    adrian "Huh, now that's an interesting thought. I don't think so, but I can't confirm it. That would be very interesting to bring up to Brandon, though."
    lucas "Why is he so interested in magic?"
    adrian "I mean, why aren't you? We can do all sorts of things, and it only came around like twenty years ago! We know so little about it, so he probably just wants to learn more."
    lucas "I guess there's merit in that."
    "You continue eating your meal."
    adrian "Hey...thanks for spending time with me. I know you're not exactly someone who cares the most about things, but thanks for showing some care to spend time with me."
    lucas "No problem."
    adrian "Talking with you has helped me think about things in a different way, I can't exactly prove that, but I appreciate you being a friend."
    lucas "Happy to help."
    adrian "You? Happy? I'll believe it when I see you care about something. Uh, no offense."
    lucas "I'll work on it."
    adrian "Good! I'll be right there next to you when you do."
    show apathy_down at topleft
    "You enjoyed a meal with Adrian."
    $ apathy -= 1
    hide apathy_down
    $ adrian3 = True
    $ last_person = "Adrian"
    return
#adrian is more lenient if lucas healed him at the bistro
label adrian_deny:
    lucas "Adrian, do you want to do something today?"
    adrian "Nah, man, but thanks for the offer."
    "Adrian denied you."
    show apathy_up at topleft
    "Typical 'friend.'"
    $ apathy += 1
    hide apathy_up
    $ adrian_check = True
    return
#brandon's first scene; mends his relationship with adrian
label scene_brandon1:
    if stay or force_stay:
        scene bg entrance
        with fade
        show lucas at midleft
        show brandon at midright
        brandon "You're staying here?"
        if force_stay:
            lucas "Naomi told me to stay here."
            brandon "Harsh of her. Let's go to my library and get some studying in."
            lucas "Alright."
        else:
            lucas "Yeah."
            brandon "I wouldn't normally offer, but come to my library and we'll get some studying in."
            lucas "Alright."
    scene bg library
    with fade
    show lucas at midleft
    show brandon at midright
    brandon "You have to check the charges of the compounds of elements on the table to balance the equations. Add the charges on both sides, and figure out which compounds need to be doubled or tripled."
    "Brandon helps you study."
    if tempGrade < 4:
        "You feel as though you'll do better on the next exams."
        $ tempGrade += 1
    else:
        "You already feel very confident for the next exams."
    lucas "What's the deal with you and Adrian?"
    brandon "There isn't a deal. He's just a friend."
    lucas "He wants to hang with you more."
    brandon "He does?"
    lucas "When we met him, he was talking about you. Something about you two in a rocky situation."
    brandon "That's one way to see it. I've been focused on the future, I don't have time for him."
    lucas "He cares about you."
    brandon "Me?"
    lucas "He's convinced himself that he won't let the friendship die."
    "Brandon is silent, and looks at his notes."
    brandon "I had to kill my best friend. Blake. He'd gone mad with power before we went to kill Miss Fortune. It's still fresh in my mind."
    lucas "So you coop yourself in this library to deal with it?"
    brandon "Yeah. Probably."
    lucas "Adrian doesn't want that."
    brandon "I'm just preventing the same situation from happening again."
    lucas "That's unfair to Adrian. You'd be familiar if it was going to happen again, anyway."
    "Brandon is silent."
    brandon "I'll talk with him tomorrow."

    scene bg hallway
    with fade
    "After class..."
    show adrian at midleft
    show brandon at midright
    brandon "Listen, I'm sorry I haven't been the best. Just with how everything happened, I was distancing myself from it."
    brandon "I thought distancing myself from the people involved would help, but I was wrong. I'm sorry. You up to do something?"
    adrian "Cool. You up for some golf?"
    brandon "Golf? The most boring sport known to man?"
    adrian "What are you thinking of doing, then?"
    "Brandon thinks."
    show brandon happy
    brandon "How about golf?"
    "Adrian laughs."
    adrian "Alright you wise-ass, let's run it."
    "The two start to walk away from you."
    hide adrian
    hide brandon
    show apathy_down at topleft
    "You can't help but form a smile."
    $ apathy -= 5
    hide apathy_down
    $ smile = True
    show lucas at midleft
    show naomi at midright
    naomi "Are you smiling, Lucas?"
    "Instinctively, you turn away from Naomi."
    naomi "That was a smile! I knew you could do it! I knew you had some humanity in you!"
    "Naomi practically knocks you over in excitement."
    lucas "Yeah, yeah, whatever. Let's leave them be and get out of here."
    naomi "Next up, getting you to laugh!"
    "You start to walk away, Naomi following you. You hear Gabriel and London talk behind you."
    hide lucas
    hide naomi
    if not dating:
        gabriel "You ok?"
        london "I'm fine."
        gabriel "Jealous of them?"
        london "Shut the fuck up, you don't know my life."
    else:
        london "She seems ecstatic."
        gabriel "And you aren't?"
        london "No, I'm...happy. I feel better."
        gabriel "Good to hear."
    $ brandon1 = True
    $ last_person = "Brandon"
    $ brandonGrade = 2
    return
#brandon's second scene; brandon teaches lucas to study for a purpose
label scene_brandon2:
    scene bg library
    with fade
    show lucas at midleft
    show brandon at midright
    brandon "Magnetic fields behave similarly to electric fields, which you learned a bit ago. Here's a diagram-see how the positive charges arc towards the negative charges?"
    "Brandon helps you study."
    if tempGrade < 4:
        "You feel as though you'll do better on the next exams."
        $ tempGrade += 1
    else:
        "You already feel very confident for the next exams."
    brandon "You're doing good work with your classes."
    lucas "It comes from studying."
    brandon "Why do you study?"
    lucas "I was told to."
    brandon "Well that's no way to study now, is it?"
    lucas "It's worked well so far."
    brandon "No, that won't do it. You're not going to get real work done without positive motivation. If you lose that 'because I was told to' attitude, your studying will drop off a cliff."
    lucas "I'm not planning on losing it."
    brandon "I didn't plan to kill my best friend. Life is full of 'I didn't plan for x' things. Change that attitude and your studying will be safe."
    lucas "What are you saying I should study for, then?"
    brandon "Studying is all in the mindset. I study for my future. I study for a future worth living. If you think of studying like that, you'll be watching your back."
    lucas "What future?"
    brandon "I don't know your future or my future. What I do know is that it will come for all of us. I'll be prepared for it, and I'll make it worth it. You should think about it."
    lucas "I suppose that makes sense."
    brandon "You have a future, you might just not know it. Work for your future, and your future will work for you."
    show apathy_down at topleft
    "You enjoyed studying with Brandon."
    $ apathy -= 1
    hide apathy_down
    $ brandon2 = True
    $ last_person = "Brandon"
    return
#brandon's third scene; brandon talks about his studies with magic
label scene_brandon3:
    scene bg library
    with fade
    show lucas at midleft
    show brandon at midright
    brandon "Use the antiderivative for indefinite integrals. It's the reverse of taking the derivative. Remember because constants are removed when you derive, add a C constant."
    "Brandon helps you study."
    if tempGrade < 4:
        "You feel as though you'll do better on the next exams."
        $ tempGrade += 1
    else:
        "You already feel very confident for the next exams."
    lucas "Do you just study in your free time?"
    brandon "Technically, yes. I study for classes and I study magic."
    lucas "What about magic intrigues you?"
    show brandon happy
    brandon "I mostly just categorize it, truth be told. Here, there's a diagram I've been working on."
    "Brandon pulls a folded paper from a drawer, and unfolds it to take up the entire desk."
    brandon "It's a little much, but it keeps me occupied."
    "You read over the diagram."
    "It contains various forms of magic, with arrows and bubbles connecting various types together."
    brandon "You'd probably be interested in this area down here, in the corner. That's where you are."
    "In a section labeled 'Elemental,' you see fire, water, electric, ground, and psionic. A small description describes the attributes below."
    brandon "'Fire effectively cauterizes wounds on the target. Strong fire additionally can create a shield around the target, but this shield does not follow the target.'"
    lucas "Feels like I'm a lab rat, with what I can do being written down."
    brandon "You wouldn't be the only one. Sarah practically had a heart attack when I described what she can do."
    lucas "She seems harmless, though."
    brandon "Slight correction, ONE of her forms of magic is basically harmless."
    lucas "What do you mean by that?"
    brandon "That's not my place to say. If she's interested in telling you, that'd be her choice."
    lucas "That's not exactly reassuring."
    brandon "As long as you're not trying to hide something from her, you won't see it."
    lucas "See what?"
    brandon "Anyway, getting back to your topic, I've been studying magic for quite some time. Actually, I've been trying to figure out how magic works genetically."
    lucas "Do you have a going theory?"
    brandon "Not at the moment. I'd need more time to think about it. All we know for certain is that if one of your parents has magic, you'll have magic. That's been true in every case."
    lucas "Then what else are you looking for?"
    brandon "I want to understand the distribution. People with many forms of magic give birth to children with multiple forms, but that's the only connection I've seen."
    lucas "You should get Adrian in here, he'd love to hear these."
    brandon "Actually? You might be right about that. I might just run some theories by him sometime. Thanks, I...wouldn't have thought of that."
    lucas "As long as you get some sunlight sometime."
    brandon "He's already told me that a million times."
    lucas "I'll bring him up here."
    brandon "You don't need to do that, I'll get him myself."
    "Brandon heads for the door."
    brandon "And...thanks. I know I'm not the best person here, but...I had fun."
    show apathy_down at topleft
    "You enjoyed studying with Brandon."
    $ apathy -= 1
    hide apathy_down
    $ brandon3 = True
    $ last_person = "Brandon"
    return
#brandon is a stickler for grades
label brandon_deny:
    if not brandon1:
        "You head to the study."
        "You knock on the door."
        show brandon at truecenter
        brandon "What?"
        lucas "Do you want to do something?"
        brandon "No."
        "Brandon shuts the door."
        hide brandon
    else:
        show brandon at truecenter
        lucas "Do you want to do something, Brandon?"
        brandon "No thanks. You need to be studying more."
    "Brandon rejected your offer."
    show apathy_up at topleft
    "Shouldn't have bothered..."
    $ apathy += 1
    hide apathy_up
    $ brandon_check = True
    return
#london's first scene; london talks about naomi's outburst
label scene_london1:
    scene bg lobby
    with fade
    show lucas at midleft
    show london at midright
    "London puts down her book."
    london "You want to talk with me? {i}Really?{/i}"
    lucas "Gabriel told me to talk to everyone."
    london "This is {i}me{/i} we're talking about. 'Just a traumatized bitch,' as Brandon has said."
    lucas "You can talk about your trauma, if you need a subject."
    london "Why do you care? If you're just trying to get with me, there's no way in hell that's happening."
    lucas "I don't care for that."
    "London looks at you in disbelief."
    london "You're weird, you know that?"
    lucas "We deal with trauma in different ways."
    show london mad
    london "Oh, because you know {i}so{/i} much about trauma, do you? You and your country life on a nice peaceful farm, what kind of trauma could you possibly have? Some chicken wouldn't lay eggs?"
    lucas "My twin was attacked by a bear when we were young."
    show london
    london "Oh, oh shit, that's right, I'm sorry. Naomi told us about that."
    lucas "What about you?"
    london "I don't trust you like that."
    lucas "Do you trust Naomi?"
    london "Not really trust, more of an afraid of. Do {i}not{/i} get on her bad side, if you don't already know. She threatened to flay someone alive on our way to get smoothies."
    lucas "Naomi did?"
    london "She wasn't in a good mood, and that was probably your fault."
    lucas "Me?"
    london "You probably did something to piss her off."
    lucas "How would I have done that?"
    london "You probably did something she didn't like, or maybe..."
    "London thinks for a moment."
    london "Sorry."
    lucas "For what?"
    london "You asked to talk, and I've just been accusing you of things."
    lucas "It's fine."
    "London scowls at you."
    london "You're still weird, though."
    lucas "Alright."
    london "Hey, if there's a next time...we can do something."
    show apathy_down at topleft
    "Surprisingly, you enjoyed time with London."
    $ apathy -= 1
    hide apathy_down
    $ london1 = True
    $ last_person = "London"
    return
#london's second scene; london talks about her trauma
label scene_london2:
    scene bg smoothie shop
    with fade
    show lucas at midleft
    show london at midright
    "You're at a smoothie shop with London."
    london "Can I ask you something?"
    lucas "Sure."
    london "What the hell is wrong with you?"
    lucas "What do you mean?"
    london "Nevermind. I don't know how you could even answer that."
    lucas "Did you want to come here just to ask what's wrong with me?"
    london "No...well maybe. Sorry."
    lucas "It's fine."
    "London squints at you."
    london "I don't get you. You're just...different. I haven't met anyone as weird as you."
    lucas "Is that a compliment?"
    london "Take it as you will."
    "Your order is done, and you grab your smoothies."
    london "I guess I somewhat trust you."
    lucas "Where's this from?"
    london "Last time I said I didn't trust you. You asked about me and I shot you down."
    lucas "You were still thinking about that?"
    london "I'm not exactly the most friendly person around, as you can no doubt tell. If you still want to know what I went through, I'm open to it."
    lucas "Go for it."
    london "I used to be so cheery, until these selfish brats opened my eyes. They thought the curse for Sarah was mine, and they treated me like an outcast. They ruined me."
    lucas "You're going to have to backpedal a bit."
    london "Oh, right. You weren't there. Sorry."
    london "No doubt Gabriel has told you about Miss Fortune, right? She gave us the curses. They were purposely worded to tear us apart, I'm sure of it."
    london "To preface, I have multiple forms of magic, courtesy of my mom. She was...kind of like a test subject for the war. She was given a lot of shit, and it's spread between me and my siblings."
    london "One of them is like an aura, literally for death. If someone's about to die, I can tell. It can be stopped, and that's what I loved to do."
    london "Sarah's curse was 'the one who sees death will bring one to death' or something like that. They thought it was me. They all shunned me."
    london "They treated me like dirt, just because they thought it was me! They were so afraid, they disarmed me and gave me the furthest bed. They weren't afraid to hide it from me."
    london "In the end, Sarah saw death. She literally saw the memories of someone who had died, and apparently the 'process' was mortifying for her. She barred herself away and killed one of the girls. Her sister, even."
    london "Their apologies were meaningless. I saw how they treated me. At least Gabriel came to talk to me, when none of them wanted to be near me. I appreciate him."
    lucas "Damn. Sounds rough."
    show london mad
    london "I open my trauma to you, and that's all you have to say?!"
    lucas "What am I supposed to say?"
    london "I-I don't know. I don't know, ok?! You happy?!"
    lucas "Calm down, we're on the same side. I'm sorry you went through that. I can't imagine what you went through."
    show london
    london "Yeah, you couldn't."
    "You continue to drink smoothies."
    lucas "You have multiple forms of magic?"
    london "Oh yeah, plenty."
    lucas "Are you going to elaborate?"
    london "No, I've talked enough. next time, though. It was...good to get that off my chest, though. Thanks."
    show apathy_down at topleft
    "You enjoyed smoothies with London."
    $ apathy -= 1
    hide apathy_down
    $ london2 = True
    $ last_person = "London"
    return
#london's third scene; london talks about happiness
label scene_london3:
    scene bg lobby
    with fade
    show lucas at midleft
    show london at midright
    london "Why are you talking to me?"
    lucas "Why...not?"
    "London stares blankly at you."
    london "I don't get you. You don't care about anything yet you find time with us."
    lucas "I have time."
    london "That's what I just said, you walnut."
    "London looks at the floor."
    london "How the hell are you and Naomi friends?"
    lucas "We've been friends since we were kids."
    london "And you were always like this?"
    lucas "No, I...when my brother died, that's when-"
    london "Oh, yikes. Yeah. I gotcha."
    "London sits in silence for a bit."
    london "I'm...kind of the same. My sisters all have their perfect boyfriends, and my ex just hated me the second he found out I had magic. I saved his damn life, and that's how he repaid me?"
    lucas "I'm sure he had his reasons."
    london "Why do my siblings get to be happy and not me? Don't I deserve to be happy?"
    lucas "If you work for it."
    london "No, we should all get to be happy. What are you even saying?"
    lucas "Happiness doesn't just fall into your lap, you have to be a good person and actively work towards it."
    london "Oh, as if you're just a ray of smiles and sunshine. Why the hell would I trust you with that? You don't care about anything!"
    lucas "I don't care for it."
    london "I bet you will."
    lucas "Why do you say that?"
    london "I mean, you were willing to sit through me complaining about everything. If you're not just making plans to talk to me, I bet these idiots will make you happy."
    lucas "I wouldn't know about that."
    london "You're sitting here, talking with the bitchiest person in this house, and you're not getting impatient or annoyed at anything I do or say. I don't get you."
    lucas "I mostly listen."
    london "Yeah, well, you can listen when I say that you care more than you realize. At least, I think so. You don't just set aside time for anyone, you have to admit-"
    "Gabriel walks into the lobby."
    show gabriel serious at truecenter
    gabriel "Hey, can I ask you something real quick?"
    london "Me?"
    gabriel "If you have time."
    london "Uh, alright."
    hide gabriel
    hide london
    "The two of them go into another room."
    "After some time, London comes back."
    show london at midright
    london "Well...that was...something."
    lucas "What happened?"
    london "He just up and asked me out."
    lucas "And what did you say?"
    if gabriel3:
        $ dating = True
        london "Well, I...I guess I'm not single anymore."
        lucas "Congrats."
        london "What, that's it?"
        lucas "Was I supposed to say something else?"
        london "That sounded half-assed, you jerk."
        lucas "I mean, there's nothing else I could really say. Congrats."
        london "You...are a very strange man. But hey, thanks for giving me a chance. I'm going to see if Gabriel wants to do something."
    else:
        london "He fumbled the bag. Really bad."
        lucas "He was probably just nervous."
        london "Well, he can try again if he fixes his attitude."
        lucas "He's not going to try again."
        london "Then that's his loss."
        lucas "Didn't you say you were the bitchiest person in this house?"
        london "Alright, alright, we're done here. But hey...thanks for giving me a chance."
    show apathy_down at topleft
    "You enjoyed talking with London."
    $ apathy -= 1
    hide apathy_down
    $ london3 = True
    $ last_person = "London"
    return
#london rejects for higher grades
label london_deny:
    lucas "Are you up for a chat, London?"
    london "Don't be ridiculous."
    "London didn't even look at you."
    show apathy_up at topleft
    "It's not worth it..."
    $ apathy += 1
    hide apathy_up
    $ london_check = True
    return
#sarah's first scene; sarah talks about killing her younger sister
label scene_sarah1:
    scene bg city
    with fade
    show lucas at midleft
    show sarah at midright
    "You're going for a walk with Sarah."
    sarah "Naomi told us about your twin...I'm so sorry."
    lucas "It's fine."
    sarah "I lost a sibling, too. My younger sister, Natalie. I...I feel terrible."
    lucas "Death is a part of life."
    show sarah sad
    sarah "No I know, but...I..."
    "Sarah appears to be trembling."
    sarah "I..."
    "Sarah lowers her head and speaks very softly."
    sarah "...I...I killed her."
    lucas "Sorry to hear."
    sarah "You don't have to apologize...it was my stupid curse thing. I hate what they made us do to each other."
    "Sarah starts to raise her voice."
    sarah "I hate that we did it, I hate that we joined that stupid group, I hate when they're arguing, I hate when they can't be happy together, I hate that we're in this mess!"
    "Sarah suddenly stops talking."
    sarah "I'm sorry. We should be enjoying a walk. I'm sorry."
    lucas "Stop apologizing so much."
    sarah "Sorry. Oh-whoops."
    show sarah
    "Sarah laughs quietly."
    sarah "Can you tell I'm nervous?"
    lucas "Why are you nervous?"
    sarah "After...Natalie...I didn't have a lot of friendships with the rest of them. Having someone to talk to, who wasn't there when I did what I did is...different."
    lucas "I had a similar feeling when I came to the city. No one gave me false pity here."
    sarah "Yeah, it's weird, right? No one here knows what I did. I'm just an average girl here. I almost don't like it."
    lucas "Used to having to face consequences?"
    sarah "I know...I was just so scared...I was scared of death, pushed everyone away, sat in my room with a gun aimed at the door...just...terrified."
    sarah "I didn't even notice I'd pulled the trigger. Natalie...she just stood there, in shock..."
    lucas "It's alright. I'm sorry you went through that."
    sarah "Now you're apologizing!"
    lucas "I suppose I am."
    "Sarah laughs quietly, and you two continue walking."
    sarah "What was your brother like?"
    lucas "He was the loud one of us. He would get Naomi to join us, and we'd use magic around the forest nearby, or work on the barn, or just enjoy each other's company."
    sarah "It sounds like you miss him."
    lucas "Yeah. I guess I do."
    sarah "We're pretty unlucky, don't you think?"
    "Sarah laughs."
    lucas "It's just part of life."
    sarah "I wish it wasn't. I wish we always had the good parts and never the bad parts."
    if adrian2:
        show apathy_down at topleft
        lucas "'If everything was always good, nothing would be good, because you'd have nothing bad to compare it with.'"
        $ apathy -= 1
        hide apathy_down
        sarah "That...I guess that's true! Where did you hear that?"
        lucas "Adrian said it."
        sarah "Wow, I'm impressed with him! He really said that?"
        lucas "I know, he's crazy."
        sarah "No, I think that sounded cool! I didn't know he spent that much time thinking about life..."
    else:
        lucas "Life won't work that way."
        sarah "It's just wishful thinking."
    show apathy_down at topleft
    "You enjoyed a walk with Sarah."
    $ apathy -= 1
    hide apathy_down
    $ sarah1 = True
    $ last_person = "Sarah"
    return
#sarah's second scene; bowling with sarah, sarah doesn't understand fun without competitiveness
label scene_sarah2:
    scene bg bowling
    with fade
    show lucas at top
    show sarah at midright
    "You're bowling with Sarah."
    show lucas at midleft with moveinright
    sarah "You're pretty good at this!"
    lucas "I've had a lot of practice."
    sarah "I wish I had more...I'm not good at a lot of things."
    lucas "I'd say you're doing fine."
    sarah "I'd like to do better, though...you've already doubled my score."
    show apathy_down at topleft
    lucas "Don't worry about the score, just have fun with it."
    $ apathy -= 1
    hide apathy_down
    sarah "I can't compete with you, though...it can't be fun for you."
    lucas "I don't need to be winning or losing to enjoy time outside the house."
    sarah "Yeah...that's a good point."
    show sarah at top with moveinright
    "Sarah curves her ball into the gutter."
    "Sarah grabs her ball and hits a few pins on her next roll."
    show sarah at midright with moveinleft
    sarah "I always start with curving left...how do you avoid that?"
    lucas "It's just a feeling, really. It'll grow on you."
    "Sarah frowns at you."
    lucas "...what?"
    sarah "That doesn't help me."
    lucas "Well, I can't give you the feeling. I don't know how else I'd explain it."
    "Sarah looks at her hands, and looks back to you."
    sarah "Can I...can you give me your hand?"
    lucas "Sure."
    "Sarah starts rubbing her thumb on your palm."
    lucas "What are you-"
    "You feel something in your head!"
    "Something is caressing your skull!"
    lucas "What...are you doing?"
    sarah "Looking at your memory. Feels weird, right? Like a hand is rubbing around your brain..."
    lucas "Why are you...doing...that?"
    sarah "Stop resisting it, I'm just looking for how you bowl. It won't stop until I stop it."
    "The feeling is indescribable."
    "Sarah lets go of your hand."
    lucas "What...was that?"
    sarah "I can look at your memories! Isn't that cool?"
    "Sarah giggles to herself."
    lucas "You could've told me."
    sarah "I like to surprise people with the feeling."
    lucas "That's...not reassuring."
    sarah "Let me take your turn, I want to try what you do!"
    show sarah at top with moveinright
    "Sarah grabs her ball and bowls."
    "It curves into the gutter."
    show sarah at midright with moveinleft
    sarah "It didn't work!"
    lucas "Maybe it's muscle memory."
    sarah "Oh...maybe."
    lucas "You could've just enjoyed the game instead of...whatever that was."
    sarah "But what about being competitive?"
    lucas "We're just having fun, there's no need to be competitive unless we want to be. Just try to have fun."
    sarah "Oh...ok. Yeah."
    lucas "And don't do whatever that was again."
    sarah "Right. Sorry."
    "Sarah laughs quietly."
    lucas "At least you're having fun. You were miserable last time."
    sarah "Yeah...sorry. I just wanted to relate to you, and I went on a tangent...sorry."
    lucas "It's alright. Just try to have fun."
    sarah "Yeah!"
    show apathy_down at topleft
    "You enjoyed bowling with Sarah."
    $ apathy -= 1
    hide apathy_down
    $ sarah2 = True
    $ last_person = "Sarah"
    return
#sarah's third scene; sarah feels better about life
label scene_sarah3:
    scene bg amusement park
    with fade
    show lucas at midleft
    show sarah at midright
    "You're at an amusement park with Sarah."
    sarah "And then she says something like, 'If you put a finger on her, I'll flay you alive!'"
    lucas "Naomi said that?"
    sarah "It caught us off guard, but the immediate fear he had on his face was priceless!"
    "Sarah laughs to herself."
    sarah "It was also reassuring...London was always trying to keep me safe until...we treated her terribly..."
    lucas "Is that why-"
    sarah "She's a stuck up bitch? Yeah...it's all our fault...even though Gabriel and I didn't treat her as badly, she still holds onto those times..."
    lucas "What exactly happened?"
    sarah "After this ride, I'll tell you."
    scene bg black
    with fade
    "Sarah practically screams her lungs out with enjoyment."
    scene bg amusement park
    with fade
    show lucas at midleft
    show sarah at midright
    sarah "I don't think I've screamed so loud in my life!"
    lucas "That was quite loud."
    sarah "That was so much fun! We should do that again at the end!"
    lucas "Alright."
    sarah "...what were we talking about before the ride?"
    lucas "Something about London?"
    sarah "Oh, right...London had one of those curses from Miss Fortune...except, not the one we thought she had. That was mine actually. Something like 'the one who sees death will kill a sister.'"
    lucas "You thought London could see death?"
    sarah "That was one of her magics, she could see when someone was about to die and stop it...and we thought she'd killer her sister, so..."
    lucas "How'd you end up seeing death?"
    sarah "So...London's mom had a friend from the war, who...turned out to be part of the afterlife process. She had possessed a dead child, and lived their life for them. I think she pitied her."
    lucas "And you...looked at her memories?"
    sarah "It was stupid, it was so stupid! She wanted to find a friend she had become obsessed with, and asked me to look back and find him...but...I saw what happens to us when we die..."
    lucas "What happens?"
    sarah "I only saw part of it, but they look at-no. I'm sorry. I shouldn't say."
    "Sarah jolts away from you."
    sarah "It traumatized me, I was deeply scared of death, and...I ended up killing my sister. Instead of London killing her sister."
    lucas "I'm sorry."
    sarah "Sorry...I-I'm trying to do better. I promise I am! Leaving the house is good, so...thanks for bringing me here."
    lucas "Uh, sure-"
    sarah "Ooh! That line over there is pretty short, let's go!"
    "Sarah drags you around the amusement park until dark."
    show apathy_down at topleft
    "You enjoyed the amusement park with Sarah."
    $ apathy -= 1
    hide apathy_down
    $ sarah3 = True
    $ last_person = "Sarah"
    return
#sarah denies if your grades are super low
label sarah_deny:
    lucas "Hi Sarah, do you want to do something today?"
    sarah "Oh, sorry! I have some plans..."
    "Sarah looks away, shyly."
    show apathy_up at topleft
    "Just never worth it..."
    $ apathy += 1
    hide apathy_up
    $ sarah_check = True
    return
#after each scene with characters are done, default scene decreases apathy
label max(characterName):
    scene black
    with fade
    "You're spending time with [characterName]."
    "..."
    show apathy_down at topleft
    "Nothing particularly exciting happens, but you still enjoyed it."
    $ apathy -= 2
    hide apathy_down
    $ last_person = characterName
    return
#choose to study; increase lucas' grade at the cost of increasing his apathy, unless brandon has taught lucas about studying for a purpose
label study:
    "You decide to study."
    scene black
    with fade
    "..."
    "..."
    "..."
    if tempGrade < 4:
        "You feel as though you'll do better on the next exams."
        $ tempGrade += 1
    else:
        "You already feel very confident for the next exams."
    if brandon2:
        show apathy_down at topleft
        "You've studied for your future. A future worth living."
        $ apathy -= 1
        hide apathy_down
    else:
        show apathy_up at topleft
        "Just studying to make your father happy..."
        $ apathy += 1
        hide apathy_up
    $ last_person = "Study"
    return
#set all checks to false; makes the player unable to farm apathy
label set_false:
    $ naomi_check = False
    $ gabriel_check = False
    $ carson_check = False
    $ adrian_check = False
    $ brandon_check = False
    $ london_check = False
    $ sarah_check = False
    return