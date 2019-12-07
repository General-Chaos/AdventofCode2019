import pytest
import mod3

def test_intersections():
    grid = mod3.WireGrid()
    grid.addwireinstructions(['R8','U5','L5','D3'])
    grid.addwireinstructions(['U7','R6','D4','L4'])
    assert mod3.getminimummanhatten(grid.getintersections()) == 6
    assert mod3.getminimumsteps(grid.getintersections()) == 30

def test_minima():
    grid = mod3.WireGrid()
    grid.addwireinstructions(['R75','D30','R83','U83','L12','D49','R71','U7','L72'])
    grid.addwireinstructions(['U62','R66','U55','R34','D71','R55','D58','R83'])
    assert mod3.getminimummanhatten(grid.getintersections()) == 159
    assert mod3.getminimumsteps(grid.getintersections()) == 610
