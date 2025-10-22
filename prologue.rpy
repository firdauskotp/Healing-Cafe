label prologue:

    $ set_scene("entrance")
    $ play_music(mattari)
    $ enter_from_right("kh") 
    
    f "Hello, the name is Fird. Welcome to Healing Coffee, where every cup is brewed with a dash of kindness."
    f "At least, that is what I hope, haha"
    f "I love coffee and thought, why not open my own shop?"
    f "But more than that, I want this place to be a haven for people who need a little pick-me-up, whether it's from a tough day or just life in general."
    f "And sometimes, I have customers, who I feel, need more than just a cup of coffee."
    f "Today is one of those days, and some of them are regular customers"
    f "But enough of introductions, let's get to work!"

    jump customer1


label customer1:
    
    "Morning Shift"
    $ set_scene("counter")
    $ play_music(mattari)
    $ enter_from_right("kh") 
    "The bell rings. A tired student walks in, dark circles under their eyes."
    f "Come in! What can I get for you today? (Ah, it's him. A student from my old university. My junior, to say the least)"

    c "One espresso, please. Make it strong."
    $ show_centre("ku","kh")
    f "You look like you’ve been up all night."

    menu:
        "What do you serve?"
        "Espresso (encourage work)":
            jump espresso_path
        "Chamomile tea (suggest rest)":
            jump chamomile_path

label espresso_path:
    f "Espresso coming right up. But you look like you could use a break. What's keeping you up at night?"
    c "The usual... deadlines wait for no one."
    "You hand over the espresso. Their hands tremble slightly as they take it."
    c "Thanks... I’ll just push through tonight."
    f "Don’t forget—coffee helps you work, but it won’t help you heal. You need to save yourself from burn out"
    c "Heh... maybe next time I’ll try that tea."
    $ healing_points = 0
    jump customer2

label chamomile_path:
    f "How about a cup of chamomile instead?"
    c "But I’ll fall asleep..."
    $ show_centre("kh","ku")
    f "Maybe that’s exactly what you need.:"
    f "I was a student, and I am still a part time student now"
    f "I know how it feels to be overwhelmed. Sometimes, the best thing you can do is step back and rest."
    f "Otherwise, you will get burn out. Tell me, what are you majoring in? What is this assignment about?"
    c "Computer engineering"
    f "That's my course, I know how it feels."
    c "Database is difficult"
    f "Do you enjoy it?"
    c "I do."
    f "Then take care of yourself, alright? Success is meaningless without health."
    f "If you get burnt out, you won’t be able to enjoy what you love. You will find it a chore instead"
    f "And you will begin to hate it."
    f "Manage your time better next time, okay? Rest is important. Remember your health is of utmost importance"
    "They stare at the steaming mug for a while, then smile faintly."
    c "...Yeah. Maybe rest is overdue."
    "The student smiled and left to sit outside drinking, he looks a bit more relaxed now."
    $ healing_points = 1
    jump customer2

label customer2:
    "The door chimes again. An elderly man steps in, his gaze lingering on the empty chair by the window."

    oldman "Black coffee, please. No sugar."
    barista "Sure thing. Still her usual order, huh?"

    menu:
        "What do you serve?"
        "Black coffee (reminisce)":
            jump blackcoffee_path
        "Hot chocolate (invite sharing)":
            jump hotchoco_path

label blackcoffee_path:
    f "Coming right up."
    c "She always loved the smell here... I still come just to remember."
    f "It’s a nice way to keep her close."
    c "Maybe. But memories don’t talk back, do they?"
    f "No... but they listen."
    "He smiles faintly, lost in thought."
    $ healing_points += 0
    jump customer3

label hotchoco_path:
    f "You know... maybe today calls for something warmer. Hot chocolate?"
    c "She’d have loved that. She had the sweetest tooth."
    f "Tell me about her."
    "He talks. You listen. The steam curls between you like gentle memories."
    c "Thank you. It’s been a while since anyone asked."
    f "She’d be happy you remembered her with warmth, not sorrow."
    $ healing_points += 1
    jump customer3

label customer3:
    "Evening settles in. A young artist stares at an empty sketchbook."

    c "Coffee, anything. Maybe it’ll make me draw again."
    f "Creative block, huh?"

    menu:
        "What do you serve?"
        "Matcha (try something new)":
            jump matcha_path
        "Latte (comfort and warmth)":
            jump latte_path

label matcha_path:
    f "Try this. A bit bitter, but maybe that’s the spark you need."
    c "Matcha? Never tried it."
    "They sip slowly, eyes lighting up at the unfamiliar taste."
    c "It’s... different. Kind of real."
    f "Sometimes change wakes us up."
    c "Maybe I’ll paint again tomorrow. Thank you."
    $ healing_points += 1
    jump ending

label latte_path:
    f "Here — a latte. Smooth, familiar. Like an old friend."
    class "Heh... maybe I just need to be kinder to myself."
    f "Even artists need rest too."
    c "Then I’ll draw tomorrow. But tonight... I’ll just be."
    $ healing_points += 1
    jump ending

# -------------------------------
# ENDING: The Barista & Friend
# -------------------------------
label ending:
    "Fird wanted to turn the sign to 'Closed.' A friend drops by, waving through the window."
    $ enter_from_right("ah", at_transform=right_side)

    a "Long day?"
    f "Yeah. Everyone seems to need healing lately."
    a "And you? Did you save some of that kindness for yourself?"

    menu:
        "How do you respond?"
        "Admit you’re tired":
            jump open_end
        "Brush it off":
            jump quiet_end

label open_end:
    $ set_scene("night_cafe")
    $ play_music(mattari)
    $ show_center("fn", "fh")
    f "Honestly... I’m exhausted. Helping people makes me forget my own mess. You remember, right?"
    $ show_right("an", "ah")
    a "I've been your friend for over 10 years"
    a "Of course I know"
    $ show_right("ah", "an")
    a "I know"
    a "Then let me buy you a drink for once."
    $ show_center("fh", "fn")
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
        $ set_scene("night_entrance")
        $ play_music(mattari)
        jump neutral_end

label quiet_end:
    $ show_center("fn", "fh")

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
    $ play_music(ending)
    f "Our pain and experience shaped us"
    f "No matter how hard it is, there is usually a way to solve it"
    f "What if we don't know how to, you might ask?"
    f "That is when friends and family come into play"
    f "And sometimes, you need a break to avoid a burnout"
    f "I need to work an early shift tomorrow to prepare for the gang coming in"
    f "Let's meet again, someday!"
    "THE END – (Good Ending)"
    return

label neutral_end:
    $ set_scene("night_entrance")
    $ play_music(bittersweet)
    $ enter_from_right("kh") 
    f "Let's lock up."    
 
    f "I helped a few people today... I think."
    $ show_center("fn", "fh")

    f "But no matter how many cups I serve, I still feel that quiet ache inside."
    $ show_center("fh", "fn")

    f "You were right, Mad... Healing takes time. Maybe I’m still learning how."
    f "Tomorrow... maybe someone will make a cup for me."
    "THE END – (Neutral Ending: A Quiet Brew)"
    return
