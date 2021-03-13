from boss import Boss
import random

class Preset:
    
    def __init__(self, name, boss_list):
        self.name = name
        self.boss_list = boss_list

    @classmethod
    def delete_preset(cls, line_number):

        # reads current file
        data = open('data/presets.txt', 'r').read().split('\n')
        new_data = []
        # creates a new list without the unwanted preset
        for x in range(0, len(data)):
            if x != line_number:
                new_data.append(data[x])
        # formats it into a string
        write_string = ''
        for x in range(0, len(new_data)-1):
            write_string += new_data[x] + '\n'
        write_string += new_data[len(new_data)-1]
        # replace the old file with the new one
        open('data/presets.txt', 'w').write(write_string)

    @classmethod
    def get_boss(cls, preset_id):
        boss_list = cls.preset_list[preset_id].boss_list
        index = random.randint(0, len(boss_list)-1)
        return boss_list[index]

    @classmethod
    def create_presets_list(cls):


        presets = []

        f = open('data/presets.txt', 'r')
        raw_data = f.read().split('\n')

        for preset in raw_data:
            preset_data = preset.split(', ')
            if len(preset_data) > 1:
                preset_name = preset_data[0]
                raw_ids = preset_data[1]
                boss_ids = []
                for x in range(0, len(raw_ids)):
                    if x % 2 == 0:
                        boss_ids.append(raw_ids[x] + raw_ids[x+1])
                new_preset = Preset(preset_name, Boss.ids_to_list(boss_ids))
                presets.append(new_preset)
        
        cls.preset_list = presets

    @classmethod
    def create_preset(cls, name, idlist):
        if len(name) < 1:
            return
        if len(idlist) < 2:
            return
        # new preset string
        preset_string = '\n'
        preset_string += name
        preset_string += ', '
        preset_string += idlist
        # read file
        f = open('data/presets.txt', 'a')
        f.write(preset_string)

    @classmethod
    def update_preset(cls, name, old_id, idlist):

        if len(idlist) < 2:
            return
        # new preset string
        preset_string = ''
        preset_string += name
        preset_string += ', '
        preset_string += idlist

        # reads current file
        data = open('data/presets.txt', 'r').read().split('\n')
        
        # changes the line
        data[old_id] = preset_string

        # converts list to string
        write_string = ''
        for x in range(0, len(data)-1):
            write_string += data[x] + '\n'
        write_string += data[len(data)-1]

        # writes back to the file
        open('data/presets.txt', 'w').write(write_string)

Preset.create_presets_list()