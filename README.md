# Twitter crawler

## How to use

1. Install Python3, Selenium, chromedriver-binary
1. Edit the source code: "*******" => the Twitter user ID you want to crawl
1. Execute the script like:

    ```
    $ python3 crawl.py > log.txt 
    ```

1. The log text is the raw HTML displayed in Twitter; you may want to extract the text like:

    ```
    perl -Mutf8 -CSD -F/\\t/ -nale 'next unless m{<}; if (not m{</div>$}) { $text .= $_."\\n"; next; } $text .= $_; $text =~ m{/status/(\d+)}; $status = $1; $text =~ m{datetime=\"([^\"]+)\"}; $time = $1; $text =~ s{^.*?<time\b[^>]*>.+?</time>}{}g; $text =~ s{<div\b[^<>]*\"group\"[^<>]*>.*$}{}; $text =~ s{<[^>]+>}{}g; print "$time\t$status\t$text"; $text = ""; ' log.txt > log_text.txt 
    ```
