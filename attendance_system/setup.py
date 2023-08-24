from setuptools import setup, find_packages
setup(
    name="attendance_system",
    version = "0.1",
    packages = find_packages(),
    install_requires = [
        'Django == 4.2.4',
        'django-filter ==23.2',
        'django-crispy-forms == 2.0',
    ],
    author = "Mfundo Monchwe",
    author_email = "diditmfundo@gmail.com",
    description = "simple attendance system which involves taking attendance and generating reports",
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.2.4',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)