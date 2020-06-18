import setuptools

# Used for installing test dependencies directly
tests_require = [
    'mock',
    'nose',
    'nose-timer',
    'flake8',
    'coverage',
    'pytest'
]

setuptools.setup(
    name="bayarea_relief",
    version="0.0.1",
    packages=setuptools.find_packages(exclude=['test', 'tests', 'test_*']),
    test_suite='nose.collector',
    tests_require=tests_require,
    install_requires=[
        "flask",
        "Flask-Migrate",
        "Flask-SQLAlchemy",
        "psycopg2-binary"
    ],
    # For installing test dependencies directly
    extras_require={'test': tests_require},
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'webserver=bayarea_relief.__main__:main',
            'migrate=bayarea_relief.manage:main',

        ]
    },
)
