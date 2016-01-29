# Setting up the chromebooks

Asus C300M

1. Charge the battery
2. Turn on the laptop and go through keyboard/country selection, and enable/connect to wifi
3. Log in as guest


## Enable Developer Mode

1. Hit Esc + Refresh (F3) + Power
2. Ctrl + D to bypass the warning, Turn off OS verification (presss Enter)
3. Ctrl + D again... wait for it to boot into developer mode.

## Setting up Crouton

1. Log in as Guest
2. `Ctrl + Alt + T` to get into a `crosh` shell.
3. Type `shell`, and get a copy of crouton from [https://goo.gl/fd3zc](https://goo.gl/fd3zc) (note: clicking this link will download it to `~/Downloads`.
4. Run `sudo sh ~/Downloads/crouton -t xfce -r trusty -n pytn`
5. Set username/password both to `pytn`
6. Once finished, run `sudo enter-chroot startxfce4` to start XFCE.
7. Run `sudo apt-get update` and `sudo apt-get upgrade`
8. (optional) Set up passwordless sudo: `sudo su -`, then run `visudo`, ensure
   entries have something like:  `ALL ALL = (ALL) NOPASSWD: ALL`

## System Tweaks

- Open Settings, Mouse and Touchpad, and disable _Tap touchpad to click_
- Click _Diable touchpad while typing_


## Installing stuff

The bulk of the packages we need can be installed with the following:

    sudo apt-get install -y build-essential git git-core python-pygame ipython idle firefox firefox-locale-en

Install the _Invent with Python_ games:

- `mkdir ~/makinggames && cd ~/makinggames && wget http://inventwithpython.com/makinggames.zip`
- `unzip makinggames.zip`
- Try it out: `python wormy.py`

(optional) Install Minecraft:

- See [this link for full details](https://goo.gl/r4ltBG)
- `sudo apt-get install -y software-properties-common python-software-properties`
- `sudo add-apt-repository -y ppa:minecraft-installer-peeps/minecraft-installer`
- `sudo apt-get -y -q update`
- `sudo apt-get -y -q install openjdk-7-jdk minecraft-installer`

Note that this is a commercial version of minecraft, and you need an account to play.

## Backups and Bootstrap files

To build a bootstrap file (e.g. for setting up additional machines), run:

    sudo sh crouton -d -f /media/removable/PYTN/pytn-1404-bootstrap.tar.bz2 -t xfce -r trusty

Then, to set up a new device using that bootstrap file:

    sudo sh crouton -f /media/removable/PYTN/pytn-1404-bootstrap.tar.bz2 -t xfce -r trusty

Once you have a system configured, you can back up your chroot (eg to a USB drive) with:

    sudo edit-chroot -f /media/removable/PYTN -b pytn

Restore from a backup:

    sudo edit-chroot -f /media/removable/PYTN -r pytn


## Handy Resources

The following are useful resources to have.

- [crouton](https://github.com/dnschneid/crouton): Allows ubuntu to run in a chroot inside of ChromeOS
- [the crouton command cheat sheet](https://github.com/dnschneid/crouton/wiki/Crouton-Command-Cheat-Sheet): Lots of examples so you can see what all crouton can do.
- [Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line) at codecademy.com: Handy for anyone new to Linux.



