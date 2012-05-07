# linux-clicky
Inspired by colszowka's [linux-typewritter](https://github.com/colszowka/linux-typewriter) script, linux-clicky produces a sound everytime you press a key on your keyboard. This might be usefull for screensharing or a screencast if you want to have some type of feedback while you type.

## Advantages over the original script:

- Entirely written in Python;
- Supports basic volume control;
- Uses threads to avoid problems with quick typing;
- Produces the sound on key down, this way the sound doesn't loop if you keep the key pressed.


## Dependencies

- Linux (tested under Ubuntu 12.04)
- Python (tested under 2.7.3)
- SoX (in debian based systems install by typing "sudo apt-get install sox");

## Future
This is a very simple script therefore it's probably not gonna have a lot of focus on development, but I would love to add some more soundbanks into it, especially from mechanical keyboards. If you are interested in providing some  recordings feel free to contact me.

## License
The code is under the supplied MIT license, therefore it's completely open source.

The keyboard sounds were extracted from ['keyboard-typing’ by Anton](http://www.freesound.org/samplesViewSingle.php?id=137) at Freesound