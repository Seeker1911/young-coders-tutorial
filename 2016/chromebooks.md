# Setting up the chromebooks

Asus C300M

1. Charge the battery
2. Turn on the laptop and go through keyboard/country selection, and enable/connect to wifi
3. Log in as guest


## RESTORING A BACKUP

If you've never set up crouton, skip to _GETTING STARTED FOR THE FIRST TIME_.

Follow these steps if you've got a crouton backup ready to install on multiple
chromebooks (e.g. you've set up crouton and quickly want to get it running on
different devices).

### Enable Developer Mode

1. Boot the device and connect to a network, set up the keyboard preferences,
   and log in as Guest.
2. Hit Esc + Refresh (F3) + Power
3. Ctrl + D to bypass the warning, Turn off OS verification (presss Enter)
4. Ctrl + D again... wait for it to boot into developer mode.


### Install crouton and Restore a backup.

1. Log in as Guest
2. `Ctrl + Alt + T` to get into a `crosh` shell.
3. Type `shell`, and get a copy of crouton from [https://goo.gl/fd3zc](https://goo.gl/fd3zc) (note: clicking this link will download it to `~/Downloads`.
4. Install the crouton binaries:  `sudo sh ~/Downloads/crouton -b`
5. Plug in your Flash Drive / SD Card and restore: `sudo edit-chroot -f /media/removable/PYTN -r pytn`
6. In ChromeOS (from the shell), create a simple executable to launch ubuntu:
  - `sudo touch /usr/local/bin/ubuntu`
  - `sudo chmod a+x /usr/local/bin/ubuntu`
  - `sudo vi /usr/local/bin/ubuntu`, type `i` to enter insert mode, type: `sudo enter-chroot startxfce4`, then hit esc and type `:wq` to save and exit.
7. **important** Let ChromeOS Update: Click _Guest_ in the bottom-right, then click Settings > About. You should seen an update progress or a message that ChromeOS is up to date. Once that happens, restart the system.
8. Once restarted, hit `Ctrl + D` to bypass the scary warning screen, log in as Guest again, `Ctrl + Alt + T`, type `shell`, then type `ubuntu`. You should see Linux launch. Open a Terminal, type: `cd ~/makinggames/ && python wormy.py`. You should see the game running.

If you get here and everything worked, you're good to go!

---

## GETTING STARTED FOR THE FIRST TIME

1. Log in as Guest
2. `Ctrl + Alt + T` to get into a `crosh` shell.
3. Type `shell`, and get a copy of crouton from [https://goo.gl/fd3zc](https://goo.gl/fd3zc) (note: clicking this link will download it to `~/Downloads`.
4. Run `sudo sh ~/Downloads/crouton -t xfce -r trusty -n pytn`
5. Set username/password both to `pytn`
6. Once finished, run `sudo enter-chroot startxfce4` to start XFCE.
7. Run `sudo apt-get update` and `sudo apt-get upgrade`
8. (optional) Set up passwordless sudo: `sudo su -`, then run `visudo`, ensure
   entries have something like:  `ALL ALL = (ALL) NOPASSWD: ALL`

### System Tweaks

- Open Settings, Mouse and Touchpad, and disable _Tap touchpad to click_
- Click _Diable touchpad while typing_


### Installing stuff

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

___

## Backups and Bootstrap files

To build a bootstrap file, run the following command. This is useful if you want
to install without needing to download lots of stuff over and over.

    sudo sh crouton -d -f /media/removable/PYTN/pytn-1404-bootstrap.tar.bz2 -t xfce -r trusty

Then, to set up a new device using that bootstrap file:

    sudo sh crouton -f /media/removable/PYTN/pytn-1404-bootstrap.tar.bz2 -t xfce -r trusty

**Notice**: Once you have a system configured, you can back up your chroot
(eg to a USB drive) with the following command, then you can restore it on
multiple devices to get an image set up quickly.

    sudo edit-chroot -f /media/removable/PYTN -b pytn

Restore from a backup:

    sudo edit-chroot -f /media/removable/PYTN -r pytn


## Handy Resources

The following are useful resources to have.

- [crouton](https://github.com/dnschneid/crouton): Allows ubuntu to run in a chroot inside of ChromeOS
- [the crouton command cheat sheet](https://github.com/dnschneid/crouton/wiki/Crouton-Command-Cheat-Sheet): Lots of examples so you can see what all crouton can do.
- [Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line) at codecademy.com: Handy for anyone new to Linux.
