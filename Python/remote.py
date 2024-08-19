import time
import random


class Remote():

    def __init__(self,tv_status= "Closed", tv_vol = 0, channel_numbers = ["Now"], channel = "Now"):
        self.tv_status = tv_status
        self.tv_sound = tv_sound
        self.channel_numbers = channel_numbers
        self.channel = channel

    def tv_open(self):
        if self.tv_status == "Closed":
            self.tv_status = "Open"
            print("Tv is Opened")

        elif self.tv_status == "Open":
            self.tv_status = "Closed"
            print("Tv is Closed")

    def change_vol(self):
        while True:
            c = input("Increase Volume '>'\nDecrease Volume '<'\nPress 'q' to exit")

            if c == ">":
                if self.tv_sound != 31:
                    self.tv_sound += 1
                    print("Sound:",self.tv_sound)

            elif c == "<":
                if self.tv_sound != 0:
                    self.tv_sound -= 1
                    print("Sound:",self.tv_sound)
            else:
                break

    def ad_chan(self, yk):
        time.sleep(0.5)
        print("Channel Appended")
        self.channel_numbers.append(yk)

    def ran(self):

        ran = random.randint(1,len(self.channel_numbers)-1)
        self.channel = self.channel_numbers[rastgele]
        print("Current Channel {}".format(self.channel))

    def __len__(self):
        return len(self.channel_numbers)

    def __str__(self):
        return "Tv status: {}\nSound status: {}\nChannel Numbers: {}\nChannel: {}".format(self.tv_status,self.tv_sound,self.channel_numbers,self.channel)
remote = Remote()
print("""
1- Tv Open/Close

2- Sound Configuration

3- Add Channel

4- Find out the Channel List

5- Random Channel

6- Channel Info

Press 'q' to exit
""")

while True:
    i = input("Select your Process")

    if i == "q":
        print("Terminating the Program")
        break

    elif i == "1":
        remote.tv_open()

    elif i == "2":
        remote.change_vol()

    elif i == "3":
        channel_names = input("Enter the channels seperating with ','  ")

        channel_names = channel_names.split(",")

        for addings in channel_numbers:
            remote.ad_chan(addings)

    elif i == "4":

        print("Number of Channels", len(remote))

    elif i == "5":
        remote.ran()

    elif i == "6":
        print(remote)

    else:
        print("Invalid Process")
