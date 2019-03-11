"""
Test cases for the image set difference function.

The function works on all images depths. All images, both input and output, must
have the same depth.

Here is the list of legal operations :
     1 / 1 = 1
     8 / 8 = 8
    32 /32 =32
    
The result in output is the set difference. It means that if the pixel in the
first input image is strictly superior to the pixel in the second input image
the pixel in the output image is set to its value and 0 otherwise.

Python function:
    diff
    
C function:
    MB_Diff
"""

from mamba import *
import unittest
import random

class TestDiff(unittest.TestCase):

    def setUp(self):
        # Creating three images for each possible depth
        self.im1_1 = imageMb(1)
        self.im1_2 = imageMb(1)
        self.im1_3 = imageMb(1)
        self.im8_1 = imageMb(8)
        self.im8_2 = imageMb(8)
        self.im8_3 = imageMb(8)
        self.im32_1 = imageMb(32)
        self.im32_2 = imageMb(32)
        self.im32_3 = imageMb(32)
        self.im8s2_1 = imageMb(128,128,8)
        self.im8s2_2 = imageMb(128,128,8)
        self.im8s2_3 = imageMb(128,128,8)
        
    def tearDown(self):
        del(self.im1_1)
        del(self.im1_2)
        del(self.im1_3)
        del(self.im8_1)
        del(self.im8_2)
        del(self.im8_3)
        del(self.im32_1)
        del(self.im32_2)
        del(self.im32_3)
        del(self.im8s2_1)
        del(self.im8s2_2)
        del(self.im8s2_3)

    def testDepthAcceptation(self):
        """Tests that incorrect depth raises an exception"""
        #self.assertRaises(MambaError, diff, self.im1_3, self.im1_2, self.im1_1)
        self.assertRaises(MambaError, diff, self.im8_3, self.im1_2, self.im1_1)
        self.assertRaises(MambaError, diff, self.im32_3, self.im1_2, self.im1_1)
        self.assertRaises(MambaError, diff, self.im1_3, self.im8_2, self.im1_1)
        self.assertRaises(MambaError, diff, self.im8_3, self.im8_2, self.im1_1)
        self.assertRaises(MambaError, diff, self.im32_3, self.im8_2, self.im1_1)
        self.assertRaises(MambaError, diff, self.im1_3, self.im32_2, self.im1_1)
        self.assertRaises(MambaError, diff, self.im8_3, self.im32_2, self.im1_1)
        self.assertRaises(MambaError, diff, self.im32_3, self.im32_2, self.im1_1)
        self.assertRaises(MambaError, diff, self.im1_3, self.im1_2, self.im8_1)
        self.assertRaises(MambaError, diff, self.im8_3, self.im1_2, self.im8_1)
        self.assertRaises(MambaError, diff, self.im32_3, self.im1_2, self.im8_1)
        self.assertRaises(MambaError, diff, self.im1_3, self.im8_2, self.im8_1)
        #self.assertRaises(MambaError, diff, self.im8_3, self.im8_2, self.im8_1)
        self.assertRaises(MambaError, diff, self.im32_3, self.im8_2, self.im8_1)
        self.assertRaises(MambaError, diff, self.im1_3, self.im32_2, self.im8_1)
        self.assertRaises(MambaError, diff, self.im8_3, self.im32_2, self.im8_1)
        self.assertRaises(MambaError, diff, self.im32_3, self.im32_2, self.im8_1)
        self.assertRaises(MambaError, diff, self.im1_3, self.im1_2, self.im32_1)
        self.assertRaises(MambaError, diff, self.im8_3, self.im1_2, self.im32_1)
        self.assertRaises(MambaError, diff, self.im32_3, self.im1_2, self.im32_1)
        self.assertRaises(MambaError, diff, self.im1_3, self.im8_2, self.im32_1)
        self.assertRaises(MambaError, diff, self.im8_3, self.im8_2, self.im32_1)
        self.assertRaises(MambaError, diff, self.im32_3, self.im8_2, self.im32_1)
        self.assertRaises(MambaError, diff, self.im1_3, self.im32_2, self.im32_1)
        self.assertRaises(MambaError, diff, self.im8_3, self.im32_2, self.im32_1)
        #self.assertRaises(MambaError, diff, self.im32_3, self.im32_2, self.im32_1)

    def testSizeCheck(self):
        """Tests that different sizes raise an exception"""
        self.assertRaises(MambaError, diff, self.im8_3, self.im8_2, self.im8s2_1)
        self.assertRaises(MambaError, diff, self.im8_3, self.im8s2_2, self.im8_1)
        self.assertRaises(MambaError, diff, self.im8_3, self.im8s2_2, self.im8s2_1)
        self.assertRaises(MambaError, diff, self.im8s2_3, self.im8_2, self.im8_1)
        self.assertRaises(MambaError, diff, self.im8s2_3, self.im8_2, self.im8s2_1)
        self.assertRaises(MambaError, diff, self.im8s2_3, self.im8s2_2, self.im8_1)

    def testComputation_1(self):
        """Test the set difference computation on binary images"""
        (w,h) = self.im1_1.getSize()
        self.im1_1.reset()
        self.im1_2.reset()
        self.im1_3.reset()
        
        drawSquare(self.im1_1,[w//2,0,w-1,h//2-1],1)
        drawSquare(self.im1_3,[w//2,0,w-1,h//2-1],1)
        drawSquare(self.im1_1,[0,h//2,w//2-1,h-1],1)
        drawSquare(self.im1_2,[0,h//2,w//2-1,h-1],1)
        drawSquare(self.im1_2,[w//2,h//2,w-1,h-1],1)
        
        diff(self.im1_1, self.im1_2, self.im1_2)
        (x,y) = compare(self.im1_3, self.im1_2, self.im1_3)
        self.assertLess(x, 0)

    def testComputation_8(self):
        """Computes the result of a set difference on 8-bit images"""
        for i in range(100):
            self.im8_3.reset()
            v1 = random.randint(0, 255)
            v2 = random.randint(0, 255)
            self.im8_1.fill(v1)
            self.im8_2.fill(v2)
            diff(self.im8_1, self.im8_2, self.im8_3)
            if v1>v2:
                self.im8_2.fill(v1)
            else:
                self.im8_2.reset()
            (x,y) = compare(self.im8_3, self.im8_2, self.im8_3)
            self.assertLess(x, 0)

    def testComputation_32(self):
        """Computes the result of a set difference on 32-bit images"""
        for i in range(100):
            self.im32_3.reset()
            v1 = random.randint(1,500000)
            v2 = random.randint(1,500000)
            self.im32_1.fill(v1)
            self.im32_2.fill(v2)
            diff(self.im32_1, self.im32_2, self.im32_3)
            if v1>v2:
                self.im32_2.fill(v1)
            else:
                self.im32_2.fill(0)
            (x,y) = compare(self.im32_3, self.im32_2, self.im32_3)
            self.assertLess(x, 0)

