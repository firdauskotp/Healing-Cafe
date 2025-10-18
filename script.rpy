label start:
    jump prologue
    


   

    # ===========================
    # 11th July 2020 — Lively arcade
    # ===========================
    $ set_scene("arcade", trans=fade)
    "11th July 2020"
    na "The arcade is lively—crowds, lights, and the clatter of buttons and tickets."
    na "But for two men inside, the mood is subdued."

    # Klein present (left), talking; Alan sits/stands nearby (no sprite needed)
    $ _safe_show("kn", at_transform=left_side)
    k "So, this machine’s what I like to play. You used to wait and complain I was wasting money."
    na "Klein points to a rhythm game, forcing a small laugh."

    a "Sorry, Klein…"
    k "Chill, bro. We’re in this together, right?"
    na "Alan gives a brief but sincere smile."

    na "It’s a Saturday; movement restrictions were lifted not long ago. More people drift in."
    na "Alan sits on a bench."
    k "Mind if I run to the washroom?"
    a "Nah, I’ll wait here."

    # ===========================
    # One week earlier — flashback
    # ===========================
    na "A week earlier… 4th July 2020."
    na "Evening birdsong; nearly night. Alan, in a football jacket, pushes Klein’s wheelchair home."

    a "Great news from the doc—you’re recovering well. Crutches soon."
    k "I’m trying to be positive."
    a "I guess so…"
    k "You still haven’t remembered what happened, have you?"
    a "That—and a lot of other things."
    k "Took you a while just to remember my name."
    na "Alan looks guilty; Klein waves it off."
    k "If it weren’t for those riders, you’d have been toast!"
    a "I wish I remembered who helped. Thankfully, no major injuries—just… this amnesia."
    k "Haven’t seen you laugh in a while."
    a "True. Maybe you could fix my amnesia by bonking me."
    k "…I did think of something. Not that."
    a "What?"
    k "Let’s go to the arcade next Saturday. We used to hang out there. Maybe it will jog your memory."
    k "My treat—as your wonderful friend, haha. And to repay you for everything."
    a "Okay… I guess?"
    k "Then it’s settled!"

    # ===========================
    # Back to 11th July — bench
    # ===========================
    na "Back to 11th July."
    k "I hope this helps, bro…"
    na "Klein heads to the washroom."

    na "Alan sits, scanning the crowd."
    a "I do remember fun here… or Klein raging at that rhythm game."
    na "He chuckles—then freezes."
    na "A girl in a snow cap, blue hair, baggy jacket and long trousers passes by."
    a "Why does she feel so important…?"

    na "Alan grabs his crutches and rushes, stumbling. He falls; people hurry over."
    w "Are you okay?"
    na "It’s the girl. She helps him up. Her eyes widen."
    s "Al… Alan?!"

    a "Everyone, I’m alright—thank you. I just need to speak with her."
    a (serious) "Tell me—who are you?"
    s "You’ve got to be joking. You forgot me—and disappeared without a word—now you’re like this?!"
    a "Who are you? I was in an accident and—"
    s "An accident? Sounds like something Klein would tell you to say."
    a "Keep his name out of this. I’ve lost my memories. He was with me—you weren’t."
    a "You seem familiar. You clearly know me."

    s "…I’m sorry."
    a "Thank you. My question still stands."
    s "Serra."
    a "Rings a bell."
    s "Of course it does. We—"
    a "We…?"
    s "Let’s walk the arcade. I’ll explain."
    a "You know Klein too?"
    s "We kind of hate each other."
    a "Why?"
    s "I’ll get to that."

    na "They walk; people ask if Alan’s okay. He nods."
    s "Brings back memories, doesn’t it? Klein introduced us here."
    a "And we came here often?"
    s "A lot. Shooters, a horror cabinet… we used to be a trio. Then Klein stopped coming. It was either you two, or you and me."
    a "Something happened?"
    s "His assumptions."
    a "That doesn’t help."

    # Stairs to 2F (restricted)
    na "They reach a staircase to the second floor, roped off for maintenance."
    s "Let’s go."
    a "Are you daft? We’ll get sued!"
    s "Shh. We need privacy."
    a "I’m not sure I want to hear this now."
    s "Just follow me!"

    # Old machine upstairs
    na "Upstairs stands a huge, worn cabinet. The title is barely legible."
    a "\"Arcade Nightmare\", huh? Cliché."
    a "Go on, Serra. Make it quick—Klein will be back soon."
    s "Fine. From the start…"

    na "A dead screen flickers. A bright light spills from the broken marquee."
    a "Huh? It works?"
    s "Can you listen for once?"
    a "For once? I’ve been listening."
    s "Do you want to fight about this now?"
    na "The light grows—brighter, brighter—"

    # ===========================
    # Klein returns to the bench
    # ===========================
    $ set_scene("arcade")
    k "Who knew the loo was that far… I hope Alan’s alright. If he were himself, he’d meme me for being late."
    na "Klein finds the bench empty. He hurries to the front counter."

    r "Welcome. Can I help?"
    k "Have you seen my friend? Bandages and crutches."
    r "Yes, he fell earlier—caused a bit of a scene."
    k "He WHAT?!"
    r "Relax. A girl helped him. They walked into the arcade together."
    k "A girl, eh? How’d she look?"
    r "About your height. Snow cap. Baggy jacket, long trousers. A bit goth."
    k "…That was his taste… that was his—wait."
    k "Is her hair coloured?"
    r "Blue."
    k "…Thanks. I need to sort this out."

    na "Klein dashes off."
    k "Serra, what are you planning this time…?"
    na "He finds a quiet staircase. No one around."
    k "She wouldn’t… he’s on crutches. Then again, not the first selfish stunt."
    na "Upstairs: the massive cabinet. Dead. No one there."
    k "Two backpacks… Alan’s—and that thorny black satchel. Serra."
    k "Where did you two go? Damn it, Serra—what have you done?!"

    na "The machine hums alive. Light blooms."
    k "It works? Looked rusty enough to be scrap—"
    na "The light surges and engulfs him."
    k "This has got to be a joke—!"

    # ===========================
    # Unknown place
    # ===========================
    $ set_scene("arcade_nightmare", trans=fade)
    na "Location: Unknown. Time: Stagnant. People: Serra, Alan."
    a "Feels like I hit my head."
    na "Alan steadies himself on crutches."
    a "Where’s Serra? Klein?"
    na "Silence answers. Neon shadows curve like a maze."
    a "Well… guess some supernatural nonsense happened."
    na "He scans the room—Pac-Man-esque corridors formed by dead machines and flickering signs…"

    return
