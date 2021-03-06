# Multi Operating System (mOS)
# Copyright (c) 2016, Intel Corporation.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

from mostests import *

logger = logging.getLogger()

class Basics(TestCase):
    require = ['copy_test']
    modules = ['lwkmem_access_test.ko']

    def test_memory(self):
        # Verify that copy_{to,from}_user works with LWK memory.
        yod(self, './copy_test', '-f')
