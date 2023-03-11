from Wappalyzer import Wappalyzer, WebPage

def wapp(url):
    try:
        url = 'https://'+url
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(url)

        wp = wappalyzer.analyze_with_categories(webpage)
        return wp
    except:
        return None