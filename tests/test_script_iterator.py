
# This file is part of PyLabControl, software for laboratory equipment control for scientific experiments.
# Copyright (C) <2016>  Arthur Safira, Jan Gieseler, Aaron Kabcenell
#
#
# PyLabControl is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyLabControl is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyLabControl.  If not, see <http://www.gnu.org/licenses/>.


from unittest import TestCase

from PyLabControl.src.core.script_iterator import ScriptIterator
from PyLabControl.src.scripts.script_dummy import ScriptDummy
import inspect

class TestScriptIterator(TestCase):

    def test_loading_and_saving(self):


        path_to_script_file = inspect.getmodule(ScriptDummy).__file__.replace('.pyc', '.py')


        script_info = {'iter_script':
                           {'info': 'Enter docstring here',
                            'scripts': {'ScriptDummy':
                                            {
                                                'info': '\nExample Script that has all different types of parameters (integer, str, fload, point, list of parameters). Plots 1D and 2D data.\n    ',
                                                'settings': {'count': 3, 'name': 'this is a counter', 'wait_time': 0.1,
                                                             'point2': {'y': 0.1, 'x': 0.1}, 'tag': 'scriptdummy',
                                                             'path': '', 'save': False, 'plot_style': 'main'},
                                                'class': 'ScriptDummy',
                                                'filepath': path_to_script_file}},
                            'class': 'ScriptIterator',
                            'settings': {'script_order': {'ScriptDummy': 0}, 'iterator_type': 'Loop'},
                            'package': 'PyLabControl'}}

        si = ScriptIterator.create_dynamic_script_class(script_info['iter_script'], verbose=True)

        print(si)



    def test_get_script_iterator(self):
        # test get_script_iterator
        package = 'PyLabControl'
        package = 'b26_toolkit'

        script_iterator = ScriptIterator.get_script_iterator(package, verbose=False)
        print('script_iterator', script_iterator)


    def test_create_dynamic_script_class(self):


        from PyLabControl.src.scripts.script_dummy import ScriptDummy
        path_to_script_file = inspect.getmodule(ScriptDummy).__file__.replace('.pyc', '.py')



        package = 'PyLabControl' #
        iterator_type = 'Loop'  #

        package = 'b26_toolkit'  #
        iterator_type = 'Iter test'  #

        script_info = {'iter_script':
                           {'info': 'Enter docstring here',
                            'scripts': {'ScriptDummy':
                                {
                                    'info': '\nExample Script that has all different types of parameters (integer, str, fload, point, list of parameters). Plots 1D and 2D data.\n    ',
                                    'settings': {'count': 3, 'name': 'this is a counter', 'wait_time': 0.1,
                                                 'point2': {'y': 0.1, 'x': 0.1}, 'tag': 'scriptdummy',
                                                 'path': '', 'save': False, 'plot_style': 'main'},
                                    'class': 'ScriptDummy',
                                    'filepath': path_to_script_file}},
                            'class': 'ScriptIterator',
                            'settings': {'script_order': {'ScriptDummy': 0}, 'iterator_type': iterator_type},
                            'package': package}}

        si = ScriptIterator.create_dynamic_script_class(script_info['iter_script'], verbose=True)

        print('================================================================================')
        print(si)


    def test_XX(self):
        from importlib import import_module
        import_module('b26_toolkit.src.scripts')


