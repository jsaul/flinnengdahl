/***************************************************************************
 * Copyright (C) GFZ Potsdam                                               *
 * All rights reserved.                                                    *
 *                                                                         *
 * Author: Joachim Saul (saul@gfz-potsdam.de)                              *
 *                                                                         *
 * GNU Affero General Public License Usage                                 *
 * This file may be used under the terms of the GNU Affero                 *
 * Public License version 3.0 as published by the Free Software Foundation *
 * and appearing in the file LICENSE included in the packaging of this     *
 * file. Please review the following information to ensure the GNU Affero  *
 * Public License version 3.0 requirements will be met:                    *
 * https://www.gnu.org/licenses/agpl-3.0.html.                             *
 ***************************************************************************/

#include <iostream>
#include <fstream>
#include <exception>
#include <math.h>

#include "fe.h"

namespace FlinnEngdahlGFZ {

#include "fe-numbers.cpp"
#include "fe-names.cpp"


FlinnEngdahl::FlinnEngdahl()
	: category("") {
	names[""] = _names;
}

bool FlinnEngdahl::read(const char *filename)
{
	using namespace std;

	ifstream ifile(filename);

	if ( ! ifile.good()) {
		throw std::runtime_error(
			std::string("failed to open ")+filename);
//		return false;
	}

	while( ! ifile.eof()) {
		bool ignore = false;
		string cat, num;

		ifile >> num >> cat;
		if (num[0] == '#')
			ignore = true;
		if (num.empty())
			ignore = true;

		// getline is needed to continue with next line
		string line;
		getline(ifile, line);

		if (ignore)
			continue;

		size_t n = std::atoi(num.c_str());

		line.erase(0, line.find_first_not_of(" \n\r\t"));

		if (names.find(cat) == names.end())
			names[cat].reserve(1000);
		if (n > names[cat].size())
			names[cat].resize(n);
		names[cat][n-1] = line;
	}

	return true;
}


void FlinnEngdahl::setCategory(const char *c)
{
	if (names.find(c) == names.end())
		throw std::invalid_argument(
			std::string("invalid category: ")+c);
	
	category = c;
}


int FlinnEngdahl::number(double lat, double lon) const
{
	if (lat < -90)
		lat = -90;
	if (lat > 90)
		lat = 90;
	while (lon < -180)
		lon += 360;
	while (lon > 180)
		lon -= 360;

	int iLat = int(floor(lat));
	int iLon = int(floor(lon));
	int n = _numbers[iLat + 90][iLon + 180];
	return n;
}

} // namespace FlinnEngdahlGFZ
