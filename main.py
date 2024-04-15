def define_env(env):
    @env.macro
    def include_file(filename):
        with open(filename, 'r') as file:
            return file.read()