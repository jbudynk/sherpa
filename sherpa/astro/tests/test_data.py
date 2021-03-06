# 
#  Copyright (C) 2007, 2015  Smithsonian Astrophysical Observatory
#
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import unittest
from sherpa.astro.data import DataPHA
from sherpa.utils import SherpaTestCase, test_data_missing
from sherpa.all import *
from sherpa.astro.all import *
import logging
logger = logging.getLogger('sherpa')

class test_filter_energy_grid(SherpaTestCase):

    _notice = numpy.ones(46, dtype=bool)
    _notice[44:46]=False

    _ignore = numpy.zeros(46, dtype=bool)
    _ignore[14:33]=True

    _emin = numpy.array([
        1.46000006e-03,   2.48199999e-01,   3.06600004e-01,   4.67200011e-01,
        5.69400012e-01,   6.42400026e-01,   7.00800002e-01,   7.44599998e-01,
        7.88399994e-01,   8.17600012e-01,   8.61400008e-01,   8.90600026e-01,
        9.49000001e-01,   9.92799997e-01,   1.03659999e+00,   1.09500003e+00,
        1.13880002e+00,   1.19719994e+00,   1.28480005e+00,   1.40160000e+00,
        1.47459996e+00,   1.60599995e+00,   1.69360006e+00,   1.81040001e+00,
        1.89800000e+00,   1.94180000e+00,   2.02940011e+00,   2.08780003e+00,
        2.19000006e+00,   2.27760005e+00,   2.39439988e+00,   2.58419991e+00,
        2.71560001e+00,   2.86159992e+00,   3.08060002e+00,   3.38720012e+00,
        3.56240010e+00,   3.79600000e+00,   4.02960014e+00,   4.24860001e+00,
        4.71579981e+00,   5.02239990e+00,   5.37279987e+00,   5.89839983e+00,
        6.57000017e+00,   9.86960030e+00], numpy.float)

    _emax = numpy.array([
        0.2482    ,   0.3066    ,   0.46720001,   0.56940001,   0.64240003,
        0.7008    ,   0.7446    ,   0.78839999,   0.81760001,   0.86140001,
        0.89060003,   0.949     ,   0.9928    ,   1.03659999,   1.09500003,
        1.13880002,   1.19719994,   1.28480005,   1.4016    ,   1.47459996,
        1.60599995,   1.69360006,   1.81040001,   1.898     ,   1.9418    ,
        2.02940011,   2.08780003,   2.19000006,   2.27760005,   2.39439988,
        2.58419991,   2.71560001,   2.86159992,   3.08060002,   3.38720012,
        3.5624001 ,   3.796     ,   4.02960014,   4.24860001,   4.71579981,
        5.0223999 ,   5.37279987,   5.89839983,   6.57000017,   9.8696003 ,
        14.95040035], numpy.float)

    def setUp(self):
        self.old_level = logger.getEffectiveLevel()
        logger.setLevel(logging.ERROR)
        self.pha = DataPHA('', numpy.arange(46, dtype=float)+1.,
                           numpy.zeros(46),
                           bin_lo = self._emin, bin_hi = self._emax )
        self.pha.units="energy"

    def tearDown(self):
        logger.setLevel(self.old_level)

    def test_notice(self):
        #clear mask
        self.pha.notice()        
        self.pha.notice(0.0, 6.0)
        #self.assertEqual(self._notice, self.pha.mask)
        assert (self._notice==numpy.asarray(self.pha.mask)).all()


    def test_ignore(self):
        #clear mask
        self.pha.notice()
        self.pha.ignore(0.0, 1.0)
        self.pha.ignore(3.0, 15.0)
        #self.assertEqual(self._ignore, self.pha.mask)
        assert (self._ignore==numpy.asarray(self.pha.mask)).all()



