from __future__ import print_function

DEBUG = False

def dprint(*args,**kwargs):
    '''Debug print'''
    print(*args,**kwargs)

_blocked = False
def nodebug(name='dprint'):
    '''Decorator to remove all functions with name 'name' being a separate expressions'''
    def helper(f):      
        global _blocked
        if _blocked:
            return f

        import inspect, ast, sys

        source = inspect.getsource(f)        
        a = ast.parse(source) #get ast tree of f

        class Transformer(ast.NodeTransformer):
            '''Will delete all expressions containing 'name' functions at the top level'''
            def visit_Expr(self, node): #visit all expressions
                try:
                    if node.value.func.id == name: #if expression consists of function with name a
                        return None #delete it
                except(ValueError):
                    pass
                return node #return node unchanged
        transformer = Transformer()
        a_new = transformer.visit(a)
        f_new_compiled = compile(a_new,'<string>','exec')

        env = sys.modules[f.__module__].__dict__
        _blocked = True
        try:
            exec(f_new_compiled,env)
        finally:
            _blocked = False
        return env[f.__name__]         
    return helper


@nodebug('dprint')        
def f():
    dprint('f() started')
    print('Important output')
    dprint('f() ended')
    print('Important output2')


f()