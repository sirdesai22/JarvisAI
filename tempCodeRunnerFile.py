speak('Playing Music')
        music_dir = 'C:\\Music\\'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, random.choice(songs)))