class test_filter_energy_grid_reversed(SherpaTestCase):

    _notice = numpy.zeros(204, dtype=bool)
    _notice[0:42]=True

    _ignore = numpy.ones(204, dtype=bool)
    _ignore[66:70]=False
    _ignore[0:17]=False

    _emin = numpy.array([
        2.39196181,  2.35973215,  2.34076023,  2.30973101,  2.2884388 ,
        2.25861454,  2.22371697,  2.20662117,  2.18140674,  2.14317489,
        2.12185216,  2.09055495,  2.06256914,  2.04509854,  2.02788448,
        2.00133967,  1.97772908,  1.96379483,  1.93868744,  1.91855776,
        1.89444292,  1.87936974,  1.85819471,  1.84568763,  1.82923627,
        1.78920078,  1.77360916,  1.76206875,  1.74499893,  1.73006463,
        1.70084822,  1.6883322 ,  1.67772949,  1.65171933,  1.63476169,
        1.59687376,  1.5745424 ,  1.55736887,  1.54051399,  1.52546024,
        1.50043869,  1.48890531,  1.47329199,  1.46072423,  1.44289041,
        1.43344045,  1.41616774,  1.40441585,  1.3979584 ,  1.38773119,
        1.37138033,  1.35170007,  1.33725214,  1.33249414,  1.31839108,
        1.30797839,  1.29657102,  1.28310275,  1.26550889,  1.25471842,
        1.24513853,  1.23672664,  1.22944438,  1.21509433,  1.21003771,
        1.20401597,  1.19705439,  1.18722582,  0.90194935,  0.89519638,
        0.88912934,  0.88492262,  0.87837797,  0.87366825,  0.8689999 ,
        0.86437255,  0.85693878,  0.84793305,  0.84404182,  0.83580172,
        0.82876647,  0.82395256,  0.81865752,  0.81185687,  0.80004948,
        0.79450154,  0.78852075,  0.77920061,  0.77340651,  0.76626247,
        0.76202762,  0.75783074,  0.75413191,  0.74727529,  0.74321008,
        0.73474538,  0.73166627,  0.72687   ,  0.71785438,  0.71488959,
        0.71068853,  0.70199603,  0.69832331,  0.69387686,  0.68788701,
        0.68354762,  0.67847627,  0.67117327,  0.66512167,  0.66175646,
        0.65620857,  0.6518243 ,  0.64605182,  0.64142239,  0.63754696,
        0.63128632,  0.62478495,  0.62006336,  0.61440694,  0.60915887,
        0.60591549,  0.60078359,  0.5938406 ,  0.59103745,  0.58488411,
        0.58124125,  0.57883304,  0.57406437,  0.57023615,  0.56442606,
        0.56041539,  0.55701393,  0.55392498,  0.55030966,  0.54346251,
        0.53728294,  0.53515989,  0.5291304 ,  0.52448714,  0.51990861,
        0.51589233,  0.50996011,  0.50509953,  0.49889025,  0.49512967,
        0.49003205,  0.48888513,  0.48524383,  0.48164544,  0.47720695,
        0.47283325,  0.46916556,  0.46660379,  0.46280268,  0.45925769,
        0.45514211,  0.45290345,  0.44987884,  0.44589564,  0.44333643,
        0.44099477,  0.43790293,  0.43446559,  0.43088335,  0.42605683,
        0.42131537,  0.41826019,  0.41506338,  0.41155648,  0.40895697,
        0.40502119,  0.40400422,  0.40164718,  0.39864835,  0.39584854,
        0.39389083,  0.39130434,  0.38890362,  0.38526753,  0.38292497,
        0.38075879,  0.37891743,  0.37648395,  0.37557775,  0.37347662,
        0.37154216,  0.36742872,  0.3641032 ,  0.36167556,  0.35983625,
        0.35634032,  0.35248783,  0.35085678,  0.34843227,  0.34669766,
        0.34418666,  0.33912122,  0.33720407,  0.33505177,  0.33279634,
        0.33081138,  0.32847831,  0.32592943,  0.3111549 ], numpy.float)

    _emax = numpy.array([
        3.06803656,  2.39196181,  2.35973215,  2.34076023,  2.30973101,
        2.2884388 ,  2.25861454,  2.22371697,  2.20662117,  2.18140674,
        2.14317489,  2.12185216,  2.09055495,  2.06256914,  2.04509854,
        2.02788448,  2.00133967,  1.97772908,  1.96379483,  1.93868744,
        1.91855776,  1.89444292,  1.87936974,  1.85819471,  1.84568763,
        1.82923627,  1.78920078,  1.77360916,  1.76206875,  1.74499893,
        1.73006463,  1.70084822,  1.6883322 ,  1.67772949,  1.65171933,
        1.63476169,  1.59687376,  1.5745424 ,  1.55736887,  1.54051399,
        1.52546024,  1.50043869,  1.48890531,  1.47329199,  1.46072423,
        1.44289041,  1.43344045,  1.41616774,  1.40441585,  1.3979584 ,
        1.38773119,  1.37138033,  1.35170007,  1.33725214,  1.33249414,
        1.31839108,  1.30797839,  1.29657102,  1.28310275,  1.26550889,
        1.25471842,  1.24513853,  1.23672664,  1.22944438,  1.21509433,
        1.21003771,  1.20401597,  1.19705439,  1.18722582,  0.90194935,
        0.89519638,  0.88912934,  0.88492262,  0.87837797,  0.87366825,
        0.8689999 ,  0.86437255,  0.85693878,  0.84793305,  0.84404182,
        0.83580172,  0.82876647,  0.82395256,  0.81865752,  0.81185687,
        0.80004948,  0.79450154,  0.78852075,  0.77920061,  0.77340651,
        0.76626247,  0.76202762,  0.75783074,  0.75413191,  0.74727529,
        0.74321008,  0.73474538,  0.73166627,  0.72687   ,  0.71785438,
        0.71488959,  0.71068853,  0.70199603,  0.69832331,  0.69387686,
        0.68788701,  0.68354762,  0.67847627,  0.67117327,  0.66512167,
        0.66175646,  0.65620857,  0.6518243 ,  0.64605182,  0.64142239,
        0.63754696,  0.63128632,  0.62478495,  0.62006336,  0.61440694,
        0.60915887,  0.60591549,  0.60078359,  0.5938406 ,  0.59103745,
        0.58488411,  0.58124125,  0.57883304,  0.57406437,  0.57023615,
        0.56442606,  0.56041539,  0.55701393,  0.55392498,  0.55030966,
        0.54346251,  0.53728294,  0.53515989,  0.5291304 ,  0.52448714,
        0.51990861,  0.51589233,  0.50996011,  0.50509953,  0.49889025,
        0.49512967,  0.49003205,  0.48888513,  0.48524383,  0.48164544,
        0.47720695,  0.47283325,  0.46916556,  0.46660379,  0.46280268,
        0.45925769,  0.45514211,  0.45290345,  0.44987884,  0.44589564,
        0.44333643,  0.44099477,  0.43790293,  0.43446559,  0.43088335,
        0.42605683,  0.42131537,  0.41826019,  0.41506338,  0.41155648,
        0.40895697,  0.40502119,  0.40400422,  0.40164718,  0.39864835,
        0.39584854,  0.39389083,  0.39130434,  0.38890362,  0.38526753,
        0.38292497,  0.38075879,  0.37891743,  0.37648395,  0.37557775,
        0.37347662,  0.37154216,  0.36742872,  0.3641032 ,  0.36167556,
        0.35983625,  0.35634032,  0.35248783,  0.35085678,  0.34843227,
        0.34669766,  0.34418666,  0.33912122,  0.33720407,  0.33505177,
        0.33279634,  0.33081138,  0.32847831,  0.32592943], numpy.float)


    def setUp(self):
        #self.old_level = logger.getEffectiveLevel()
        #logger.setLevel(logging.ERROR)
        self.pha = DataPHA('', numpy.arange(204, dtype=float)+1.,
                           numpy.zeros(204),
                           bin_lo = self._emin, bin_hi = self._emax )
        self.pha.units="energy"

    def tearDown(self):
        #logger.setLevel(self.old_level)
        pass

    def test_notice(self):
        #clear mask
        self.pha.notice()
        self.pha.notice(4., 8.3)
        assert (self._notice==numpy.asarray(self.pha.mask)).all()


    def test_ignore(self):
        #clear mask
        self.pha.notice()
        self.pha.ignore(10.3, 13.8)
        self.pha.ignore(4.6, 6.2)
        assert (self._ignore==numpy.asarray(self.pha.mask)).all()


