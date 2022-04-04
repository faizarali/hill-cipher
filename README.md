# Hill Cipher

- This README is in works. Some details may **not** be more fully described at this time.

This program encrypts the alphabetic letters in a file using the Hill cipher where the Hill matrix can be any size from 2 x 2 up to 9 x 9.

This program will take two command line parameters containing the names of the file storing the encryption key and the file to be encrypted. The first command line parameter will be the key file and the second command line parameter will be the plaintext file.

The program will output the following to the console (terminal) screen:
```txt
1. Print out the input key file
2. Print out the input plaintext file
3. Ciphertext output produced from running the cipher against the input
   plaintext file.
```

**Sample Key File**
```txt
3
6 24 1
13 16 10
20 17 15
```
**Sample Input File**
```txt
Recursion is the process a procedure goes through when one of the steps of the
procedure involves invoking the procedure itself. A procedure that goes through
recursion is said to be 'recursive'.

To understand recursion, one must recognize the distinction between a procedure
and the running of a procedure. A procedure is a set of steps based on a set of
rules, while the running of a procedure involves actually following the rules
and performing the steps.

Recursion is related to, but not the same as, a reference within the
specification of a procedure to the execution of some other procedure.
```

**Corresponding Output File**

```txt
Key matrix:

6  24  1
13  16  10
20  17  15


Plaintext:

recursionistheprocessaproceduregoesthroughwhenoneofthestepsoftheprocedureinvolve
sinvokingtheprocedureitselfaprocedurethatgoesthroughrecursionissaidtoberecursive
tounderstandrecursiononemustrecognizethedistinctionbetweenaprocedureandtherunnin
gofaprocedureaprocedureisasetofstepsbasedonasetofruleswhiletherunningofaprocedur
einvolvesactuallyfollowingtherulesandperformingthestepsrecursionisrelatedtobutno
tthesameasareferencewithinthespecificationofaproceduretotheexecutionofsomeotherp
rocedurex


Ciphertext:

stwakxhqvfkxxtryxkgagnuqgukvjfacchkvwjplkjswvldrbodajnwgpqzkzxilusgukvjfvyvfjrgx
ercuugyhnxxtryxkmopybiedseptsjthqxmavwvfmpqhkvwjplkjstwakxhqveainczjnjuanpwljafa
cpteqikpxndontpwlcieldrucmjgciqmsctfhvldtfkxyuvivycrzwpiyapsjthqxmavdegajnxvrxlt
nornuqgukvjfnutyxkmopybiwygacpnxpmehyleggdslkacpqrnyxmwkdzhbznvdakcidwcbsjthqxma
vrcufwcocwuknpaosmvgrtzyrfkcketyxmdegvnztrvryzfkchkvmehstwakxhqvdqtcuhfdzjnjrsin
aeaxkgyeqcuvxpuanahqfgdnldajneuzbwrsgmivydbbnuqgukvjfacpajnislrqphqvoalmyybkgfgw
yxkmopnvz
```

Here is a sample run command of this program through the command line:
```txt
Python program:
prompt> python3 hillcipher.py k6.txt p6.txt
```
Also included is a bash shell script called `hillcipher-tester.sh`, which will test the source code with a number of key files and plaintext file to a corresponding sample output of those files.
