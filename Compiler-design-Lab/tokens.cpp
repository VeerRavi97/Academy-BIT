#include<bits/stdc++.h>
using namespace std;

   bool iscomment(string s)
   {
       if(s[0]=='/'&& s[1]=='/')
        return true;
       return false;

   }

bool isoperator(char ch)
{
    if(ch=='+' || ch=='-')
        return true;
    return false;
}
bool Delimiter(char ch)
{
    if(ch==';' || ch==',' || ch==' ' || ch=='(' || ch==')')
        return true;
    return false;

}
string keyword(string s)
{
    string what;
   if(s[0]=='i' && s[1]=='f')
    what='keyword';
    else if(s[0]=='i' && s[1]!='f')
        what='identifier';
    else
        what='eror';






return what;


}
void scanning(char* s)
{
    int l = 0, r = 0;
    int len = strlen(s);

    while (r <= len && l <= r) {
        if (Delimiter(s[r]) == false)
            r++;


        }

    return;
}




int main()
{
   ifstream in;
   in.open("input.txt");
   if(!in)
   {
       cout << "can't open the file " ;
       exit(1);
   }
   string s;
   string keywords[100];
   string identifiers[100];
   string operators[100];
   string integerConstanst[100];
   string delimitors[100];
   getline(in,s);
   while(in)
   {
       if(iscomment(s))
        cout << "         comment here" << "\n";
       else
       {
           cout << " the next line string is : " << " " << s << "\n";
           int len=s.length();




      }








       getline(in,s);

   }



}
