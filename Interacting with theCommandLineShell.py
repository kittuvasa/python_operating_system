# pipes and pipelines

cat pipes.txt | tr ' ' '\n'|sort|uniq -c|sort -nr| head
