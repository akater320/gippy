/*##############################################################################
#    GIPPY: Geospatial Image Processing library for Python
#
#    AUTHOR: Matthew Hanson
#    EMAIL:  matt.a.hanson@gmail.com
#
#    Copyright (C) 2015 Applied Geosolutions
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
##############################################################################*/

#include <gip/gip.h>
#include <ogrsf_frmts.h>

namespace gip {

    // Global options given initial values here
    std::string Options::_DefaultFormat("GTiff");
    float Options::_ChunkSize(128.0);
    int Options::_Verbose(1);
    int Options::_Cores(2);

	std::string Options::defaultformat() { return _DefaultFormat; }

	void Options::set_defaultformat(std::string str) { _DefaultFormat = str; }

	float Options::chunksize() { return _ChunkSize; }

	void Options::set_chunksize(float sz) { _ChunkSize = sz; }

	int Options::verbose() { return _Verbose; }

	void Options::set_verbose(int v) {
		_Verbose = v;
		if (v > 4) {
			// turn on GDAL output
			CPLPushErrorHandler(CPLDefaultErrorHandler);
		}
		else {
			CPLPushErrorHandler(CPLQuietErrorHandler);
		}
	}

	int Options::cores() { return _Cores; }

	void Options::set_cores(int n) { _Cores = n; }

    // Register file formats with GDAL and OGR
    void init() {
        GDALAllRegister();
        OGRRegisterAll();
        CPLPushErrorHandler(CPLQuietErrorHandler);
    }

#ifdef WIN32
	//The entry point that setuptools exports.
	void PyInit_libgip() {}
#endif // WIN32


} // namespace gip