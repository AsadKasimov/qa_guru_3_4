def replay(name_funk, *args):
    fullname = name_funk.__name__.title().replace('_', ' ')
    print(fullname, *args)


def open_browser(browser_name):
    replay(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    replay(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    replay(find_registration_button_on_login_page, page_url, button_text)


open_browser('Chrome')
go_to_companyname_homepage('https://qa.guru/')
find_registration_button_on_login_page('https://qa.guru/', 'login')
