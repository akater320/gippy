CC=g++
CFLAGS=-c -Wall -Wextra -fPIC -O3 -std=c++11 -DGDAL2 -I./ -I/usr/include/gdal

all: gippy

gippy: GeoAlgorithms.o GeoImage.o GeoRaster.o GeoResource.o GeoVectorResource.o gip.o
	$(CC) -shared GeoAlgorithms.o GeoImage.o GeoRaster.o GeoResource.o GeoVectorResource.o gip.o -L/usr/lib -lgdal -L./ -o gippyLib 

GeoAlgorithms.o: GeoAlgorithms.cpp
	$(CC) $(CFLAGS) GeoAlgorithms.cpp

GeoImage.o: GeoImage.cpp
	$(CC) $(CFLAGS) GeoImage.cpp

GeoRaster.o: GeoRaster.cpp
	$(CC) $(CFLAGS) GeoRaster.cpp

GeoResource.o: GeoResource.cpp
	$(CC) $(CFLAGS) GeoResource.cpp

GeoVectorResource.o: GeoVectorResource.cpp
	$(CC) $(CFLAGS) GeoVectorResource.cpp

gip.o: gip.cpp
	$(CC) $(CFLAGS) gip.cpp

clean:
	rm *o gippyLib
