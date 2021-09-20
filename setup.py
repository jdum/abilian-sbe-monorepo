
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='abilian-sbe-next',
    version='0.1.0',
    python_requires='==3.*,>=3.8.0',
    author='Abilian SAS',
    author_email='contact@abilian.com',
    packages=['abilian-sbe-monorepo', 'abilian-sbe-monorepo.abilian', 'abilian-sbe-monorepo.abilian.cli', 'abilian-sbe-monorepo.abilian.core', 'abilian-sbe-monorepo.abilian.core.extensions', 'abilian-sbe-monorepo.abilian.core.models', 'abilian-sbe-monorepo.abilian.core.models.tests', 'abilian-sbe-monorepo.abilian.core.tests', 'abilian-sbe-monorepo.abilian.sbe', 'abilian-sbe-monorepo.abilian.sbe.apps', 'abilian-sbe-monorepo.abilian.sbe.apps.calendar', 'abilian-sbe-monorepo.abilian.sbe.apps.calendar.tests', 'abilian-sbe-monorepo.abilian.sbe.apps.communities', 'abilian-sbe-monorepo.abilian.sbe.apps.communities.tests', 'abilian-sbe-monorepo.abilian.sbe.apps.communities.views', 'abilian-sbe-monorepo.abilian.sbe.apps.documents', 'abilian-sbe-monorepo.abilian.sbe.apps.documents.cmis', 'abilian-sbe-monorepo.abilian.sbe.apps.documents.tests', 'abilian-sbe-monorepo.abilian.sbe.apps.documents.views', 'abilian-sbe-monorepo.abilian.sbe.apps.documents.webdav', 'abilian-sbe-monorepo.abilian.sbe.apps.forum', 'abilian-sbe-monorepo.abilian.sbe.apps.forum.tests', 'abilian-sbe-monorepo.abilian.sbe.apps.main', 'abilian-sbe-monorepo.abilian.sbe.apps.notifications', 'abilian-sbe-monorepo.abilian.sbe.apps.notifications.tasks', 'abilian-sbe-monorepo.abilian.sbe.apps.notifications.views', 'abilian-sbe-monorepo.abilian.sbe.apps.preferences', 'abilian-sbe-monorepo.abilian.sbe.apps.preferences.panels', 'abilian-sbe-monorepo.abilian.sbe.apps.social', 'abilian-sbe-monorepo.abilian.sbe.apps.social.tests', 'abilian-sbe-monorepo.abilian.sbe.apps.social.views', 'abilian-sbe-monorepo.abilian.sbe.apps.wall', 'abilian-sbe-monorepo.abilian.sbe.apps.wiki', 'abilian-sbe-monorepo.abilian.sbe.apps.wiki.tests', 'abilian-sbe-monorepo.abilian.services', 'abilian-sbe-monorepo.abilian.services.activity', 'abilian-sbe-monorepo.abilian.services.antivirus', 'abilian-sbe-monorepo.abilian.services.audit', 'abilian-sbe-monorepo.abilian.services.auth', 'abilian-sbe-monorepo.abilian.services.conversion', 'abilian-sbe-monorepo.abilian.services.image', 'abilian-sbe-monorepo.abilian.services.image.tests', 'abilian-sbe-monorepo.abilian.services.indexing', 'abilian-sbe-monorepo.abilian.services.preferences', 'abilian-sbe-monorepo.abilian.services.repository', 'abilian-sbe-monorepo.abilian.services.security', 'abilian-sbe-monorepo.abilian.services.settings', 'abilian-sbe-monorepo.abilian.services.tagging', 'abilian-sbe-monorepo.abilian.services.viewtracker', 'abilian-sbe-monorepo.abilian.services.vocabularies', 'abilian-sbe-monorepo.abilian.testing', 'abilian-sbe-monorepo.abilian.web', 'abilian-sbe-monorepo.abilian.web.admin', 'abilian-sbe-monorepo.abilian.web.admin.panels', 'abilian-sbe-monorepo.abilian.web.admin.panels.groups', 'abilian-sbe-monorepo.abilian.web.admin.panels.users', 'abilian-sbe-monorepo.abilian.web.assets', 'abilian-sbe-monorepo.abilian.web.attachments', 'abilian-sbe-monorepo.abilian.web.comments', 'abilian-sbe-monorepo.abilian.web.coreviews', 'abilian-sbe-monorepo.abilian.web.forms', 'abilian-sbe-monorepo.abilian.web.preferences', 'abilian-sbe-monorepo.abilian.web.search', 'abilian-sbe-monorepo.abilian.web.setupwizard', 'abilian-sbe-monorepo.abilian.web.tags', 'abilian-sbe-monorepo.abilian.web.tests', 'abilian-sbe-monorepo.abilian.web.tools', 'abilian-sbe-monorepo.abilian.web.uploads', 'abilian-sbe-monorepo.abilian.web.views', 'abilian-sbe-monorepo.extranet'],
    package_dir={"abilian-sbe-monorepo": "src"},
    package_data={"abilian-sbe-monorepo": ["instance/data/uploads/0/*.metadata", "instance/tmp/*.jpg", "instance/whoosh/default/*.toc"], "abilian-sbe-monorepo.abilian": ["translations/*.pot", "translations/de_DE/LC_MESSAGES/*.mo", "translations/de_DE/LC_MESSAGES/*.po", "translations/en/LC_MESSAGES/*.mo", "translations/en/LC_MESSAGES/*.po", "translations/es/LC_MESSAGES/*.mo", "translations/es/LC_MESSAGES/*.po", "translations/es_ES/LC_MESSAGES/*.mo", "translations/es_ES/LC_MESSAGES/*.po", "translations/fr/LC_MESSAGES/*.mo", "translations/fr/LC_MESSAGES/*.po", "translations/fr_FR/LC_MESSAGES/*.mo", "translations/fr_FR/LC_MESSAGES/*.po", "translations/id_ID/LC_MESSAGES/*.mo", "translations/id_ID/LC_MESSAGES/*.po", "translations/it_IT/LC_MESSAGES/*.mo", "translations/it_IT/LC_MESSAGES/*.po", "translations/nl/LC_MESSAGES/*.mo", "translations/nl/LC_MESSAGES/*.po", "translations/nl_NL/LC_MESSAGES/*.mo", "translations/nl_NL/LC_MESSAGES/*.po", "translations/pt_BR/LC_MESSAGES/*.mo", "translations/pt_BR/LC_MESSAGES/*.po", "translations/pt_PT/LC_MESSAGES/*.mo", "translations/pt_PT/LC_MESSAGES/*.po", "translations/tr_TR/LC_MESSAGES/*.mo", "translations/tr_TR/LC_MESSAGES/*.po", "translations/zh_CN/LC_MESSAGES/*.mo", "translations/zh_CN/LC_MESSAGES/*.po", "translations/zh_TW/LC_MESSAGES/*.mo", "translations/zh_TW/LC_MESSAGES/*.po"], "abilian-sbe-monorepo.abilian.core": ["*.yml"], "abilian-sbe-monorepo.abilian.sbe": ["static/csv/*.csv", "static/fileicons/*.png", "static/fileicons/*.txt", "static/icons/*.png", "static/images/*.jpg", "static/images/*.png", "static/img/*.jpg", "static/img/*.png", "static/js/*.js", "static/less/*.less", "static/less/*.txt", "static/less/modules/*.less", "static/moment/*.js", "static/pdfjs/*.css", "static/pdfjs/*.js", "static/pdfjs/*.txt", "static/pdfjs/cmaps/*.bcmap", "static/pdfjs/images/*.cur", "static/pdfjs/images/*.gif", "static/pdfjs/images/*.png", "static/pdfjs/images/*.svg", "static/pdfjs/locale/*.properties", "static/pdfjs/locale/en-US/*.properties", "static/pdfjs/locale/fr/*.properties", "static/vendor/*.js", "templates/*.html", "translations/*.pot", "translations/es/LC_MESSAGES/*.mo", "translations/es/LC_MESSAGES/*.po", "translations/fr/LC_MESSAGES/*.mo", "translations/fr/LC_MESSAGES/*.po", "translations/tr/LC_MESSAGES/*.mo", "translations/tr/LC_MESSAGES/*.po", "translations/zh/LC_MESSAGES/*.mo", "translations/zh/LC_MESSAGES/*.po"], "abilian-sbe-monorepo.abilian.sbe.apps.calendar": ["templates/calendar/*.html"], "abilian-sbe-monorepo.abilian.sbe.apps.communities": ["templates/community/*.html"], "abilian-sbe-monorepo.abilian.sbe.apps.communities.views": ["data/*.png"], "abilian-sbe-monorepo.abilian.sbe.apps.documents": ["templates/cmis/*.xml", "templates/documents/*.html", "templates/documents/*.txt"], "abilian-sbe-monorepo.abilian.sbe.apps.documents.tests": ["data/*.xml", "data/dummy_files/*.bin", "data/dummy_files/*.jpg", "data/dummy_files/*.pdf", "data/dummy_files/*.txt", "data/dummy_files/*.zip"], "abilian-sbe-monorepo.abilian.sbe.apps.forum": ["templates/forum/*.html", "templates/forum/mail/*.html"], "abilian-sbe-monorepo.abilian.sbe.apps.forum.tests": ["data/*.email"], "abilian-sbe-monorepo.abilian.sbe.apps.notifications": ["templates/notifications/*.css", "templates/notifications/*.html"], "abilian-sbe-monorepo.abilian.sbe.apps.preferences": ["templates/preferences/*.html"], "abilian-sbe-monorepo.abilian.sbe.apps.social": ["templates/social/*.html", "templates/social/mail/*.txt"], "abilian-sbe-monorepo.abilian.sbe.apps.wall": ["templates/wall/*.html"], "abilian-sbe-monorepo.abilian.sbe.apps.wiki": ["data/*.txt", "templates/wiki/*.html"], "abilian-sbe-monorepo.abilian.services": ["sandbox/*.txt"], "abilian-sbe-monorepo.abilian.services.auth": ["templates/login/*.html", "templates/login/email/*.txt"], "abilian-sbe-monorepo.abilian.services.conversion": ["dummy_files/*.doc", "dummy_files/*.docx", "dummy_files/*.jpg", "dummy_files/*.odt", "dummy_files/*.pdf", "dummy_files/*.xls"], "abilian-sbe-monorepo.abilian.services.image.tests": ["*.jpg"], "abilian-sbe-monorepo.abilian.services.vocabularies": ["templates/admin/*.html", "templates/admin/macros/*.html"], "abilian-sbe-monorepo.abilian.web": ["resources/bootbox/*.js", "resources/bootstrap-datepicker/css/*.css", "resources/bootstrap-datepicker/js/*.js", "resources/bootstrap-datepicker/js/locales/*.js", "resources/bootstrap-datepicker/less/*.less", "resources/bootstrap-switch/*.js", "resources/bootstrap-switch/less/bootstrap3/*.less", "resources/bootstrap-timepicker/css/*.css", "resources/bootstrap-timepicker/js/*.js", "resources/bootstrap-timepicker/less/*.less", "resources/bootstrap/fonts/*.eot", "resources/bootstrap/fonts/*.svg", "resources/bootstrap/fonts/*.ttf", "resources/bootstrap/fonts/*.woff", "resources/bootstrap/fonts/*.woff2", "resources/bootstrap/js/*.js", "resources/bootstrap/less/*.json", "resources/bootstrap/less/*.less", "resources/bootstrap/less/mixins/*.less", "resources/ckeditor/*.css", "resources/ckeditor/*.js", "resources/ckeditor/*.md", "resources/ckeditor/adapters/*.js", "resources/ckeditor/lang/*.js", "resources/ckeditor/plugins/*.png", "resources/ckeditor/plugins/a11yhelp/dialogs/*.js", "resources/ckeditor/plugins/a11yhelp/dialogs/lang/*.js", "resources/ckeditor/plugins/a11yhelp/dialogs/lang/*.txt", "resources/ckeditor/plugins/about/dialogs/*.js", "resources/ckeditor/plugins/about/dialogs/*.png", "resources/ckeditor/plugins/about/dialogs/hidpi/*.png", "resources/ckeditor/plugins/autolink/*.js", "resources/ckeditor/plugins/bootstrapVisibility/*.js", "resources/ckeditor/plugins/bootstrapVisibility/*.md", "resources/ckeditor/plugins/bootstrapVisibility/*.txt", "resources/ckeditor/plugins/bootstrapVisibility/lang/*.js", "resources/ckeditor/plugins/clipboard/dialogs/*.js", "resources/ckeditor/plugins/colordialog/dialogs/*.js", "resources/ckeditor/plugins/dialog/*.js", "resources/ckeditor/plugins/div/dialogs/*.js", "resources/ckeditor/plugins/find/dialogs/*.js", "resources/ckeditor/plugins/flash/dialogs/*.js", "resources/ckeditor/plugins/flash/images/*.png", "resources/ckeditor/plugins/forms/dialogs/*.js", "resources/ckeditor/plugins/forms/images/*.gif", "resources/ckeditor/plugins/iframe/dialogs/*.js", "resources/ckeditor/plugins/iframe/images/*.png", "resources/ckeditor/plugins/image/dialogs/*.js", "resources/ckeditor/plugins/image/images/*.png", "resources/ckeditor/plugins/link/dialogs/*.js", "resources/ckeditor/plugins/link/images/*.png", "resources/ckeditor/plugins/link/images/hidpi/*.png", "resources/ckeditor/plugins/liststyle/dialogs/*.js", "resources/ckeditor/plugins/magicline/images/*.png", "resources/ckeditor/plugins/magicline/images/hidpi/*.png", "resources/ckeditor/plugins/pagebreak/images/*.gif", "resources/ckeditor/plugins/pastefromword/filter/*.js", "resources/ckeditor/plugins/preview/*.html", "resources/ckeditor/plugins/scayt/*.md", "resources/ckeditor/plugins/scayt/dialogs/*.css", "resources/ckeditor/plugins/scayt/dialogs/*.js", "resources/ckeditor/plugins/showblocks/images/*.png", "resources/ckeditor/plugins/smiley/dialogs/*.js", "resources/ckeditor/plugins/smiley/images/*.gif", "resources/ckeditor/plugins/smiley/images/*.png", "resources/ckeditor/plugins/specialchar/dialogs/*.js", "resources/ckeditor/plugins/specialchar/dialogs/lang/*.js", "resources/ckeditor/plugins/specialchar/dialogs/lang/*.txt", "resources/ckeditor/plugins/table/dialogs/*.js", "resources/ckeditor/plugins/tabletools/dialogs/*.js", "resources/ckeditor/plugins/templates/dialogs/*.css", "resources/ckeditor/plugins/templates/dialogs/*.js", "resources/ckeditor/plugins/templates/templates/*.js", "resources/ckeditor/plugins/templates/templates/images/*.gif", "resources/ckeditor/plugins/wsc/*.md", "resources/ckeditor/plugins/wsc/dialogs/*.css", "resources/ckeditor/plugins/wsc/dialogs/*.html", "resources/ckeditor/plugins/wsc/dialogs/*.js", "resources/ckeditor/samples/*.html", "resources/ckeditor/samples/css/*.css", "resources/ckeditor/samples/img/*.png", "resources/ckeditor/samples/js/*.js", "resources/ckeditor/samples/old/*.css", "resources/ckeditor/samples/old/*.html", "resources/ckeditor/samples/old/*.js", "resources/ckeditor/samples/old/*.php", "resources/ckeditor/samples/old/assets/*.jpg", "resources/ckeditor/samples/old/assets/*.php", "resources/ckeditor/samples/old/assets/inlineall/*.png", "resources/ckeditor/samples/old/assets/outputxhtml/*.css", "resources/ckeditor/samples/old/assets/uilanguages/*.js", "resources/ckeditor/samples/old/dialog/*.html", "resources/ckeditor/samples/old/dialog/assets/*.js", "resources/ckeditor/samples/old/enterkey/*.html", "resources/ckeditor/samples/old/htmlwriter/*.html", "resources/ckeditor/samples/old/htmlwriter/assets/outputforflash/*.fla", "resources/ckeditor/samples/old/htmlwriter/assets/outputforflash/*.js", "resources/ckeditor/samples/old/htmlwriter/assets/outputforflash/*.swf", "resources/ckeditor/samples/old/magicline/*.html", "resources/ckeditor/samples/old/toolbar/*.html", "resources/ckeditor/samples/old/wysiwygarea/*.html", "resources/ckeditor/samples/toolbarconfigurator/*.html", "resources/ckeditor/samples/toolbarconfigurator/css/*.css", "resources/ckeditor/samples/toolbarconfigurator/font/*.eot", "resources/ckeditor/samples/toolbarconfigurator/font/*.json", "resources/ckeditor/samples/toolbarconfigurator/font/*.svg", "resources/ckeditor/samples/toolbarconfigurator/font/*.ttf", "resources/ckeditor/samples/toolbarconfigurator/font/*.txt", "resources/ckeditor/samples/toolbarconfigurator/font/*.woff", "resources/ckeditor/samples/toolbarconfigurator/js/*.js", "resources/ckeditor/samples/toolbarconfigurator/lib/codemirror/*.css", "resources/ckeditor/samples/toolbarconfigurator/lib/codemirror/*.js", "resources/ckeditor/skins/moono/*.css", "resources/ckeditor/skins/moono/*.md", "resources/ckeditor/skins/moono/*.png", "resources/ckeditor/skins/moono/images/*.gif", "resources/ckeditor/skins/moono/images/*.png", "resources/ckeditor/skins/moono/images/hidpi/*.png", "resources/datatables/css/*.css", "resources/datatables/images/*.ico", "resources/datatables/images/*.png", "resources/datatables/images/*.psd", "resources/datatables/js/*.js", "resources/fileapi/*.js", "resources/fileapi/*.swf", "resources/fileapi/plugins/*.js", "resources/font-awesome/css/*.css", "resources/font-awesome/fonts/*.eot", "resources/font-awesome/fonts/*.otf", "resources/font-awesome/fonts/*.svg", "resources/font-awesome/fonts/*.ttf", "resources/font-awesome/fonts/*.woff", "resources/font-awesome/fonts/*.woff2", "resources/font-awesome/less/*.less", "resources/font-awesome/scss/*.scss", "resources/highlightjs/*.css", "resources/highlightjs/*.js", "resources/img/*.png", "resources/jquery/js/*.js", "resources/js/*.js", "resources/js/widgets/*.js", "resources/less/*.less", "resources/nvd3/*.css", "resources/nvd3/*.js", "resources/nvd3/*.txt", "resources/requirejs/*.js", "resources/select2/*.css", "resources/select2/*.gif", "resources/select2/*.js", "resources/select2/*.json", "resources/select2/*.md", "resources/select2/*.png", "resources/select2/*.sh", "resources/select2/*.template", "resources/typeahead/*.css", "resources/typeahead/*.js", "resources/typeahead/*.less", "templates/*.html", "templates/*.js", "templates/debug_panels/*.html", "templates/default/*.html", "templates/default/*.svg", "templates/macros/*.html", "templates/preferences/*.html", "templates/widgets/*.html"], "abilian-sbe-monorepo.abilian.web.admin": ["templates/admin/*.html"], "abilian-sbe-monorepo.abilian.web.preferences": ["tests/*.png"], "abilian-sbe-monorepo.abilian.web.search": ["templates/search/*.html"], "abilian-sbe-monorepo.abilian.web.setupwizard": ["templates/setupwizard/*.html"], "abilian-sbe-monorepo.abilian.web.tags": ["templates/admin/*.html"]},
    install_requires=['alembic>=0.9', 'bcrypt', 'bleach>=2', 'celery==4.*,>=4.0.0', 'chardet', 'clamd', 'closure==20161201', 'cssmin', 'deprecated', 'devtools', 'flask==1.*,>=1.0.0', 'flask-assets>=0.12', 'flask-babel<2,>=0.11', 'flask-env', 'flask-login>=0.4', 'flask-mail>=0.9.1', 'flask-migrate>=2.0', 'flask-sqlalchemy<=2.1', 'flask-talisman>=0.6', 'flask-wtf<0.13,>=0.12', 'gunicorn', 'html2text==2020.*,>=2020.1.16', 'hyperlink', 'importlib-resources==5.*,>=5.2.2', 'itsdangerous<2', 'jinja2<3', 'jsmin', 'langid>=1.1', 'lxml', 'markdown==3.*,>=3.0.0', 'markupsafe>=0.21', 'openpyxl==2.*,>=2.3.0', 'pandas>=0.17', 'pathlib', 'pillow', 'psycopg2-binary', 'pygeoip', 'python-dateutil==2.*,>=2.4.0', 'python-dotenv==0.*,>=0.19.0', 'python-magic', 'pyyaml', 'raven', 'redis==3.*,>=3.0.0', 'rich==10.*,>=10.9.0', 'sentry-sdk[flask]', 'sqlalchemy==1.*,==1.3.*,>=1.1.0,>=1.3.0', 'sqlparse', 'toolz', 'tqdm', 'validate-email', 'webassets<2', 'werkzeug<1', 'whoosh==2.*,>=2.5.0', 'wtforms<2.2', 'wtforms-alchemy>=0.12', 'wtforms-sqlalchemy', 'xlwt'],
    extras_require={"dev": ["black", "coveralls", "flake8", "flake8-bugbear", "flake8-comprehensions", "flake8-mutable", "flake8-pytest", "flake8-super-call", "flake8-tidy-imports", "flask-debugtoolbar>=0.10", "flask-linktester", "honcho==1.*,>=1.0.1", "html5lib==1.*,>=1.1.0", "isort", "mastool", "mccabe", "mypy==0.*,>=0.910.0", "plumbum", "pre-commit", "profilehooks", "pytest-cov", "pytest-flask==1.*,>=1.0.0", "pytest-xdist==2.*,>=2.3.0", "safety==1.*,>=1.10.3", "types-bleach==3.*,>=3.3.3", "types-chardet==0.*,>=0.1.5", "types-deprecated==0.*,>=0.1.3", "types-markdown==3.*,>=3.3.2", "types-python-dateutil==0.*,>=0.1.4", "types-pytz==2021.*,>=2021.1.0", "types-pyyaml==5.*,>=5.4.3", "types-redis==3.*,>=3.5.4", "types-requests==2.*,>=2.25.1", "types-setuptools==57.*,>=57.0.0", "watchgod==0.*,>=0.7.0"]},
)
