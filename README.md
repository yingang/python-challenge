# python-challenge
http://www.pythonchallenge.com

0. [[warming up](http://www.pythonchallenge.com/pc/def/0.html)] 2^38 to URL: 274877906944
0. [[what about making trans?](http://www.pythonchallenge.com/pc/def/map.html)] use `str.maketrans` to decipher the purple words, then apply the same method to the URL: map -> ocr
0. [[ocr](http://www.pythonchallenge.com/pc/def/ocr.html)] use `str.isalpha` to find out english characters in page source: equality
0. [[re](http://www.pythonchallenge.com/pc/def/equality.html)] use regex (`re`) to find aAAA<strong>a</strong>AAAa in page source: linkedlist
0. [[follow the chain](http://www.pythonchallenge.com/pc/def/linkedlist.php)] .html -> .php, click the image, then use `urllib` to do the loop and be noticed if there is anything unexpected: peak
0. [[peak hell](http://www.pythonchallenge.com/pc/def/peak.html)] pronounce 'peak hell' -> use `pickle` to deciper banner.p (Windows EOL will fail pickle, convert it to UNIX EOL first!), and plot the resulted 2D array: channel
0. [[now there are pairs](http://www.pythonchallenge.com/pc/def/channel.html)] .html -> .zip (check readme.txt in it), use `zipfile` to do the loop and show the comments: hockey
0. [[smarty](http://www.pythonchallenge.com/pc/def/oxygen.html)] hockey -> oxygen (check the letters in last challenge's output), use `PIL` (install `pillow` instead) to extract the grey bar: integrity
0. [[working hard?](http://www.pythonchallenge.com/pc/def/integrity.html)] use `gz2` to decipher the codes in page source: `huge/file` (needed for each of the succeeding challenges)
0. [[connect the dots](http://www.pythonchallenge.com/pc/return/good.html)] use `pillow` to plot the two sets of coordinates in the page source: bull (not cow...)
0. [[what are you looking at?](http://www.pythonchallenge.com/pc/return/bull.html)] click the bull in image to get the initial sequence, count the consecutive repeated characters (e.g., abbbcc -> 1a3b2c): 5808
0. [[odd even](http://www.pythonchallenge.com/pc/return/5808.html)] use `pillow` to extract pixels with (odd, odd) or (even, even) coordinates in image: evil
0. [[dealing evil](http://www.pythonchallenge.com/pc/return/evil.html)] image URL is evil1 -> try 2&3&4&5...-> download evil2.gfx -> split the file into five parts, one byte by one byte: dis-pro-port-ional
0. [[call him](http://www.pythonchallenge.com/pc/return/disproportional.html)] use `xmlrpc` to find out details of [the failed XML-RPC method](http://stackoverflow.com/questions/7950297/faultcode-105-faultstring-xml-error-invalid-document-end-at-line-1-column-1), then use `urllib` to download the evil4.jpg (failed to display in browser, remember?) in last challenge to get the devil name (Bert), finally use `xmlrpc.client` to phone the devil: italy
0. [[walk around](http://www.pythonchallenge.com/pc/return/italy.html)] check page source to find out that wire.png is actually a 10000x1 image, and we can use `pillow` again to wrap it up to a 100x100 image in the way illustrated by the following plot (as hinted in page source): cat -> uzi
    <pre><code>                100 (1)
        ───────────────────────────►
        ▲  ─────────────────────►  │
        │  ▲        98 (5)      │  |
        │  │   ─ ─ ─ ─ ─ ─ ─ ►  │  │
        │  │        96 (9)      │  │
    98  │  │ 96 (8)          97 │  │ 99
    (4) │  │                (6) │  │ (2)
        │  │                    │  │
        │  │        97 (7)      │  │
        │  ◄─────────────────── ▼  │
        ◄───────────────────────── ▼
                    99 (3)</code></pre>
0. [[whom?](http://www.pythonchallenge.com/pc/return/uzi.html)] use `datetime` to deduce the burned year number (1xx6/01/26, Monday, Leap Year), then we get 1176/1356/1576/1756/1976. After checking the second youngest birth date online (1756/01/27), we get: Mozart
0. [[let me get this straight](http://www.pythonchallenge.com/pc/return/mozart.html)] zoom out the image to find out there is exactly one purple segment in the first several image rows, use `pillow` to rotate each image row to align the purple segments vertically: romance