python

from game.sound.echo import echo_test # 1) 함수 import
echo_test()

from game.sound import echo # 2) 함수가 들어있는 모듈 import
echo.echo_test()

import game.sound # 3) 함수가 들어있는 모듈이 들어있는 패키지 import
game.sound.echo.echo_test()

# import game.sound.echo.echo_test 처럼 사용하는 건 불가능하다.
# 패키지를 from절에, 파일이나 함수를 import절에 써야 한다.

# 만약 import game 같은 상위 패키지를 import 하면
# 바로 접근할 수 있는 game 디렉터리의 모듈이나 __init__.py에만 접근할 수 있다.
# 만약 __init__.py 파일을 지운 디렉터리에 from 문으로 패키지인 것처럼 접근하면 에러 난다.

# import * 처럼 쓰려면 해당 패키지의 __init__.py 파일에 특정 내용을 추가해야 한다.

from game.sound import * # 4) 패키지 내의 모든 모듈 import
echo.echo_test()

# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려준다.