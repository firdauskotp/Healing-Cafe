label prologue:
    $ healing_points = 0
    $ set_scene("entrance")
    $ play_music(mattari)
    $ enter_from_right("kh") 
    
    f "Hello, the name is Fird. Welcome to Healing Cafe, where every cup is brewed with a dash of kindness."
    f "At least, that is what I hope, haha"
    f "I love coffee and thought, why not open my own shop?"
    f "But more than that, I want this place to be a haven for people who need a little pick-me-up, whether it's from a tough day or just life in general."
    f "And sometimes, I have customers, who I feel, need more than just a cup of coffee."
    f "Today is one of those days, and some of them are regular customers"
    f "But enough of introductions, let's get to work!"
    f "Er quick disclaimer: Names and events are fictional, any resemblance to real persons, living or dead, is purely coincidental."
    f "There are also two endings to this story, depending on how much healing I can provide to my customers today"
    f "Now for real, let's get started!"
    jump customer1


label customer1:
    
    $ set_scene("counter")
    "Morning Shift"
    $ play_music(teagarden)
    $ enter_from_right("kh") 
    "The bell rings. A tired student walks in, dark circles under their eyes."
    f "Come in! What can I get for you today? (Ah, it's him. A student from my old university. My junior, to say the least)"

    c "One espresso, please. Make it strong."
    $ show_center("ku","kh")
    f "You look like you’ve been up all night."

    menu:
        "What do you serve?"
        "Espresso (encourage work)":
            jump espresso_path
        "Chamomile tea (suggest rest)":
            jump chamomile_path

label espresso_path:
    $ show_center("kn","ku")
    f "Espresso coming right up. But you look like you could use a break. What's keeping you up at night?"
    c "The usual... deadlines wait for no one."
    "You hand over the espresso. Their hands tremble slightly as they take it."
    c "Thanks... I’ll just push through tonight."
    $ show_center("ksmile","kn")
    f "Don’t forget, coffee helps you work, but it won’t help you heal. You need to save yourself from burn out"
    c "Heh... maybe next time I’ll try that tea."
    $ healing_points = 0

    jump customer2

label chamomile_path:
    # f "How about a cup of chamomile instead?"
    # c "But I’ll fall asleep..."
    # $ show_center("ksmile","ku")
    # f "Maybe that’s exactly what you need.:"
    # f "I was a student, and I am still a part time student now"
    # f "I know how it feels to be overwhelmed. Sometimes, the best thing you can do is step back and rest."
    # f "Otherwise, you will get burn out. Tell me, what are you majoring in? What is this assignment about?"
    # c "Computer engineering"
    # f "That's my course, I know how it feels."
    # c "Database is difficult"
    # f "Do you enjoy it?"
    # c "I do."
    # f "Then take care of yourself, alright? Success is meaningless without health."
    # f "If you get burnt out, you won’t be able to enjoy what you love. You will find it a chore instead"
    # f "And you will begin to hate it."
    # f "Manage your time better next time, okay? Rest is important. Remember your health is of utmost importance"
    # "They stare at the steaming mug for a while, then smile faintly."
    # c "...Yeah. Maybe rest is overdue."
    f "How about a cup of chamomile instead?"
    c "But I’ll fall asleep before I finish the report."
    $ show_center("ksmile","ku")
    f "Maybe that’s exactly what you need."
    "You pour the tea slowly, the gentle scent of flowers drifting through the room."
    f "I was like you once. I’m still studying part-time, actually. I am also teaching coding on the side. So believe me, I know the spiral."
    c "Teaching and studying? That’s rough."
    f "It can be. There were nights I stared at the screen for hours, debugging the same error, thinking I was useless."
    c "I get that. Databases are frying my brain at this point."
    f "Ah, databases. My old nemesis. Funny thing,I used to tell my students that a good database needs rest too. You can’t overload it; it crashes. Same with us."
    c "Never thought of it that way."
    f "Tell me, do you still enjoy what you’re studying?"
    c "I do. I love building things, but lately it just feels like pressure, not passion."
    $ show_center("ku","ksmile")

    f "That’s burnout talking. It tricks you into thinking you hate what you love. Step away for a while and the spark usually finds its way back."
    c "But if I rest, I’ll fall behind."
    f "If you don’t rest, you’ll fall apart. There’s a difference."
    "He looks down at the steaming cup. The light reflects softly in his tired eyes."
    f "Health first. Success means nothing if you collapse halfway through."
    c "You really sound like a lecturer now."
    $ show_center("kh","ksmile")

    f "Maybe. But I learnt it the hard way. I started this café after one of my students fainted during an exam week. It reminded me how fragile we all are."
    "He nods quietly, clutching the mug as if holding on to warmth itself."
    c "...Yeah. Maybe rest is overdue."
    f "Good. The world will wait a night for your best work."
    "The student smiled and left to sit outside drinking, he looks a bit more relaxed now."
    $ healing_points = 1
    jump customer2

