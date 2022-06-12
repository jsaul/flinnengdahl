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

#ifndef FLINNENGDAHL_H_INCLUDED
#define FLINNENGDAHL_H_INCLUDED

#include<string>
#include<vector>
#include<map>

namespace FlinnEngdahlGFZ {

typedef std::vector<std::string> StringVector;
typedef std::map<std::string, StringVector> StringVectorMap;

class FlinnEngdahl {
	public:
		FlinnEngdahl();

		bool read(const char *filename);

		void setCategory(const char *c);

		int number(double lat, double lon) const;

		const std::string& name(
			int num,
			const char *c=nullptr) const
		{
			return names.at(c ? c : category.c_str()).at(num-1);
		}

		const std::string& name(
			double lat, double lon,
			const char *c=nullptr) const
		{
			return name(number(lat, lon), c);
		}

	private:
		std::string category;
		StringVectorMap names;
};

} // namespace FlinnEngdahlGFZ

#endif
