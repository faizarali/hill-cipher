# 1. Execute the command: chmod +x *.sh
# 2. Compile & test with the command: ./hillcipher-tester.sh hillcipher.xyz
#    (where xyz is either c, cpp, java, go, or py)
#    In my case: ./hillcipher-tester.sh hillcipher.py

case $1 in
hillcipher.c)
	gcc hillcipher.c
	EXE="./a.out"
	;;
hillcipher.cpp)
	g++ hillcipher.cpp
	EXE="./a.out"
	;;
hillcipher.java)
	javac hillcipher.java
	EXE="java hillcipher"
	;;
hillcipher.go)
	go build hillcipher.go
	EXE="./hillcipher"
	;;
hillcipher.py)
	EXE="python3 hillcipher.py"
	;;
*)
	echo "Invalid source file name"
	exit 1
esac

echo "Case #1"
eval $EXE k1.txt p1.txt > myOutput1.txt
diff myOutput1.txt sample_output/k1p1.txt
echo "Case #1 - complete"

echo "Case #2"
eval $EXE k2.txt p2.txt > myOutput2.txt
diff myOutput2.txt sample_output/k2p2.txt
echo "Case #2 - complete"

echo "Case #3"
eval $EXE k3.txt p3.txt > myOutput3.txt
diff myOutput3.txt sample_output/k3p3.txt
echo "Case #3 - complete"

echo "Case #4"
eval $EXE k4.txt p4.txt > myOutput4.txt
diff myOutput4.txt sample_output/k4p4.txt
echo "Case #4 - complete"

echo "Case #5"
eval $EXE k5.txt p5.txt > myOutput5.txt
diff myOutput5.txt sample_output/k5p5.txt
echo "Case #5 - complete"

echo "Case #6"
eval $EXE k6.txt p6.txt > myOutput6.txt
diff myOutput6.txt sample_output/k6p6.txt
echo "Case #6 - complete"
