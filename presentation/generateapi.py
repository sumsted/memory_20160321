import os
import ast
import optparse

"""
Generate a server, client and test modules from a given module.
Usage: %prog [-v | --view] {python module}
"""


end_point = {'host': '0.0.0.0', 'port': 8080}

client_header = """import requests

host = 'http://%(host)s:%(port)d'


def g(action, *args):
    url = host+'/'+action
    for arg in args:
        url += '/'+str(arg)
    r = requests.get(url)
    return r.json()


"""

client_footer = """if __name__ == '__main__':
    pass
"""


def write_client(filename, functions):
    """ Create a client module from a list of function objects. """
    module_name = os.path.splitext(os.path.split(filename)[1])[0]
    with open(module_name + '_client' + '.py', "wt") as oout_file:
        oout_file.write(client_header % end_point)
        for function in functions:
            arguments = ''
            for i, arg in enumerate(function['arguments']):
                arguments += arg if i == 0 else ', ' + arg
            oout_file.write("def %s(%s):\n" % (function['name'], arguments))
            oout_file.write("    return g('%s', %s)['return_value']\n\n\n" % (function['name'], arguments))
        oout_file.write(client_footer)


server_header = """from bottle import get, route, request, response, run, post
import %(module_name)s


def handle_padded(handler):
    def decorator(**kwargs):
        r = handler(kwargs)
        try:
            callback = request.query.get('callback')
        except Exception, e:
            callback = None
        if callback is None:
            return r
        else:
            response.content_type = 'text/javascript'
            return "%%s(%%r);" %% (callback, r)
    return decorator

"""
server_route = """
@get('/%(function_name)s%(parameters)s')
@handle_padded
def %(function_name)s(kargs):
    r = {'return_value': %(module_name)s.%(function_name)s(%(arguments)s)}
    return r

"""
server_footer = """
run(host='%(host)s', port=%(port)d, debug=True)
"""


def write_server(filename, functions):
    """
    Create a server module from a list of function objects.
    The generated stub assumes all parameters are integers. Change it.
    """
    module_name = os.path.splitext(os.path.split(filename)[1])[0]
    with open(module_name + '_server' + '.py', "wt") as out_file:
        out_file.write(server_header % {'module_name': module_name})
        for function in functions:
            arguments = ''
            params = ''
            for i, arg in enumerate(function['arguments']):
                arguments += "int(kargs['%s'])" % arg if i == 0 else ", int(kargs['%s'])" % arg
                params += '/<%s>' % arg
            out_file.write(
                server_route % {'function_name': function['name'], 'parameters': params, 'module_name': module_name,
                                'arguments': arguments})
        out_file.write(server_footer % end_point)


test_header = """from unittest import TestCase, main
from %s_client import *


class Test%s(TestCase):
"""

test_footer = """if __name__ == '__main__':
    main()
"""


def write_tests(filename, functions):
    """
    Create a test module from a list of function objects.
    Plan to update the generated stub.
    """
    module_name = os.path.splitext(os.path.split(filename)[1])[0]
    upper_name = module_name[:1].upper() + module_name[1:]
    with open(module_name + '_test.py', "wt") as out_file:
        out_file.write(test_header % (module_name, upper_name))
        for function in functions:
            out_file.write("    def test_%s(self):\n" % function['name'].replace('.', '_'))
            for arg in function['arguments']:
                out_file.write("        %s = None\n" % arg)
            assert_line = "        self.assertEqual(%s(" % function['name']
            for i, arg in enumerate(function['arguments']):
                assert_line += arg if i == 0 else ', ' + arg
            assert_line += "), None)\n\n"
            out_file.write(assert_line)
        out_file.write(test_footer)


def find_functions(ast_body, prefix=None):
    """
    Loop through the ast nodes looking for functions and classes.
    Add functions to the returned list.
    Call this find_functions again if we find a class.
    """
    functions = []
    for node in ast_body:
        if isinstance(node, ast.FunctionDef):
            name = node.name if prefix is None else prefix + '_' + node.name
            arguments = []
            for i, arg in enumerate(node.args.args):
                if arg.id != 'self':
                    arguments.append(arg.id)
            functions.append({'name': name, 'arguments': arguments})
        elif isinstance(node, ast.ClassDef):
            name = node.name if prefix is None else prefix + '_' + node.name
            functions.extend(find_functions(node.body, name))
    return functions


def main(filename, view):
    """
    Given a module filename use ast to parse the source.
    Find all functions in ast nodes.
    Then if view is not set create test, client and server modules.
    """
    print(filename)
    with open(filename, "rt") as in_file:
        ast_body = ast.parse(in_file.read()).body
    functions = find_functions(ast_body)
    for function in functions:
        print('%s %s' % (function['name'], str(function['arguments'])))
    if view is False:
        write_tests(filename, functions)
        write_client(filename, functions)
        write_server(filename, functions)


if __name__ == '__main__':
    option_parser = optparse.OptionParser("Usage: %prog [-v | --view] {python module}")
    option_parser.add_option("-v", "--view", dest="view", default=None, type="string", help="display only")
    (options, args) = option_parser.parse_args()
    if len(args) != 1:
        option_parser.error("incorrect number of arguments, provide python module")
    main(args[0], options.view is not None)
    print('done')