from .context import CommandContext
import shlex

class MenuFlow(Exception):
    pass

class CommandStop(MenuFlow):
    pass

class ExitMenu(MenuFlow):
    pass

class CommandMenu:
    prompt = "%> "
    cmds = {}

    def __init__(self):
        self.commands = {}
        for name, item in type(self).cmds.items():
            self.commands[name] = item(self)

    def run(self, ctx):
        while True:
            cmd = input(self.prompt)
            args = shlex.split(cmd)
            cmdname = args[0]
            args = args[1:]
            if cmdname not in self.commands:
                print(f"{cmdname}: command not found")
                continue

            command = self.commands[cmdname]
            try:
                command.run(ctx, args)
            except CommandStop as e:
                if len(e.args):
                    print("Error:", *e.args)
                continue
            except ExitMenu as e:
                self.quit(ctx)
                raise

    def quit(self, ctx):
        pass

class Runner:
    def __init__(self):
        pass

    def run(self, initialmenu):
        self.ctx = CommandContext()
        stack = [initialmenu()]
        while len(stack):
            current = stack.pop()
            try:
                current.run(self.ctx)
            except ExitMenu as e:
                if len(e.args):
                    stack.append(current)
                    stack.append(e.args[0]())
