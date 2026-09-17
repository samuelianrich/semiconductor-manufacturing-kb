"""Dimensional and physical invariants for the explicitly hypothetical examples."""
import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from content_checks import reviewed_module_errors

class FabExamples(unittest.TestCase):
    def test_resolution_and_focus_tradeoff(self):
        self.assertAlmostEqual(.35*193/1.35,50.0,places=1)
        self.assertAlmostEqual(1/1.5**2,.4444444444)
        self.assertLess(1/1.5**2,1/1.5)

    def test_etch_mask_budget(self):
        target_rate,selectivity,depth=100.,5.,200.
        time=depth/target_rate
        mask_loss=target_rate/selectivity*time
        self.assertEqual(mask_loss,40.)
        self.assertEqual(mask_loss*1.2,48.)
        self.assertEqual(10/.5,20.)

    def test_implant_current_charge_and_area_units(self):
        dose=1e-6*10/(1.602176634e-19*10)
        self.assertAlmostEqual(dose/1e12,6.241509,places=5)
        self.assertAlmostEqual(dose*10*1.602176634e-19,1e-5)

    def test_oxide_silicon_conservation(self):
        ratio=2.196/2.329*28.0855/60.0843
        self.assertAlmostEqual(ratio,.4407,places=4)
        oxide_nm=100
        consumed=oxide_nm*ratio
        self.assertAlmostEqual(consumed+oxide_nm*(1-ratio),oxide_nm)
        # Compare silicon atom amount per unit area on both sides.
        self.assertAlmostEqual(consumed*2.329/28.0855,oxide_nm*2.196/60.0843)

    def test_cmp_length_time_conversion(self):
        rate_m_s=1e-13*20000*.5
        rate_nm_min=rate_m_s*1e9*60
        self.assertAlmostEqual(rate_nm_min,60.)
        self.assertAlmostEqual(180/rate_nm_min,3.)

    def test_zero_detection_and_process_signal(self):
        miss=.99**100
        self.assertAlmostEqual(miss,.366,places=3)
        self.assertGreater(miss,.3)
        self.assertLess(.99**200,miss)
        self.assertGreater(107,100+3*2)
        self.assertLess(107,110)

    def test_reviewed_module_requires_owned_reviewed_content(self):
        mods=[dict(id='M39',path='39_history',status='reviewed')]
        self.assertTrue(reviewed_module_errors(mods,[]))
        self.assertTrue(reviewed_module_errors(mods,[dict(path='39_history/a.md',status='drafted')]))
        self.assertTrue(reviewed_module_errors(mods,[dict(path='39_history_extra/a.md',status='reviewed')]))
        self.assertFalse(reviewed_module_errors(mods,[dict(path='39_history/a.md',status='reviewed')]))

if __name__=='__main__':unittest.main()
