#%%
from AoC import AoC
session = AoC()


# %%
with open('inputs/input7.txt') as input_file:
    raw_logs = input_file.readlines()
    raw_logs = (line.strip() for line in raw_logs)


class File:
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = int(size)

    def __eq__(self, other):
        if other == None:
            return False
        return (self.name == other.name) & (self.parent == other.parent) 


class Directory(File):
    def __init__(self, name, parent = None):
        super().__init__(name, parent, size = 0)
        self.children = []

    def add_child(self, new_child):
        """adds object described by line to children"""
        # exit if child already exists, else create child entry
        if self.is_parent(new_child):
            return
        else:
            self.children.append(new_child)
#            print(f'added {new_child.name} to {self.name}')
    
    def get_total_size(self):
        total = 0
        for child in self.children:
            if isinstance(child, File):
                total += child.size
            elif isinstance(child, Directory):
                total += child.get_total_size()
        return total

    def get_matching_child(self, new_child):
        candidates = [child for child in self.children if new_child.__eq__(child)]
        if candidates:
            return candidates[0]
        else:
            return None

    def is_parent(self, child):
        return self.get_matching_child(child) is not None


class FileSystem:
    def __init__(self):
        self.home_directory = Directory('/')
        self.register = {'/':self.home_directory}
    
    def add_to_register(self, file):
        exists = any(file.__eq__(val) for key, val in self.register.items())
        if not exists:
            self.register[file.name] = file


class Session:
    def __init__(self, raw_logs):
        self.file_system = FileSystem()
        self.cwd = self.file_system.home_directory
        self.logs = raw_logs
        self.current_line = next(self.logs)

    def get_next_line(self):
        try:
            self.current_line = next(self.logs)
        except StopIteration:
            raise StopIteration

    def run(self):
        finished = False
        while not finished:
            try:
                if self.current_line.startswith('$'):
                    self.parse_command()
            except StopIteration:
                finished = True
        return self.file_system

    def parse_command(self):
        parameter = self.current_line.split(' ')[-1]
        if ' cd ' in self.current_line:
            self.change_directory(parameter)
            self.get_next_line()
        elif parameter == 'ls':
            self.parse_contents()

    def parse_contents(self):
        """reads until next $ line creating child files in cwd"""
        output_finished = False
        while not output_finished:
            self.get_next_line()
            if self.current_line.startswith('$'):
                output_finished = True
            else:
                child = self.parse_child(self.current_line)
                if not self.cwd.is_parent(child):
                    self.cwd.add_child(child)
                    self.file_system.add_to_register(child)

    def parse_child(self, line):
        line = line.split(' ')
        
        child_name = line[1]
        child_size = line[0]
        if child_size == 'dir':
            child = Directory(name = child_name, parent = self.cwd)
        else:
            child = File(name = child_name, parent = self.cwd, size = child_size)

        return child

    def change_directory(self, parameter):
        if parameter == '/':
            self.cwd = self.file_system.home_directory
        elif parameter == '..':
            if self.cwd.parent != None:
                self.cwd = self.cwd.parent
        else:
            child = self.parse_child('dir ' + parameter)
            if not self.cwd.is_parent(child):
                self.cwd.add_child(child)
                self.file_system.add_to_register(child)
            else:
                child = self.cwd.get_matching_child(child)
            self.cwd = child
#        print(f'Changed dir to {self.cwd.name}')


    def part_one(self):
        self.run()
        directories = [file.get_total_size() for name, file in self.file_system.register.items() if isinstance(file, Directory)]
        
        total = 0
        for dir in directories:
            size = dir.get_total_size()
            if size <= 100000:
                total += size
        
        print(total)

                
if __name__ == '__main__':
    console = Session(raw_logs)
    console.part_one()
# %%
