import unittest

# Model
from test_cases.models.user import TestUser
from test_cases.models.order import TestOrder
from test_cases.models.orderItem import TestOrderItem

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
if __name__ == '__main__':
    unittest.main()
