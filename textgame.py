import time
# Global inventory list 

inventory = []

def remove(item):
    if item in inventory:
        inventory.remove(item)
        print(f"{item} has now been used.")
    else:
        print(f"This {item} does not exsist.")

def intro():
    print("\nWelcome to the magical mushroom search!")
    time.sleep(1)
    print("\nWhere you can talk to mushrooms like a crazy person and even become part of a mazzive mushroom soup!")
    time.sleep(2)
    
    print("\nYou open your eyes, your head aching slightly, Your bag empty next to you. You are surronded by tall trees unlike anything you've ever seen before.\n You get up confused but knowing that this isn't somwhere you can stay. You need to decide on where to go.\n There are 2 forks in the pathway you stand.The left seems to be very bright, a scent of newly cut grass blowing in.\n the right is slightly overgrown, the tall trees blocking the sunlight. A faint of food wafts from there.")
    time.sleep(1)
    path()
    
def path():
    choice = input("choose which way, right or left").lower()
    if choice == "right":
        print("\nYou want to go towards the food but the path looks too dangerous so you decide to see if there is anything interesting down the other path instead, you pick up your bag and head right.")
        time.sleep(3)
        right()
        
    elif choice == "left":
        print("\nThe path looks dangerous, but you decide to go that way anyway since you are starving.Before you forget you pick up your bag and leave.")
        time.sleep(3)
        left()
        
    else:
        print("\nAnd for those of you who are trying to find a secrect ending just stop trying already!\nYour're not gonna find one this early!")
        path()

def right():
    print("\nAs you walk down the path,you see a field of small pastel mushrooms,you wonder if they are safe to eat and decide they are good enhough as you are desperate for food.\nAs you walk closer you notice a tiny face on one of them and think your going crazy.\n you wonder if you should eat the mushroom or not, maybe even speak to it.")
    
    time.sleep(3)
    answer = input("\nchoose, eat or speak").lower()
    
    if answer == "eat":
        print("\nYou chose to eat the mushroom, as you swallow it you feel a tingling sensation then...") 
        
        time.sleep(3)
        
        print("\nfaint.\nAs you wake up. you realise you're back at the fork in the path.")
        intro()
        
    elif answer == "speak":
        print("\nYou start to speak to the mushroom, asking it for a way back home.\n Suddenly the mushroom opens its round eyes, it hops from your hand and begins to speak in a squeaky voice.\n 'Hello human, if you want to go back you must return back from where you came and turn left. \n However I can show you the magical heart of this forest if you desire as I can see you have much optimism in you.'\n You think on the mushrooms words... what shall you do? Go back or follow")
        
        choice = input("choose, back or follow").lower()
        
        if choice == 'back':
            print("\nYou say bye to the mushroom and make you're way back to the begining.")
            intro()
                
            
        elif choice == 'follow':
            print("\nThe mushroom smiles with joy and begins to run with it's little feet through the field,\n though it is small, it is very fast and soon you find yourself running to keep up with it.\n You run through series of fields and forests, finding the area changin the further you venture.\n The once brown tress with luscious grren leaves have turned a vibrant purple with pink petals growing instead.\n You find yourself slowing down at the splendor surronding you.\n The mushroom stops besides a large fern and beckons you forward, it walks through the fern and you follow....")
            
            time.sleep(4)
            village_end()
        
def village_end(): 
    
    print("\nYour mouth drops as you view the beutiful forest before you, pixies fly about, their golden wings fluttering in the warm sun.\n A crystal blue lake stands in the heart of the forest, pretty mermaids swim around in it,\n their multicoloured tails casting rainbows across the forest floor.\nSmall huts litter the area, painted in soft pastel hues.\n You have never seen anything this pretty, you know that this is your true home now...")
    
         
def left():
    print("\nYou walk through the overgrown grass, the dried grass crunching beneath your feet, the sounds echo around the forest, creating an eerie feeling.\n Suddenly the dark forest gives way to an open field, infront of you is an elf. trapped by a cage and surronded by nasty goblins.\n The goblins stare, red beady eyes pointed at you.\n They begin to surrond you sharp sticks raised to your face. The head goblin speaks, voice nasaly and cruel.\n 'What brings you here', you point to the mushroom stew, the goblin laughs and speaks again 'solve my riddles or you will be dinner'")
    
    time.sleep(4)
    quiz()

