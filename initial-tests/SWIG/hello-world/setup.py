from distutils.core import setup, Extension

pht_module = Extension('_Hello_world',
                        sources=['hello_world_wrap.cxx',
                                 'hello_world.cpp',
                                ],
                      )

setup(name = 'Hello_world',
        description = 'Simple swig pht from docs',
        ext_modules = [pht_module],
        py_modules = ['Hello_world'],
    )
