# 📊 Function Call Difference Report

## ➕ Added Function Calls
- __init__ → _get_werkzeug_version
- __init__ → urlsplit
- add → shared_task
- after_sync → Response
- block → shared_task
- create_app → celery_init_app
- create_app → dict
- create_jinja_environment → NotImplementedError
- dump_session_contents → Markup
- get_debug_flag → bool
- index → Markup
- index → ValueError
- process → range
- process → shared_task
- register → deferred
- result → AsyncResult
- routes_command → any
- routes_command → enumerate
- routes_command → itemgetter
- routes_command → range
- session_transaction → TypeError
- test → Markup
- test_config_from_file_json → common_object_test
- test_config_from_file_toml → common_object_test
- test_filters → Markup
- test_filters2 → Markup
- test_host → Flask
- test_host → FlaskGroup
- test_no_routes → Flask
- test_no_routes → FlaskGroup
- test_subdomain → Flask
- test_subdomain → FlaskGroup
- test_with_categories → Markup
- url_for → _url_quote

## ➖ Removed Function Calls
- __delete__ → super
- __get__ → super
- __init__ → Lock
- __init__ → RLock
- __init__ → url_parse
- __set__ → super
- _find_package_path → _matching_loader_thinks_module_is_package
- _find_package_path → hasattr
- _find_package_path → iter
- _matching_loader_thinks_module_is_package → AttributeError
- _matching_loader_thinks_module_is_package → hasattr
- _matching_loader_thinks_module_is_package → type
- create_namespace → str
- default → _default
- get_cookie_domain → is_ip
- get_debug_flag → print
- htmlsafe_dump → htmlsafe_dumps
- htmlsafe_dumps → _jinja_htmlsafe_dumps
- inner → str
- iscoroutinefunction → isinstance
- modules_tmpdir → str
- modules_tmpdir_prefix → str
- routes_command → attrgetter
- routes_command → zip
- run → print
- send_file_max_age_default → _make_timedelta
- signal → _FakeSignal
- site_packages → str
- test_config_from_file → common_object_test
- test_egg_installed_paths → install_egg
- test_egg_installed_paths → str
- test_explicit_instance_paths → str
- test_from_pyfile_weird_encoding → str
- test_no_routes → invoke_no_routes
- test_session_transaction_needs_cookies → str
- test_uninstalled_module_paths → str
- test_uninstalled_package_paths → str
- update_template_context → func
- url_for → url_quote

## 🔼 Newly Introduced Functions
- after_sync
- block
- process
- result
- test_config_from_file_json
- test_config_from_file_toml
- test_host
- test_subdomain

## 🔽 Removed Functions
- __delete__
- __get__
- __set__
- _matching_loader_thinks_module_is_package
- create_namespace
- get_cookie_domain
- htmlsafe_dump
- htmlsafe_dumps
- inner
- iscoroutinefunction
- modules_tmpdir
- modules_tmpdir_prefix
- send_file_max_age_default
- signal
- site_packages
- test_config_from_file
- test_egg_installed_paths
- test_explicit_instance_paths
- test_from_pyfile_weird_encoding
- test_session_transaction_needs_cookies
