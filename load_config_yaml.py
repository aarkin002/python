import yaml

my_project = {
    'settings':
        ['__init__.py',
         'dev.py',
         'prod.py'],
    'mainapp':
        ['__init__.py',
         'models.py',
         'views.py',
         {'templates':
             {'mainapp':
                 ['base.html',
                  'index.html']}}],
    'authapp':
        ['__init__.py',
         'models.py',
         'views.py',
         {'templates':
             {'authapp':
                 ['base.html',
                  'index.html']}}]
}

with open('config.yaml', 'w') as f:
    yaml.dump(my_project, f, default_flow_style=False)
