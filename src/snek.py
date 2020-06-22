class Snek:
    snek = """\
      --..,_                     _,.--.
         `'.'.                .'`__ o  `;__.
            '.'.            .'.'`  '---'`  `
              '.`'--....--'`.'
                `'--....--'`
    """
    def get(self):
        return self.snek


def main():
    s = Snek()
    print(s.get())

