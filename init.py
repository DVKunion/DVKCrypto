# -*-coding: UTF-8 -*-
# Author DVK

import random
import sys,getopt

import server


class parameter:
    Sel = ["eb64=", "db64=" ,"eb32=" ,"db32=","eb16=","db16=","emd5=","dmd5=",
           "esha1=","dsha1=","esha224=","esha256=","esha384=","esha512=",
           "casa=","rot13=","path="]
    def get_parameter(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "he:d:p:m", self.Sel)
        except getopt.GetoptError:
            print '\033[1;31m[Error]: try python mian.py -h or --help to get help\033[0m'
            sys.exit(-1)
        for opt, arg in opts:

            server.do(self,opt,arg)
class start:
    para = parameter
    STARTNUM = random.randint(0, 10)
    COLOR = random.randint(31,37)
    STARTCODE = ["_              _               \n /_`   _  _  _  / | _  _  _   _/_  _ \n._//_//_//_'/  /_.'/_'/_ /_//_//_'/  \n     /                               \n",
".---..-..-..---..---..---.  .--. .---..---..----..--. .---..---.\n \ \ | || || |-'| |- | |-<  | \ \| |- | |  | || || \ \| |- | |-<    \n`---'`----'`-'  `---'`-'`-' `-'-'`---'`---'`----'`-'-'`---'`-'`-'   \n                                                                    \n",
"  ____                          ____                     _       \n / ___| _   _ _ __   ___ _ __  |  _ \  ___  ___ ___   __| | ___ _ __ \n \___ \| | | | '_ \ / _ \ '__| | | | |/ _ \/ __/ _ \ / _` |/ _ \ '__|\n  ___) | |_| | |_) |  __/ |    | |_| |  __/ (_| (_) | (_| |  __/ |   \n |____/ \__,_| .__/ \___|_|    |____/ \___|\___\___/ \__,_|\___|_|   \n             |_|                                                     \n",
"..######..##.....##.########..########.########.....########..########..######...#######..########..########.########.\n.##....##.##.....##.##.....##.##.......##.....##....##.....##.##.......##....##.##.....##.##.....##.##.......##.....## \n.##.......##.....##.##.....##.##.......##.....##....##.....##.##.......##.......##.....##.##.....##.##.......##.....## \n..######..##.....##.########..######...########.....##.....##.######...##.......##.....##.##.....##.######...########. \n.......##.##.....##.##........##.......##...##......##.....##.##.......##.......##.....##.##.....##.##.......##...##.. \n.##....##.##.....##.##........##.......##....##.....##.....##.##.......##....##.##.....##.##.....##.##.......##....##. \n..######...#######..##........########.##.....##....########..########..######...#######..########..########.##.....## \n",
" ___  __  __  ____  ____  ____    ____  ____  ___  _____  ____  ____  ____ \n / __)(  )(  )(  _ \( ___)(  _ \  (  _ \( ___)/ __)(  _  )(  _ \( ___)(  _ \ \n\__ \ )(__)(  )___/ )__)  )   /   )(_) ))__)( (__  )(_)(  )(_) ))__)  )   / \n(___/(______)(__)  (____)(_)\_)  (____/(____)\___)(_____)(____/(____)(_)\_) \n",
" ,---.                                   ,------.                         ,--.              \n '   .-' ,--.,--. ,---.  ,---. ,--.--.    |  .-.  \  ,---.  ,---. ,---.  ,-|  | ,---. ,--.--. \n`.  `-. |  ||  || .-. || .-. :|  .--'    |  |  \  :| .-. :| .--'| .-. |' .-. || .-. :|  .--' \n.-'    |'  ''  '| '-' '\   --.|  |       |  '--'  /\   --.\ `--.' '-' '\ `-' |\   --.|  |    \n`-----'  `----' |  |-'  `----'`--'       `-------'  `----' `---' `---'  `---'  `----'`--'    \n                `--'                                                                         \n",
".------..------..------..------..------.     .------..------..------..------..------..------..------.\n|S.--. ||U.--. ||P.--. ||E.--. ||R.--. |.-.  |D.--. ||E.--. ||C.--. ||O.--. ||D.--. ||E.--. ||R.--. | \n| :/\: || (\/) || :/\: || (\/) || :(): ((5)) | :/\: || (\/) || :/\: || :/\: || :/\: || (\/) || :(): | \n| :\/: || :\/: || (__) || :\/: || ()() |'-.-.| (__) || :\/: || :\/: || :\/: || (__) || :\/: || ()() | \n| '--'S|| '--'U|| '--'P|| '--'E|| '--'R| ((1)) '--'D|| '--'E|| '--'C|| '--'O|| '--'D|| '--'E|| '--'R| \n`------'`------'`------'`------'`------'  '-'`------'`------'`------'`------'`------'`------'`------' \n",
"                                                     d8b                             d8b                 \n                                                     88P                             88P                  \n                                                    d88                             d88                   \n .d888b,?88   d8P?88,.d88b, d8888b  88bd88b     d888888   d8888b d8888b d8888b  d888888   d8888b  88bd88b \n ?8b,   d88   88 `?88'  ?88d8b_,dP  88P'  `    d8P' ?88  d8b_,dPd8P' `Pd8P' ?88d8P' ?88  d8b_,dP  88P'  ` \n   `?8b ?8(  d88   88b  d8P88b     d88         88b  ,88b 88b    88b    88b  d8888b  ,88b 88b     d88      \n`?888P' `?88P'?8b  888888P'`?888P'd88'         `?88P'`88b`?888P'`?888P'`?8888P'`?88P'`88b`?888P'd88'      \n                   88P'                                                                                   \n                  d88                                                                                     \n                  ?8P         \n",
"  __                            __                               \n /                            |/  |                   |           \n(___       ___  ___  ___      |   | ___  ___  ___  ___| ___  ___  \n    )|   )|   )|___)|   )     |   )|___)|    |   )|   )|___)|   ) \n __/ |__/ |__/ |__  |         |__/ |__  |__  |__/ |__/ |__  |     \n          |                                                     \n",
"  __                   __                      \n  (_ `     _   _   _    ) ) _   _  _   _ ) _   _ \n.__) (_( )_) )_) )    /_/ )_) (_ (_) (_( )_) )  \n        (   (_           (_             (_      \n",
"  _, _,_ __, __, __,   __, __,  _,  _, __, __, __,\n (_  | | |_) |_  |_)   | \ |_  / ` / \ | \ |_  |_) \n , ) | | |   |   | \   |_/ |   \ , \ / |_/ |   | \ \n  ~  `~' ~   ~~~ ~ ~   ~   ~~~  ~   ~  ~   ~~~ ~ ~ \n",
]
    def __init__(self):
        self.prints(self.STARTCODE[self.STARTNUM],str(self.COLOR))
        self.para().get_parameter()

    def prints(self, text, color):
        start_line = '\033[1;'+ color + 'm'
        end_line = '\033[0m'
        print start_line+ text +' '+ end_line
