# import unittest

# # Model
# from test_cases.models.user import TestUser
# from test_cases.models.order import TestOrder
# from test_cases.models.event import TestEvent

# # ModelMapper
# from test_cases.modelMappers.user import (TestUserMapperCreate,
#                                           TestUserMapperRead,
#                                           TestUserMapperUpdate)
# from test_cases.modelMappers.order import (TestOrderMapperCreate,
#                                            TestOrderMapperRead,
#                                            TestOrderMapperUpdate)
# from test_cases.modelMappers.event import (TestEventMapperCreate,
#                                            TestEventMapperRead,
#                                            TestEventMapperUpdate)

# if __name__ == '__main__':
#     unittest.main()

from bot.logic.shop import ShopLogic

s = ShopLogic()
print(s._process_quantity("aaa", "packetB"))
