# Puppet Facebench v0.3a  
_Originally posted to XenTaX.com on 2018/10/20_  
by mug

## I. About & Disclaimer

Equally janky companion tool for [puppetWorkbench](https://github.com/muge/puppetWorkbench).
Lets you slap together a CharaFace_Icon sheet with less hassle (maybe).

This work is now licensed under GNU General Public License v3.0, please refer to the included LICENSE file.  
*This was FORMERLY licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License, which may be found in various archived (pre-2025) versions of this script around the internet.*

**DISCLAIMER**:  
By using this script you agree that I'm not responsible if you muck up your files (game-related or otherwise) or computer beyond repair.  
Script was only (briefly) tested on Windows 7 64-bit, using Python 3.7.0 32/64-bit.


## II. Things you'll need

1. Python 3.7.0 (https://www.python.org/downloads/release/python-370/) 
	* PROTIP: check add Python 3.7 to PATH when installing
2. Install Pillow (cmd to your python.exe directory "python -m pip install Pillow")
	* If this doesn't work, you're figuring it out yourself, may have to do with Windows PATH environmental variable?
3. Photoshop
4. Basic Photoshop skills
5. Patience


## III. Prepping Icon Files

In the `\src_temp\` folder, there are PNG versions of the default CharaFace_Icon sheets, along with two other PNGs and PSDs.  
There are three icons: Colored, BW, and a smaller Battlelog Icon.  
They are arranged into a "chip" so they're easier to organize/modularize (if that's a word?) and share.  
You don't NEED to use the templates (so you can make your own fancy borders), but puppetFacebench follows this "chip" format, so the dimensions of each icon & chip **MUST** match!  

### Dimensions:
|Chip||
|:-|:-|
|4K| 112 x 296|
|HD| 56 x 148|

|Icon (Colored & BW)||
|:-|:-|
|4K|112 x 112|
|HD| 56 x 56|

|Battlelog Icon||
|:-|:-|
|4K| 112 x 72|
|HD| 56 x 36|

If you're sharing your mod, it's recommended you share the chips and not the actual sheet, that way people can choose where they want to slot the character, and saves them some copy-paste job.

### Saving and Naming your Images

After you're finished making edits to your chip, save it as a .PNG image file. 
Next, you MUST include in your file's name, the intended class/facet and palette that the chip is replacing.

#### Classes (Facets):
- Easy way to remember the facets are that **-m** and **-f** are used to denote gender, followed by the initials of the class.  
    - Note that Gothic Coppelia and Demon Reaper only have one gender.  

| Facet | Male | Female |
|:----------------|:-----|:-------|
| Aster Knight | -mak | -fak |
| Peer Fortress | -mpf | -fpf  |
| Shinobushi | -msb | -fsb |
| Mad Raptor | -mmr | -fmr  |
| Theatrical Star | -mts | -fts  |
| Marginal Maze | -mmm | -fmm  |
| Gothic Coppelia | | -gc  |
| Demon Reaper | | -dr  |

#### Palette: 
**1p**, **2p**, **3p**, or **4p**  

So for example:
- Demon Reaper 3rd Palette: "-dr3p"
- Male Marginal Maze 1p: "-mmm1p"
	etc.

This identifier is required or the chip will be ignored by puppetFacebench.  
It also can be anywhere in the filename, so `lewdscytheloli-dr3p.png` or `this.-mmm1p.went.on.a.diet.png` will both work.  

Icons should be saved in the `mods\[modName]` folder of your choice.  
For ease of use, puppetFacebench will also scan subfolders of `mods\[modName]` for valid chips to use.  


## IV. Usage

0. Make sure your chips are all present in the intended mods\[modName] folder with identifiers and all.
1. Run puppetFacebench.py
2. modName [-options]
3. Wait until it's finished (4K sheets may take a few minutes)

--------
### **modName**  
- Determines location of the chips and the destination of the output file.
```
mods\modName\*.png
mods\modName\CharaFace_Icon[_4k].png
```
- Must be specified after the input filename. 
- Illegal characters will be stripped. 

--------
### **[-options]**
- Can be input in any order. 
#### HD or 4K
-hd, -4k
- Not specifying will generate a 4K sheet by default.

--------

EXAMPLE:
Male Peer Fortress, Palette 2, 4K version in folder `mods\babbysFirstMod\`
```
babbysFirstMod stimky-mpf2p -4k
```

After sheet generation, you still must vertically-flip and save as DDS before using puppetWorkbench to convert it to a working .dds.phyre file.
As such, refer to the [puppetWorkbench](https://github.com/muge/puppetWorkbench) README if you're unfamiliar with the process.

--------
### Changelog
```
v0.00 - v0.1
	Initial proof of concept ver.
	Shoddy README.txt
v0.2 -
	Removed need to specify HD/4K parameter explicitly
	Fixed corrupted output images from incorrect RGBA conversion call
	Combined class/facet and gender parameter in filenames
	Fixed misaligned Battlelog Icons
	Deprecated individual icons in favor of "chip" format
v0.3 - 
	4K sheet now default behaviour if -hd/-4k not specified
	Added subfolder-searching behaviour in favor of icon organization
	Added "Working..." progress feedback
	Rearranged environment so puppetFacebench can co-exist with puppetWorkbench in the same folder for ease of use
```
	
