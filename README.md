# linux-clicky
[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=skkeeper&url=https://github.com/skkeeper/linux-clicky&title=linux-clicky&language=&tags=github&category=software)

Inspired by colszowka's [linux-typewritter](https://github.com/colszowka/linux-typewriter) script, linux-clicky produces a sound everytime you press a key on your keyboard. This might be useful for screensharing or a screencast if you want to have some type of feedback while you type.

## Usage

Run the main.py file and it will automaticly detect your keyboards and start *clickytty click*.

**Because the way the script detects the keypresses (by tying itself to the event file in Linux, just like a keylogger would do) it requires root access**

If you are worried about malicious code, the script is pretty small you can easily read it in five minutes, so feel free to.

## Advantages over the original script:

- Entirely written in Python;
- Supports basic volume control;
- Uses threads to avoid problems with quick typing;
- Produces the sound on key down, this way the sound doesn't loop if you keep the key pressed.
- It's possible to diversify the sound of some keys. By default the SPACE and ENTER key have a specific sound. In the future, if more soundbanks are added, more special sounds for specific keys can also be easily added.

## Disadvantages

- Requires root access
- It was coded while I was taking a break from another project, so expect a bit of bad code here and there (feel free to submit patches).

## Dependencies

- Linux (tested under Ubuntu 12.04)
- Python (tested under 2.7.3)
- SoX (in debian based systems install by typing "sudo apt-get install sox");

## Future

This is a very simple script therefore it's probably not gonna have a lot of focus on development, but I would love to add some more soundbanks into it, especially from mechanical keyboards. If you are interested in providing some  recordings feel free to contact me.

## Support Developers

Flattr is a great way of supporting developers (and content creators) so we can continue developing better tools for free. So if you enjoy this piece of software please consider donating by clicking in the Flattr icon bellow or contacting me directly. Thank you :)
[![Flattr this git repo](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=skkeeper&url=https://github.com/skkeeper/linux-clicky&title=linux-clicky&language=&tags=github&category=software) 

## License

The code is under the supplied MIT license, therefore it's completely open source.

evdev.py (by Micah Dowty <micah@navi.cx>) is included under the terms of the GPLv2. Thanks to Micah Dowty for writing this module since without it this script would not be possible, or at least not as easy to code.

The keyboard sounds were extracted from ['keyboard-typing’ by Anton](http://www.freesound.org/samplesViewSingle.php?id=137) at Freesound