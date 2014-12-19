import os
import shutil

globalindex = 0
def CopyToNew(srcloc, destloc, prefix):
    global globalindex
    index = 0
     #for filename in os.listdir("./WalkingMeditation"):
    for dirname, dirnames, filenames in os.walk(srcloc):
        for filename in filenames:
            index = index + 1
            newname = destloc+prefix+str(index)+".jpg"
            oldname = os.path.join(dirname, filename)
            #print "Copying " + oldname + " to " + newname
            shutil.copyfile(oldname, newname)
    print ("Renamed " + str(index) + " files " + srcloc)
    globalindex = globalindex + index

def RenameWalkingMeditation(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/Walking Meditation", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def Renamesports(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/sports", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def Renamemis(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/mis", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def RenameSittingMeditation(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/Sitting Meditation", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def RenamePhapThoai(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/Phap Thoai", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def RenameOrientation(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/Orientation", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def RenameOanhVu(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/Oanh Vu", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def RenameGroupDiscussion(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/Group Discussion", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def RenameDonVi(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/Don Vi", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def RenameCleanup(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/Clean up", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def RenameCampfire(prefix):
    CopyToNew("/Users/lcle/Pictures/MocLan/Camp fire", "/Users/lcle/Pictures/MocLan/Renamed/", prefix)

def cleanup(path):
    print "cleaning up: " + path
    try:
        shutil.rmtree(path)
    except Error as err:
        errors.extend(err.args[0])
    os.makedirs(path)

def main():
    cleanup("/Users/lcle/Pictures/MocLan/Renamed/")
    RenameOrientation("a")
    RenamePhapThoai("b")
    RenameSittingMeditation("c")
    RenameGroupDiscussion("d")
    RenameOanhVu("e")
    RenameWalkingMeditation("g")
    Renamesports("h")
    RenameCampfire("i")
    Renamemis("j")
    RenameCleanup("k")
    RenameDonVi("l")
    print "Total file renamed: " + str(globalindex)

main()

