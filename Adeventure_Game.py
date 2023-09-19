import time, datetime,random
def getsleeptime():
    time.sleep(10)
startlist = []
def openDoor():
    action = input(
        "After providing the password It's time to unlock the door. Choose 'open' to open the door. ").lower()
    if action == "open":
        print("Congratulations! Door opened, you have found the treasure. ")
    else:
        thankyou()
def findKnowledge(n):
    if n == 1:
        print("Question - New Year's Day (celebrated nationwide)")
        action = input("Answer is provide only date value as input to open the lock ex:1-10 numbers only ").lower()
        if action == "1":
            openDoor()
    elif n == 2:
        print("Question - Which day is National Read Across America Day")
        action = input("Answer is provide only date value as input to open the lock ex:1-10 numbers only ").lower()
        if action == "2":
            openDoor()
    elif n == 3:
        print("Question - Which day is National Boyfriend's Day")
        action = input("Answer is provide only date value as input to open the lock ex:1-10 numbers only ").lower()
        if action == "3":
            openDoor()
    elif n == 4:
        print("Question - When Mahavir Jayanti is Celebrated")
        action = input("Answer is provide only date value as input to open the lock ex:1-10 numbers only ").lower()
        if action == "4":
            openDoor()
    elif n == 5:
        print("Question - When Buddha Purnima is Celebrated")
        action = input("Answer is provide only date value as input to open the lock ex:1-10 numbers only ").lower()
        if action == "5":
            openDoor()
    elif n == 6:
        print("Question - When was the atomic bomb dropped on the Japanese city of Hiroshima.")
        action = input("Answer is provide only date value as input to open the lock ex:1-10 numbers only ").lower()
        if action == "6":
            openDoor()
    elif n == 7:
        print("Question - When is World Athletics Day")
        action = input("Answer is provide only date value as input to open the lock ex:1-10 numbers only ").lower()
        if action == "7":
            openDoor()
    elif n == 8:
        print("Question - When was World Red Cross Day")
        action = input("Answer is provide only date value as input to open the lock ex:1-10 numbers only ").lower()
        if action == "8":
            openDoor()
    elif n == 9:
        print("Question - When was Rabindranath Tagore Jayanti Celebrated")
        action = input("Answer is provide only date value as input to open the lock ex:1-10 numbers only ").lower()
        if action == "9":
            openDoor()
    elif n == 10:
        print("Question - When was Hrithik Roshan Birthday")
        action = input("Answer is provide only date value as input to open the lock ex:1-10 numbers only ").lower()
        if action == "10":
            openDoor()
def swimTime():
    print("Press any key for 10 times in 20 seconds to get near the door")
    start_time = time.time()
    while len(startlist) <= 9:
        line = input()
        if line:
            startlist.append(line)
        else:
            break
    elapsed_time = time.time() - start_time
    time_limit = 20
    startlist.clear()
    if elapsed_time <= time_limit:
        print("Before opening the door identify or guess the last number from the question mentioned?")
        n = random.randrange(1, 10)
        # action = input("You have entered the forest area. Please be careful. Type 'ok' to proceed.").lower()
        findKnowledge(n)
    else:
        getcave()
def getcave():
    print("Congrats,now you have entered the cave Search for the Key ")
    print("Searching ...")
    getsleeptime()
    print("Got the Key need to swim to get near the door. ")
    swimTime()
def findCaveentry():
    start_time = time.time()
    while len(startlist) <= 9:
        line = input()
        if line:
            startlist.append(line)
        else:
            break
    elapsed_time = time.time() - start_time
    time_limit = 20
    startlist.clear()
    if elapsed_time <= time_limit:
        getcave()
    else:
        goforest()
def setActiontocave(action):
    if action == "10:00":
        print("Now run towards cave entry type run for 10 times to the point else you will fail")
        findCaveentry()
def waitTomorrow():
    print("Wait tomorrow for the same time")
    getsleeptime()
    action = input("Please enter the time. ").lower()
    setActiontocave(action)
def goforest():
    print("")
    action = input("You have entered the forest area. Please be careful. Type 'ok' to proceed.").lower()
    if action == "ok":
        print("Hey I've found Anaconda, and it's attacking me. Please give me some time to kill it. ")
    getsleeptime()
    print("I Killed it,")
    key_forest = random.randrange(1, 10)
    print("Searching for the key.....")
    print("Got the key and now it's time to search for the Tree of Souls. ")
    print("Searching .....")
    getsleeptime()
    print(" I've found the tree; now it's time to hunt for the key. ")
    action = input("Did you get the key? Choose one: 'searching', 'yes', or 'no'. ").lower()
    if action == "yes":
        print("Great! The next level is to find the cave entry. ")
        print("Sharp 10 AM the shadow of the cave shows the cave entry")
        action = input("Please enter the time. ").lower()
        if action == "10:00":
            setActiontocave(action)
        else:
            waitTomorrow()
    elif action == "searching":
        print("ok")
        getsleeptime()
        print("I finally got the key and am now heading to the cave. ")
        action = input("Please enter the time. ").lower()
        if action == "10:00":
            setActiontocave(action)
        else:
            waitTomorrow()
    else:
        thankyou()
def takeboat():
    action = input("Are you interested in taking the boat? Please type 'yes' or 'no'. ").lower()
    if action == "yes":
        print("You have taken the boat and are traveling. Please wait for some time to reach the destination")
        getsleeptime()
        print("You reached the destination. ")
        print("The next level is entering into the forest: 'forest'. ")
        action = input("If you're interested, go to the forest now. Type 'yes' or 'no'. ").lower()
        if action == "yes":
            goforest()
        else:
            thankyou()
    else:
        thankyou()
def followrules():
    print("\n Follow the Levels to get the Treasure:\n Level-1 (Enter into the Boat)\n Level-2 (Enter into the forest)\n Level-3 (Fight with Anaconda)\n Level-4 (Search for Tree of Souls)\n Level-5 (Search for Key)\n Level-6 (Find the entry to the Cave)\n Level-7 (Enter into the cave to get the treasure)")
    action = input("If you want to play, type 'boat'; otherwise, to exit, type 'no'. ").lower()
    if action == "no":
        thankyou()
    if action == "boat":
        takeboat()
def thankyou():
    print("Thank you. Better luck next time.")
def main():
    print("Welcome to the Adventure Game to find the treasure!")
    print("\n Enter the game: Provide 'yes'; otherwise, provide 'no'. ")
    action = input("What would you like to do? ").lower()
    if action == "yes":
        print("It's good to see that you're playing!")
        followrules()
    else:
        thankyou()
if __name__ == "__main__":
    main()