label customer2:
    "The bell above the door rings softly. An elderly man steps inside, his eyes resting on the empty chair by the window."
    f "Good afternoon. What can I get for you today?"
    c "Black coffee, please. No sugar."
    $ show_center("kn","ksmile")

    f "Sure thing. Still her usual order, huh?"

    menu:
        "What do you serve?"
        "Black coffee (reminisce)":
            jump blackcoffee_path
        "Hot chocolate (invite sharing)":
            jump hotchoco_path

label blackcoffee_path:
    $ show_center("ksmile", "kn")
    f "Coming right up."
    "Fird grind the beans in silence; the earthy aroma fills the air."
    c "She always loved that smell... I still come here just to remember."
    f "It’s a nice way to keep her close."
    c "Maybe. But memories don’t talk back, do they?"
    f "No... but they listen. Sometimes that’s enough for the heart to speak."
    c "Hah. You sound like her. She used to say things like that."
    $ show_center("kh", "kn")

    f "Maybe she taught us both something about kindness."
    "He stares at the cup, steam curling like ghosts of the past."
    c "Thank you, lad. It still feels lonely, but... a bit less so tonight."
    f "How about something sweet next time?"
    c "Sounds like a good idea. I'll be heading off for now."
    f "Thank you and take care!"
    $ healing_points += 0
    jump customer3

label hotchoco_path:
    f "You know, perhaps today calls for something sweeter. How about a hot chocolate?"
    c "She’d have loved that. She had the sweetest tooth you could imagine."
    $ show_center("kh","kn")
    f "Tell me about her—if you don’t mind."
    "He chuckles softly, the lines on his face easing as he talks."
    c "We met during the war, you know. She used to knit scarves for the neighbours. Always said love’s warmer when it’s shared."
    f "Sounds like she brought warmth wherever she went."
    c "Aye. And I’ve been trying to keep a little of it alive."
    $ show_center("ksmile","kh")
    f "You have. Every time you come in, she’s here with you—in stories, in smell, in the sound of your cup."
    "He sits quietly for a moment, then smiles."
    c "Thank you. It’s been years since anyone asked me about her. This... this helped."
    f "She’d be happy you remember her with warmth, not sorrow."
    "He takes a long sip, eyes glistening but peaceful."
    c "That... really helps. Thank you. I will be taking my leave now."
    f "No worries, it is my pleasure to help. Take care of yourself!"
    c "Will do, lad. Will do."
    $ show_center("kn","ksmile")
    f "(Hmm, take care of yourself, eh)"
    $ show_center("ksmile","kn")
    f "No, why I am overthinking now? Ahahaha"
    $ healing_points += 1
    jump customer3

label customer3:
    "Evening has draped itself across the café. Outside, the rain has slowed to a whisper against the window."
    "A young artist sits by the counter, sketchbook open but untouched. The pencil rests like a burden between their fingers."
    $ show_center("kn","ksmile")
    f "Evening. You look as if you’ve been staring at that page for a while now. Seems like you're lost"
    c "In thoughts, all alone?"
    $ show_center("kh","kn")
    f "I love it when someone catched my reference! Ahaha"
    c "Ahahaha."
    c "About your earlier question. I do feel lost. Feels like the more I look at it, the less I know what to draw."
    $ show_center("kn","kh")
    f "Creative block?"
    c "Something like that. Coffee, anything. Maybe it’ll make me draw again."
    f "Let’s see what we can brew for that."

    menu:
        "What do you serve?"
        "Matcha (try something new)":
            jump matcha_path
        "Latte (comfort and warmth)":
            jump latte_path

