import random

class Boss:

    def __init__(self, id, name, dir):
        self.name = name
        self.dir = dir
        self.id = id

    @classmethod
    def get_bosses(cls):

        boss_list = []

        f = open('data/bosses.txt', 'r')
        raw_data = f.read().split('\n')

        for boss in raw_data:
            boss_data = boss.split(', ')
            boss_id = boss_data[0]
            boss_name = boss_data[1]
            boss_dir = boss_data[2]
            new_boss = Boss(boss_id, boss_name, boss_dir)
            boss_list.append(new_boss)

        cls.all_bosses = boss_list

    @classmethod
    def ids_to_list(cls, idlist):

        boss_list = []

        f = open('data/bosses.txt', 'r')
        raw_data = f.read().split('\n')

        for boss in raw_data:
            boss_data = boss.split(', ')
            boss_id = boss_data[0]
            boss_name = boss_data[1]
            boss_dir = boss_data[2]
            if boss_id in idlist:
                new_boss = Boss(boss_id, boss_name, boss_dir)
                boss_list.append(new_boss)

        return boss_list

        

Boss.get_bosses()