 # Python 3.7 and Pillow required
 # Puppet Facebench for Labyrinth of Refrain: Coven of Dusk (PC)
 # v0.3a by mug
 import os, sys, mmap, shutil, pathlib, msvcrt, time, glob
from PIL import Image

script_dir = os.path.dirname(__file__) #os.path.join(script_dir, rel_path)
valClas = ['-mak', '-fak', '-msb', '-fsb', '-mts', '-fts', '-mmm', '-fmm', '-mpf', '-fpf', '-mmr', '-fmr', '-gc', '-dr']
valPalt = ['1p', '2p', '3p', '4p']
inWidth = ['112', '56'] 
inHeight = ['296', '148']
inRes = ['-hd','-4k', '-all']
intWidth = list(map(int, inWidth))
intHeight = list(map(int, inHeight))
clear = lambda: os.system('cls')
run = True
if not os.path.exists(script_dir+"\\mods\\"):
    os.makedirs(script_dir+"\\mods\\")

def motd():
    print("Puppet Facebench v0.3a by mug")
    print("'As always, read the README' edition")
    print("-------------------------------------------------")
    print("Syntax: modName -options")
    print("Refer to README or enter \"help\".")
    print("-------------------------------------------------")
    return

def help():
    print("Read the README lol!")
    print("modName specifies folder of modName inside \mods\.")
    print("       faceBench automatically scans the modName folder and its subfolders.")
    print("-options:")
    print("       Leave empty to create '4K' setting sheet.\n Specify '-hd' to create 'HD' setting sheet.")    
    return

def chk4K(inputs):
    chk4K = bool("-4k" in inputs[1].lower())
    return chk4K

def wrk():
    print("Working",end="")
    return

def valArg(inputVal): #validate input and feedback
    while True:
        try:
            inputLine = input(inputVal)
            inputTemp = inputLine.split()
            modName = inputTemp[0]
            if len(inputTemp) > 1 and bool(set(inRes).intersection(inputTemp[1])) is True:
                outRes = inputTemp[1]
            else:
                inputTemp.append('-4k')
            # strip illegal characters
            remove_punctuation_map = dict((ord(char), None) for char in '\/*?:"<>|')
            modName.translate(remove_punctuation_map)
        except IndexError:
            print("Missing parameters or invalid input.")
            continue
        except IOError:
            print("Missing or invalid file?")
            continue
        except:
            print("uhhh????")
            continue
        if os.path.isdir(script_dir+"\\mods\\"+modName) is False:
            if modName != "help":
                print("mods\\"+modName+" does not exist.")
                continue
            else:
                help()
                continue
        #print("done validation")
        break
    return inputTemp

def valIcons(inputVal):
    output = list()
    is4K = chk4K(inputVal)
    #create list of detected icons
    for i in range(0,len(valClas)):
        for file in glob.glob("mods\\"+inputVal[0]+"\\**\\*"+str(valClas[i])+"[1-4]p*.png", recursive=True):
            jj = Image.open(file)
            if is4K is True:
                if jj.width == intWidth[0] and jj.height == intHeight[0]:
                    output.append(file)
            elif is4K is False and jj.width == intWidth[1] and jj.height == intHeight[1]:
                output.append(file)
            jj.close()
    return output

def getTyp(filename):
    for i in range(0,len(valClas)):
        if valClas[i] in filename:
            clsInd = i
            break
    for j in range(0, len(valPalt)):
        if valPalt[j] in filename:
            palInd = j
            break
    output = [clsInd,palInd]
    #print(output)
    return output

def genCord(typelist, inputs, icon):
    output = list()
    spc = 8
    spcY = 4
    xCor = 0
    yCor = 0
    m4K = 1
    icW = icH = 56
    row = 0
    rowPos = 0
    col = 0
    colPos = 0
    
    if chk4K(inputs) is True:
        spc = 16
        spcY = 8
        m4K = 2
        icW = icH = 112

    if typelist[0] <= 4: # x-col: 1p of each classgroup / y-row of sheet
        xCor = typelist[0] * ( 3 * (icW + spc))
        if icon == 2:
            row = 6 * (icH+spc)
        else:
            row = 0
    elif typelist[0] >= 5 and typelist[0] <= 9:
        xCor = (typelist[0] - 5) * ( 3 * (icW + spc))
        if icon == 2:
            row = 6 * (icH+spc) + (icH-(m4K*20)+spcY)
        else:
            row = (icH+spc)
    elif typelist[0] >= 10:
        xCor = (typelist[0] - 10) * ( 3 * (icW + spc))
        if icon == 2:
            row = 6 * (icH+spc) + 2 * (icH-(m4K*20)+spcY)
        else:
            row = 2*(icH+spc)
    if typelist[1] != 2: #palette basecoords
        if typelist[1] <= 1:
            col = typelist[1] * (icW + spc)
        elif typelist[1] == 3:
            col = 2 * (icW + spc)
        yCor = 0
        if icon < 2: #if not battlelog_icon and not 3p
            row = row + (icon * 3 * (icH + spc))
    elif typelist[1] == 2: #palette 3 uniques
        xCor = typelist[0] * (icW + spc)
        yCor = 510*m4K
        col = 0
        row = 0
        if icon < 2: #if not battlelog_icon and 3p
            row = row + (icon * (icH + spc))
        elif icon == 2: #if bl_icon and 3p
            row = 2 * (icH + spc) + (7*m4K) #magic space
    
    colPos = (xCor + col)
    rowPos = (yCor + row)
    output = [colPos,rowPos]
    return output

def doSheet(inputVal):
    outSheet = inputVal[0]
    str4K = ""
    if chk4K(inputVal) is True:
        str4K = "_4k"
    sheetName = "CharaFace_icon"+str4K+".png"

    outPath = script_dir+"\\mods\\"+outSheet+"\\"+sheetName
    shutil.copy(script_dir+"\\src_temp\\"+sheetName, outPath)
    imgsheet = Image.open(outPath).convert('RGBA')
    doList = list()

    iconList = valIcons(inputVal)
    #print(iconList)
    for i in range(0,len(iconList)):
        doList.append(getTyp(os.path.basename(iconList[i])))
    wrk() #printfeedback
    for j in range(0,len(doList)):
        if chk4K(inputVal) is True:
            box = [(0, 0,intWidth[0],intWidth[0]),(0, intWidth[0],intWidth[0],intWidth[0]*2),(0, intWidth[0]*2,intWidth[0],intHeight[0])]
        else:
            box = [(0, 0,intWidth[1],intWidth[1]),(0, intWidth[1],intWidth[1],intWidth[1]*2),(0, intWidth[1]*2,intWidth[1],intHeight[1])]

        imgicon = Image.open(iconList[j]).convert('RGBA')
        for k in range(0,3):
            regn = imgicon.crop(box[k])
            imgsheet.paste(regn,genCord(doList[j],inputVal,k))
            imgsheet.save(outPath)
        imgicon.close()
        print(".",end="")
    imgsheet.close()
    print("\nDone!\nOutput file: \\"+os.path.relpath(outPath,script_dir))
    return

def main():
    motd()
    inputs = valArg("Input: ")
    doSheet(inputs)
    return

def wait():
    try:
        input(">>> Hit ENTER to continue.")        
    except:
        print("Something fucked up, just close and re-run I guess lmao")
        pass

while run == True:
    main()
    run = False
    wait()
    clear()
    run = True
