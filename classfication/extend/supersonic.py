# SuperSonicAirplane 클래스 생성

from classfication.airplane import Airplane

class SuperSonicAirPlane(Airplane):
    #1번 - NORMAL, 2번 - SUPERSONIC
    # 상수 설정
    NORMAL = 1
    SUPERSONIC = 2
    #모드 - 멤버 변수
    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.NORMAL

    def fly(self):
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC :
            print("비행기가 초음속으로 비행합니다.")
        else:
            super().fly()

#sa = SuperSonicAirPlane()
#sa.take_off()
# sa.fly()
# sa.fly_mode = SuperSonicAirPlane.SUPERSONIC
# sa.fly()
# sa.land()