label matcha_path:
    f "Want to try matcha? It’s a little bitter at first, but it has a way of clearing the fog."
    c "Matcha? Looks... greener than I expected."
    "Fird whisk the powder carefully; a thin froth forms, bright against the porcelain cup."
    $ show_center("ksmile","kn")
    f "A new taste can stir old feelings. Sometimes you need a different flavour to find your rhythm again."
    c "My tutor used to say the same — that stagnation kills art faster than failure."
    f "He was wise. I teach coding part-time, and I tell my students the same thing: never be afraid to break something. It’s the only way to understand it."
    c "You’re a teacher?"
    $ show_center("kh","ksmile")

    f "Yeah, a coding teacher. Python mostly. I run a few evening classes after closing time here."
    c "Teaching and coffee? That’s an interesting mix."
    f "Both require patience and timing, and both smell better when they’re warm."
    "The artist chuckles, the first hint of ease all evening."
    c "I don’t know a thing about coding. Must be all numbers and logic, right?"
    f "That’s what most people think. But code is just structured creativity. When I write Python, I’m painting with logic, indentation instead of brushstrokes."
    c "That’s... surprisingly poetic."
    f "I tell my students that a bug isn’t failure, it’s feedback. It means the programme’s trying to talk back to you, just like art when it doesn’t feel right."
    "They nod slowly, intrigued."
    c "So when your code fails, you don’t get angry?"
    $ show_center("ksmile","kh")
    f "Sometimes I do," 
    f "but then I remind myself it’s only showing me where to look next. I think that’s what you’re facing right now. Your art’s talking back."
    "The artist stares into the cup, watching the foam settle."
    c "You might be right. I’ve been stuck since my tutor passed. Everything I draw feels hollow."
    f "Grief makes silence heavy. But even in code, silence has meaning — an empty line still shapes the structure."
    c "I never thought of it like that."
    f "You don’t have to rush the next masterpiece. Just draw something small, even a bug, a leaf, a line. Remember to start with version one, and let version two come later."
    c "‘Version two.’ I like that."
    "They lift the cup and smile faintly after a sip."
    c "Bitter... but clean. Like a restart."
    f "Exactly. Every restart writes a new line."
    $ show_center("kh","ksmile")

    c "Thank you. I think I’ll try again — maybe sketch this place tomorrow."
    f "I’ll keep your seat ready."
    $ healing_points += 1
    jump ending


# -----------------------------------
# LATTE PATH — “Gentle Comfort”
# -----------------------------------
label latte_path:
    $ show_center("ksmile","kn")
    f "How about a latte? Smooth, comforting, easy on the heart."
    "You pour the milk slowly, swirling it into a simple heart pattern."
    c "Nice art. Maybe I should learn that, it’s neater than my sketches lately."
    f "Heh. Took years of practise. I’ve spilt enough milk to learn patience beats perfection."
    c "Sounds like experience talking."
    f "I suppose so. I teach coding part-time. Mostly Python. Happen with myself in both coding and teaching. And to my students too."
    c "A teacher? Bet that’s rewarding."
    $ show_center("kh","ksmile")

    f "It is, though it tests your patience. Students forget colons, mix up loops, panic over little bugs. I always remind them that every mistake’s just progress with attitude."
    c "Ha! I could use that mindset. Every sketch I make lately feels wrong."
    f "Then maybe it’s time to look at it like debugging, not deleting. Just understanding why it behaves differently."
    c "You think art can be debugged?"
    f "In a way. The process is the same: observe, adjust, run again. Creation isn’t about avoiding errors, it’s about learning from them."
    c "That’s… actually comforting. I keep restarting drawings, hoping the next one’s perfect."
    f "You sound like my students. I always tell them, ‘perfection kills progress’. You can’t build something if you never run it."
    c "True. Maybe I’ve been stuck chasing the perfect line."
    $ show_center("ksmile","kh")
    f "Sometimes you need to leave a note to your future self. I leave comments in my code: ‘# remember to rest’. Helps me not forget that humans need recharging too."
    $ show_center("kh","ksmile")
    "They laugh softly, the tension in their shoulders easing."
    c "Maybe I’ll start leaving notes to myself like that. ‘# breathe’, ‘# take a walk’. Might help."
    f "See? You’re already rewriting your script."
    "They sip their latte, the warmth softening their eyes."
    c "I think I’ll stay for a while. Maybe sketch the counter before you close."
    f "As long as you promise not to draw my messy apron."
    c "No promises."
    "They both laugh quietly — a shared moment of calm between teacher and artist."
    $ healing_points += 1
    jump ending


