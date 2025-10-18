init -1 python:
    # Change scene with dissolve
    
    def set_scene(image_name, trans=dissolve, layer="master"):
        # 1) Clear the layer (equivalent to: scene)
        renpy.scene(layer=layer)
        # 2) Show an image by its defined name (equivalent to: show <name>)
        renpy.show(image_name, layer=layer)
        # 3) Apply transition (equivalent to: with dissolve)
        if trans:
            renpy.with_statement(trans)

    # Play background music
    def play_music(music_file, music_vol=0.5):
        if music_file:
            renpy.music.play(music_file, fadein=3.0, loop=True, synchro_start=True, channel="music")
            renpy.music.set_volume(music_vol, delay=0, channel="music")

    # Stop background music
    def stop_music():
        renpy.music.stop(fadeout=3.0, channel="music")

    def _safe_show(image_name, at_transform=None, layer="master"):
        """
        Shows an image only if it's defined; logs a note otherwise.
        """
        try:
            # renpy.has_image works with tag names like "klein neutral"
            if renpy.has_image(image_name):
                if at_transform is not None:
                    renpy.show(image_name, at_list=[at_transform], layer=layer)
                else:
                    renpy.show(image_name, layer=layer)
                return True
            else:
                renpy.log("-- Image not found: {}".format(image_name))
                return False
        except Exception as e:
            renpy.log("-- Error showing '{}': {}".format(image_name, e))
            return False

    def show_left(new_character, initial_character):
        renpy.hide(initial_character)
        _safe_show(new_character, at_transform=left_side)

    def show_center(new_character, initial_character):
        renpy.hide(initial_character)
        _safe_show(new_character, at_transform=center_side)

    def show_right(new_character, initial_character):
        renpy.hide(initial_character)
        _safe_show(new_character, at_transform=right_side)

    # ---- slide-on-entry helpers (transitions are applied with 'with', not in at_list)
    def enter_from_left(image_name, at_transform=center_side):
        if _safe_show(image_name, at_transform=at_transform):
            renpy.with_statement(moveinleft)

    def enter_from_right(image_name, at_transform=center_side):
        if _safe_show(image_name, at_transform=at_transform):
            renpy.with_statement(moveinright)

    def exit_to_left(image_name):
        if renpy.has_image(image_name):
            renpy.hide(image_name)
            renpy.with_statement(moveoutleft)

    def exit_to_right(image_name):
        if renpy.has_image(image_name):
            renpy.hide(image_name)
            renpy.with_statement(moveoutright)

    #play music for a certain period of time
    def fade_to_black_and_play_sfx(sfx_name, fadeout_bgm=0.5, black_trans=fade):
        """
        Stops BGM, fades/cuts to black, plays a one-shot SFX on the 'sound' channel,
        and waits until it finishes.
        """
        # Stop background music
        renpy.music.stop(channel="music", fadeout=fadeout_bgm)

        # Go to black background
        renpy.scene()
        renpy.show("black")  # Ren'Py has a built-in 'black' Solid
        if black_trans:
            renpy.with_statement(black_trans)

        # Play SFX on 'sound' channel (non-looping) and wait for it to end
        renpy.music.play(sfx_name, channel="sound", loop=False, synchro_start=True)
        while renpy.music.get_playing(channel="sound"):
            renpy.pause(0.1)