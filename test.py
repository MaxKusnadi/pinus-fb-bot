import unittest

# Model
from test_cases.models.user import TestUser
from test_cases.models.order import TestOrder
from test_cases.models.event import TestEvent
from test_cases.models.songRequest import TestSongRequest

# ModelMapper
from test_cases.modelMappers.user import (TestUserMapperCreate,
                                          TestUserMapperRead,
                                          TestUserMapperUpdate)
from test_cases.modelMappers.order import (TestOrderMapperCreate,
                                           TestOrderMapperRead,
                                           TestOrderMapperUpdate)
from test_cases.modelMappers.event import (TestEventMapperCreate,
                                           TestEventMapperRead,
                                           TestEventMapperUpdate)
from test_cases.modelMappers.songRequest import (TestSongRequestMapperCreate,
                                                 TestSongRequestMapperRead)

if __name__ == '__main__':
    unittest.main()
