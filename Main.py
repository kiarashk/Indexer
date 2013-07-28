#!/usr/local/bin/python3

#   Created By Kiarash Kiani
#   kiarash.kiani.h@gmail.com
#   Tested in Mac OS X 10.8.3
#   Python 3 

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

def main():
	_path = input('Get URL for searching: ')
	x = get_ListOfFiles(_path)
	print(x)
	print("returnd")
	for i ,j in enumerate(x):
		print(i , j)

def get_countOfFiles(_path):
	count =0
	for i in os.listdir(path=_path):
		count = count + 1
	return count

def get_ListOfFiles(_path):
	array = []
	arrayFolder = []
	for item in os.listdir(path=_path):
		if os.path.isdir(_path + "/" + item):
			arrayFolder.append(_path + "/" + item)
		else:
			array.append(_path + "/" + item)
	if arrayFolder:
		for folder in arrayFolder:
			for item in get_ListOfFiles(folder):
				array.append(item)
		return array
	else:
		return array


if __name__ == "__main__" : main()
