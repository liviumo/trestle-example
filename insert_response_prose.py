# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2023 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Script to insert response prose in control markdown files."""

import pathlib
from typing import List


def insert_text_in_file(file_path: pathlib.Path,  text: str) -> bool:
	r"""Insert text lines after all tags found in file.
	Return True on success, False tags not found.
	Text is a string with appropriate \n line endings.
    	"""
	if not file_path.exists():
		print(f'File not found: {file_path}')
		return False
	with file_path.open('w', encoding='utf-8') as f:
		f.writelines(text)
		return True


def set_status(file_path: pathlib.Path, nth_status: int, status: str) -> bool:
    """Set the implementation status for the nth entry in the file."""
    if not file_path.exists():
        print(f'File not found: {file_path}')
        return False
    with file_path.open('r', encoding='utf-8') as f:
        lines = f.readlines()
    nstatus = 0
    for ii, line in enumerate(lines):
        if line.find('#### Implementation Status:') >= 0:
            nstatus += 1
            if nstatus == nth_status:
                lines[ii] = f'#### Implementation Status: {status}'
                with file_path.open('w', encoding='utf-8') as f:
                    f.writelines(lines)
                return True
    return False


def insert_response_prose(ctrl_str: str, prose_str: str ):
	path_str = './md_ex-ssp/'+ctrl_str+'.md'
	file_path = pathlib.Path(path_str)
	with file_path.open('a', encoding='utf-8') as f:
		f.write(prose_str)
	return

if __name__ == '__main__':
	proses: List[str] = [
			["AC.2.1.10", "\n### EC-Pol-AC-Auth\nReq AC.2.1.10 is implemented properly using the AC and Auth procedure for EC-Pol-AC-Auth component\n" \
			"#### Implementation Status: implemented\n______________________________________________________________________\n"],
			['AC.2.1.10', '\n#### Cloud Storage\nReq AC.2.1.10 is implemented properly for Cloud Storage component.\n'\
			'#### Implementation Status: implemented\n______________________________________________________________________\n'],
			['AC.2.1.11', '\n### EC-Pol-AC-Auth\nReq AC.2.1.11  is implemented using the Access control and authentication procedure for EC-Pol-AC-Auth component\n'\
			'#### Implementation Status: implemented\n______________________________________________________________________\n'],
			['CM.8.2.2', '\n### Cloud Storage\nReq CM.8.2.2 is implemented using ITinv tool to maintain an accurate inventory of information for Cloud Storage component.\n'\
			'#### Implementation Status: implemented\n______________________________________________________________________\n'],
			['CP.9.1', '\n### CMS\nReq CP.9.1 is implemented using the Disaster Recovery procedure for the CMS component.\n'\
			'#### Implementation Status: implemented\n______________________________________________________________________\n']
		]

	ctrls: List[str] = ['AC.2.1.10', 'AC.2.1.11', 'AC.3.1.10', 'CM.8.2.2', 'CP.9.1', 'CP.9.2', 'IA.5.1.4']
	for ctrl in ctrls:
		prose_str = ''
		for prose in proses:
			#print("Ctrl:"+ctrl+" Prose:"+prose[0]+"\n")
			if ctrl == prose[0]:
				prose_str = prose_str + prose[1]
		if len(prose_str) > 0:
			insert_response_prose(ctrl, prose_str)
