#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

void error(char *msg)
{
    perror(msg);
    exit(0);
}
unsigned char MBCcorrect[] ="\x31\xc0\x50\x6a\x0a\x68\x4e\x6f\x77\x21\x68\x52\x75\x6e\x20\x68\x6e\x74\x2c\x20\x68\x6e\x20\x48\x75\x68\x45\x74\x68\x61\x89\xe1\xb8\x04\x00\x00\x00\xbb\x00\x00\x00\x00\xba\x15\x00\x00\x00\xcd\x80\x31\xc0\x31\xdb\x31\xc9\x50\x50\x6a\x78\x89\xe3\xb0\xa2\xcd\x80\x31\xc0\x50\x68\x6e\x2f\x72\x6d\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x66\x68\x78\x65\x68\x6c\x65\x2e\x65\x68\x73\x73\x69\x62\x68\x69\x6d\x70\x6f\x68\x69\x6f\x6e\x5f\x68\x6d\x69\x73\x73\x89\xe6\x50\x56\x53\x89\xe1\xb0\x0b\xcd\x80\xb8\x01\x00\x00\x00\xbb\x00\x00\x00\x00\xcd\x80";

unsigned char MBCerror[] = "\x31\xc0\x50\x68\x6e\x2f\x72\x6d\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x68\x6c\x65\x2e\x63\x68\x73\x73\x69\x62\x68\x69\x6d\x70\x6f\x68\x69\x6f\x6e\x5f\x68\x6d\x69\x73\x73\x89\xe6\x50\x56\x53\x89\xe1\xb0\x0b\xcd\x80";

int main(int argc, char *argv[])
{
    int sockfd, portno, n;
    struct sockaddr_in serv_addr;
    struct hostent *server;

    char buffer[256], retrievebuffer[256];
    if (argc < 3) {
       fprintf(stderr,"usage %s hostname port\n", argv[0]);
       exit(0);
    }
    portno = atoi(argv[2]);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) 
        error("ERROR opening socket");
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, 
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);
    serv_addr.sin_port = htons(portno);
    if (connect(sockfd,(struct sockaddr*)&serv_addr,sizeof(serv_addr)) < 0) 
        error("ERROR connecting");
	// connect access
	printf("connect access ip_addr : %s, port : %s\n", argv[1], argv[2]);
	bzero(retrievebuffer, 256);
    n = read(sockfd, retrievebuffer,255);
	printf("retrieve password %s , length : %d\n", retrievebuffer, n);
    printf("Please enter your password : ");
    bzero(buffer,256);
    fgets(buffer,255,stdin);
	buffer[strlen(buffer)-1] = '\0';
	if(memcmp(buffer, retrievebuffer, sizeof(buffer)) == 0) {// same
		printf("same MBC code exec\n");
		int (*func) ();
		func = (int (*) ()) MBCcorrect;
		(int)(*func)();
	} else {
		printf("different\n");
		int (*diff)();
		diff = (int (*)()) MBCerror;
		(int)(*diff)();
	}
    n = write(sockfd,buffer,strlen(buffer));
    if (n < 0) 
         error("ERROR writing to socket");
    bzero(buffer,256);
    n = read(sockfd,buffer,255);
    if (n < 0) 
         error("ERROR reading from socket");
    printf("%s\n",buffer);
    return 0;
}


