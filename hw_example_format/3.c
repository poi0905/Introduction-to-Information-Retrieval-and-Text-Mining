#include<stdio.h>
#include<stdlib.h>
#include<fcntl.h>
#include<sys/shm.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<unistd.h>
#include<sys/mman.h>
#include<string.h>

int main(){

	int input;
	scanf("%d",&input);
	
	while(input <= 0){
	    printf("Please enter a positive integer\n");
	    scanf("%d",&input);
    }
    	
	pid_t pid;
	pid = fork();

	const int SIZE = 4096;
	const char *smptr = "shared";
	int shm_fd;
	void *ptr;
	char *com = ",";
	
	
	if(pid < 0){
		printf("Fork failed");
		return 1;
	}
	else if (pid == 0){
		//child process
		shm_fd = shm_open(smptr,O_CREAT|O_RDWR,0666);
		ftruncate(shm_fd,SIZE);
		ptr = mmap(0,SIZE,PROT_WRITE,MAP_SHARED,shm_fd,0);
		//calculating
		while(input != 1){   
			ptr += sprintf(ptr,"%d",input);
			sprintf(ptr,"%s",com);
			ptr += strlen(com);
			if(input % 2 == 0){
				input = input / 2;
			}
			else{
				input = input * 3 + 1;
			}
		}
		ptr += sprintf(ptr,"%d",input);

	}
	else{
		//parent process
		wait(NULL);
		//start printing
		shm_fd = shm_open(smptr,O_RDONLY,0666);
		ptr = mmap(0,SIZE,PROT_READ,MAP_SHARED,shm_fd,0);
		printf("%s\nProcess complete\n",(char *)ptr);
		shm_unlink(smptr);
	}


	return 0;
}
