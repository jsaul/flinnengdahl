/***************************************************************************
 * Copyright (C) GFZ Helmholtz Centre for Geosciences                      *
 * All rights reserved.                                                    *
 *                                                                         *
 * Author: Joachim Saul (saul@gfz.de)                                      *
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
#include <algorithm>
#include <math.h>

#include "fe.h"

namespace RegionNaming {

#include "fe-numbers.cpp"
#include "fe-names.cpp"


FlinnEngdahl::FlinnEngdahl()
	: language("en"), uppercase(false), names(_names)
{
	setLanguage(language.c_str());
}


bool FlinnEngdahl::read(const std::string &filename)
{
	std::ifstream ifile(filename.c_str());

	if ( ! ifile.good()) {
		throw std::runtime_error("failed to open " + filename);
	}

	while ( ! ifile.eof()) {
		bool ignore = false;
		std::string lang, num;

		ifile >> num >> lang;
		if (num[0] == '#')
			ignore = true;
		if (num.empty())
			ignore = true;

		std::string line;
		std::getline(ifile, line);

		if (ignore)
			continue;

		size_t n = std::atoi(num.c_str());

		line.erase(0, line.find_first_not_of(" \n\r\t"));

		names[lang][n] = line;
	}

	return true;
}


void FlinnEngdahl::setLanguage(const std::string &lang)
{
	language = lang;
	namesIterator = names.find(language);
	if (namesIterator == names.end())
		throw std::invalid_argument("invalid language: " + language);
	
}


void FlinnEngdahl::setCategory(const std::string &lang)
{
	setLanguage(lang);
}


void FlinnEngdahl::setUpperCase(bool choice)
{
	uppercase = choice;
}


std::string FlinnEngdahl::name(int num) const
{
	const NamesByNumber &namesByNumber = namesIterator->second;
	auto it = namesByNumber.find(num);
	if (it == namesByNumber.end())
		throw std::invalid_argument("invalid region number: " + std::to_string(num));

	if (uppercase) {
		std::string result = namesByNumber.at(num);
		// convert first character to upper case
		std::transform(result.begin(), result.begin() + 1, result.begin(), toupper);
		return result;
	}

	return namesByNumber.at(num);
}


std::string FlinnEngdahl::name(double lat, double lon) const
{
	return name(number(lat, lon));
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


namespace Testing {

void many(size_t runs)
{
	FlinnEngdahl fe;

	for (auto& item: _names) {
		const std::string language(item.first);
		fe.setLanguage(language);
		for (auto& i: item.second) {
			for (size_t run=0; run < runs; run++) {
				fe.name(i.first);
			}
		}
	}
}

}

} // namespace RegionNaming
