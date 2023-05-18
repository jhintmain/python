
# import game.sound.echo
# game.sound.echo.echo_test()

# from game.sound import echo
# echo.echo_test()

# from game.sound.echo import echo_test
# echo_test()


# game 디렉토리 하위 모듈을 접근하고 싶을때 __init__.py에 정의 한것만 참조가능하다
# __init__.py는 해당 디렉토리가 패키지 일부라는걸 알려주는 역할을 하는데, v3.3부터는 없어도 인식가능 . >> 하위 버전들을 위해 모듈 디렉토리는 __init__.py을 써주자
# import game
# game.sound.echo.echo_test()  # error

# from game.sound import *
# echo.echo_test() # error >> game.sound아래에  __init__.py에 선언되어있지않고 써서 그럼


from game.graphic.render import render_test
render_test()