# -------------------------------
# ENDING: The Barista & Friend
# -------------------------------
label ending:
    $ set_scene("night_cafe")
    $ play_music(mattari)
    $ show_left("kn","kh")

    "Fird wanted to turn the sign to 'Closed.' A friend drops by, waving through the window."
    $ enter_from_right("ah", at_transform=right_side)

    a "Long day?"
    $ show_left("kh","kn")
    f "Eh Mad! Didn't expect to see you here this late."
    a "Gotta drop by. I heard you made the best coffee in town now!"
    f "Hah, flattery won't get you a free cup my friend."
    f "Long day. Everyone seems to need healing lately."
    $ show_right("an","ah")
    a "And you? Did you save some of that kindness for yourself?"

    menu:
        "How do you respond?"
        "Admit you’re tired":
            jump open_end
        "Brush it off":
            jump quiet_end

label open_end:
    
    $ show_left("kn", "kh")
    f "Honestly... I’m exhausted. Helping people makes me forget my own mess. You remember, right?"
    $ show_right("an", "ah")
    a "I've been your friend for over 10 years"
    a "Of course I know"
    $ show_right("ah", "an")
    a "I know"
    a "Then let me buy you a drink for once."
    $ show_left("kh", "kn")
    f "Ha, you’ll ruin my business model."
    a "Maybe healing’s not about running a café. Maybe it’s about sharing the table."
    "They both sit, two cups between you. For the first time today, the silence feels peaceful."

    
    
    
    if healing_points >= 3:
        $ set_scene("present")

        $ play_music(insecurity)

        a "Fird... you told everyone to rest today. But you never said why this place matters to you."
        f "Because once, I was exactly like them."
        f "Work chewing me up. Studies on my neck. Personal issues. I kept smiling like nothing was wrong."
        a "Yet that smile was obviously fake for us. But you kept on denying to meet us."
        f "I stopped showing up for people. Even for myself."
        a "I remember calling you. You’d let it ring out."
        a "Not only me, but many of us. Remember how even one of our friends had to call your mum to make sure you were okay?"
        f "I didn’t have the energy to answer. Not even to say 'help'."
        a "You stopped appearing in classes as well."
        f "I kinda did, didn't I? But hey, I still scored a 3.7 GPA that semester!"
        a "Heh, sure did, but you didn't beat me still"
        f "Beating you is hard, especially in programming, my rival!"
        a "Heh."
        a "Anyways, I still couldn't believe how those incidents happen in a short amount of time"
        f "Life is funny right? But then I realised the saying 'God will not burden you beyond that it can bear' means"
        f "Took some time to realise it, it is all thanks to you and the rest of the gang!"
        a "Heh, that same year, I had troubles as well. What a weird year. Who helped me that time? It was you!"
        f "Two broken friends helping each other out that time, eh! Hahaha"
        a "Yeahh! Anyways, I got too impatient to help you that time. You were a shell of your former self"
        f "Surprisingly I became worse than you that time."
        a "Indeed! Then, I force you to meet me at our favourite cafe."
        f "Yeah. You dragged me out even though I said I was 'injured'."
        a "Desperate times call for desperate measures"
        jump good_end
    else:
        $ set_scene("entrance_night")
        $ play_music(mattari)
        jump neutral_end

