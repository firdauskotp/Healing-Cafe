label prologue:
    $ set_scene("university")
    $ play_music(mattari)
    # play music mattari loop

    "17th June 2020"

    na "Universities and schools have been opened again. Most of the students are happy to be back as online learning had been difficult."
    na "They missed hanging out with their friends and that 'education' vibe."
    na "At a university in town connected to a mall, two students head out. Semester break is near, and they’re planning what to do."

    # Klein pops in from the left, slightly raised (use your tuned left_side transform)
    $ enter_from_left("kh", at_transform=left_side)
    k "ARCADE!"

    $ enter_from_right("ah", at_transform=right_side)
    a "Bro, we are going to spend a week at the arcade?"

    # Swap Klein to neutral without slide (optional)
    $ show_left("ksmile", "kh")
    k "No, just one of the days, man!"
    $ show_right("an", "ah")
    a "Ahaha, one day—then it’s okay, Klein!"

    k "Hahaha… yeah, let’s plan something big, Lan!"
    $ show_left("kn", "ksmile")
    k "I will miss you guys during this period"
    $ show_right("ah", "an")
    n "* Alan ruffles Klein's cap"
    $ show_left("ku", "kn")
    k "Hey, don't treat me like a kid, although i am younger than you"
    a "Ahaha, chill, we have been friends for the longest time"
    a "You don't think a break will shatter our friendship, will you?"
    $ show_left("kn", "ku")
    a "..."
    $ show_right("ashock", "ah")
    a "Earth to Klein!"
    $ show_left("ksmile", "kn")
    k "Sorry, lost in thoughts"
    $ show_right("ah", "ashock")
    a "All alone?"
    k "Ahahah nice reference! Let's go, Lan! It is already drizzling"
    na "They chat while walking towards their motorcycles."
    $ stop_music()
    $ play_music(thunder)
    $ set_scene("rain_uni")
    $ show_left("kshock", "ksmile")
    $ show_right("ashock", "ah")
    na "Thunder roared as drizzle turned to steady rain."
    
    k "I think I’ll just park at the nearest station and take the train home."
    $ show_right("ah", "ashock")
    a "Eh? Since when are you scared of rain?"
    na "Alan sits on his bike and turns the key. The engine grumbles—then another thunderclap booms."
    k "You're kidding, right"
    k "That doesn’t scare you?"
    $ show_right("ashock", "ah")
    a "Yeah… this is pretty scary."
    a "But there isn’t a train station near my place, remember?"
    k "Alan, your house is further than mine. Ride safely, alright?"
    $ exit_to_right("ashock")
    $ exit_to_left("kshock")
    

    na "Klein removes his red cap and starts his scooter."
    na "Alan laughs, pulls on a snow cap, then his helmet. Klein fits a full-face helmet."
    na "They say their goodbyes and ride off."
    jump downpour

    