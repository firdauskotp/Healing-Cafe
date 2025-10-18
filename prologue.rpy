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
    
    "The bell rings. A tired student walks in, dark circles under their eyes."

    student "One espresso, please. Make it strong."
    barista "You look like you’ve been up all night."

    menu:
        "What do you serve?"
        "☕ Espresso (encourage work)":
            jump espresso_path
        "🍵 Chamomile tea (suggest rest)":
            jump chamomile_path

label espresso_path:
    barista "Espresso coming right up. You’ll need the strength for whatever battle you’re fighting."
    student "Yeah... deadlines wait for no one."
    "You hand over the espresso. Their hands tremble slightly as they take it."
    student "Thanks... I’ll just push through tonight."
    barista "Don’t forget—coffee helps you work, but it won’t help you heal."
    student "Heh... maybe next time I’ll try that tea."
    $ healing_points = 0
    jump customer2

label chamomile_path:
    barista "How about a cup of chamomile instead?"
    student "But I’ll fall asleep..."
    barista "Maybe that’s exactly what you need."
    "They stare at the steaming mug for a while, then smile faintly."
    student "...Yeah. Maybe rest is overdue."
    $ healing_points = 1
    jump customer2

# -------------------------------
# CUSTOMER 2: Lonely Old Man
# -------------------------------
label customer2:
    scene cafe_afternoon
    show oldman sad at left
    "The door chimes again. An elderly man steps in, his gaze lingering on the empty chair by the window."

    oldman "Black coffee, please. No sugar."
    barista "Sure thing. Still her usual order, huh?"

    menu:
        "What do you serve?"
        "☕ Black coffee (reminisce)":
            jump blackcoffee_path
        "🍫 Hot chocolate (invite sharing)":
            jump hotchoco_path

label blackcoffee_path:
    barista "Coming right up."
    oldman "She always loved the smell here... I still come just to remember."
    barista "It’s a nice way to keep her close."
    oldman "Maybe. But memories don’t talk back, do they?"
    barista "No... but they listen."
    "He smiles faintly, lost in thought."
    $ healing_points += 0
    jump customer3

label hotchoco_path:
    barista "You know... maybe today calls for something warmer. Hot chocolate?"
    oldman "She’d have loved that. She had the sweetest tooth."
    barista "Tell me about her."
    "He talks. You listen. The steam curls between you like gentle memories."
    oldman "Thank you. It’s been a while since anyone asked."
    barista "She’d be happy you remembered her with warmth, not sorrow."
    $ healing_points += 1
    jump customer3

# -------------------------------
# CUSTOMER 3: The Artist
# -------------------------------
label customer3:
    scene cafe_evening
    show artist blank at left
    "Evening settles in. A young artist stares at an empty sketchbook."

    artist "Coffee, anything. Maybe it’ll make me draw again."
    barista "Creative block, huh?"

    menu:
        "What do you serve?"
        "🍵 Matcha (try something new)":
            jump matcha_path
        "☕ Latte (comfort and warmth)":
            jump latte_path

label matcha_path:
    barista "Try this. A bit bitter, but maybe that’s the spark you need."
    artist "Matcha? Never tried it."
    "They sip slowly, eyes lighting up at the unfamiliar taste."
    artist "It’s... different. Kind of real."
    barista "Sometimes change wakes us up."
    artist "Maybe I’ll paint again tomorrow. Thank you."
    $ healing_points += 1
    jump ending

label latte_path:
    barista "Here — a latte. Smooth, familiar. Like an old friend."
    artist "Heh... maybe I just need to be kinder to myself."
    barista "Even artists need rest too."
    artist "Then I’ll draw tomorrow. But tonight... I’ll just be."
    $ healing_points += 1
    jump ending

# -------------------------------
# ENDING: The Barista & Friend
# -------------------------------
label ending:
    scene cafe_night
    show friend smile at right
    "You turn the sign to 'Closed.' A friend drops by, waving through the window."

    friend "Long day?"
    barista "Yeah. Everyone seems to need healing lately."
    friend "And you? Did you save some of that kindness for yourself?"

    menu:
        "How do you respond?"
        "Admit you’re tired":
            jump open_end
        "Brush it off":
            jump quiet_end

label open_end:
    barista "Honestly... I’m exhausted. Helping people makes me forget my own mess."
    friend "Then let me buy you a drink for once."
    barista "Ha, you’ll ruin my business model."
    friend "Maybe healing’s not about running a café. Maybe it’s about sharing the table."
    "You both sit, two cups between you. For the first time today, the silence feels peaceful."
    if healing_points >= 3:
        jump good_end
    else:
        jump neutral_end

label quiet_end:
    barista "I’m fine. Just tired, that’s all."
    friend "Sure... But even coffee goes cold if you leave it alone too long."
    "You smile quietly. Outside, the rain stops."
    if healing_points >= 3:
        jump good_end
    else:
        jump neutral_end

label good_end:
    scene cafe_closure
    "You close the café, the smell of roasted beans lingering."
    "Maybe healing isn’t found in the cup… but in the people who share it."
    "THE END – (Good Ending)"
    return

label neutral_end:
    scene cafe_closure
    "You lock up alone. The air is still warm, but something inside you feels empty."
    "Tomorrow, maybe someone will make a cup for you."
    "THE END – (Neutral Ending)"
    return
