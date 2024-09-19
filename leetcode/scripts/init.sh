touch $1.py

read -p 'Algorithm: ' algorithm
read -p 'Level(Easy, Medium, Hard): ' level
read -p 'Status(Accepted, Failed): ' status

echo "\"\"\"LeetCode

Algorithm : 
    $(echo $algorithm)
Level :
    $(echo $level)
Status :
    $(echo $status)

$(date)
\"\"\"" > $1.py