
#include<bits/stdc++.h>
using namespace std;
int main()
{
  ios ::sync_with_stdio(0);
  cin.tie(0);
  string s;
  printf("Enter the production as a string :");
  cin >> s;
  char ss=s[0];
  int index=3;
  int len=s.length();
  vector<string> alpha;
  vector<string>beta;
  int pos=0;
  int subl;
  cout << "\n" ;
  cout << "After Eliminating Left Recursion" << "\n";
   while(index<len)
  {
      pos=s.find('|',index);
     // cout << "pos " << pos;
     // cout << "\n";
      if(pos<0) pos=len;

      subl=pos-index;
      string s1=s.substr(index,subl);
    //  cout << s1 << "\n";
      if(s1[0]==ss)
      {
          string s2=s1.substr(1,subl-1);
         // cout <<s2 << "\n";
      alpha.push_back(s2);
          index=pos+1;
      }
      else
      {
         string s2=s1.substr(0,subl);
       //   cout <<s2 << "\n";

          beta.push_back(s2);
          index=pos+1;


      }
  }

for(int i=0;i<beta.size();i++)
{

     if(i==beta.size()-1)
        cout << ss<<"->"<<beta[i]<< ss <<"'" ;
     else

    cout << ss<<"->"<<beta[i]<< ss <<"'" << "|";
}
cout << "\n";
for(int i=0;i<alpha.size();i++)
{

     if(i==alpha.size()-1)
        cout << ss<<"'"<<"->"<<alpha[i]<< ss <<"'" << "|" << "epsilon" ;
     else

    cout << ss<<"'"<<"->"<<alpha[i]<< ss <<"'" << "|";
}

cout << "\n";
cout << "\n";

}

