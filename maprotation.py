import glob
import json
import mariadb
import sys

def main():
    map_dir = r"/home/csgoserver/serverfiles/csgo/maps/"
    config_dir = r"/home/csgoserver/serverfiles/csgo/addons/sourcemod/configs/"
    
    surfmaps = fetchMaps(map_dir)
    surfmaps = CompareMapsToDatabase(surfmaps)

    print("Admin menu maplist maker")
    
    choice = input("Would you like to make a new map config? (y/n): ")
    if choice.lower() != "y":
        return
    
    print(f"Here are the current zoned maps in the directory:")
    printMaps(surfmaps)
        
    while True: #Ask's the user which maps they would like to exclude.
        choice = input("Exclude maps? (y/n): ")
        if choice.lower() != "y":
            while choice.lower() != "y" and choice.lower() != "n":
                choice = input("Error | must be y or n!\nExclude maps? (y/n): ")
            if choice.lower() == "n":
                break
                
        while choice.lower() == "y":
            print(f"Here are the current maps in the directory:")
            
            printMaps(surfmaps)
                
            while True:
                try:
                    exclude = int(input("Map #: "))
                    surfmaps.remove(surfmaps[exclude - 1])
                    break
                except ValueError:
                    print("Map was not found, please try again.")
            break
            
        
        printMaps(surfmaps)
    

    choice = input("Build menu.ini file? (y/n): ")  
    if choice.lower() == "y":
        printMaps(surfmaps)
        
        print("Done.")
        configBuilder(surfmaps, config_dir)
        input()
    

    
def printMaps(maps):
    i = 0
    for map in maps:
        i+=1
        print(f"{i}. {map}")


def configBuilder(maps, dir): # Builds maplist and writes to server.
    with open(dir + "adminmenu_maplist.ini", 'w') as f: #
        for map in maps:
            f.write(map + "\n")
            
            
def fetchMaps(dir):
    surfmaps = []
    maps = glob.glob(dir + "surf_*.bsp")
    
    for path in maps: # gets map name and creates a surf map list
        filename = path.replace(dir, "")
        filename = filename.replace(".bsp", "")
        #print(f"Found surf map: {filename}")
        surfmaps.append(filename)
        
    return surfmaps  
            
def CompareMapsToDatabase(maps):
    surfmaps = maps
    zonedmaps = []
    f = open("secrets.json")
    creds = json.load(f)
    cnx = mariadb.connect(
        user=creds['mysql']['user'],
        password=creds['mysql']['pass'],
        host=creds['mysql']['ip'],
        port=int(creds['mysql']['port']),
        database=creds['mysql']['database']
        )
    
    cur = cnx.cursor()
    cur.execute("SELECT `mapname` FROM `ck_maptier` WHERE `mapname` LIKE '%surf%' ORDER BY `mapname`")
    for maps in cur:
        if maps[0] in surfmaps:
            zonedmaps.append(maps[0])
    return zonedmaps    
            
            
if __name__ == '__main__':
    main()
