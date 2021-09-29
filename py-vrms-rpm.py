#     py-vrms-rpm: A program for analyzing and listing license files on RPM-based operating systems.
#     Copyright 2021 Christian Hollinger
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


import rpm
from termcolor import *


if __name__ == '__main__':

    # Number of packages by license type.
    foss = 0
    proprietary = 0
    mixed = 0
    total = 0

    # Open the list of licenses and strip newlines.
    license_file = open("license-list.txt")
    raw_licenses = license_file.readlines()
    licenses = [x[:-1] for x in raw_licenses]

    # Get all installed packages.
    ts = rpm.TransactionSet()
    db = ts.dbMatch()
    for header in db:
        total += 1
        color = 'red'
        package_license = header['license'].upper()

        for text in licenses:
            if package_license.__contains__(text):
                # If the package contains the text of a free license, display it in green.
                color = 'green'
                if package_license.__contains__("FIRMWARE"):
                    # However, is the package contains nonfree blobs, display it in yellow.
                    # TODO Add license/keyword list for proprietary licenses.
                    color = 'yellow'

        # Add to the totals based on license type.
        if color == 'red':
            proprietary += 1
        elif color == 'yellow':
            mixed += 1
        elif color == 'green':
            foss += 1

        cprint("%s %s: %s" % (header['name'], header['version'], header['license']), color)

    # Finally, display a summary of package data.
    print("\nOut of a total of %d packages..." % total)


    def get_percentage(value):
        """Simple method for calculating a percentage."""
        return (value * 100) / total


    cprint("-%d%s (%d) are free." % (get_percentage(foss).__round__(), "%", foss), 'green')
    cprint("-%d%s (%d) have nonfree parts." % (get_percentage(mixed).__round__(), "%", mixed), 'yellow')
    cprint("-%d%s (%d) are proprietary." % (get_percentage(proprietary).__round__(), "%", proprietary), 'red')