class test_filter_wave_grid(SherpaTestCase):

    _notice = numpy.ones(16384, dtype=bool)
    _notice[8465:16384]=False

    _ignore = numpy.zeros(16384, dtype=bool)
    _ignore[14064:15984]=True

    _emin = numpy.arange(205.7875, 0.9875, -0.0125)

    _emax = _emin + 0.0125

    def setUp(self):
        self.old_level = logger.getEffectiveLevel()
        logger.setLevel(logging.ERROR)
        self.pha = DataPHA('', numpy.arange(16384, dtype=float)+1,
                           numpy.zeros(16384),
                           bin_lo = self._emin, bin_hi = self._emax )

    def tearDown(self):
        logger.setLevel(self.old_level)

    def test_notice(self):
        self.pha.units = 'wavelength'
        #clear mask
        self.pha.notice()
        self.pha.notice(100.0, 225.0)
        assert (self._notice==numpy.asarray(self.pha.mask)).all()

    def test_ignore(self):
        self.pha.units = 'wavelength'
        #clear mask
        self.pha.notice()
        self.pha.ignore(30.01, 225.0)
        self.pha.ignore(0.1, 6.0)        
        assert (self._ignore==numpy.asarray(self.pha.mask)).all()


if __name__ == '__main__':

    from sherpa.utils import SherpaTest
    import sherpa.astro
    SherpaTest(sherpa.astro).test()
