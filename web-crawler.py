# only used to simulate a branching website structure
def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
                    '<p> It is a good idea to '
                    '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
                    'crawl</a> before you try to  '
                    '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
                    'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
                    '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
                    'am quite good at '
                    '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
                    '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
                    '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
                    '</body> </html>')
    except:
        return ""
    return ""

# returns the next link in the page and the end quote
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

# joins two lists without repeating items
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True: # keeps adding links until there are no more left in the page
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

# finds all links that branch from seed website.
# Will stop searching once max_pages is reached
def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl: # while there are pages to crawl still
        page = tocrawl.pop() # searches the last website in the tocrawl list for links
        if page not in crawled:
            if len(crawled) < max_pages:
                union(tocrawl, get_all_links(get_page(page)))
                crawled.append(page) # adds the links found on the list
    return crawled


print(crawl_web("http://www.udacity.com/cs101x/index.html", 1))
print(crawl_web("http://www.udacity.com/cs101x/index.html", 3))

