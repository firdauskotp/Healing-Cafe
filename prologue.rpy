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
        "☕ Espresso (encourage work)":
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

# -------------------------------
# CUSTOMER 2: Lonely Old Man
# -------------------------------
label customer2:
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

# -------------------------------
# CUSTOMER 3: The Artist
# -------------------------------
label customer3:
    "Evening settles in. A young artist stares at an empty sketchbook."

    c "Coffee, anything. Maybe it’ll make me draw again."
    f "Creative block, huh?"

    menu:
        "What do you serve?"
        "🍵 Matcha (try something new)":
            jump matcha_path
        "☕ Latte (comfort and warmth)":
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
