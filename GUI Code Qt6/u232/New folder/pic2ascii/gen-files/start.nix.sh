x=ps -p $(ps -p $$ -o ppid=) -o args=
echo $x