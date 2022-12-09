echo "Location in which the maximum number of purchases has been made: "
awk -F, '{print $5}' bank_transactions.csv | sort | uniq -c | sort -nr | head -1 > location.md
cat location.md
echo "Did Females spend more than Males? "
awk -F, '{arr[$4] += $9} END {if (arr["M"] > arr["F"]) {print("Males");} else{print("Females");}}' bank_transactions.csv
echo "The customer with the highest average transaction amount: "
awk -F, '{arr[$2]+=$9; count[$2]++} END {for (cust in arr)print  arr[cust]/count[cust],cust}' bank_transactions.csv | sort -nr | head -1
