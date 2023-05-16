# import theater_module
# theater_module.price(3)
# theater_module.price_morming(4)
# theater_module.price_soldier(5)

# 모듈 import 방법 1 
# import travel.th
# trip_to = travel.th.ThailandPackage()
# trip_to.detail()

# 모듈 import 방법 2
# from travel.th import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

from travel import *
# trip_to = vt.VietnamPackage()
# trip_to.detail()

# trip_to = th.ThailandPackage()
# trip_to.detail()

import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(th))

