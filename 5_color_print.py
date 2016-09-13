# -*- coding: utf-8 -*-


"""
带颜色的输出
"""


class Colored(object):

    """Keep it simple, only use `red` and `green` color."""

    RED = '\033[91m'
    GREEN = '\033[92m'

    #: no color
    RESET = '\033[0m'

    def color_str(self, color, s):
        return '{}{}{}'.format(
            getattr(self, color),
            s,
            self.RESET
        )

    def red(self, s):
        return self.color_str('RED', s)

    def green(self, s):
        return self.color_str('GREEN', s)


if __name__ == '__main__':
    colored = Colored()

    msg = "hello world"
    print(colored.red(msg))
    print(colored.green(msg))
