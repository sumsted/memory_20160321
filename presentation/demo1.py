import ast


def examine(ast_body, class_name=None):
    for node in ast_body:
        if isinstance(node, ast.ClassDef):
            examine(node.body, node.name)
        elif isinstance(node, ast.FunctionDef):
            arguments = []
            for i, arg in enumerate(node.args.args):
                if arg.id != 'self':
                    arguments.append(arg.id)
            if class_name is None:
                print({'name': node.name, 'arguments': arguments})
            else:
                print({'class_name': class_name, 'name': node.name, 'arguments': arguments})


if __name__ == '__main__':
    ast_body = ast.parse(open('gopigo.py', 'r').read()).body
    examine(ast_body, None)
