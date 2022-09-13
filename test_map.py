from cppBase.cppMap import cppMap
from cppBase.cppMap import drawMap
from shapely.geometry import Point, Polygon

def main():
    p1 = (1, 0)
    p2 = (0, 2)
    p3 = (-1, 0)

    poli = Polygon([p1,p2,p3])

    mapota = cppMap(poli)

    drawMap(mapota)

    print("Hello World!")

if __name__ == "__main__":
    main()
