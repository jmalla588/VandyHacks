from groupy import Group
from groupy import Member
from groupy import Bot
from operator import itemgetter
import pprint
import time
import groupy

# ID of the group that the bot is in
groupid = '26740408'

# Returns the proper group from all current groups
def getGroup(groups):
    for group in groups:
        if group.id == groupid:
            return group

    return None

group = getGroup(Group.list())
members = group.members()


myBots = Bot.list(); botExists = True;

for b in myBots:
    if b.name == 'DoorGuard':
        botExists = True;
        DoorGuard = b;
        break;

if not botExists:
    DoorGuard = Bot.create("DoorGuard", \
                     group, \
                     "http://my.xfinity.com/blogs/tv/files/2012/09/probst.jpg")


DoorGuard.post("Someone is at the front door!", picture_url=None)

print("DoorGuard has posted a warning message!")

#myBots[1].destroy();
