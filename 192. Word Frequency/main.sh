awk '{for(i=1;i<=NF;i++) {print $i}}' words.txt | sort -n | uniq -c | sort -nr | awk ' {print $2,$1} '
