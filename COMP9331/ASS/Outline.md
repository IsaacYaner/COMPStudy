# Ass

## Submission

+ 22/04/2022
+ *server.py
+ *client.py
+ *credentials.txt
+ And so on

## Outline

+ Forum
+ Design application layer protocol
+ Bot UDP and TCP(Files only) 

## Server

+ Argument
  + server_port
+ UDP retransmission

## Client

+ Authentication
  + **Enter User name**
    + Confirmation
      + No double online
        + Username
    + Create a new account
      + Enter password
        + Please check write permission
      + Confirmation
  + **Enter Password**
    + Welcome
    + Mismatch
      + Enter User name
+ Operation
  + Display all commands
    + CRT: Create Thread 
      + CRT threadtitle
    + LST: List Threads 
    + MSG: Post Message 
      + MSG threadtitle message
    + DLT: Delete Message
      + DLT threadtitle messagenumber
    + RDT: Read Thread 
      + RDT threadtitle
    + EDT: Edit Message
      + EDT threadtitle messagenumber message
    + UPD: Upload File
      + UPD threadtitle filename
    + DWN: Download File
      + DWN threadtitle filename
    + RMV: Remove Thread
      + RMV threadtitle
    + XIT: Exit
  + Prompt to select one command
  + Wrong action
    + Please select the correct acction
  + Missing / additional arguments
    + Show error message
    + Prompt (See Section 8)
    

## Authentication

+ credentials.txt
+ [A-Z,a-z,0-9,(~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/]
+ case-sensitive

## Command

+ Uppercase
+ Argument
  + one word each
  + [A-Z,a-z,0-9,.]
  + Text can include white space
  + No need to check
+ Do
  + Prompt

### UPD DWN

+ TCP
+ close once transfer concludes

## Question

+ (no need to check)
+ chmod +w credentials.txt
+ If a match is found, then a message to this effect should be sent to the server and 
displayed at the prompt for the user and they should be prompted to enter a username.
+ Subsequent prompts for action should include this same message
  + Prompt after every query?