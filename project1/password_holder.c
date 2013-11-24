/* A simple server in the internet domain using TCP
   The port number is passed as an argument */
#include <stdio.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#define PWDLENGTH 256
char inputbuffer[PWDLENGTH];
void error(char *msg)
{
    perror(msg);
    exit(1);
}
void obtainPwd() {
	printf("Please Input a character string without white space as a password.\n");
	printf("Password : ");
    bzero(inputbuffer,PWDLENGTH);
	fgets(inputbuffer, PWDLENGTH-1, stdin);// inputbuffer will have '\n' character.
	printf("Input OK, wait for client socket.\n");
}
// g++ file_name.cpp -o output_file_name
// ./output_file_name argv[1]

// g++ password_holder.c -o password_holder
// ./password_holder 2013
int main(int argc, char *argv[]) // argv[1] : port number.
{
     int sockfd, newsockfd, portno;
     unsigned int clilen;
     char buffer[256];
     struct sockaddr_in serv_addr, cli_addr;
     int n;
     if (argc < 2) {
         fprintf(stderr,"ERROR, no port provided\n");
         exit(1);
     }
     sockfd = socket(AF_INET, SOCK_STREAM, 0);// make a 'TCP' socket from socketstream.
     if (sockfd < 0) 
        error("ERROR opening socket");
     bzero((char *) &serv_addr, sizeof(serv_addr));// memset init.
     portno = atoi(argv[1]);// get input port nubmer.
     serv_addr.sin_family = AF_INET; // Internet address
     serv_addr.sin_addr.s_addr = INADDR_ANY; // 0.0.0.0 address
     serv_addr.sin_port = htons(portno); // input port number
     if (bind(sockfd, (struct sockaddr *) &serv_addr,
              sizeof(serv_addr)) < 0) 
              error("ERROR on binding");
     listen(sockfd, 5); // listen(socketfd, MAX_CLIENT_NUM)

     obtainPwd();
     // wait for client socket.
     clilen = sizeof(cli_addr);
     newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
     if (newsockfd < 0) 
          error("ERROR on accept");
	 n = write(newsockfd, inputbuffer, strlen(inputbuffer)-1);
     bzero(buffer,256);
     n = read(newsockfd,buffer,255);
     if (n < 0) error("ERROR reading from socket");
     printf("Here is the message: %s\n",buffer);
     n = write(newsockfd,"I got your message",18);
     if (n < 0) error("ERROR writing to socket");
     return 0; 
}


