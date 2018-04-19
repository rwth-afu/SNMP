echo ".1.3.6.1.4.1.51218.1.1.2.1"
echo "Integer32"
temp=`tail -1 /sys/bus/w1/devices/10-000800c312bf//w1_slave |  awk -F 't=' '{print $2/1000}'`
echo "($temp+0.5)/1" | bc
