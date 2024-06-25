def configure_settings(**settings):
    for key, value in settings.items():
        print(key, "is", value)
configure_settings(databace = 'MySQL', port = 3306, timeout= 30)