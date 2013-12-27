#! /usr/bin/env python
import time
import argparse
from linkfetcher import Linkfetcher
from webcrawler import Webcrawler

Usage = '''
 $ ./crawler -d5 <url>
    Here in this case it goes till depth of 5 and url is target URL to
    start crawling.
'''
Version = '0.0.1'


def option_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument("-l", "--links", action="store_true",
        default=False,dest='links', help="Get links for target url only.")

    parser.add_argument("-d", "--depth", action="store", type=int ,
        default=5, dest='depth', help="Maximum depth to traverse.")
    parser.add_argument("url",help="The target URL.")

    args = parser.parse_args()

    if len(vars(args)) < 1:
        parser.print_help()
        raise SystemExit, 1
    return args


def getlinks(url):
    page = Linkfetcher(url)
    page.linkfetch()
    for i, url in enumerate(page):
        print "%d ==> %s" % (i, url)


def main():

    args = option_parser()
    url = args.url
    if "http://" not in url:
        url = "http://"+ url

    if args.links:
        getlinks(url)
        raise SystemExit, 0

    depth = args.depth
    if depth < 0:
        print "You cant have negative depth!"
        raise SystemExit, 0

    sTime = time.time()

    print "Crawler started for %s, will crawl upto depth %d" %(url, depth)
    print "==============================================================="
    webcrawler = Webcrawler(url, depth)
    webcrawler.crawl()
    print "\n".join(webcrawler.urls)

    eTime = time.time()
    tTime = eTime - sTime
    print "\n"
    print "Crawler Statistics"
    print "=================="
    print "No of links Found: %d" % webcrawler.links
    print "No of follwed:     %d" % webcrawler.followed
    print "Time Stats : Found all links  after %0.2fs" % tTime


if __name__ == "__main__":
    main()