label quiet_end:
    $ show_left("kn", "kh")

    f "I’m fine. Just tired, that’s all."
    $ show_right("an", "ah")

    a "Sure... But even coffee goes cold if you leave it alone too long."
    f "Heh, I get what you mean. Another time?"
    a "Sure, buddy"
    
    jump neutral_end

label good_end:

    $ set_scene("flashback")
    $ play_music(memories)
    pa "You said you were injured, but I knew that was just your heart talking."
    pf "Heh. Guess you were right."
    pa "You hadn’t eaten all day. You looked like a zombie when I picked you up."
    pf "That was my 'grindset' era. I thought if I kept working, the pain would disappear."
    pa "Instead, you disappeared."
    pf "Yeah... I guess I did."
    pa "You know, it scared me. Watching someone so full of life fade like that."
    pf "I didn’t mean to push anyone away."
    pa "We knew. We just didn’t know how to reach you."
    pf "You did, though. You showed up."
    pa "Because you did the same for me once."
    pf "Huh?"
    pa "Remember my internship mess? When I thought I ruined everything?"
    pf "Ah... you mean when your code deleted half the client’s data?"
    pa "HEY— it was a test server!"
    pf "Hahaha! Still the funniest meltdown I’ve ever seen."
    pa "You stayed up all night helping me fix it. Never complained once."
    pf "I remember. You looked like you were gonna quit."
    pa "I almost did. But you remembered what you told me?"
    pf "Eh?"
    pa "Failuer is a step to success, and mistakes are what make you a better version of yourself."
    pf "Can’t believe you still remember that cringey statement."
    pa "I do. You told me, 'As long as you keep learning, you’re winning.' I needed that. So when you fell apart... I just returned the favour."
    pa "Also, it is not cringy, it is the truth. A truth not many are ready to accept."
    pf "You know, Mad… it wasn’t just work that broke me."
    pa "I know. Marie."
    pf "Yeah. She said she couldn’t recognise me anymore. Maybe I couldn’t either."
    pf "I tried so hard to be with her as I promised but..."
    pa "You kept chasing the next goal to forget the last goodbye."
    pf "Exactly. And every time I hit a milestone, it felt emptier. Like I was collecting trophies for a life I wasn’t living."
    pa "You thought love made you weak."
    pf "And I learned the hard way that it doesn’t, neglect does."
    pa "She doesn't understand you as much, but she has a point too"
    pa "You know I don't agree with her on a lot of things, but she made you happy, and... she is correct in this instance"
    pa "But what else can you do except acknowledge your mistake and grow stronger now."
    pf "You know..."
    pf "I felt useless. I didn’t want to talk, didn’t want to wake up, didn’t want to feel. But then… you called."
    pa "You mean when I spammed you with voice notes until your phone crashed?"
    pf "Yeah. That."
    pa "Desperate times call for desperate measures."
    pf "Ahahah yeah"
    pa "That's the Fird I know!"
    pf "That's the Mad I know too!"
    pa "You think you were the only one hurting? I was falling apart too. So I can give some advice"
    pf "You?"
    pa "Yeah. After Nadia left. Remember her?"
    pf "Of course. You used to write her poems in Python comments."
    pa "Don’t remind me!"
    pf "Hahaha, 'def love_you_forever():' that was legendary!"
    pa "You still remember that?! That was last year!"
    pf "Hard to forget. You looked like you’d been hit by an exception error for weeks."
    pa "I was. I thought she was the one. And when she walked away, I lost my anchor."
    pf "You kept smiling though."
    pa "So did you."
    pf "Touché."
    pf "She meant a lot to you, I know. But I know she hurt you a lot too."
    pa "Same as Marie to you."
    pf "Touché. Yet again"
    pf "I remember having to bring you to the arcade to make you calm"
    pf "You were always number one but you just faded off, I was worried back then"
    pa "Heh, thanks. I tried my best for her"
    pf "I know, I thought the problems you two were facing were solved?"
    pa "Momentarily. It was my fault as well, she said she wanted to break up but I just kept hanging"
    pf "When was this?"
    pa "About 5 months ago"
    pf "HUH?! During that time when you were saying everything was being fixed?"
    pa "In my defense, it was being fixed. But I can't do my part to move on"
    pa "Remember the last time we hang out and I was hurt by her? When I came to your dorm because the rest of your roommates went for hiking?"
    pf "I remember, I kinda hated her since then."
    pa "Hahahah, I know. Anyways..."
    pa "You’re the one who told me, 'Some people aren’t meant to stay, they’re meant to teach us how to love better next time.'"
    pf "I said that?"
    pa "Yeah. You said it while pouring me instant coffee at 3 a.m. in your dorm kitchen. I never forgot it."
    pf "And now you’re using my own wisdom against me, huh?"
    pa "That’s what friends are for."

    f "I think that day was the first time I really breathed. Like everything heavy finally had permission to exist."
    a "You didn’t have to be fixed, Fird. You just needed to be found again."
    f "And you found me."
    a "We found each other. Two broken guys trying to patch up their code and hearts at the same time."
    f "I realised something that night. Coffee doesn’t heal pain. But it gives you time to face it."
    a "And that time became Healing Cafe."
    f "Yeah. A place for tired people to pause. To remember that life still tastes warm if you let it."


    $ set_scene("present")
    $ play_music(lovefromafar)
    f "I think that day was the first time I really breathed. Like everything heavy finally had permission to exist."
    a "You didn’t have to be fixed, Fird. You just needed to be found again."
    f "And you found me."
    a "We found each other. Two broken guys trying to patch up their code and hearts at the same time."
    f "I realised something that night. Coffee doesn’t heal pain. But it gives you time to face it."
    a "And that time became Healing Cafe."
    f "Yeah. A place for tired people to pause. To remember that life still tastes warm if you let it."

    f "I forgot how raw our hangouts are."
    a "We were just teenagers pretending to be invincible."
    f "And yet… that tiny café became the blueprint for this one."
    a "Healing Cafe."
    f "Funny, huh? You were the one who dragged me to that table, but now this table drags people back to life."
    a "Guess we made a full loop."
    f "And broke the loop, too. No more running from pain."
    a "No more pretending either."
    f "You know, Mad… I think we both healed each other. Bit by bit, cup by cup."
    a "That’s how it’s supposed to be. Healing isn’t a solo act, it’s a duet. Or sometimes, an orchestra!"
    f "I think I finally understand it now. About healing"
    f "Took me a long time to get back to where I was, thanks to you guys!"
    a "Heh, I was back to normal thanks to you too."
    f "Ahaha, anyways, about the healing duet, or orchestra"
    f "When's the encore?"
    a "Tomorrow morning. Same stage, same coffee."
    f "Deal. Ring up the rest of the guys, alright!"
    a "Of course!"
   
    $ set_scene("black")
    # $ set_scene("goodend")

    $ play_music(ending)
    scene goodend with fade
    f "Our pain and experience shaped us"
    f "No matter how hard it is, there is usually a way to solve it"
    f "What if we don't know how to, you might ask?"
    f "That is when friends and family come into play"
    f "And sometimes, you need a break to avoid a burnout"
    f "I need to work an early shift tomorrow to prepare for the gang coming in"
    f "Let's meet again, someday!"
    "Good Ending - Coffee's Solace"
    return

label neutral_end:
    $ set_scene("entrance_night")
    $ play_music(bittersweet)
    $ enter_from_right("kh") 
    f "Let's lock up."    
 
    f "I helped a few people today... I think."
    $ show_center("kn", "kh")

    f "But no matter how many cups I serve, I still feel that quiet ache inside."
    $ show_center("ksmile", "kn")

    f "You were right, Mad... Healing takes time. Maybe I’m still learning how."
    f "Tomorrow... maybe someone will make a cup for me."
    scene neutralend with fade

    "Neutral Ending - A Quiet Brew"
    return
