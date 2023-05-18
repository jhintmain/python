#from game.sound.echo import echo_test
from ..sound.echo import echo_test      # relative하게 접근하기

def render_test():
    print("render")
    echo_test()