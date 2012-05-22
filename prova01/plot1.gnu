plot "data.txt" u 1:2 title "S"
replot "data.txt" u 1:3 title "I"
replot "data.txt" u 1:4 title "R"
replot "data.txt" u 1:5 title "tot"
set xlabel "R0"
set ylabel "1-s"
#set xrange[0:10]
#set yrange[0:1]
replot
pause -1

