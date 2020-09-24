#include<stdio.h>
#include<stdlib.h>
#include<sys/wait.h>
#include<sys/types.h>
#include<unistd.h>

int main(){

	int input;
	scanf("%d",&input);
	
	while(input <= 0){
	    printf("Please enter a positive integer\n");
	    scanf("%d",&input);
    }

	pid_t pid;
	pid = fork();

	if (pid < 0){
		printf("Fork failed");
		return 1;
	}
	else if (pid == 0){
		//child process
		printf("%d",input);
		while (input != 1){
			printf(",");
			if(input % 2 == 0){
				input = input / 2;
				printf("%d",input);
			}
			else{
				input = input *3 + 1;
				printf("%d",input);
			}
		}
	}
	else{
		//parent process
		wait(NULL);
		printf("\nChild process is done\n");
	}
 	 
	return 0;
}


