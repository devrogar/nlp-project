#include<string.h>
#include<stdio.h>
#include<stdlib.h>
  
void lower_string(char s[]);
void clean(char s[]);
void clear(char s[]);
void delete(char *s,char *rm);
void main()
  {
   FILE *fp,*fc,*fs;
   char doc[500];
   
   
   fp=fopen("data.txt","r+");
   fc=fopen("output.txt","w+");
   if(fp==NULL)
        {
                printf("cant open file\n");
        }
   else
        {
                while(fgets(doc,500,fp)!=NULL)
                        {
                                lower_string(doc);
                                int i=0;
                                while(i<100){
                                clean(doc);i++;}
                                clear(doc);
                                fputs(doc,fc);
                        }    
                if(fp)
                {
                        fclose(fp);
                        fclose(fc);
                }   
        }
  }
  
 
void lower_string(char s[]) {
   int c = 0;
   while (s[c] != '\0') {
      if (s[c] >= 'A' && s[c] <= 'Z') {
         s[c] = s[c] + 32;

      }
      c++;
   }
}

void clean(char s[]) {
        int c = 1;
        while(s[c] != '\0') {
                if(s[c] == '\n' || (s[c] >= 'a' && s[c] <= 'z' ))
                        {
                                c++;
                        }
                        else
                        {
                                s[c] = ' ';
                                c++;
                        }
        }
        c=1;
        while(s[c] != '\0') {
                if(s[c]==' ' && s[c+1]==' ')
                {
                        int i=c;
                        while(s[i+1] != '\0')
                                {
                                        s[i+1] = s[i+2];
                                        i++;
                                }
                                c++;
                }
                else{
                c++;}
        }
}

void clear(char s[]) {
FILE *fs;
char temp[500];
char *new_str;
strcpy(temp,s);
fs=fopen("stopwords.txt","r+");
char rm[20];
while(fgets(rm,20,fs)!=NULL){
    char *buf;
    rm[strcspn(rm, "\r\n")] = 0;

    new_str = calloc(strlen(temp)+1, sizeof(char));

    buf = strtok(temp, " \t\n");
    while(buf)
    {
        if(strcmp(buf,rm) != 0)
        {
            strcat(new_str, buf);
            strcat(new_str, " ");
        }
        buf = strtok(NULL, " \t\n");
    }
    strcpy(temp,new_str);
    free(new_str);
    }
    strcat(temp,"\n");
    strcpy(s,temp);

}

