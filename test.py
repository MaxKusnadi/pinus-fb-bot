import unittest

# Model
from test_cases.models.user import TestUser
from test_cases.models.order import TestOrder
from test_cases.models.orderItem import TestOrderItem
from test_cases.models.event import TestEvent

# ModelMapper
from test_cases.modelMappers.user import (TestUserMapperCreate,
                                          TestUserMapperRead,
                                          TestUserMapperUpdate)
from test_cases.modelMappers.order import (TestOrderMapperCreate,
                                           TestOrderMapperRead,
                                           TestOrderMapperUpdate)
from test_cases.modelMappers.orderItem import (TestOrderItemCreate,
                                               TestOrderItemRead,
                                               TestOrderItemUpdate)
from test_cases.modelMappers.event import (TestEventMapperCreate,
                                           TestEventMapperRead,
                                           TestEventMapperUpdate)

if __name__ == '__main__':
    unittest.main()
