import unittest
import slicer

class DICOMCheckDBTest(unittest.TestCase):
  def setUp(self):
    self.assertTrue(hasattr(slicer, 'modules'))
    self.assertTrue(hasattr(slicer.modules, 'dicomcheck'))

    self.slicerStartedUp = False
    self.db = None

    self.dicomCheckModule = slicer.modules.dicomcheck.widgetRepresentation().self()
    slicer.app.connect("startupCompleted()", self.onSlicerStartupComplete)
    # it might already have been triggered before connected to it
    if self.dicomCheckModule.dicomDatabase is None and slicer.dicomDatabase is not None:
      slicer.util.delayDisplay("Start up was completed with no signal? slicer database set, but not module")


  def onSlicerStartupComplete(self):
    slicer.util.delayDisplay('DICOMCheckDBTest: onSlicerStartupComplete')
    self.slicerStartedUp = True
    self.db = self.dicomCheckModule.dicomDatabase


  def runTest(self):
    self.setUp()
    flag = True

    flag = flag and self.test_DICOMDB()

    return flag

  def test_DICOMDB(self):
    slicer.util.delayDisplay('test_DICOMDB, start up = ' + str(self.slicerStartedUp) + "\nslicer db is none: " + str(slicer.dicomDatabase is None) + "\nmodule db is none: " + str(self.dicomCheckModule.dicomDatabase is None) + "\ntest db is none: " + str(self.db is None), 5000)
    self.assertTrue(self.slicerStartedUp)
    self.assertFalse(slicer.dicomDatabase is None)
    self.assertFalse(self.dicomCheckModule.dicomDatabase is None)
    self.assertFalse(self.db is None)