def quiz():
    score = 0
    
    print("\nThe mean goblins sneered, answer our riddles and we may let you go!")
    
    answer = input("\nWhen a goblin is hungry and wants somthing to munch, what do you think he will eat for lunch? ").lower()
    
    if answer == "soup" or answer == "goofy goblin":
        print("\nHow did you know!?")
        score = score + 10
    else:
        print("\nThe goblins laugh")
        
    answer = input("\nwhat has a pointy hat, sharp teeth and loves to cause mischief? ").lower()
    
    if answer == "a goblin" or answer == "goofy goblin":
        print("\nHow did you know!?")
        score = score + 10
    else:
        print("\nThe goblins laugh")
        
    answer = input("\nI'm stitched from the shadows, worn with glee, By creatures of night, where none can see.\n What am I? ").lower()
    
    if answer == "cloak" or answer == "goofy goblin":
        print("\nHow did you know!?")
        score = score + 10
    else:
        print("\nThe goblins laugh")
    
    if score  == 30:
        print("\nYou know too much,we need to move you to a more secure place!")
        
        time.sleep(2)
        secret_ending()
        
    else:
        print("\nyou are picked up by the horde of angry goblins who jeer at your stupidity. \n They tie you up and bring you to the boiling culdron of mushroom stew, without a second thought...\n they toss you in")
        
        time.sleep(3) 
        dream()
            
def secret_ending():
    print('\nThe goblins take you away,\n"We have to keep you secure otherwise you will escape!" \n will you ever be free?')
    time.sleep(3)
    print("Time passes slowly while you are trapped in the dark cave, The goblins guard your cell throughout the day, \n leaving you alone with nothing but the moonlight as company during the nights. The goblin guarding you leaves as the sun sets, accidently dropping the key close to your cell. The goblin runs off unaware. \n You have aquired cell key")
    
    inventory.append("cell key")
    
    for items in inventory:
        print("inventory:", items)
        
    time.sleep(2)
    
    print("You think about what to do with the key in your hand, if you try to escape now, there is a high chance you will be able to get out of the cage.\n After all your cell is unguarded and the darkness your ally, however you do not know this place and you can hear distant and erie noises from the dark all around you. \n Do you dare try your luck tonight or wait for another opportunity, be aware you may not have another one in time for whatever punishment they give you.")
    time.sleep(2)
    
    answer = input("choose, open cell or Wait").lower()
    
    if answer == "open cell":
        
        open_cell()
    
    else: 
        bad_end()
        
def bad_end():
    
    print ("You decide to stay since you don't want to get in trouble but you soon start to realise you had less time then you thought\n You stay in the cage for two more days before they move you to a different cage trapped along with lots of tiny mushrooms pleading not to be put in soup but the mean goblins just laugh and in the next few hours you were dropped into a boiling hot mushroom soup the worst kind.")
    time.sleep(3)
    print("you have been made into soup... \n you lose \nbut atleast you were yummy.")
    
    remove("cell key")
    
def open_cell():
    print("\n You open up the cell door and before the goblins see you, you make a run for it.\n Aftera while of running you take a rest on some rocks and look into your backpack for food.\n As you realise you have no food you see a tree with delicious looking apples on it as susspicious as it is you et a few and keep some in your bag\n A few minites later you go and keep running again and after a while you run into a fimmilliar place you realise you are 2 blocks away from you house.\n As you arrive you arrive back home the first thing you do is sit down and tell your family about your great adventures.")
    
def dream():
    
    print("\nThe goblins let go of your body, you scream as you begin to fall into the couldron, closing your eyes")
    time.sleep(1)
    
    print("\nAs you panic, wondering how to get out of this mess, waiting to feel the hot liquid of soup upon your skin,\n you feel a cold gust that makes you flinch. your eyes fly open and infront of you lays acres of fields. \n You look around confused,and after taking a moment to process what had happened in you dream you sigh with relief and say 'im glad that wasn't real' standing and stretching your body you see in the corner of your eye a little mushroom running away.")

   
intro()


