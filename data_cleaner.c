#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
  
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
   //fs=fopen("stopwords.txt","r+");
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
fs=fopen("stopwords.txt","r+");
char rm[20];

                while(fgets(rm,20,fs)!=NULL)
                        {

                                        const char *o_doc = s;
                                        char *str = strdup(o_doc);
                                        const char *rm_word = rm;
                                        char *sw = strdup(rm_word);
                                        delete(str,sw);
                                        //printf("%s\n",rm);
                        }      
}

void delete(char *str, char *str_to_remove) {

    char *buf;
    char *new_str;

    new_str = calloc(500, sizeof(char));

    buf = strtok(str, " ");
    while(buf)
    {
        if(strcmp(buf, str_to_remove) != 0)
        {
            strcat(new_str, buf);
            strcat(new_str, " ");
        }
        buf = strtok(NULL, " \t\n");
    }
    printf("%s\n",new_str);
    printf("%s\n",str_to_remove);
    free(new_str);
    getchar();

}


