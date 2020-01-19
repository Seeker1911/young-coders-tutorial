# Setting up the chromebooks

This is a guide to setting up a Chromebook for use during the Young Coders
class (for PyTennessee 2018). We used the
[HP Chromebook 11 G5](http://www8.hp.com/us/en/products/laptops/product-detail.html?oid=10477089),
manually set up one laptop using crouton and installing all necessary packages
in linux, then used crouton's backup tools to restore that laptop to all of the
others.

**Note**: Cycle through Chromium OS and Ubuntu `Ctrl+Alt+Shift+Back` and `Ctrl+Alt+Shift+Forward`.

## Resources / Notes:

You can download the [full PyTN Ubuntu backup image, here](https://www.dropbox.com/s/nux1zfmsr6lsf5x/pytn-20180113-1600.tar.gz?dl=0)
(approximagely 1.56Gb). It's Ubuntu 16.04 (Xenial), with all the necessary packages and
resources already installed. In the [Restoring a backup](#restoring-a-backup)
guide below, you can use this to restore (quick and relatively easy). I saved
this on several flash drives named `PYTN` (hence the path names in the guide
below), and loaded it on multiple devices at once.

## Get started

1. Charge the battery
2. Turn on the laptop and go through keyboard/country selection, and enable/connect to wifi
3. Log in as guest

## Enable Developer Mode

To get started, we have to first
[enable developer mode](http://www.chromium.org/a/chromium.org/dev/chromium-os/developer-information-for-chrome-os-devices/generic).
Boot the device, and the perform the following:

1. Boot the device and connect to a network, set up the keyboard preferences,
   and log in as Guest.
2. Invoke recovery mode: Hold `ESC` and `Refresh` (F3) and hit the power button.
3. Once the computer reboots, hit `Ctrl-D`. (It'll ask you to confirm, just hit `Enter`).
4. Upon reboot you'll see a scary warning screen. Just hit `Ctrl-D` to skip this.


## RESTORING A BACKUP

If you've never set up crouton, skip to <a href="#getting-started-for-the-first-time">GETTING STARTED FOR THE FIRST TIME</a>.

Follow these steps if you've got a crouton backup ready to install on multiple
chromebooks (e.g. you've set up crouton and quickly want to get it running on
different devices).


### Install crouton and Restore a backup.

1. Log in as Guest
2. `Ctrl + Alt + T` to get into a `crosh` shell.
3. Type `shell`, and get a copy of crouton from [https://goo.gl/fd3zc](https://goo.gl/fd3zc)
   (note: clicking this link will download it to `~/Downloads`.
4. Install the crouton binaries:  `sudo sh ~/Downloads/crouton -b`
5. Plug in your Flash Drive / SD Card and restore: `sudo edit-chroot -f /media/removable/PYTN -r pytn`
6. In ChromeOS (from the shell), create a simple executable to launch ubuntu:
  - Run `./media/removable/PYTN/create-shortcust.sh`
  - If the above doesn't work, run: `echo 'sudo startxfce4' | sudo tee /usr/local/bin/ubuntu;`
  - Then: `sudo chmod a+x /usr/local/bin/ubuntu;`
7. **Important** Let ChromeOS Update: Click _Guest_ in the bottom-right, then
   click Settings &gt; About. You should seen an update progress or a message that
   ChromeOS is up to date. Once that happens, restart the system.
8. Once restarted, hit `Ctrl + D` to bypass the scary warning screen, log in as
   Guest again, `Ctrl + Alt + T`, type `shell`, then type `ubuntu`. You should
   see Linux launch. Open a Terminal, type: `cd ~/makinggames/ && python wormy.py`.
   You should see the game running.

If you get here and everything worked, you're good to go!

---

## GETTING STARTED FOR THE FIRST TIME

First, enable developer mode (see instructions above). Now, we can set up Crouton.

1. Log in as Guest.
2. `Ctrl + Alt + T` to get into a `crosh` shell.
3. Type `shell`, and get a copy of crouton from [https://goo.gl/fd3zc](https://goo.gl/fd3zc) (note: clicking this link will download it to `~/Downloads`.
4. Run `sudo sh ~/Downloads/crouton -r xenial -t xfce -n pytn` (you can also
   specify `-r xenial` to ensure you get 16.04, but that's the default)
5. Set username/password both to `pytn`
6. Once finished, run `sudo startxfce4` to start XFCE.
7. Run `sudo apt-get update` and `sudo apt-get upgrade`
8. (optional) Set up passwordless sudo: `sudo su -`, then run `visudo`, ensure
   entries have something like:  `ALL ALL = (ALL) NOPASSWD: ALL`
9. (optional) install the [crouton extension](https://goo.gl/OVQOEt)
10. (optional) If the touchpad isn't working (e.g. seems non-responsive), you
    may need to run `synclient FingerLow=1 FingerHigh=5` (and stick it in .bashrc).
    See [Issue #214](https://github.com/dnschneid/crouton/issues/214).

### Installing stuff

The bulk of the packages we need can be installed with the following:

    sudo apt-get install -y build-essential git git-core python-pygame ipython idle firefox firefox-locale-en gedit

Install the _Invent with Python_ games:

- `mkdir ~/makinggames && cd ~/makinggames && wget http://inventwithpython.com/makinggames.zip`
- `unzip makinggames.zip`
- Try it out: `python wormy.py`

(optional) Install Minecraft:

- See [this link for full details](https://goo.gl/r4ltBG)
- `sudo apt-get install -y software-properties-common python-software-properties`
- `sudo add-apt-repository -y ppa:minecraft-installer-peeps/minecraft-installer`
- `sudo apt-get -y -q update`
- `sudo apt-get -y -q install openjdk-8-jdk minecraft-installer`

Note that this is a commercial version of minecraft, and you need an account to play.

Install a few other games just for fun?

    sudo apt-get install kigo iagno supertuxkart extremetuxracer pychess

### System Tweaks

- Open Settings, Mouse and Touchpad, and disable _Tap touchpad to click_
- Click _Disable touchpad while typing_
- (Optional) Restrict xfce to only one workspace (during the class, several
  students accidentally switched to a new workspace with the touchpad, which
  was really confusing)
- Do any other system / desktop configuration here as well (e.g. add Firefox,
  IDLE, Gedit, etc to the bottom panel).
- _Ideally_ you'd get some external mice as well.


### Backup your chroot

Once you have a system configured, you can back up your chroot
(eg to a USB drive) with the following command, then you can restore it on
multiple devices to get an image set up quickly. First, exit Ubuntu, then
run the following from ChromeOS's shell:

    sudo edit-chroot -f /media/removable/YOUR_USB_DEVICE -b pytn

Then, to restore from a backup:

    sudo edit-chroot -f /media/removable/YOUR_USB_DEVICE -r pytn

----

## More Handy Resources

The following are useful resources to have.

- [crouton](https://github.com/dnschneid/crouton): Allows ubuntu to run in a chroot inside of ChromeOS
- [the crouton command cheat sheet](https://github.com/dnschneid/crouton/wiki/Crouton-Command-Cheat-Sheet): Lots of examples so you can see what all crouton can do.
- [Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line) at codecademy.com: Handy for anyone new to Linux.

### Crouton cheat-sheet

If you want to remove (and/or reinstall) linux, this list of `crouton` commands
may be helpful. See the [official cheat-sheet](https://github.com/dnschneid/crouton/wiki/Crouton-Command-Cheat-Sheet)
for more details.

Prior to setting up the chroot

- `sh crouton -r list` -- List available linux releases.
- `sh crouton -t help` -- help w/ targets (flavors of desktop, etc)
- `sudo sh crouton -t xfce` -- Create a Precise 12.04 with XFCE
- `sudo sh crouton -t xfce -r xenial -n pytn` -- Create a named chroot
- `sudo sh crouton -d -f pytn.tar.bz2 -t xfce -r xenial` -- Create a bootstrap file
- `sudo sh crouton -f pytn.tar.bz2 -t xfce -r xenial` -- Create a chroot from a bootstrap file
- `sudo delete-chroot precise` -- Removes an install chroot named "precise"
- `sudo sh crouton -n precise -u` -- Upgrade your chroot
- `sudo edit-chroot -f /media/removable/PYTN -b pytn` -- Make a BACKUP
- `sudo edit-chroot -f /media/removable/PYTN -r pytn` -- RESTORE a backup
- `sudo edit-chroot -a` -- list your installed chroots

Steps to start working w/ linux once it's set up:

1. Power on, (Ctrl+D during boot to skip the scary screen).
2. Browse as Guest or log in
3. `Ctrl+Alt+T`, then type `shell`
4. Type `sudo startxfce4`
5. Switch between chroot desktops &amp; Chrome OS with:
	- `Ctrl+Alt+Shift+Back`
	- `Ctrl+Alt+Shift+Forward`

