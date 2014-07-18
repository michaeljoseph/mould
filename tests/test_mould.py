from . import BaseTestCase

from mould import mould


class TestMould(BaseTestCase):

    def test_something(self):
        self.assertEquals(
            'Hello World!',
            mould(),
        )
