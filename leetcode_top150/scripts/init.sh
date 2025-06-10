touch $1/$2.py

read -p 'Level(Easy, Medium, Hard): ' level
read -p 'Status(Accepted, Failed): ' status
read -p 'Note(optional): ' note

echo "\"\"\"LeetCode Top 150
Level:
    $(echo $level)
Status:
    $(echo $status)
Note:
    $(echo $note)

$(date)
\"\"\"" > $1/$2.py
