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

test_case_num=7

for ((i = 1; i <= test_case_num; i++))
do
	echo "Case #$i"
    eval $EXE k$i.txt p$i.txt > myOutput$i.txt
    diff myOutput$i.txt sample_output/k${i}p${i}.txt
    echo "Case #$i - complete"
done
