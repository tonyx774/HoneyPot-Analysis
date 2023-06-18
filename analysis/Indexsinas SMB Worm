
# Indexinas SMB Worm

SHA-256: **8a7f479d9c6cbe277d760844917a979ba17f3e07be479c205d1491e682a71866**

File Type: **32-bit Windows DLL**

This sample is an SMB Worm known as Indexinas, it arrived in my honeypot through SMB protocol and it has a couple of different features I will talk about.

<br><br><br>

## Main Function:
The main function contains a bunch of calls to functions as we can see below, we will step through these functions in this analysis which will give us an understanding of the inner workings of this ransomware.

![Alt text](images/mainFunction.png)


<br><br><br><br>

## DontDisplayConsoleWindow (Sub_407200)

 This function gets a handle to the console window and sets show window with parameter of 0 indicating it should not be displayed 


![Alt text](images/consoleWindow.png)

<br><br><br><br>

## Get Handle To Heap (sub_407290) 

Create Heap / Get Handle to existing Heap


![Alt text](images/createHeap.png)

<br><br><br><br>

## Set Privileges For The Running Process (sub_4055B0)

This function is used to set multiple privileges for the currently running process

![Alt text](images/privelegesBeingSet.png)
