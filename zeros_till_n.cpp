//zeros
#include<iostream>
#include<cstdlib>
#include<cmath>

using namespace std;
//int sum;
int count(int n_i,int d,int f,int x[],string n,int cnt);

int main()
{

string n;
while(n!="q")
{

cin>>n;
                         // input in string form
int n_i=atoi(n.c_str());           // input in integer form
//cout<<"num is "<<n_i;
int d=n.length();       //no. of digits
//cout<<"d is "<<d<<endl;
int *x=new int[d];
x[0]=0;
x[1]=0;
//x[2]=9;                   //  0 denotes 2
int i;
int sum=x[1];
//int p=pow(10,d-2);
//cout<<"p is "<<p<<endl;
for(i=2;i<d;i++)          // calculates all till d-1
    {
     x[i]=9*(pow(10,i-2)+x[i-1]);
     sum=sum+x[i];
    }
int f;
int cnt=0;
//cout<<"n[0] is "<<n[0]<<endl;
char c=n[0];
f=atoi(&c);               // first digit
//cout<<"f is "<<f<<endl;
//int s=count(n_i,d,f,x,n,cnt);
//cout<<"s is "<<s;
sum=sum+count(n_i,d,f,x,n,cnt);
/*for(i=0;i<d;i++)
{
    if(n[i]=='0')
    {
        sum++;
        break;
    }
} */
cout<<"sum is "<<sum<<endl;
}

}

//    CHECK  FROM HERE
int count(int n_i,int d,int f,int x[],string n,int cnt)
{
    //cout<<"f is "<<f<<endl;
  if(d<=1)
  {
      return 0;
  }
  //cout<<"d is "<<d<<endl;
  int p=pow(10.00,d-2);
  //cout<<"p is "<<p<<endl;
  int low_check=(f)*p*10;            //lowest d digit no.    10 bcz it should be 10^d-1
  //cout<<"n_i "<<n_i<<endl;
  //cout<<"l_c "<<low_check<<endl;
  int diff=n_i-low_check;

  //cout<<"diff is "<<diff<<endl;
  int sum;
  if(f!=1)
  {
    sum=(f-1)*(p+x[d-1]);
    if(diff<p)
    {
      sum=sum+diff+1;             //CORRECT THIS
      return sum;
    }
    else
    {
      sum=sum+p;
      n_i=n_i-low_check;
      cnt++;
      char c=n[cnt];
       f=atoi(&c);
      sum=sum+count(n_i,d-1,f,x,n,cnt);
      return sum;
    }
  }
  else
  {
    if(diff<p)
    {
      sum=diff+1;
      return sum;
    }
    else
    {

      sum=p;
      //cout<<"sum is "<<sum<<endl;
      n_i=n_i-low_check;
      cnt++;
      char c=n[cnt];
       f=atoi(&c);

      sum=sum+count(n_i,d-1,f,x,n,cnt);
      return sum;
    }
  }
// */
}
