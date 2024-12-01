# Python Client-Server programme
This laba is about interprocess communication via a file descriptor.
Our python programm is based on client-server algorithm: 
  -there are two apps: client and server. Applications exchange messages: ping(client)-pong(server response)

Client is sending to the server a message and the server is returning a reversed line. 
Example: 
input: hello it is me
output: em si ti olleh

# Run
The client is communicating with server using terminal. To use the programm:
1) Firstly run the server.py in dedicated terminal
2) After that run the client.py in dedicated terminal as well
3) Enter the line you want to make reversed
4) Receive the reversed line
5) To finish communication with the server enter 'q' to stop the programm

Some features:
* server stops waiting for the client`s messages after 1 minute of silence
* warning if the server is not running
* if server is disconnected for some reasons, the client will see a message about it
  
