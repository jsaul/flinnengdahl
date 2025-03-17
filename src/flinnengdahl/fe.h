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

#ifndef FLINNENGDAHL_H_INCLUDED
#define FLINNENGDAHL_H_INCLUDED

#include <string>
#include <map>

namespace RegionNaming {

// If the numbers are guaranteed to be consecutive, implementation as a simple list
// would be much more efficient. The map allows to add arbitrary 'local' numbers,
// which would be a deviation from the 'official' F-E numbering but which we will
// probably do at some point (e.g. western part of Dodecanese Islands).
typedef std::map<size_t, std::string> NamesByNumber;
typedef std::map<std::string, NamesByNumber> Container;

class FlinnEngdahl
{
	public:
		FlinnEngdahl();

		// Read a text file name with the region names
		bool read(const std::string &filename);

		// Select the output language
		void setLanguage(const std::string &language);

		// Obsolete; same as setLanguage
		void setCategory(const std::string &language);

		// If true, the first letter of each returned region name will be upper case
		void setUpperCase(bool choice=false);

		// Get the region number by latitude and longitude
		int number(double latitude, double longitude) const;

		// Get the region name by region number
		std::string name(int num) const;

		// Get the region name by latitude and longitude
		std::string name(double latitude, double longitude) const;

	private:
		std::string language;
		bool uppercase;
		Container names;
		Container::iterator namesIterator;
};


extern Container _names;


namespace Testing {

// Many runs over all categories and all regions. Only for speed testing.
void many(size_t runs=100000);

} // namespace Testing

} // namespace RegionNaming

#endif
