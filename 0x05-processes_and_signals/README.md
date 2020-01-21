# 0x05. Processes and signals
---
## Description

This project in the System engineering & DevOps series is about:

* What is a PID
* What is a process
* How to find a process PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

---
File|Task
---|---
0-what-is-my-pid | Bash script that displays its PID
1-list_your_processes | Bash script that displays a list of currently running processes for all users
2-show_your_bash_pid | Bash script that displays line containing the `bash` word, which allows you to easily obtain the PID of the process
3-show_your_bash_pid_made_easy | Displays the PID along with the process name that contain the word `bash`
4-to_infinity_and_beyond | Displays `To infinity and beyond` indefinitely
5-kill_me_now | Bash script that can kill another process
6-kill_me_now_made_easy | Bash script that can kill another process without using kill or killall
7-highlander | Display `To infinity and beyond` indefinitely with sleep 2 between each iteration and displays `I am invincible!!!` when `SIGTERM` signal has been recieved
8-beheaded_process | Bash script that kills the `7-highlander` process
