import unittest
import functions.roomGenerator as roomGenerator
from functions.distanceBetweenPoints import distanceBetweenPoints 

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.max_x = 1000
        self.max_y = 500
        self.room_count = 10
        self.rooms = roomGenerator.roomRectGenerator(1000, 500, 10)
        self.room_points = roomGenerator.roomPoints(self.rooms)

    def test_room_generation_length(self):
        room_list = roomGenerator.roomRectGenerator(self.max_x, self.max_y, self.room_count)
        self.assertEqual(len(room_list), 10)
        room_list = roomGenerator.roomRectGenerator(self.max_x, self.max_y, self.room_count-3)
        self.assertEqual(len(room_list), 7)
        room_list = roomGenerator.roomRectGenerator(self.max_x, self.max_y, self.room_count-9)
        self.assertEqual(len(room_list), 1)

    def test_room_points_length(self):
        room_list = roomGenerator.roomRectGenerator(self.max_x, self.max_y, self.room_count)
        room_points = roomGenerator.roomPoints(room_list)

        self.assertEqual(len(room_points), len(room_list))
    
    def test_room_points_type(self):
        for point in self.room_points:
            self.assertIsInstance(point, tuple)
    
    def test_distance_between_poitns(self):
        self.assertEqual(distanceBetweenPoints((0,0),(0,2)), 2)
        self.assertEqual( round(distanceBetweenPoints((3,7), (5,3)), 5), 4.47214)

        # Testing if giving the function the same two points in different order keeps the equality
        self.assertEqual(distanceBetweenPoints(self.room_points[0], self.room_points[1]), distanceBetweenPoints(self.room_points[1], self.room_points[0]))
    
