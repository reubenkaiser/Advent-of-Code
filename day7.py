#%%
from AoC import AoC
session = AoC()


# %%
with open('inputs/input7.txt') as input_file:
    raw_logs = input_file.readlines()
    raw_logs = (line.strip() for line in raw_logs)

class File:
    # List of all files created
    register = []

    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = int(size)
        File.register.append(self)

    def __eq__(self, other):
        if other == None:
            return False
        return (self.name == other.name) & (self.parent == other.parent)
    
    def to_string(self, depth = 0):
        return f'- {self.name} (file, size:{self.size})'

class Directory(File):
    """A file which has size 0 and can have children files"""
    def __init__(self, name, parent = None):
        super().__init__(name, parent, size = 0)
        self.children = []

    def add_child(self, new_child):
        """Adds new_child object to children"""
        self.children.append(new_child)
        #print(f'added {new_child.name} to {self.name}')
    
    def get_total_size(self):
        total = 0
        for child in self.children:
            if isinstance(child, Directory):
                total += child.get_total_size()
            elif isinstance(child, File):
                total += child.size
        return total

    def get_matching_child(self, line):
        name = line.split(' ')[1]

        candidates = [child for child in self.children if child.name == name]
        if candidates != []:
            return candidates[0]
        else:
            return None

    def has_child(self, line):
        return self.get_matching_child(line) is not None

    def to_string(self, depth = 0):
        tabs = '\t'*depth
        own_string = f'- {self.name} (dir)'
        for child in self.children:
            own_string += f'\n{tabs}\t{child.to_string(depth+1)}'
        return own_string
    
    def display(self):
        print(self.to_string())

class Session:
    def __init__(self, raw_logs):
        self.home_directory = Directory('/')
        self.cwd = self.home_directory
        self.logs = raw_logs
        self.current_line = next(self.logs)
        self.run()

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
            self.get_next_line() # loop through lines after ls command
            if self.current_line.startswith('$'): # finish loop when next command is reached
                output_finished = True
            elif not self.cwd.has_child(self.current_line): # if not already a child, add to children
                child = self.parse_file(self.current_line)
                self.cwd.add_child(child)

    def parse_file(self, line):
        """take text input from ls command and create directory or file"""
        line = line.split(' ')
        
        child_name = line[1]
        child_size = line[0]
        if child_size == 'dir':
            child = Directory(name = child_name, parent = self.cwd)
        else:
            child = File(name = child_name, parent = self.cwd, size = child_size)

        return child

    def change_directory(self, parameter):
        if parameter == '/': # make cwd the home directory
            self.cwd = self.home_directory
        elif parameter == '..': # make cwd the parent of cwd
            if self.cwd.parent != None:
                self.cwd = self.cwd.parent
        else: # move to child directory
            entry = 'dir ' + parameter
            self.add_child_to_cwd(entry)
        #print(f'Changed dir to {self.cwd.name}')

    def add_child_to_cwd(self, line):
        if not self.cwd.has_child(line):
            child = self.parse_file(line)
            self.cwd.add_child(child)
        else:
            child = self.cwd.get_matching_child(line)
        self.cwd = child

    def part_one(self):
        directories = [file for file in File.register if isinstance(file, Directory)]
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
